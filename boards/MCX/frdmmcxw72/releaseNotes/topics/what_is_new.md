# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw1\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
    -   Threshold for the invalid number of Anchor Monitor events received by the target anchor
    -   **Experimental Monitoring Advertisers** feature in Bluetooth LE Host
    -   **Experimental Randomized RPA** feature in Bluetooth LE Host
    -   Application defines for default connection and default advertising tx power

    ### Improved
    -   Miscellaneous applications updates
    -   Central applications now wait for status of Encrypt procedure in case of bonded device
    -   Logging data on localization applications
    -   NBU Low Power Mode enabled by default for Localization Applications
    -   PCT rotation calibration added to localization apps
    -   Configured CS Reflector to start the CS procedure with the tdm command and updated the documentation
    -   Populated the optionalSubfeaturesSupported field correctly
    -   Prevented CORE 0 from entering deep sleep while LCE is computing by setting the low power mode constraint to PWR_WFI during LCE computation and releasing it afterwards
    -   Implemented in CCC_CS, Channel Sounding data transfer from the anchor to the device
    -   Documentation miscellaneous updates
    -   Updated armgcc ld linker files to take gUseInternalStorageLink_d flag value into consideration

    ### Fixed
    -   Memory issue when setting scan response data would return an error status from the LL
    -   Set advertises with the public address, overwritten by a previously used random address on receiving the Advertising Set Terminated event

    ### Changed
    -   Updated memory configuration: replaced the extended heap area in the available SMU2 memory with a 24KB array in the data1
    -   Removed redundant cached remote capabilities write on reflectors, as the initiator will always trigger a capabilities exchange and trying to write cached capabilities afterwards results in an HCI error

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Channel sounding updates:
        -   Fixed the RF-PHY receiver testcases (RF-PHY/RCV-LE/CA/BV-7-C, RF-PHY/RCV-LE/CA/BV-13-C, RF-PHY/RCV-LE/CA/BV-30-C, RF-PHY/RCV-LE/CA/BV-31-C).
        -   Fix provided to set bit in pHadmConn->uiFlags for rxed LL_CS_CAPABILITIES_REQ/RSP, allow multiple LE CS Write Cached Remote Supported Capabilities.
        -   RTT bias compensation : Updated software to align with Chip IFR version 2.5

    - PAwR/PAST updates:
        -   Fixed multiple responses formatting in the Periodic Advertising Responses report.
        -   Fixed the double message allocation causing a memory leak.

    - DBAF update:
        -   Fixed case where sometimes AUX_ADV_IND with LE Coded Phy was not scheduled.
        
    - Fixed handling of duplicate Connection Request using different Peer RPA (LL/SEC/ADV/BI-01-C & LL/SEC/INI/BI-01-C conformance tests).
    - Fixed the missing chained packet TX when coded PHY is used on multiple Advertising sets and the Advertising interval is small (LL/DDI/ADV/BV-30-C conformance test).
    - Fixed issue with packet time restrictions after PHY update (packet payload too long). This fixes the LL/CON/PER/BV-53-C, LL/CON/PER/BV-56-C and LL/CON/PER/BV-59-C conformance tests.
    - Fixed case where address resolution was stuck.

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
