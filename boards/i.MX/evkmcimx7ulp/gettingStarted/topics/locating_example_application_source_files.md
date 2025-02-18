# Locating example application source files

When opening an example application in any of the supported IDEs, various source files are referenced. The MCUXpresso SDK devices folder is the central component to all example applications. It means that the examples reference the same source files and, if one of these files is modified, it could potentially impact the behavior of other examples.

The main areas of the MCUXpresso SDK tree used in all example applications are:

-   `devices/<device_name>`: The device’s CMSIS header file, MCUXpresso SDK feature file and a few other files
-   `devices/<device_name>/cmsis_drivers`: All the CMSIS drivers for your specific MCU
-   `devices/<device_name>/drivers`: All of the peripheral drivers for your specific MCU
-   `devices/<device_name>/<tool_name>`: Toolchain-specific startup code, including vector table definitions
-   `devices/<device_name>/utilities`: Items such as the debug console that are used by many of the example applications
-   `devices/<devices_name>/project`: Project template used in CMSIS PACK new project creation

For examples containing an RTOS, there are references to the appropriate source code. RTOSes are in the `rtos` folder. The core files of each of these are shared, so modifying one could have potential impacts on other projects that depend on that file.

**Note:** The RPMsg-Lite library is located in the *<install\_dir\>/middleware/multicore/rpmsg-lite* folder. For detailed information about the RPMsg-Lite, to see the RPMsg-Lite User’s Guide, open the index.html located in the *<install\_dir\>/middleware/multicore/rpmsg\_lite/doc* folder.

**Parent topic:**[MCUXpresso SDK Board Support Folders](../topics/mcuxpresso_sdk_board_support_folders.md)

