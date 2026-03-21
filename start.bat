@echo off
echo.
echo ========================================
echo   UNFOLDED - Biography Generator
echo   Starting Web Application...
echo ========================================
echo.

cd /d "%~dp0"

echo Installing/checking dependencies...
.venv\Scripts\pip install fastapi uvicorn[standard] websockets google-genai python-docx -q

echo.
echo Starting server at http://localhost:8000
echo Opening frontend in browser...
echo.
echo Press Ctrl+C to stop the server
echo.

start "" "%~dp0frontend\index.html"

cd backend
..\\.venv\\Scripts\\python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
