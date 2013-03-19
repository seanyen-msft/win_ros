
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



