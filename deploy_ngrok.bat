@echo off
echo.
echo ========================================
echo   UNFOLDED - Public Deployment with ngrok
echo ========================================
echo.

:: Check if ngrok is installed
where ngrok >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ngrok not found! Installing via winget...
    winget install ngrok.ngrok
    echo.
    echo Please restart this script after installation.
    pause
    exit /b
)

echo Starting backend server...
start "Backend" cmd /c "cd /d %~dp0backend && ..\.venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak >nul

echo.
echo Starting ngrok tunnel...
echo.
echo Share the HTTPS URL with your cofounder!
echo.
ngrok http 8000
