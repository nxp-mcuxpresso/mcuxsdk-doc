# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.06.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Tire Pressure Monitoring System (TPMS) sample demo applications.
	-   Tire Pressure Monitoring System (TPMS) documentation added to the Demo Applications User Guide (DAUG).
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
        - [SecLib] Refactored SecLib functions with improved error handling and naming conventions. Added return status codes for better testing, added the `SecLib_` prefix for all functions with backward compatibility maintained via `#define` stubs. Added parameter checks on all functions and improved test coverage for all SecLib flavors.
        - [SecLib] Updated CryptoLibSW APIs by removing unused pMultiplicationBuffer argument from `Ecdh_ComputeDhKeyUltraFast()`, `ECP256_GeneratePublicKeyUltraFast()`, and `ECP256_GenerateKeyPairUltraFast()`. Renamed `ECP256_GeneratePublicKey()` to `ECP256_GeneratePublicKeySeg()` in legacy implementation. Added new `ECP256_GeneratePublicKey()` API for SPAKE2+ ComputeL procedure.

    - **Minor Changes**
        - [FunctionLib] Enhanced `FLib_StrLen()` to return an error value when the string size exceeds maximum limit (4096 bytes), adopting strnlen behavior.
        - [Common] Cleaned deprecated mbedtls2x Kconfig configurations.
        - [wireless_mcu][lcl] Updated FEM API to send configuration to NBU for proper XCVR timing adaptation during Channel Sounding activity. XCVR register backup and restore uses current mechanism with config sent through `PLATFORM_NbuApiReq()`.
        - [SecLib_RNG] Removed support for deprecated devices including `FSL_FEATURE_SOC_SIM_COUNT` for RNG and QN908x platforms.
        - [FactoryDataProvider] Removed deprecated FactoryDataProvider service as it is no longer used following mbedtls2.x deprecation.

    - **Bug Fixes**
        - [wireless_mcu] Fixed FRO6M calibration failure in OEM closed lifecycle by replacing inaccessible DWT cycle counter with SysTick timer. The implementation saves/restores SysTick state to maintain FreeRTOS compatibility.
        - [wireless_mcu][ble] Removed redundant assert in `PLATFORM_SendHciVendorEvent()` as invalid parameters are already sanitized with the error returned to the caller.
        - [SecLib] Fixed `CMakeLists.txt` lib_crypto variant dependency.
        - [MISRA] Various MISRA compliance fixes in OTA, flash related files, FSCI, NVM, platform files, and ICS modules. Fixed potential flash blank check issue with unaligned pointers and split `OTA_PostWriteToFlash()` to match the `HIS_LEVEL` constraint. Also prevented infinite loop in `FLib_StrLen()` and ensured that unions have a consistent non-zero size across compilers.

