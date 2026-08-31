#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DOCX -> 고화질 PDF 변환기 (Windows)

Word를 열어 두고 docx를 수정한 뒤, 이 스크립트만 실행하면 같은 폴더에
같은 이름의 PDF가 벡터 텍스트 + 폰트 임베딩 상태로 다시 만들어진다.

사용법
------
    python scripts/docx_to_pdf.py                 # files/ByungjunKim_CV_*.docx (최신) 변환
    python scripts/docx_to_pdf.py a.docx b.docx   # 지정한 파일들 변환
    python scripts/docx_to_pdf.py --out out.pdf a.docx
    python scripts/docx_to_pdf.py --engine libreoffice a.docx

품질 관련
--------
* 기본 엔진은 **LibreOffice**다. 이미지 300 DPI·무손실, 폰트 임베딩, 태그 PDF
  옵션을 명시적으로 켠다.
* Word(ExportAsFixedFormat)는 폴백이다. 인쇄 품질로 내보내긴 하지만
  **CFF(.otf) 계열 폰트를 PDF에 임베딩하지 못한다.** 이 CV의 본문 폰트인
  Pretendard가 정확히 그 경우라, Word로 뽑으면 폰트가 임베딩되지 않아
  Pretendard가 없는 PC에서는 전혀 다른 폰트로 보인다. 그래서 순서를 뒤집었다.
* 변환 후 임베딩 상태를 자동 검사해, 빠진 폰트가 있으면 경고를 출력한다
  (pymupdf 가 설치돼 있을 때).

주의: 대상 docx를 Word에서 열어 둔 채로 실행해도 되지만, 저장하지 않은 변경
사항은 PDF에 반영되지 않는다. 먼저 저장(Ctrl+S)하고 실행할 것.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_GLOB = os.path.join(REPO_ROOT, "files", "ByungjunKim_CV_*.docx")


# --------------------------------------------------------------------------- #
# 대상 파일 찾기
# --------------------------------------------------------------------------- #
VERSION_RE = re.compile(r"ByungjunKim_CV_(\d{4})\.docx$", re.IGNORECASE)


def _sort_key(path: str) -> tuple[int, float]:
    """파일명 끝의 YYMM(예: 2608, 2609, 2701)을 1순위, 수정 시각을 2순위로."""
    m = VERSION_RE.search(os.path.basename(path))
    yymm = int(m.group(1)) if m else -1
    return (yymm, os.path.getmtime(path))


def default_targets() -> list[str]:
    """files/ 의 CV docx 중 파일명 YYMM이 가장 큰 것(= 최신 월 버전)을 고른다.

    매달 ByungjunKim_CV_2609.docx 처럼 새 파일을 만들어도 자동으로 따라간다.
    구버전이 files/ 에 남아 있고 나중에 수정되더라도 최신 월 버전이 우선한다.
    (files/CV/ 로 옮긴 지난 버전은 글롭 대상이 아니라 애초에 걸리지 않는다.)
    """
    cands = [p for p in glob.glob(DEFAULT_GLOB) if not os.path.basename(p).startswith("~$")]
    if not cands:
        return []
    latest = max(cands, key=_sort_key)
    others = [os.path.basename(p) for p in cands if p != latest]
    print(f"대상: {os.path.basename(latest)}"
          + (f"  (files/ 내 다른 후보: {', '.join(sorted(others))})" if others else ""))
    return [latest]


def pdf_path_for(docx: str, explicit_out: str | None) -> str:
    if explicit_out:
        return os.path.abspath(explicit_out)
    return os.path.splitext(os.path.abspath(docx))[0] + ".pdf"


# --------------------------------------------------------------------------- #
# 엔진 1: MS Word COM
# --------------------------------------------------------------------------- #
def convert_with_word(pairs: list[tuple[str, str]]) -> None:
    import pythoncom  # noqa: F401  (pywin32)
    import win32com.client as win32

    # Word 상수 (win32com.client.constants 는 late binding 시 비어 있을 수 있어 직접 명시)
    wdExportFormatPDF = 17
    wdExportOptimizeForPrint = 0
    wdExportAllDocument = 0
    wdExportDocumentContent = 0
    wdExportCreateHeadingBookmarks = 1
    wdDoNotSaveChanges = 0

    pythoncom.CoInitialize()
    word = win32.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = False
    try:
        for docx, pdf in pairs:
            doc = word.Documents.Open(
                docx,
                ReadOnly=True,
                AddToRecentFiles=False,
                Visible=False,
                ConfirmConversions=False,
            )
            try:
                doc.ExportAsFixedFormat(
                    OutputFileName=pdf,
                    ExportFormat=wdExportFormatPDF,
                    OpenAfterExport=False,
                    OptimizeFor=wdExportOptimizeForPrint,   # 화면용 압축 대신 인쇄 품질
                    Range=wdExportAllDocument,
                    Item=wdExportDocumentContent,
                    IncludeDocProps=True,
                    KeepIRM=True,
                    CreateBookmarks=wdExportCreateHeadingBookmarks,
                    DocStructureTags=True,                  # 접근성 태그 + 텍스트 선택 품질
                    BitmapMissingFonts=False,               # 폰트를 비트맵화하지 않고 임베딩
                    UseISO19005_1=False,
                )
            finally:
                doc.Close(SaveChanges=wdDoNotSaveChanges)
            report(docx, pdf, "Word")
    finally:
        word.Quit()
        pythoncom.CoUninitialize()


