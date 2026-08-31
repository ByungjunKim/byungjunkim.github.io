@echo off
REM ---------------------------------------------------------------
REM  CV docx -> 고화질 PDF (더블클릭 실행용)
REM  Word에서 docx를 수정/저장한 뒤 이 파일을 더블클릭하면 끝.
REM  특정 파일을 변환하려면 그 docx를 이 배치파일 위로 끌어다 놓으면 된다.
REM ---------------------------------------------------------------
setlocal
cd /d "%~dp0.."
python "scripts\docx_to_pdf.py" %*
if errorlevel 1 (
  echo.
  echo [!] 변환 실패. 위 메시지를 확인하세요.
) else (
  echo.
  echo [OK] PDF 생성 완료.
)
echo.
pause
