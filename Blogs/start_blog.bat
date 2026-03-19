@echo off
echo Starting Personal Blog Server...
echo.

cd /d D:\My-Blogs\Blogs

if not exist venv\ (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo Virtual environment activated.
echo Starting Flask server...
echo.
echo Your blog will be available at:
echo   - http://localhost:5000/
echo   - http://127.0.0.1:5000/
echo.
echo Press CTRL+C to stop the server.
echo.

python run.py

pause
