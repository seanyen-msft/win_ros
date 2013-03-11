@echo off


rem ************************** Variables ********************************

set PWD=%~dp0
set COMMAND=%1
rem set CMAKE_INSTALL_PREFIX=%PWD%\install
set CMAKE_INSTALL_PREFIX=C:\opt\rosdeps\groovy\x86

rem ************************** Options Parser ********************************

if X%COMMAND%==X set COMMAND=help
if X%COMMAND%==Xhelp goto Help
if X%COMMAND%==Xclean goto Clean
if X%COMMAND%==Xcompile goto Compile
if X%COMMAND%==Xinstall goto Install
goto Help

:Help
echo.
echo Usage: make [subcommand]
echo.
echo Creates local build and install directories for building a static tinyxml lib.
echo.
echo   clean      Remove build and install directories
echo   compile    Cmake and nmake the static library
echo   install    Collected headers and static library together
echo.
goto End

rem ************************** Targets ********************************

:Clean
echo "Cleaning build and install directories."
rm -rf build
rm -rf install
goto End

:Compile
mkdir %PWD%\build
cd %PWD%\build
cmake -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="%CMAKE_INSTALL_PREFIX%" ..
nmake
cd %PWD%
goto End

:Install
mkdir %PWD%\install
cd %PWD%\build
nmake install
goto End

:End
cd %PWD%
