@echo off
echo ========================================================
echo  OpportunityBob - Push to GitHub Helper
echo ========================================================
echo.
echo Make sure you have created the empty repository on GitHub:
echo https://github.com/new with repository name: bengaluru-opporbob-ai
echo.
git remote remove origin 2>nul
git remote add origin https://github.com/SatyaRamDinkar/bengaluru-opporbob-ai.git
git branch -M main
echo Pushing code to GitHub...
git push -u origin main
echo.
if %errorlevel% equ 0 (
    echo [SUCCESS] Your project has been pushed to GitHub successfully!
) else (
    echo [ERROR] Push failed. Please verify that the repository exists on GitHub.
)
pause
