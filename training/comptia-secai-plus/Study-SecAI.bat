@echo off
REM ============================================================
REM  SecAI+ (CY0-001) Study Launcher
REM  Double-click to start a study session. Flashcards + quizzes
REM  run fully offline (stdlib Python only). --explain on the
REM  quiz needs Ollama on SENTRY; not required here.
REM ============================================================
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
title SecAI+ Study Launcher
cd /d "%~dp0lab"

REM --- locate a Python interpreter (py launcher preferred on Windows) ---
set "PY="
where py >nul 2>nul && set "PY=py"
if not defined PY ( where python >nul 2>nul && set "PY=python" )
if not defined PY (
  echo.
  echo  [!] Python was not found on this machine.
  echo      Install it from https://www.python.org/downloads/ ^(check "Add to PATH"^),
  echo      or from the Microsoft Store, then run this launcher again.
  echo.
  pause
  exit /b 1
)

:menu
cls
echo ============================================================
echo                  SecAI+ (CY0-001) Study
echo ============================================================
echo.
echo   FLASHCARDS (recall drills, offline)
echo     1^) Week 1  - Domain 1 terminology        (55 cards)
echo     2^) Week 2  - Domain 2 terminology        (72 cards)
echo     3^) Week 3  - Domain 2 applied defense    (55 cards)
echo     4^) Week 4  - Domain 3 terminology        (56 cards)
echo     5^) Week 5  - Domain 4 terminology        (60 cards)
echo     6^) Acronyms - all 62 official acronyms   (62 cards)
echo     7^) ALL decks, shuffled                   (360 cards)
echo.
echo   QUESTION BANKS (graded, ~1 min/question)
echo     8^) Quick quiz - 25 mixed questions
echo     9^) Domain drill - pick a domain
echo    10^) Full timed mock exam (60 Q)
echo.
echo     L^) List parsed card/question counts
echo     Q^) Quit
echo.
set "choice="
set /p "choice=Select an option: "

if /i "%choice%"=="1"  ( %PY% flashcards.py --deck week1     & goto after )
if /i "%choice%"=="2"  ( %PY% flashcards.py --deck week2     & goto after )
if /i "%choice%"=="3"  ( %PY% flashcards.py --deck week3     & goto after )
if /i "%choice%"=="4"  ( %PY% flashcards.py --deck week4     & goto after )
if /i "%choice%"=="5"  ( %PY% flashcards.py --deck week5     & goto after )
if /i "%choice%"=="6"  ( %PY% flashcards.py --deck acronyms  & goto after )
if /i "%choice%"=="7"  ( %PY% flashcards.py                  & goto after )
if /i "%choice%"=="8"  ( %PY% quiz.py --n 25                 & goto after )
if /i "%choice%"=="9"  ( goto domain )
if /i "%choice%"=="10" ( %PY% quiz.py --domain mock --n 60   & goto after )
if /i "%choice%"=="L"  ( echo. & %PY% flashcards.py --list & echo. & %PY% quiz.py --list & goto after )
if /i "%choice%"=="Q"  ( exit /b 0 )

echo  Unrecognized choice: "%choice%"
timeout /t 1 >nul
goto menu

:domain
cls
echo  Domain drill - which domain?
echo    1^) Domain 1   2^) Domain 2   3^) Domain 3   4^) Domain 4
set "d="
set /p "d=Domain (1-4): "
if "%d%"=="1" ( %PY% quiz.py --domain domain1 --n 30 & goto after )
if "%d%"=="2" ( %PY% quiz.py --domain domain2 --n 40 & goto after )
if "%d%"=="3" ( %PY% quiz.py --domain domain3 --n 30 & goto after )
if "%d%"=="4" ( %PY% quiz.py --domain domain4 --n 30 & goto after )
goto domain

:after
echo.
echo ------------------------------------------------------------
echo  Session done. Log scores/weak areas in 99-PROGRESS-TRACKER.md
echo ------------------------------------------------------------
echo.
pause
goto menu
