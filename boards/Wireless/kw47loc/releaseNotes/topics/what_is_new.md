# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.06.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Added LE Power Control support in BLE Shell application.
	-   LE Read All Remote Features (LLEFS) support in HOST-GAP.
	-   LE Channel Assessment (CHAS) Config HCI command support in HOST-GAP.

    ### Improved
	-   CS procedure auto-loop shell command; improved RAS data drop mechanism.
	-   Allow setting the value of the `setnumprocs` parameter to `0` for infinite CS procedure repeats.
	-   Subevent interval added to RADE algorithm API.
	-   Documentation updates.

    ### Fixed
	-   L2CAP data fragmentation fix causing incorrect fragmentation over the air.
	-   Fix for no valid subevents in localization.
	-   Allowed the value `255` for the `sub_mode_type` parameter in CS config params.
	-   Channel Sounding subevent abort (No CS_SYNC mode0) after rebond.
	-   Set `preferredPeerAntenna` based on peer capabilities.
	-   Miscellaneous minor application bug fixes.

    ### Changed
	-   Reduced cyclomatic complexity (CCM) in multiple localization functions.
	-   Decoupled buttons from LEDs in Bluetooth applications.

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
    LE Power Control:
      -   Fixed LE Power Control (LEPC) failures on EBQ (LL/PCL/CEN/BV-01-C, LL/PCL/CEN/BV-36-C, LL/PCL/CEN/BV-40-C, LL/PCL/PER/BV-01-C, LL/PCL/PER/BV-29-C, LL/PCL/PER/BV-40-C, LL/PCL/PER/BV-49-C).
    LL Extended Feature Set:
      -   Fixed Extended Feature Set EBQ test failures (HCI/CIN/BV-15-C, LL/CON/CEN/BV-164-C, LL/CON/CEN/BV-165-C, LL/CON/CEN/BV-166-C, LL/CON/PER/BV-168-C, LL/CON/PER/BV-169-C, LL/CON/PER/BV-170-C).
    Channel Sounding:
      -   Fixed CS capabilities exchange failures in central role (LL/CS/CEN/INI/BV-03-C, LL/CS/CEN/REF/BV-03-C).
      -   Fixed CS_IND rejection due to incorrect PHY validation (TX PHY vs RX PHY).
    Periodic Advertising Sync Transfer:
      -   Fixed Periodic Advertising sync lost event not generated after losing sync in PAST mode or when sync timeout smaller than Periodic Advertising interval.
      -   Fixed sync offset management when value exceeds maximum (PAwR intervals in seconds range).

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

