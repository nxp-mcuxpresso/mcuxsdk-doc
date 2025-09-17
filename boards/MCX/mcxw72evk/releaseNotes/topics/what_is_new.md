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

-   **Connectivity framework**

    -   **Major Changes**
        -   [wireless_mcu][wireless_nbu] Introduced PLATFORM_Get32KTimeStamp() API, available on platforms that support it.
        -   [RNG] Switched to using a workqueue for scheduling seed generation tasks.
        -   [Sensors] Integrated workqueue to trigger temperature readings on periodic timer expirations.
        -   [wireless_nbu] Removed outdated configuration files from wireless_nbu/configs.
        -   [SecLib_RNG][PSA] Added a PSA-compliant implementation for SecLib_RNG. ⚠️ This is an experimental feature and should be used with caution.
        -   [wireless_mcu][wireless_nbu] Implemented PLATFORM_SendNBUXtal32MTrim() API to transmit XTAL32M trimming values to the NBU.
    -   **Minor Changes (no impact on application)**
        -   [MWS] Migrated the Mobile Wireless Standard (MWS) service to the public repository. This service manages coexistence between connectivity protocols such as BLE, 802.15.4, and GenFSK.
        -   [HWParameter][NVM][SecLib_RNG][Sensors] Addressed various MISRA compliance issues across multiple modules.
        -   [Sensors] Applied a filtering mechanism to temperature data measured by the application core before forwarding it to the NBU, improving data reliability.
        -   [Common] Relocated the GetPowerOfTwoShift() function to a shared module for broader accessibility across components.
        -   [RNG] Resolved inconsistencies in RNG behavior when using the fsl_adapter_rng HAL by aligning it with other API implementations.
        -   [SecLib] Updated the AES CMAC block counter in AES_128_CMAC() and AES_128_CMAC_LsbFirstInput() to support data segments larger than 4KB.
        -   [SecLib] Utilized sss_sscp_key_object_free() with kSSS_keyObjFree_KeysStoreDefragment to avoid key allocation failures.
        -   [WorkQ] Increased workqueue stack size to accommodate RNG usage with mbedtls.
        -   [wireless_mcu][ot] Suppressed chip revision transmission when operating with nbu_15_4.
        -   [platform][mflash] Ensured proper address alignment for external flash reads in PLATFORM_ReadExternalFlash() when required by platform constraints.
        -   [RNG] Corrected reseed flag behavior in RNG_GetPseudoRandomData() after reaching gRngMaxRequests_d threshold.
        -   [platform][mflash] Fixed uninitialized variable issue in PLATFORM_ReadExternalFlash().
        -   [platform][wireless_nbu] Fixed an issue on KW47 where PLATFORM_InitFro192M incorrectly reads IFR1 from a hardcoded flash address (0x48000), leading to unstable FRO192M trimming. The function is now conditionally compiled for KW45 only.


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
