@echo off

REM Used to help execute winros_make because windows is trivially fixated 
REM on extensions.

set DIR=%~dp0
python %DIR%\winros_make.py %*
