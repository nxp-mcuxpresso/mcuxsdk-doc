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
    - [Common] Added MDK compatibility for the errno framework header.
    - [OTA] Corrected definition of `gEepromParams_WriteAlignment_c` flag for mcxw23
    - [OTA] Enabled calling `OTA_GetImgState()` prior to `OTA_Initialize()`.
    - [OTA] Removed `gUseInternalStorageLink_d` linker flag definition when external OTA storage is used.
    - [mcxw23] Implemented missing `PLATFORM_OtaClearBootInterface()` API.
    - [mcxw23] Refactored fwk_platform.c to separate BLE-specific logic into fwk_platform_ble.c.
    - [mcxw23] Added support for OTA using external flash.
    - [mcxw23] Introduced `PLATFORM_GetRadioIdleDuration32K()` to estimate time until next radio event.
    - [mcxw23] Extended `CopyAndReboot()` to support external flash OTA.
    - [mcxw23] Implement `PLATFORM_IsExternalFlashBusy()` API.
    - [mcxw23] Implemented HCI interface using PLATFORM API as preliminary requirement for Zephyr enablement, introducing `PLATFORM_SendHciMessageAlt()` alternative API.
    - [mcxw23] Added experimental SecLib PSA support with additional configuration for MBEDTLS_ECP_C and MBEDTLS_BIGNUM_C.
