# What is new

The following changes have been implemented compared to the previous SDK release version \(26.03.00-pvw2\).

- **Bluetooth Synopsys controller**
    - Fix scan response not always sent when filtering duplicates is enabled
    - Avoid network privacy if Peer IRK is all zero
    - Take also SID into account when adding a unique entry in the periodic advertiser list
    - Reject peer random static addresses in the resolving list when it does not contain 11 as MSb

- **Bluetooth LE**
    - **Major Changes**
        - Added support for switching to the coded PHY mode.
    - **Minor Changes**
        - [PSA] Added the project_segment Kconfig option to enable selection of an optimized PSA configuration for Bluetooth LE applications.

- **Connectivity Framework**

    - **Major Changes**
        - [SecLib] Refactored SecLib functions with improved error handling and naming conventions. Added return status codes for better testing, added the `SecLib_` prefix for all functions with backward compatibility maintained via `#define` stubs. Added parameter checks on all functions and improved test coverage for all SecLib flavors.
        - [SecLib] Updated CryptoLibSW APIs by removing unused pMultiplicationBuffer argument from `Ecdh_ComputeDhKeyUltraFast()`, `ECP256_GeneratePublicKeyUltraFast()`, and `ECP256_GenerateKeyPairUltraFast()`. Renamed `ECP256_GeneratePublicKey()` to `ECP256_GeneratePublicKeySeg()` in legacy implementation. Added new `ECP256_GeneratePublicKey()` API for SPAKE2+ ComputeL procedure.

    - **Minor Changes**
        - [FunctionLib] Enhanced `FLib_StrLen()` to return an error value when the string size exceeds maximum limit (4096 bytes), adopting strnlen behavior.
        - [Common] Cleaned deprecated mbedtls2x Kconfig configurations.
        - [SecLib_RNG] Removed support for deprecated devices including `FSL_FEATURE_SOC_SIM_COUNT` for RNG and QN908x platforms.
        - [FactoryDataProvider] Removed deprecated FactoryDataProvider service as it is no longer used following mbedtls2.x deprecation.

    - **Bug Fixes**
        - [SecLib] Fixed `CMakeLists.txt` lib_crypto variant dependency.
        - [MISRA] Various MISRA compliance fixes in OTA, flash related files, FSCI, NVM, and platform files. Fixed potential flash blank check issue with unaligned pointers and split `OTA_PostWriteToFlash()` to match the `HIS_LEVEL` constraint. Also prevented infinite loop in `FLib_StrLen()` and ensured that unions have a consistent non-zero size across compilers.
