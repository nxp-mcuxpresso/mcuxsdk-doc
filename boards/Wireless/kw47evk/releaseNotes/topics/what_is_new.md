# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.06.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   RSSI-based adaptive CS procedure interval for localization applications (experimental; disabled by default).
	-   Added BTCS timer mechanism to ensure CS procedure loop restarts are not blocked by failed L2CAP transfers.

    ### Improved
	-   CS procedure parameters are now updated on connection interval change to avoid CS request rejection.
	-   Aligned wireless_uart preinclude settings across all platforms for consistency.
	-   Updated ble_shell periodic advertising default interval; set to 1 second for improved discoverability.
	-   Increased host task stack size across multiple applications.
	-   Extended ble_shell periodic advertising handling to support `gPeriodicDeviceScannedV2_c` event.
	-   RADE component naming updated in documentation.
	-   Unified CS results complete event handling; real-time transfer moved to `AppLocalization_HandleCompleteResults()`.

    ### Fixed
	-   Fixed out-of-bounds access in `gap.c`.
	-   HCI LE Read All Remote Features command is now issued if supported by the controller.
	-   Power Control APIs now return `gBleFeatureNotSupported_c` if the controller does not indicate support.
	-   Fixed array index overflow in application `ranging_client.c`.
	-   Fixed local RSSI parsing: correct byte is now collected before advancing parse pointer.
	-   Fixed bounds check for `gaAntPermNAp` in `processMode2Data` and `processMode3Data`.
	-   Fixed localization index overflow; added sanity check.
	-   Corrected bounds check for deviceId.
	-   Fixed `mAdvPending` flag of wireless_uart application to prevent multiple advertising starts during multi-peer disconnect.
	-   Fixed missing RSSI variables causing compilation issues in `app_localization_utils.c`.
	-   TPMS sensor Signing Key and sequence number now saved in NVM to prevent MAC check failures.
	-   CS IPT mode now configured with only 1 antenna path to fix Samsung phone CS request rejection.
	-   Fixed systick drift when `PWR_DisallowDeviceToSleep()` is active.
	-   CS: Added check for valid `numAntennaPaths` in `processCsResultsEvent`.
	-   Miscellaneous MISRA fixes.
	-   Miscellaneous Coverity fixes.

    ### Changed
	-   Reverted incorrect connection handle handling for non-connection enhanced notification events.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    -   Fixed default local SCA to 500 ppm.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control Power Amplifier (PA) ramp type and duration.

-   **Connectivity framework**

    - **Major Changes**
        - [NVM] Enhanced robustness of NVM MIT (Meta Information Tag) operations with improved validation and error handling. Added checksum validation feature controlled by `gNvmMetaCheckSum_d` compilation switch. Systematically validates MIT fields before use and triggers page switch if corruption detected. Fixed `mNvTableSizeInFlash` tracking when table entries are modified. Refactored `NvWriteRecord()` and added `NvModuleSwitchPage()` for better ECC fault handling. Added `NvSetChecksumEnable()` API to control feature at runtime. The feature is disabled by default.
        - [SecLib_RNG] Refactored SecLib mutex declaration and made Lock/Unlock functions public. Changed return type from `osa_status_t` to `secResultType_t` for SecLib mutex functions and moved mutex Lock/Unlock function declarations to SecLib.h.
        - [SecLib_RNG][PSA] Activated PSA opaque execution with s200 and its secure key storage. Switched from PSA transparent mode to opaque mode for all functions except `CMAC_LsbFirstInput()` which is currently not supported in opaque version. Optimized `SecLib_psa_config` to fully accelerate all `PSA_WANT_KEY_TYPE_ECC_KEY_PAIR` functions.

    - **Minor Changes**
        - [wireless_mcu][ble] Refactored `PLATFORM_SetBleMaxTxPower()` API moved from platform file to `fwk_platform_ble.c` for Zephyr compatibility.
        - [wireless_mcu] Modified `PLATFORM_GetBDAddr()` to return consistent address across calls when `gPlatformUseHwParameter_d` is disabled.
        - [Common] Enhanced external flash API with C++ compatibility by adding extern "C" guards.
        - [wireless_nbu] Replaced `FPGA_TARGET` guard with `FWK_KW43_MCXW70_NBU_FAMILIES` for CPU clock configuration to better reflect target family.
        - [DBG] Disabled DTEST signals and GPIO debug for debug target to prevent significant low power current consumption degradation.
        - [kw45_k32w1_mcxw71][kw47_mcxw72] Removed use of SIRCCSR SDK definitions for wakeup by UART0.
        - [platform] Added platform abstraction macros `PLATFORM_GET_IPSR`, `PLATFORM_SET_INT_MASK`, and `PLATFORM_CLEAR_INT_MASK` to allow platform-specific customization of IPSR read and interrupt mask functions while maintaining backward compatibility.

    - **Bug Fixes**
        - [OTA][Coverity] Sanitized the `pImageOffset` parameter in OTA functions to avoid possible overflow.
        - [SecLib] Fixed multiplication buffer pointer initialization for segmented ECDH operations. Fixed EC P256 multistep operations using SW legacy library. Fixed `ECDH_P256_ComputeDhKeySeg()` and `ECDH_P256_GenerateKeysSeg()` argument checking across SecLib variants. Fixed `SecLib_AES_CMAC_PRF_128()` behavior for SecLib sss variant that tolerated VK length to be 0. Removed unreachable code from `SecLib_HMAC_SHA256_Finish()`.
        - [Platform] Fixed TSTMR timestamp 64 bit read compilation failure when `gPlatformTstmr32Bit_d` is undefined.
        - [NVM] Fixed initialization procedure in `InitNVMConfig()` to validate `start_addr` and `partition_size`.
        - [wireless_nbu] Fixed resource access issue by reverting TSTMR read restriction on NBU as underlying issue has been resolved.
        - [wireless_mcu][wireless_nbu] Fixed timestamp initialization to ensure a defined value when the `tstmrId` is out of range.
        - [SecLib_RNG] Corrected copyright header in `seclib.c`.
        - [MISRA] Various MISRA and CERT-C compliance fixes in NVM module.

