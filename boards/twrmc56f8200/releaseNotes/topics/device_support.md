# Device support

The device folder contains the whole software enablement available for the specific System-on-Chip \(SoC\) subfamily. This folder includes:

-   SoC-specified clock driver
-   Device register header files
-   Device feature header files
-   Peripheral drivers
-   System configuration source files
-   Tool chain support
-   A standard debug console

The device-specific header files provide a direct access to the microcontroller peripheral registers and an overall SoC memory-mapped register definition. The device-specified feature header file provides feature list for peripherals of each device.

The toolchain folder, CodeWarrior, contains the startup code and linker files for each supported toolchain. The startup code efficiently transfers the code execution to the `main()` function.

**Parent topic:**[MCUXpresso SDK release package](../topics/mcuxpresso_sdk_release_package.md)

