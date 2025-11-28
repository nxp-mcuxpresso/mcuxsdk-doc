# What is new

The following changes have been implemented compared to the previous SDK release version \(25.06.00\).

- **Bluetooth Synopsys controller**
    - LE ping stops after feature exchange.
    - Connection drops as central after Connection Update from the slave.
    - Fixed state not correctly reset when terminating periodic advertising sync leading to hard fault.
    - Tx power is not changed in the database when the Tx power table changes.
    - Provide API to enable/disable Channel Assessment.
    - Debug HCI: Fix missed deferred HCI event logs.
    - Disable checking irq priorities against unused BLE_SLP_TMR_IRQ.
    - Fixed the wrong Local Resolvable Private Address in the LE Enhanced Connection Complete event.

- **Bluetooth LE**
    - **Common changes**
        - Support for **IAR toolchain** added.
        - Support for **OTA upgrade over external flash** added.
        - Support for the **MCXW235B SoC variant** added.
        - **SRAM placement updated** - data placement now starts at `0x20004000` instead of `0x20008000`.
        - **NVM storage integration improved** - NVM operations are now performed when the radio is not active for enough time
        - **Experimental** support of mebdtls PSA. The feature can be enabled for **testing** purpose by setting `CONFIG_MCUX_COMPONENT_middleware.wireless.framework.seclib_rng_port.psa=y`, `CONFIG_MCUX_COMPONENT_component.psa_crypto_driver.casper=y`, `CONFIG_MCUX_COMPONENT_component.psa_crypto_driver.hashcrypt=y` configs in the application `prj.conf` file.

    - **Health Care IoT Reference design applications**
        - Support for **Keil toolchain** added.
        - Fixed central application not retaining bonding information
        - Moved **ENABLE_LOW_POWER** flag to app_preinclude.h for the peripheral application

    - **Bluetooth LE host stack and applications**
        - Support for **EATT Central/Peripheral** applications.
        - Support for **FSCI black box** application.
        - Support for **Beacon** application.
        - **HCI transport** now uses the Connectivity Framework's PLATFORM API implementation

- **Connectivity Framework**

      **Minor Changes**
        -   [RNG] Replaced `gRngHasSecLibDependency_d` compilation switch with `gRngUseSecLib_d`.
        -   [mcxw23] Defined `gRngIsrPrio_c` on the preprocessor to make it global and avoid redefinition warnings.
        -   [mcxw23] Implemented `PLATFORM_ResetCrypto()` API called by RNG_reinit/SecLib_reinit.
        -   [mcxw23] Added support of Timer Manager timestamp with OSTIMER.
      **Bug fixes**
        -   [NVM] Fixed `NvIdle()` to prevent looping for more operations than the queue size.
        -   [NVS] Fixed blank check procedure to return false (non-blank) when checking a 0 length area.
        -   [NVS] Made external and internal flash ports consistent.
        -   [MISRA] Various MISRA compliance fixes in NVM, HWParameter, LowPower, SecLib, Platform modules and IFR offset definitions.
