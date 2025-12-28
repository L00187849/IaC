@echo off
cls

echo "**********************************************"
echo Python Project Directory Builder
echo Name: Liam Saunders  (L00187849)
echo Date: 16-DEC-2024
echo "**********************************************"
echo *** Press [ctrl][c] to exit or any key to continue ***
pause >nul

set /p PROJECT=Enter the name of the project then press [return]: 
echo.

echo Creating project: %PROJECT%
echo.

REM Create root folder
mkdir "%PROJECT%"
cd "%PROJECT%"

REM Standard project folders
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
mkdir Images
mkdir Templates

REM Create __init__.py so Source can act like a package (optional but useful)
type nul > Source\__init__.py

REM Create placeholder README and requirements
echo # %PROJECT% > README.md
echo.>> README.md
echo ## Name: Liam Saunders ^(L00187849^)>> README.md
echo ## Date: 16-DEC-2024>> README.md
echo.>> README.md
echo ## Purpose>> README.md
echo - Project created from template>> README.md

type nul > requirements.txt

REM Create a main.py template with your header style
(
echo """ 
echo Name: Liam Saunders
echo Student Number: L00187849
echo Date: 16-DEC-2024
echo Version: 1.0
echo Purpose:
echo     Entry point for the project.
echo """
echo.
echo def main() ^-> None:
echo     print("Project created successfully!")
echo.
echo if __name__ == "__main__":
echo     main()
) > main.py

cls
echo "**********************************************"
echo Project created: %PROJECT%
echo "**********************************************"
echo.
tree /f
echo.

cd ..
pause
