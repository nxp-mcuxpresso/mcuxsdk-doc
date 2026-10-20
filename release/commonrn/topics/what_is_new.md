# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.09.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Note: Version 1.10.23 is the first NXP Bluetooth LE Host release officially certified according to the Bluetooth® Core Specification Version 6.3.

    ### Added
	-   Low Energy (LE) Power Control can now be enabled/disabled at application level via `gHostInclusionLePowerControl_d`.

    ### Improved
	-   Platform Security Architecture (PSA) integration: optimized BLE Host stack size per application for KW43/MCXW70.
	-   Reduced anchor monitoring current consumption by lowering the monitoring rate.
	-   Anchor Monitor: added Received Signal Strength Indicator (RSSI) value display.
	-   KW43 BLE Host memory review and optimization.
	-   Handover time synchronization optimization.
	-   Ranging algorithm productization: added logging module and result streaming.

    ### Fixed
	-   Fixed Bluetooth Channel Sounding (BTCS) server corrupting L2CAP segments when the step data of a subevent spans a segment boundary.
	-   Handover: added API to set the LL CS context by monitored connection handle, fixing `Gap_HandoverSetCsLlContext` after handover in the KW47 CS CCC demo.
	-   Handover: correctly handle `gHandoverAnchorSearchStartLl_c` on supervision timeout.
	-   Fixed Host Privacy scan response data length mismatch (31 versus 17 bytes).
	-   Fixed BusFault in the RADE algorithm caused by invalid buffer pointers.
	-   Fixed digital_key CS and localization application failures on frdmkw43/kw43loc.
	-   Prevented out-of-bounds array access and enforced NULL pointer detection in sample applications.
	-   Fixed KW43-LOC RF switch control.
	-   Fixed distance measurement accuracy (~0.5 m double-correction) and refined phase correction.
	-   Ensured that `csAlgoBuf` is the last member in its structure.
	-   Miscellaneous Coverity fixes.
	-   Miscellaneous CERT-C fixes.
	-   Miscellaneous MISRA fixes.
	-   Miscellaneous MSG fixes.

    ### Changed
	-  Added application-level mitigation for Bluetooth Low Energy Re-Pairing (BLERP) forced re-pairing attacks.
	-  Removed dead reassembly code from the BTCS client.

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

-   **IEEE 802.15.4**
     - API cleanup: remove unmaintained slotted support
     - support for MAC split architecture
       - fix condition to enter low power
     - minor fixes and stability improvements for connectivity_test example application
     - experimental support for mcxw72 NBU core

-   **Zigbee**
      - NCP Host Updates and fixes
      - R23 fixes
        - Device can't establish a new TCLK through ZDO Start Key Update procedure
        - Security Start Key Update Request is not relayed to joining ZED in multi hop key negotiation
      - propagate APS ACK to end-user application
      - documentation updates
