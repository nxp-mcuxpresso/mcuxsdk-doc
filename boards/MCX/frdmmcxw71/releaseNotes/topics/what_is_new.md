# What is new

The following changes have been implemented compared to the previous SDK release version \(24.12.00-pvw2\).


-   **Bluetooth LE host stack and applications**
    -  Minor fixes and stability improvements
    -  Documentation updates

-   **Bluetooth LE controller**
    -  Added initial experimental support for Bluetooth LE Controller feature: Periodic Advertising with Responses \(PAwR)\
    -  Minor fixes and stability improvements

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration

-   **Connectivity framework**

    -   **Minor Changes (no impact on application)**

        - [Platform]
            - Ignore the secure bit from RAM addresses when comparing used ram bank in bank retention mechanism
            - Add `gPlatformNbuDebugGpioDAccessEnabled_d` Compile Macro (enabled by default). Can be used to disable the NBU debug capability using IOs in case Trustzone is enabled (``PLATFORM_InitNbu()` code executed from unsecure world).
            - Fix in NBU firmware when sending ICS messages gFwkSrvNbuApiRequest_c (from controller_api.h API functions)
        - [OTA]
            - Add choice name to OtaSupport flash selection in Kconfig
        - [NVM]
            - Add gNvmErasePartitionWhenFlashing_c feature support to gcc toolchain
        - [SecLib_RNG]
            - Misra fixes

    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)

-   **Zigbee and IEEE 802.15.4**
    -  Added Zigbee Pro 2023 and examples applications for ZC, ZR, ZED
    -  Introduced experimental support for MAC split architecture with FreeRTOS host stack and examples applications for ZC, ZR, ZED 
    -  Fixed PHY low power timer cancellation
    -  Minor fixes for Zigbee PRO R22 configuration
    -  Minor fixes and stability improvements for connectivity_test example application
    -  Fixed the size of TLVs for Node_desc_req in R23 examples