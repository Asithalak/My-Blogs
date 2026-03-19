@echo off
echo ================================================
echo   Daily Updates Feature - Database Setup
echo ================================================
echo.

cd /d D:\My-Blogs\Blogs

if not exist venv\ (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo Updating database with DailyUpdate table...
echo.

python update_database.py

echo.
echo ================================================
echo Database update complete!
echo.
echo Next steps:
echo   1. Run start_blog.bat to start your blog
echo   2. Click "Daily Update" in the navbar
echo   3. Add your first daily update!
echo ================================================
echo.

pause
