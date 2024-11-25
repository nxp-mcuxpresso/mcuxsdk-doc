# Other limitations 

-   Documentation may not be fully updated to refer to MCX W72 devices.
-   Low Power configurations are not supported for Bluetooth LE Reference Design and IEEE 802.15.4, \(Zigbee/Thread\) stacks in this release.
-   GenFSK Connectivity\_test application is not operational with ARMGCC compiler.
-   GenFSK `Connectivity_test` application is not operational with Low Power enabled.
-   Serial manager is only supported on UART \(not I2C nor SPI\).
-   SDK components may expose MISRA Required issues due to alignment with legacy codebases. Improvements are planned in the next MCUXpresso SDK release.
-   The `--no-warn-rwx-segments` cannot been recognized on legacy MCUXpresso IDE versions.

    The `--no-warn-rwx-segments` option in MCUXpresso projects should be manually removed from the project settings if someone needs to use legacy \(< 11.8.0\) MCUXpresso IDE versions

-   If the FRO32K is configured as the clock source of Core 0 then the debug session will stuck in both IAR, MCUX CMSIS-DAP while debugging. Use a lower debug wire speed, for example 1 MHz instead of the default one.

    In IAR, the option is in **Runtime Checking** -\> **Debugger** -\> **CMSIS DAP** -\> **Interface** -\> **Interface speed**.

    In MCUXpresso IDE, the option is in **LinkServer Debugger** -\> **Advanced Settings** -\> **Wirespeed \(Hz\)**.

-   If the configuration tool is used to clone `tfm-related` projects, there is a problem that *region\_defs.h* cannot be found in the cloned project.
-   Low-power configurations are not supported.
-   Not supported features:

    -   Platform low power modes not fully enabled in this release.
    -   FRO32K mode not fully supported in this release.

**Parent topic:**[Known issues](../topics/known_issues.md)

