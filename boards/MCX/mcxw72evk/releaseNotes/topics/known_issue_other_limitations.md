# Other limitations 
-   Zigbee: incorrect randomization of transmission CCA backoff may cause packets to be missed by receiver nodes or procedure retry.
-   Documentation may not be fully updated to refer to MCX W72 devices.
-   Low Power configurations are not supported for Bluetooth LE Reference Design and IEEE 802.15.4, \(Zigbee/Thread\) stacks in this release.
-   GenFSK Connectivity\_test application is not operational with ARMGCC compiler.
-   GenFSK `Connectivity_test` application is not operational with Low Power enabled.
-   No MCUXpresso projects for Extended NBU Applications
-   Limited support for multiple connection for Extended NBU Applications
-   Serial manager is only supported on UART \(not I2C nor SPI\).
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
-   Low power reference design applications do not work properly with armgcc toolchain
-   NBU core can enter in hardfault if a call to PLATFORM_NbuApiReq()(mainly used by Controller_xxx APIs) happen while the NBU is sending a HCI message
-   Some connection event can be missed by the nbu core when asynchronous wake up are also triggered from the host

**Parent topic:**[Known issues](../topics/known_issues.md)
s
