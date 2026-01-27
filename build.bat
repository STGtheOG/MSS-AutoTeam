@echo off
setlocal

REM Ensure deps are installed
uv sync

REM Clean old builds
rmdir /s /q build dist 2>nul

REM Build exe
uv run pyinstaller ^
  --onefile ^
  --name mss-autoteam ^
  --noconsole ^
  main.py

REM Copy config files to dist
copy options.json dist\
copy teams.json dist\

echo.
echo Build complete: dist\mss-autoteam.exe
endlocal
