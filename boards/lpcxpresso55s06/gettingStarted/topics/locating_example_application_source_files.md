# Locating example application source files {#GUID-4FDC6A05-F710-4E71-A1FF-A98C91DFE1B2}

When opening an example application in any of the supported IDEs, various source files are referenced. The MCUXpresso SDK devices folder is the central component to all example applications. It means that the examples reference the same source files and, if one of these files is modified, it could potentially impact the behavior of other examples.

The main areas of the MCUXpresso SDK tree used in all example applications are:

-   `devices/<device_name>`: The device’s CMSIS header file, MCUXpresso SDK feature file and a few other files
-   `devices/<device_name>/cmsis_drivers`: All the CMSIS drivers for your specific MCU
-   `devices/<device_name>/drivers`: All of the peripheral drivers for your specific MCU
-   `devices/<device_name>/<tool_name>`: Toolchain-specific startup code, including vector table definitions
-   `devices/<device_name>/utilities`: Items such as the debug console that are used by many of the example applications
-   `devices/<devices_name>/project`: Project template used in CMSIS PACK new project creation

For examples containing an RTOS, there are references to the appropriate source code. RTOSes are in the `rtos` folder. The core files of each of these are shared, so modifying one could have potential impacts on other projects that depend on that file.

There are two boards in LPC55xx SDK: LPCXpresso55S69 and LPCXpresso55S28. This document uses LPCXpresso55S69 as example. Same steps are applied to LPCXpresso55S28 SDK.

Refer document here for LPC55xx 1 B silicon IDE update: [https://community.nxp.com/docs/DOC-345024](https://community.nxp.com/docs/DOC-345024)

**Note:** The multicore example and TrustZone example not support in LPCXpresso55S28 SDK.

**Parent topic:**[MCUXpresso SDK board support package folders](../topics/mcuxpresso_sdk_board_support_package_folders.md)

