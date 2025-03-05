# Compiler/Debugger

The MCUXpresso SDK i.MX 95 release supports building and debugging with the toolchains listed in [Table 1](compiler_debugger.md#TABLE_TOOLCHAININFO).

The user can choose the appropriate one for development.

For supported toolchain versions, see MCUXpresso SDK Release Notes for for IMX95LPD5EVK-19, IMX95LP4XEVK-15, and IMX95VERDINEVK \(*document: MCUXSDKIMX95SERIESRN*\).

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

-   To support i.MX 95, the patch for IAR and Segger J-Link must be installed. To get the patch, download it from [the NXP website](https://www.nxp.com/webapp/Download?colCode=iar_segger_support_patch_imx95_240807&appType=license) or contact your local field applications engineer \(FAE\) or the sales representative.

**Parent topic:**[Toolchain introduction](../topics/toolchain_introduction.md)

