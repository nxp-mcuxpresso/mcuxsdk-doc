# What is new

The following changes have been implemented compared to the previous SDK release version \(25.09.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
    -   CCC sample applications updated to **CCC Digital Key v4.0.0** Specification.


    ### Improved
    -   Various sample applications have been updated.

    ### Fixed
    -   Ble_shell updated to set the Random Static Address properly.
    -   Always set the Advertising Legacy Set handle if the legacy API was used.
    -   PAWR parameters in PeriodicSyncTransferReceived are now parsed correctly.
    -   Ensure an RPA/NRPA is properly set from the application to enable a central using Controller Privacy to connect to unbonded peripherals.
    -   Various sample applications bug fixes applied.

    ### Changed
    -   Merged Gap_SetExtAdvertisingParameters and Gap_SetExtAdvertisingParametersV2 into **Gap_SetExtAdvertisingParameters**.
    -   BLE_Shell prints Random Static address as identity address instead of the Public Device Address.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    -   Remove support for Channel Sounding.
    -   Fix Periodic Advertising interval field in HCI Extended advertising reports.
    -   Manage procedure collisions between PAST and connections.
    -   Do not send Periodic Advertising reports with "Failed to received" status if the reports are not enabled (PAWR).
    -   Fix DTM RX failure when the first packet is received with incorrect smaller packet length and invalid CRC.

-   **Transceiver Drivers (XCVR)**
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

-   **Zigbee**
      - NCP Host Updates and fixes
      - R23 fixes
        - Device can't establish a new TCLK through ZDO Start Key Update procedure
        - Security Start Key Update Request is not relayed to joining ZED in multi hop key negotiation
      - propagate APS ACK to end-user application
      - documentation updates
