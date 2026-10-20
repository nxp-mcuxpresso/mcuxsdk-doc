# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.09.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Note: Version 1.10.23 is the first NXP Bluetooth LE Host release officially certified according to the Bluetooth® Core Specification Version 6.3.

    ### Added
	-   LE Power Control can now be enabled/disabled at application level via `gHostInclusionLePowerControl_d`.

    ### Improved
	-   Reduced anchor monitoring current consumption by lowering the monitoring rate.
	-   Anchor Monitor: added RSSI value display.
	-   Handover time synchronization optimization.
	-   Ranging algorithm productization: added logging module and result streaming.

    ### Fixed
	-   Fixed BTCS server corrupting L2CAP segments when a subevent's step data spans a segment boundary.
	-   Handover: added API to set the LL CS context by monitored connection handle, fixing `Gap_HandoverSetCsLlContext` after handover in the KW47 CS CCC demo.
	-   Handover: correctly handle `gHandoverAnchorSearchStartLl_c` on supervision timeout.
	-   Fixed Host Privacy scan response data length mismatch (31 vs 17 bytes).
	-   Fixed BusFault in the RADE algorithm caused by invalid buffer pointers.
	-   Prevented out-of-bounds array access and enforced NULL pointer detection in sample applications.
	-   Fixed distance measurement accuracy (~0.5 m double-correction) and refined phase correction.
	-   Ensured `csAlgoBuf` is the last member in its structure.
	-   Miscellaneous Coverity fixes.
	-   Miscellaneous CERT-C fixes.
	-   Miscellaneous MISRA fixes.
	-   Miscellaneous MSG fixes.

    ### Changed
	-  Added application-level mitigation for BLERP forced re-pairing attacks.
	-  Removed dead reassembly code from the BTCS client.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    - Fixed EBQ failure — packet time restrictions not applied after LL_PHY_RSP (LL/CON/PER/BV-53-C).
    PAwR:
    - Fixed memory leak in PAWR.
    Handover:
    - Fixed an issue where after connection handover the connection update procedure causes a disconnection.
    LEPC:
    - Fixed EBQ LEPC coded phy tests (LL/PCL/CEN/BV-36-C, LL/PCL/CEN/BV-40-C, LL/PCL/PER/BV-29-C, LL/PCL/PER/BV-40-C).
    Channel Sounding:
    - Fixed incorrect reporting of mode0 step quality in case of CS sniffer mode.
    - Fixed and issue where BT SIG CS sniffing demo may crash in NBU when environment is noisy.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control Power Amplifier (PA) ramp type and duration.

