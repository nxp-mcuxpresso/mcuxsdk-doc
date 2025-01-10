# What is new

The following changes have been implemented compared to the previous SDK release version \(2.16.100\).

-   **Bluetooth LE host stack and applications**
    -  Added initial experimental support for Bluetooth LE host feature: Periodic Advertising with Responses \(PAwR\)
    -  Added initial experimental support for Bluetooth LE host feature: Encrypted Advertising Data \(EAD\)
    -  Minor fixes and stability improvements

-   **Bluetooth LE controller**
    -  Added initial experimental support for Bluetooth LE Controller feature: Periodic Advertising with Responses \(PAwR)\
    -  Minor fixes and stability improvements

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration

-   **Connectivity framework**

    History can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)

-   **Zigbee and IEEE 802.15.4**
    -  Added Zigbee Pro 2023 and examples applications for ZC, ZR, ZED
    -  Introduced experimental support for MAC split architecture with FreeRTOS host stack and examples applications for ZC, ZR, ZED 
    -  Fixed PHY low power timer cancellation
    -  Minor fixes for Zigbee PRO R22 configuration
    -  Minor fixes and stability improvements for connectivity_test example application
    -  Fixed the size of TLVs for Node_desc_req in R23 examples