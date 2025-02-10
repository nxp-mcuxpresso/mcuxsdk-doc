# Other limitations

-   Documentation may not be fully updated to refer to KW47 devices.
-   GenFSK Connectivity\_test application is not operational with ARMGCC compiler.
-   GenFSK `Connectivity_test` application is not operational with Low Power enabled.
-   Serial manager is only supported on UART \(not I2C nor SPI\).
-   The `--no-warn-rwx-segments` cannot been recognized on legacy MCUXpresso IDE versions.

    The `--no-warn-rwx-segments` option in MCUXpresso projects should be manually removed from the project settings if someone needs to use legacy \(< 11.8.0\) MCUXpresso IDE versions

-   If the FRO32K is configured as the clock source of Core 0 then the debug session will stuck in both IAR, MCUX CMSIS-DAP while debugging. Use a lower debug wire speed, for example 1 MHz instead of the default one.

    In IAR, the option is in **Runtime Checking** -\> **Debugger** -\> **CMSIS DAP** -\> **Interface** -\> **Interface speed**.

    In MCUXpresso IDE, the option is in **LinkServer Debugger** -\> **Advanced Settings** -\> **Wirespeed \(Hz\)**.

-   If the configuration tool is used to clone `tfm-related` projects, there is a problem that *region\_defs.h* cannot be found in the cloned project.
-   Not supported features:
    -   Platform low power modes not fully enabled in this release.
    -   FRO32K mode not fully supported in this release.
-   Buttons (SW2/SW3) do not wake up device when it is in low power
-   Low power reference design applications are not supported for the armgcc toolchain from zip archives. Please use MCUXpresso IDE or IAR toolchains for development using these applications.
-   Some connection events may be missed by the NBU core firmware when an asynchronous wake up is triggered from the application core.

**Parent topic:**[Known issues](../topics/known_issues.md)

