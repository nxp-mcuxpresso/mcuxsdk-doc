# Locating example application source files

When opening an example application in any of the supported IDEs \(except MCUXpresso IDE\), a variety of source files are referenced. The MCUXpresso SDK devices folder is the central component to all example applications. It means that the examples reference the same source files and, if one of these files is modified, it could potentially impact the behavior of other examples.

The main areas of the MCUXpresso SDK tree used in all example applications are:

-   `devices/<device_name>`: The device’s CMSIS header file, MCUXpresso SDK feature file, and a few other things.
-   `devices/<device_name>/cmsis_drivers`: All the CMSIS drivers for your specific MCU.
-   `devices/<device_name>/drivers`: All of the peripheral drivers for your specific MCU.
-   `devices/<device_name>/<tool_name>`: Toolchain-specific startup code. Vector table definitions are here.
-   `devices/<device_name>/utilities`: Items such as the debug console that are used by many of the example applications.
-   `devices/<devices_name>/project template`: Project template used in CMSIS PACK new project creation.

For examples containing an RTOS, there are references to the appropriate source code. RTOSes are in the *rtos* folder. Again, the core files of each of these are shared, so modifying one could have potential impacts on other projects that depend on that file.

**Parent topic:**[MCUXpresso SDK board support package folders](../topics/mcuxpresso_sdk_board_support_package_folders.md)
