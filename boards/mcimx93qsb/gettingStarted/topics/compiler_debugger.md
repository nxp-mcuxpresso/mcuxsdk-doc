# Compiler/Debugger

The MCUXpresso SDK i.MX 93 release supports building and debugging with the toolchains listed in [Table 1](compiler_debugger.md#TABLE_TOOLCHAININFO).

The user can choose the appropriate one for development.

For supported toolchain versions, see MCUXpresso SDK Release Notes for MCIMX93-QSB \(*document: MCUXSDKMCIMX93QSBRN*\).

-   Arm GCC + SEGGER J-Link GDB Server. This is a command line tool option and it supports both Windows OS and Linux OS.
-   IAR Embedded Workbench for Arm and SEGGER J-Link software. The IAR Embedded Workbench is an IDE integrated with editor, compiler, debugger, and other components. The SEGGER J-Link software provides the driver for the J-Link Plus debugger probe and supports the device to attach, debug, and download.

|Compiler/Debugger|Supported host OS|Debug probe|Tool website|
|-----------------|-----------------|-----------|------------|
|ArmGCC/J-Link GDB server|Windows OS/Linux OS|J-Link Plus|[developer.arm.com/open-source/gnu-toolchain/gnu-rm](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm)

 [www.segger.com](http://www.segger.com)

|
|IAR/J-Link|Windows OS|J-Link Plus|[www.iar.com](https://www.iar.com)

 [www.segger.com](http://www.segger.com)

|

Download the corresponding tools for the specific host OS from the website.

**Note:**

-   To support i.MX 93, the patch for IAR and Segger J-Link must be installed. To download, navigate to [https://www.nxp.com/webapp/Download?colCode=SDK\_MX93\_3RDPARTY\_PATCH&appType=license\)](https://www.nxp.com/webapp/Download?colCode=SDK_MX93_3RDPARTY_PATCH&appType=license)).

**Parent topic:**[Toolchain introduction](../topics/toolchain_introduction.md)

