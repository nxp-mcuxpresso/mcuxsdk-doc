# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   'Monitoring Advertisers' support in the 'fsci_black_box' and 'ble_shell' applications

    ### Fixed
	-   Missing handler for Version2 of the Set RPA Timeout command

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    Periodic Advertising with Responses (PAwR):
    -  Fixed Periodic Advertising Subevent Data mechanism when handling more than five subevents.
    -  Fixed a problem preventing PAwR from being enabled while another advertising activity was active.

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration.

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