# Other limitations

-   Documentation may not be fully updated to refer to MCX W72 devices.
-   Low Power configurations are not supported for Bluetooth LE Reference Design and IEEE 802.15.4, \(Zigbee/Thread\) stacks in this release.
-   The following Connectivity Framework configurations are Experimental and not recommended for mass production:

    -   Power down on application power domain.

    -   XTAL32K less board with FRO32K support.

    -   FRO32K notifications callback is for debug only. Application shall not execute long processing \(such as PRINTF\) as it is executed in ISR context.

-   A hardfault can be encountered when using fsl\_component\_mem\_manager\_light.c memory allocator and shutting down some unused RAM banks in low power. It is due to a wrong reinitialization of ECC RAM banks. To be sure not to reproduce the issue, `gPlatformShutdownEccRamInLowPower` should be set to 0.

-   GenFsk `Connectivity_test` application is not operational with Low Power enabled.
-   No MCUXpresso projects for Extended NBU Applications
-   Limited support for multiple connection for Extended NBU Applications
-   Serial Manager is only supported on UART \(not I2C nor SPI\).
-   The `--no-warn-rwx-segments` cannot been recognized on legacy MCUXpresso IDE versions.

    The `--no-warn-rwx-segments` option in MCUXpresso projects should be manually removed from the project settings if someone needs to use legacy \(< 11.8.0\) MCUXpresso IDE versions.

-   If the FRO32K is configured as the clock source of the CM33 Core then the debug session will block in both IAR, MCUX CMSIS-DAP while debugging. Use a lower debug wire speed, for example 1 MHz instead of the default one.

    In IAR, the option is in **Runtime Checking** -\> **Debugger** -\> **CMSIS DAP** -\> **Interface** -\> **Interface speed**.

    In MCUXpresso IDE, the option is in **LinkServer Debugger** -\> **Advanced Settings** -\> **Wirespeed \(Hz\)**.

-   If the configuration tool is used to clone `tfm-related` projects, there is a problem that *region\_defs.h* cannot be found in the cloned project.
-   Not supported features:
    -   Platform low power modes not fully enabled in this release.
    -   FRO32K mode not fully supported in this release.
-   Low power reference design applications are not supported for the armgcc toolchain from zip archives. Please use MCUXpresso IDE or IAR toolchains for development using these applications.
-   Some connection events may be missed by the NBU core firmware when an asynchronous wake up is triggered from the application core.

**Parent topic:**[Known issues](../topics/known_issues.md)