# --------------------------------------------------------------------------- #
# 엔진 2: LibreOffice (폴백)
# --------------------------------------------------------------------------- #
def find_soffice() -> str | None:
    exe = shutil.which("soffice") or shutil.which("soffice.exe")
    if exe:
        return exe
    for base in (os.environ.get("ProgramFiles", r"C:\Program Files"),
                 os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")):
        cand = os.path.join(base, "LibreOffice", "program", "soffice.exe")
        if os.path.isfile(cand):
            return cand
    return None


def convert_with_libreoffice(pairs: list[tuple[str, str]]) -> None:
    soffice = find_soffice()
    if not soffice:
        raise RuntimeError("LibreOffice(soffice)를 찾을 수 없습니다.")

    # writer_pdf_Export 필터 옵션: 이미지 무손실 + 300 DPI, 폰트 임베딩, 태그 PDF
    filter_opts = (
        "pdf:writer_pdf_Export:"
        '{"UseLosslessCompression":{"type":"boolean","value":"true"},'
        '"ReduceImageResolution":{"type":"boolean","value":"false"},'
        '"MaxImageResolution":{"type":"long","value":"300"},'
        '"EmbedStandardFonts":{"type":"boolean","value":"true"},'
        '"UseTaggedPDF":{"type":"boolean","value":"true"},'
        '"ExportBookmarks":{"type":"boolean","value":"true"}}'
    )

    for docx, pdf in pairs:
        outdir = os.path.dirname(pdf)
        subprocess.run(
            [soffice, "--headless", "--norestore", "--convert-to", filter_opts,
             "--outdir", outdir, docx],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        produced = os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + ".pdf")
        if os.path.abspath(produced) != os.path.abspath(pdf):
            shutil.move(produced, pdf)
        report(docx, pdf, "LibreOffice")


# --------------------------------------------------------------------------- #
def check_embedded_fonts(pdf: str) -> None:
    """PDF 안의 모든 폰트가 임베딩됐는지 확인하고, 빠진 게 있으면 경고한다.

    임베딩되지 않은 폰트는 그 폰트가 깔려 있지 않은 PC에서 다른 폰트로 대체되어
    docx 와 전혀 다른 인상을 준다. 조용히 넘어가면 알아채기 어려운 종류의 사고라
    변환할 때마다 검사한다.
    """
    try:
        import pymupdf
    except ImportError:
        return
    missing = set()
    with pymupdf.open(pdf) as doc:
        pages = doc.page_count
        for page in doc:
            for font in page.get_fonts(full=True):
                basefont, ext = font[3], font[1]
                if ext in ("n/a", ""):
                    missing.add(basefont)
    print(f"        {pages}쪽", end="")
    if missing:
        print(f"  [경고] 임베딩되지 않은 폰트: {', '.join(sorted(missing))}")
        print("        -> 해당 폰트가 없는 PC에서는 다른 폰트로 보입니다.")
    else:
        print("  모든 폰트 임베딩 확인")


def report(docx: str, pdf: str, engine: str) -> None:
    size = os.path.getsize(pdf) / 1024
    print(f"[{engine}] {os.path.basename(docx)} -> {os.path.basename(pdf)} ({size:,.0f} KB)")
    check_embedded_fonts(pdf)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="docx를 고화질 PDF로 변환한다.")
    ap.add_argument("docx", nargs="*", help="변환할 docx (생략 시 files/ByungjunKim_CV_*.docx 중 최신본)")
    ap.add_argument("--out", help="출력 PDF 경로 (docx를 하나만 지정했을 때만 유효)")
    ap.add_argument("--engine", choices=["auto", "word", "libreoffice"], default="auto")
    args = ap.parse_args(argv)

    targets = [os.path.abspath(p) for p in args.docx] or default_targets()
    if not targets:
        print("변환할 docx가 없습니다.", file=sys.stderr)
        return 1
    if args.out and len(targets) > 1:
        print("--out 은 docx 하나만 지정했을 때 쓸 수 있습니다.", file=sys.stderr)
        return 1

    for p in targets:
        if not os.path.isfile(p):
            print(f"파일이 없습니다: {p}", file=sys.stderr)
            return 1

    pairs = [(p, pdf_path_for(p, args.out)) for p in targets]

    # LibreOffice 우선: Word 는 CFF(.otf) 폰트를 임베딩하지 못한다(위 독스트링 참고).
    engines = {"auto": ["libreoffice", "word"], "word": ["word"], "libreoffice": ["libreoffice"]}[args.engine]
    last_err: Exception | None = None
    for eng in engines:
        try:
            if eng == "word":
                convert_with_word(pairs)
            else:
                convert_with_libreoffice(pairs)
            return 0
        except Exception as exc:  # noqa: BLE001 - 다음 엔진으로 폴백
            last_err = exc
            print(f"{eng} 엔진 실패: {exc}", file=sys.stderr)

    print(f"변환에 실패했습니다: {last_err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
