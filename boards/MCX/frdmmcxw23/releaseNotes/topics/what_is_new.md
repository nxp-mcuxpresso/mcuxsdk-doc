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

-   **Connectivity framework**

    - **Major Changes**
        - [NVM] Refactored NVM handling to centralize address computation using offset-based flash access helpers (`*_AtOffset`) instead of stored flash addresses, reducing unsafe pointer arithmetic. `NvUpdateSize()` now returns `uint16_t`, added `NV_PartitionBlankCheckAtOffset()`, and deprecated `NvIsMemoryAreaBlank()`. Also fixed a data integrity issue in `NvSaveAllDataSetEntry()` and various Coverity/CERT-C findings.
        - [SecLib_RNG] Enabled PSA by default on KW43/MCXW70 platforms.

    - **Minor Changes**
        - [platform][zephyr] Zephyr feature flag overrides are now owned by the framework repo in a per platform `configs/fwk_config_zephyr.h`, included at the top of `fwk_config.h` under `__ZEPHYR__`, removing the dual maintenance with the Zephyr integration. Platforms: kw43_mcxw70, kw45_k32w1_mcxw71, kw47_mcxw72, mcxw23, rw61x.
        - [NVS] Replaced `memcpy()` by `HAL_FlashRead()` for internal flash reads so that HAL checks and Async Flash mode synchronization are not bypassed.
        - [settings] Added IAR compiler support for iterable sections and disabled the `SETTINGS_NAME_END` IAR warning.
        - [SecLib_RNG] Added to `RNG_psa.c` seed support including WorkQueue-based automatic reseeding `gRngEnableAutoReseed_d`, NBU seed forwarding via `PLATFORM_SendRngSeed()`, reseed counter logic `gRngMaxRequests_d`, and new APIs `RNG_NotifyReseedNeeded()` and `RNG_IsReseedNeeded()`.
        - [OTA] Added a blank check of the OTA partition to avoid unnecessary erase operations and refactored `OTA_MakeHeadRoom()`.

    - **Bug Fixes**
        - [NVM] Fixed offset validation in `NvGetEntryFromDataPtr()` and corrected the bottom record address calculation in `NvGetPageFreeSpace()` when `gUnmirroredFeatureSet_d` is undefined.
        - [docs] Fixed Sphinx/docutils warnings and errors in the framework documentation..
        - [Coverity] Various Coverity compliance fixes in SecLib (DHKey handling in `SecLib_GenerateBluetoothF5KeysSecure()`) and OTA (replaced union with structure for callback/argument passing in message buffer).
        - [MISRA][CERT-C] Various MISRA, CERT-C and Coverity compliance fixes gathered across platform, LowPower, ICS (wireless_mcu and wireless_nbu), OTA, FSCI, SFC, SecLib and NVM modules.
