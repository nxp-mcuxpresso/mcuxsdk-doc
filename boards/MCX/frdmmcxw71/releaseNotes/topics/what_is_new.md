# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.09.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Note: Version 1.10.23 is the first NXP Bluetooth LE Host release officially certified according to the Bluetooth® Core Specification Version 6.3.

    ### Added
	-   Added Wireless UART support for NBU core-dump packet reception (`gEnableCoredumpPackets`).


    ### Fixed
	-   Fixed ExtendedFeatures mismatch between GAPInit and the `HCILEReadAllRemoteFeaturesCompleteevent`.
	-   Fixed EATT out-of-bounds read in `IsEnhncdChanReconfInProgress()`.
	-   Fixed `GattDbDynamic_AddCharServiceChanged` using Notify instead of Indicate property.
	-   Fixed `ShellGap_ConnectFromPawr` setting the success status incorrectly.
	-   Miscellaneous Coverity fixes.
	-   Miscellaneous CERT-C fixes.
	-   Miscellaneous MISRA fixes.

    ### Changed
	-   Bluetooth 6.3 Compliance: removed Data Signing (LE Security Mode 2).

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    -   Fixed default local SCA to 500 ppm.

-   **Transceiver Drivers (XCVR)**
    -   Added API to control Power Amplifier (PA) ramp type and duration.

-   **Connectivity framework**

    - **Major Changes**
        - [NVM] Refactored NVM handling to centralize address computation using offset-based flash access helpers (`*_AtOffset`) instead of stored flash addresses, reducing unsafe pointer arithmetic. `NvUpdateSize()` now returns `uint16_t`, added `NV_PartitionBlankCheckAtOffset()`, and deprecated `NvIsMemoryAreaBlank()`. Also fixed a data integrity issue in `NvSaveAllDataSetEntry()` and various Coverity/CERT-C findings.
        - [platform] IFR BLE BD address is now reversed to match the BLE Host stack expectation. The `PLATFORM_IFR_BD_ADDR_IS_MSB_FIRST` option was removed with the reverse loop reworked accordingly.
        - [OTA] Introduced `gOtaEraseWholePartitionOnInit_d` option (KW43 only, disabled by default) to erase the whole OTA partition at start of image transfer.
        - [wireless_mcu] Replaced the critical section in `PLATFORM_RemoteActiveReq()` and `PLATFORM_RemoteActiveRel()` with a shared mutex to reduce critical section duration. These APIs must not be called from ISR anymore.
        - [wireless_nbu] Updated the low power callback to check for pending RPMSG buffers so the NBU enters WFI only when a Tx message is pending, reducing main core latency.

    - **Minor Changes**
        - [platform][zephyr] Zephyr feature flag overrides are now owned by the framework repo in a per platform `configs/fwk_config_zephyr.h`, included at the top of `fwk_config.h` under `__ZEPHYR__`, removing the dual maintenance with the Zephyr integration. Platforms: kw43_mcxw70, kw45_k32w1_mcxw71, kw47_mcxw72, mcxw23, rw61x.
        - [NVS] Replaced `memcpy()` by `HAL_FlashRead()` for internal flash reads so that HAL checks and Async Flash mode synchronization are not bypassed.
        - [wireless_mcu] Added the missing `fwk_config.h` as first include in the kw43_mcxw70, kw45_k32w1_mcxw71 and kw47_mcxw72 platform files so that feature flag overrides are taken into account.
        - [settings] Added IAR compiler support for iterable sections and disabled the `SETTINGS_NAME_END` IAR warning.
        - [SecLib_RNG] Added to `RNG_psa.c` seed support including WorkQueue-based automatic reseeding `gRngEnableAutoReseed_d`, NBU seed forwarding via `PLATFORM_SendRngSeed()`, reseed counter logic `gRngMaxRequests_d`, and new APIs `RNG_NotifyReseedNeeded()` and `RNG_IsReseedNeeded()`.
        - [OTA] Added a blank check of the OTA partition to avoid unnecessary erase operations and refactored `OTA_MakeHeadRoom()`.

    - **Bug Fixes**
        - [WorkQ] Increased the default `FWK_SYSWORKQ_STACK_SIZE` from 608 to 640 bytes to fix a stack overflow on the system work queue thread.
        - [platform][TSTMR] Fixed the 56 bit version of the timestamp, now reading the TSTMR instance base and testing only the base pointer validity.
        - [wireless_mcu] Fixed FRO6M calibration by replacing `FWK_MRCC_TSTMR0_CC`/`FWK_MRCC_TSTMR0_MUX` macros with `MRCC_CC`/`MRCC_MUX` from `fsl_clock.h` and preserving the MUX clock selection in `PLATFORM_StartFro6MCalibration()`.
        - [zephyr][lib][crc] Fixed build conflict with EdgeFast OPN CRC by guarding CRC sources with the Zephyr common framework component check to avoid symbol redefinition.
        - [NVM] Fixed offset validation in `NvGetEntryFromDataPtr()` and corrected the bottom record address calculation in `NvGetPageFreeSpace()` when `gUnmirroredFeatureSet_d` is undefined.
        - [docs] Fixed Sphinx/docutils warnings and errors in the framework documentation.
        - [SFC] Prevent unnecessary SFA measurement retrieval when SFC is disabled by adding a check in the SFC ISR to verify that the SFC module is enabled before retrieving the SFA frequency measurement.
        - [Coverity] Various Coverity compliance fixes in SecLib (DHKey handling in `SecLib_GenerateBluetoothF5KeysSecure()`) and OTA (replaced union with structure for callback/argument passing in message buffer).
        - [MISRA][CERT-C] Various MISRA, CERT-C and Coverity compliance fixes gathered across platform, LowPower, ICS (wireless_mcu and wireless_nbu), OTA, FSCI, SFC, SecLib and NVM modules.

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