-   **Connectivity framework**

    - **Major Changes**
        - [platform][DBG] Moved the NBU software watchdog (handshake based NBU stuck detection) into the common platform_dbg sources, making the feature available on both KW43/MCXW70 and KW47/MCXW72 without additional files.
        - [NVM] Refactored NVM handling to centralize address computation using offset-based flash access helpers (`*_AtOffset`) instead of stored flash addresses, reducing unsafe pointer arithmetic. `NvUpdateSize()` now returns `uint16_t`, added `NV_PartitionBlankCheckAtOffset()`, and deprecated `NvIsMemoryAreaBlank()`. Also fixed a data integrity issue in `NvSaveAllDataSetEntry()` and various Coverity/CERT-C findings.
        - [platform] IFR BLE BD address is now reversed to match the BLE Host stack expectation. The `PLATFORM_IFR_BD_ADDR_IS_MSB_FIRST` option was removed with the reverse loop reworked accordingly.
        - [OTA] Introduced `gOtaEraseWholePartitionOnInit_d` option (KW43 only, disabled by default) to erase the whole OTA partition at start of image transfer.
        - [wireless_mcu] Replaced the critical section in `PLATFORM_RemoteActiveReq()` and `PLATFORM_RemoteActiveRel()` with a shared mutex to reduce critical section duration. These APIs must not be called from ISR anymore.
        - [wireless_nbu] Updated the low power callback to check for pending RPMSG buffers so the NBU enters WFI only when a Tx message is pending, reducing main core latency.

    - **Minor Changes**
        - [platform][zephyr] Zephyr feature flag overrides are now owned by the framework repo in a per platform `configs/fwk_config_zephyr.h`, included at the top of `fwk_config.h` under `__ZEPHYR__`, removing the dual maintenance with the Zephyr integration. Platforms: kw43_mcxw70, kw45_k32w1_mcxw71, kw47_mcxw72, mcxw23, rw61x.
        - [DBG] The NBU debug path now preserves the first fault/assert information: `NBUDBG_StateCheck()` no longer consumes the NBU debug state before a consumer callback is registered, the `sys_debug_panic_triggered` guard is hoisted in the hard fault handler so capture, host indication and coredump only run for the first fault, and only the first fault/assert is recorded through the new `NBUDBG_RECORD_CLAIMED()` macro.
        - [DBG] Added host-triggered NBU force fault for coredump capture through new `PLATFORM_ForceNbuFault()` and `NBUDBG_ForceNbuFault()` APIs, signaled to the NBU over MCMGR.
        - [DBG] Deferred the stall HCI event out of `NBUDBG_StateCheck()`, which now only sets the halted state and notifies the callback. Added new `NBUDBG_SendStallEvent()` API to emit the stall vendor event on demand.
        - [DBG] Integrated Zephyr coredump capture into the app-core fault handler under `CONFIG_DEBUG_COREDUMP`.
        - [NVS] Replaced `memcpy()` by `HAL_FlashRead()` for internal flash reads so that HAL checks and Async Flash mode synchronization are not bypassed.
        - [wireless_mcu] Added the missing `fwk_config.h` as first include in the kw43_mcxw70, kw45_k32w1_mcxw71 and kw47_mcxw72 platform files so that feature flag overrides are taken into account.
        - [settings] Added IAR compiler support for iterable sections and disabled the `SETTINGS_NAME_END` IAR warning.
        - [SecLib_RNG] Added to `RNG_psa.c` seed support including WorkQueue-based automatic reseeding `gRngEnableAutoReseed_d`, NBU seed forwarding via `PLATFORM_SendRngSeed()`, reseed counter logic `gRngMaxRequests_d`, and new APIs `RNG_NotifyReseedNeeded()` and `RNG_IsReseedNeeded()`.
        - [OTA] Added a blank check of the OTA partition to avoid unnecessary erase operations and refactored `OTA_MakeHeadRoom()`.

    - **Bug Fixes**
        - [WorkQ] Increased the default `FWK_SYSWORKQ_STACK_SIZE` from 608 to 640 bytes to fix a stack overflow on the system work queue thread.
        - [platform][TSTMR] Fixed the 56 bit version of the timestamp, now reading the TSTMR instance base and testing only the base pointer validity.
        - [wireless_mcu] Fixed FRO6M calibration by replacing `FWK_MRCC_TSTMR0_CC`/`FWK_MRCC_TSTMR0_MUX` macros with `MRCC_CC`/`MRCC_MUX` from `fsl_clock.h` and preserving the MUX clock selection in `PLATFORM_StartFro6MCalibration()`.
        - [DBG] Guarded FreeRTOS `sys_dump_callstack_ext()` with `INCLUDE_xTaskGetHandle` to fix `-Werror=unused-function` build failures.
        - [zephyr][lib][crc] Fixed build conflict with EdgeFast OPN CRC by guarding CRC sources with the Zephyr common framework component check to avoid symbol redefinition.
        - [NVM] Fixed offset validation in `NvGetEntryFromDataPtr()` and corrected the bottom record address calculation in `NvGetPageFreeSpace()` when `gUnmirroredFeatureSet_d` is undefined.
        - [docs] Fixed Sphinx/docutils warnings and errors in the framework documentation.
        - [SFC] Prevent unnecessary SFA measurement retrieval when SFC is disabled by adding a check in the SFC ISR to verify that the SFC module is enabled before retrieving the SFA frequency measurement.
        - [Coverity] Various Coverity compliance fixes in SecLib (DHKey handling in `SecLib_GenerateBluetoothF5KeysSecure()`) and OTA (replaced union with structure for callback/argument passing in message buffer).
        - [MISRA][CERT-C] Various MISRA, CERT-C and Coverity compliance fixes gathered across platform, LowPower, ICS (wireless_mcu and wireless_nbu), OTA, FSCI, SFC, SecLib and NVM modules.
