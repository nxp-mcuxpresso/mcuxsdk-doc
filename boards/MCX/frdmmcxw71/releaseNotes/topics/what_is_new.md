# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.06.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Improved
	-   Aligned wireless_uart preinclude settings across all platforms for consistency.
	-   Updated ble_shell periodic advertising default interval set to 1 second for improved discoverability.
	-   Increased host task stack size across multiple applications.
	-   Extended ble_shell periodic advertising handling to support gPeriodicDeviceScannedV2_c event.

    ### Fixed
	-   Fixed out-of-bounds access in gap.c.
	-   HCI LE Read All Remote Features command is now issued if supported by the controller.
	-   Power Control APIs now return gBleFeatureNotSupported_c if the controller does not indicate support.
	-   Fixed array index overflow in application ranging_client.c.
	-   Corrected bounds check for deviceId.
	-   Fixed wireless_uart mAdvPending flag to prevent multiple advertising starts during multi-peer disconnect.
	-   Fixed systick drift when PWR_DisallowDeviceToSleep() is active.
	-   Miscellaneous MISRA fixes.
	-   Miscellaneous Coverity fixes.

    ### Changed
	-   Reverted incorrect connection handle handling for non-connection enhanced notification events.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
-   Fixed incorrect SCA value (always 500 ppm) reported in LE connection complete event.
    -   Fixed stale byte reported in LE Extended Advertising report when scan response data shrinks between consecutive advertisements.
    -   Fixed new anchor point of connection update overlapping with existing connection.
    -   Fixed Periodic Advertising EBQ test failures after reset due to unreleased buffer and signals (HCI/CCO/BI-124-C, HCI/DDI/BI-50-C).
    -   Fixed issue where the controller failed to reject LL PDUs larger than 26 bytes when no feature exchange was performed (LL/CON/CEN/BV-108-C).
    -   Fixed invalid RSSI value from 0xFF to 0x7F in enhanced notification event.
    -   Fixed KW47 Tx output power exceeding 10 dBm causing RFPHY qualification failures (RFPHY/TRM/BV-01-C, RFPHY/TRM/BV-19-C).
    -   Added new HCI vendor command to retrieve BLE Tx statistics.
    -   Added HCI command to transmit continuously modulated or unmodulated signal for RF tests.
    LL Extended Feature Set:
      -   Fixed Extended Feature Set EBQ test failures (HCI/CIN/BV-15-C, LL/CON/CEN/BV-164-C, LL/CON/CEN/BV-165-C, LL/CON/CEN/BV-166-C, LL/CON/PER/BV-168-C, LL/CON/PER/BV-169-C, LL/CON/PER/BV-170-C).
    Periodic Advertising Sync Transfer:
      -   Fixed Periodic Advertising sync lost event not generated after losing sync in PAST mode or when sync timeout smaller than Periodic Advertising interval.
      -   Fixed sync offset management when value exceeds maximum (PAwR intervals in seconds range).

-   **Transceiver Drivers (XCVR)**
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
        - [DBG] Disabled DTEST signals and GPIO debug for debug target to prevent significant low power current consumption degradation.
        - [kw45_k32w1_mcxw71][kw47_mcxw72] Removed use of SIRCCSR SDK definitions for wakeup by UART0.
        - [platform] Added platform abstraction macros `PLATFORM_GET_IPSR`, `PLATFORM_SET_INT_MASK`, and `PLATFORM_CLEAR_INT_MASK` to allow platform-specific customization of IPSR read and interrupt mask functions while maintaining backward compatibility.

    - **Bug Fixes**
        - [OTA][Coverity] Sanitized the `pImageOffset` parameter in OTA functions to avoid possible overflow.
        - [SecLib] Fixed multiplication buffer pointer initialization for segmented ECDH operations. Fixed EC P256 multistep operations using SW legacy library. Fixed `ECDH_P256_ComputeDhKeySeg()` and `ECDH_P256_GenerateKeysSeg()` argument checking across SecLib variants. Fixed `SecLib_AES_CMAC_PRF_128()` behavior for SecLib sss variant that tolerated VK length to be 0. Removed unreachable code from `SecLib_HMAC_SHA256_Finish()`.
        - [Platform] Fixed TSTMR timestamp 64 bit read compilation failure when `gPlatformTstmr32Bit_d` is undefined.
        - [NVM] Fixed initialization procedure in `InitNVMConfig()` to validate `start_addr` and `partition_size`.
        - [wireless_mcu][wireless_nbu] Fixed timestamp initialization to ensure a defined value when the `tstmrId` is out of range.
        - [SecLib_RNG] Corrected copyright header in `seclib.c`.
        - [MISRA] Various MISRA and CERT-C compliance fixes in NVM module.

-   **IEEE 802.15.4**
     - API cleanup: remove unmaintained slotted support
     - support for MAC split architecture
       - fix condition to enter low power
     - minor fixes and stability improvements for connectivity_test example application

-   **Zigbee**
      - NCP Host Updates and fixes
      - R23 fixes
        - Device can't establish a new TCLK through ZDO Start Key Update procedure
        - Security Start Key Update Request is not relayed to joining ZED in multi hop key negotiation
      - propagate APS ACK to end-user application
      - documentation updates
