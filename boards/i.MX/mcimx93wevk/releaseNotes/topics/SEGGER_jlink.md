# SEGGER J-Link debugger usage problem

When an M core software is already running, it is possible to get HardFault or data verification issue during loading image into TCM by debugger.

The following steps are recommended to use the J-Link debugger.

1.  Configure switch SW1301 to M core boot; low-power boot. Ensure that there is no image on the boot source.
2.  Power the board and start the debugger for use.
3.  To restart the debugger, stop the debugger, power off the board, and repeat step \#2.

**Parent topic:**[Known Issues](../topics/known_issues.md)

