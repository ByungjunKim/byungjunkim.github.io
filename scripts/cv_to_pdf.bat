@echo off
REM ---------------------------------------------------------------
REM  CV docx -> high-quality PDF  (double-click to run)
REM
REM  Word에서 docx를 수정/저장(Ctrl+S)한 뒤 이 파일을 더블클릭하면 끝.
REM  파일명이 매달 바뀌어도(_2608 -> _2609) 최신 월 버전을 자동으로 찾는다.
REM  특정 파일을 변환하려면 그 docx를 이 배치파일 위로 끌어다 놓으면 된다.
REM
REM  (아래 echo 문구는 콘솔 코드페이지 문제를 피하려고 영문으로 둔다.
REM   한글 안내는 UTF-8로 출력되는 파이썬 쪽에서 나온다.)
REM ---------------------------------------------------------------
setlocal
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
cd /d "%~dp0.."
python "scripts\docx_to_pdf.py" %*
if errorlevel 1 (
  echo.
  echo [FAILED] See the message above.
) else (
  echo.
  echo [OK] PDF created.
)
echo.
pause
