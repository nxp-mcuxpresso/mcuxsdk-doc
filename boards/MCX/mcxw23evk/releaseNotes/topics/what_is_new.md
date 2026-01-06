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
        - Support for **FSCI Black Box** application.
        - Support for **Beacon** application.
        - Support for **Temperature Collector/Sensor** applications.
        - Support for **ANCS Client** application.
        - Support for **Extended Advertising Central/Peripheral** applications.
        - Support for **HID Device/Host** applications.
        - Support for **BLE Shell** application.
        - **HCI transport** now uses the Connectivity Framework's Platform API implementation

        **Note**
            These applications do not support low-power operation. For low-power features, see the reference design `Health Care IoT` applications.

- **Connectivity Framework**

-   **Connectivity framework**

      **Major Changes**
        -   [SecLib] Removed unused cryptographic implementations (SHA1, AES-EAX, AES-OFB) and obsolete `FSL_FEATURE_SOC_AES_HW` option to reduce code size and complexity.
      **Bug fixes**
        -   [MISRA] Various MISRA compliance fixes in SFC, SecLib, Platform (including platform_ics and platform low power), FSCI, and PDUM modules.
