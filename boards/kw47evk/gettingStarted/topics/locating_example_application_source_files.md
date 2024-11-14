# Locating example application source files {#locating_example_application_source_files}

When opening an example application in any of the supported IDEs, various source files are referenced. The MCUXpresso SDK devices folder is the central component to all example applications. It means that the examples reference the same source files and, if one of these files is modified, it could potentially impact the behavior of other examples.

The main areas of the MCUXpresso SDK tree used in all example applications are:

-   *devices/<device\_name\>*: CMSIS header file of the device, MCUXpresso SDK feature file, and a few other files
-   *devices/<device\_name\>/drivers*: All the peripheral drivers for your specific MCU
-   *devices/<device\_name\>/<tool\_name\>*: Toolchain-specific startup code, including vector table definitions
-   *devices/<device\_name\>/utilities*: Items such as the debug console that are used by many of the example applications
-   *devices/<device\_name\>/project\_template*: Project template used by MCUXpresso IDE to create projects

For examples containing an RTOS, there are references to the appropriate source code. RTOSes are in the `rtos` folder. The core files of each of these are shared, so modifying one could have potential impacts on other projects that depend on that file.

**Parent topic:**[MCUXpresso SDK board support package folders](../topics/mcuxpresso_sdk_board_support_package_folders.md)

