
## Developing Win Ros Tools

Installation is usually via the .msi download, but that is painful when developing/modifying the win_ros python tools.

* Uninstall the .msi
* In this directory:

```
# Make some changes to python sources in src/win_ros or scripts/winros_xxx
> make install
# Test
# make uninstall
```

Make sure that you don't move files between install and uninstall as the moved files will not be uninstalled.

## New Release Instructinos

If updating the version number for rospkg, rosinstall, vcstool and wstool.

* Update version numbers in make.bat

otherwise if win_ros, just add your code, and then...important!

* Test
* Update version number in setup.py
* Upload (just run 'make clean' and 'make' and add your password at the end)
* Update version number in the download link on http://ros.org/wiki/win_python_build_tools




