# What is new

The following changes have been implemented compared to the previous SDK release version \(25.09.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
    -   **RAS/RAP PTS** 8.7.4 test support added in Localization Sample applications.
    -   Support for CS start procedure while the previous procedure is not completed; old procedure replaced with the new one.
    -   Support for arm gcc for ncp_loc_reader.

    ### Improved
    -   Localization Sample Applications Ram partition.
    -   **RAS/RAP** profile and service.
    -   Various sample applications have been updated.

    ### Fixed
    -   Privacy setting issue on ncp_loc_reader.
    -   Extended NBU FSCI message handling issue.
    -   Ble_shell updated to set the Random Static Address properly.
    -   Always set the Advertising Legacy Set handle if the legacy API was used.
    -   fsci_bridge and w_uart_host memory leak.
    -   PAWR parameters in PeriodicSyncTransferReceived are now parsed correctly.
    -   Ensure an RPA/NRPA is properly set from the application to enable a central using Controller Privacy to connect to unbonded peripherals.
    -   CS algorithm buffer overwrite issue during Connection Handover application.
    -   Various sample applications bug fixes applied.
    -   Pass correct Codded PHY (S2) to Channel Sounding Set Procedure Parameters.

    ### Changed
    -   Merged Gap_SetExtAdvertisingParameters and Gap_SetExtAdvertisingParametersV2 into **Gap_SetExtAdvertisingParameters**.
    -   ce_status_buffer type changed to int32_t.
    -   BLE_Shell prints Random Static address as identity address instead of the Public Device Address.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Channel sounding updates:
        -   Handle Procedure collision between LLCP CS Procedure and non-CS Procedure and between two LLCP CS procedures.
        -   Start Feature Exchange autonomously if needed prior initiating the CS Capability Exchange Procedure.
        -   Fix CS Procedure aborted with CS_SYNC=2Mbps and T_PM=40.
        -   Fix phase accuracy bias when CFO is high [-50ppm, +50ppm].
        -   Fix RTT bias due to chip sample RC Calibration imprecision. Chip IFR now contains appropriate calibration value used by software to compensate associated delay.
        -   Fix wrong PRBS payload coding in HADM test mode.
        -   Fix testmode generating more than one subevent with subevt_int=0 and more than 160 steps.
        -   Fix CS handover regression due to MISRA fix.
        -   Use precompiled libraries for CS support.

    - PAwR/PAST updates:
        -   Window widening for PAwR responses supports the worst clock accuracy (500ppm) to avoid interoperability issues.
        -   Autonomous Feature Exchange is done prior PAST Procedure.
        
    - Fix Connection Update state machine on peripheral side after Connection Update rejection.
    - Fix to handle correctly concurrent Connection Update procedures initiated by peer and local devices on different connections.
    - Support 4 Advertising set with optimized Advertising placement when Advertising intervals are multiple of each other.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework (compared to 25.06.00 release)**

    -   **Major Changes**
        - [wireless_mcu] Replaced the ICS RX linked list with message queue to eliminate memory allocation in the ISR context and enable user callbacks to run in thread context where memory allocation is permitted.
        - [wireless_mcu] Added HCI RX workqueue processing support to reduce ISR execution time and system impact. Feature controlled by `gPlatformHciUseWorkqueueRxProcessing_d` configuration option (enabled by default on kw45_k32w1_mcxw71 and kw47_mcxw72 platforms in freertos applications). When enabled, HCI transport processes received data in system workqueue thread, allowing user callbacks to run in thread context.
        - [wireless_nbu] Introduced `PLATFORM_ConfigureSmuDmemMapping()` API to configure SMU and DMEM sharing on NBU for kw47_mcxw72 platform, using linker file symbols for correct configuration.
        - [wireless_mcu][wireless_nbu] Added NBU2Host event manager for status indications to host (Information, Warning, Error) sent over RPMSG.
        - [wireless_mcu] Added a call to `PLATFORM_IcsRxWorkHandler()` within `PLATFORM_NbuApiReq()` for baremetal applications to prevent potential deadlocks.
        - [wireless_mcu] Adjusted default value of `BOARD_RADIO_DOMAIN_WAKE_UP_DELAY` from 0x16 to 0x10 to address stability issues observed with the previous setting. This change enhances system reliability but will reduce low-power performance.
        - [wireless_nbu] Enhanced XTAL32M trimming handling: updates are applied when requested by the application core and the NBU enters low-power mode, ensuring no interference from ongoing radio activity. Introduced new APIs to lock (`PLATFORM_LockXtal32MTrim()`) and unlock XTAL32M (`PLATFORM_UnlockXtal32MTrim()`) trimming updates using a counter-based mechanism. Also added a reset API (`PLATFORM_ResetContext()`) for platform-specific variables (currently limited to the trimming lock).
        - [wireless_mcu] Introduced a new API, `PLATFORM_SetLdoCoreNormalDriveVoltage()`, to enable support for NBU clock frequency at 64 MHz, as required by BLE channel sounding applications.
        - [wireless_mcu][wireless_nbu] Increased delayLpoCycle default from 2 to 3 to address link layer instabilities in low-power NBU use cases. Adjusted `BOARD_RADIO_DOMAIN_WAKE_UP_DELAY` from 0x10 to 0x16 to balance power consumption and stability. ⚠️ NBU may malfunction if delayLpoCycle (or `BOARD_LL_32MHz_WAKEUP_ADVANCE_HSLOT`) is set to 2 while `BOARD_RADIO_DOMAIN_WAKE_UP_DELAY` is 0x16.

    -   **Minor Changes (no impact on application)**
        - [wireless_mcu] Fixed variable underflow issue in `PLATFORM_RemoteActiveRel()`.
        - [SecLib_RNG] Fixed escaping local HashKeyBuffer address issue and added missing cast in `RNG_GetTrueRandomNumber()` function.
        - [Common] Fixed heap memory manager return values and added missing include to fwk_freertos_utils.h.
        - [rw61x] Prevented array out of bounds in `PLATFORM_RegisterRtcHandle()`.
        - [FSCI] Fixed memory leak in FSCI module.
        - [NVM] Enhanced debug facilitation by restricting variable scope, assigning return statuses to variables, and fixing display format in `NV_ShowFlashTable()`.
        - [wireless_mcu] Added new chip revision A2.1 support in `PLATFORM_SendChipRevision()` API.
        - [kw47_mcxw72] Implemented BLE BD address retrieval from IFR memory with fallback to OUI + RNG.
        - [DBG] Added ThreadX support to fault handlers and reworked fault handler structure with dedicated RTOS files.
        - [DBG][Common] Added NBU debug support on host side to detect faults and system errors, with debug info extraction capability (limited to MCXW72/KW47).
        - [Common] Platform CMake rework and Kconfig renaming, removing unneeded checks and renaming PRJSEG platform Kconfigs to COMPONENT.
        - [wireless_mcu] Cleaned CMakeLists.txt to avoid wrong inclusions of files and folders from incorrect platforms.
        - [wireless_mcu][wireless_nbu] Added NBU2Host warning when 32MHz crystal is unready on low power exit.
        - [wireless_mcu][ot] Introduced `gPlatformUseOuiFromIfr` to use OUI from IFR for the extended address (disabled by default). When enabled and IFR is not blank, copies first three bytes to OUI field of extended address, otherwise uses static OUI as fallback.
        - [General] Removed useless warning about TSTMR_CLOCK_FREQUENCY_MHZ definition.
        - [General] Updated framework license and SBOM for 25.09 RFP release.
        - [wireless_mcu] Fixed unused variable warning when `gPlatformIcsUseWorkqueueRxProcessing_d` and `gPlatformHciUseWorkqueueRxProcessing_d`are disable
        - [Common] Added MDK compatibility for the errno framework header.
        - [OTA] Enabled calling `OTA_GetImgState()` prior to `OTA_Initialize()`.
        - [wireless_mcu] Fixed `PLATFORM_IsExternalFlashSectorBlank()` to check the entire sector instead of just one page.
        - [OTA] Removed `gUseInternalStorageLink_d` linker flag definition when external OTA storage is used.
        - [wireless_mcu] Resolved counter wrap issue in `PLATFORM_GetDeltaTimeStamp()`.
        - [kw47_mcxw72] Updated shared memory allocation for RPMsg adapter.
        - [kw45_mcxw71][kw47_mcxw72] Moved RAM bank definitions from the connectivity framework to device-specific definitions.
        - [WorkQ] Increased stack size when RNG use mbedtls port and coverage is enabled.
        - [FSCI] Resolved an issue where messages remained unprocessed in the queue by ensuring `OSA_EventSet()` is triggered when pending messages are detected.
        - [OTA] Fixed a bug in `OTA_PullImageChunk()` that prevented retrieval of data previously received via `OTA_PushImageChunk()` when still buffered in RAM during posted operations.
        - [OTA] Various MISRA and coverity fixes.
        - [SFC] Remove obsolete flag `gNbuJtagCapability`.
        - [wireless_mcu] Introduced new API `PLATFORM_GetRadioIdleDuration32K()`. Deprecated `PLATFORM_CheckNextBleConnectivityActivity()` API.
        - [DBG] Cleaned up fwk_fault_handler.c.


Details can be found in [CHANGELOG.md](../../../../../../middleware/wireless/framework/CHANGELOG.md)

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
