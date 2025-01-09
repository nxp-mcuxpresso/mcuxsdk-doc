# What is new 

MCUXpresso SDK version 24.12.00 is an early adopter release provided as preview for early development.

The following changes have been implemented compared to the previous SDK release version \(24.12.00-pvw2\).

-   **Bluetooth LE host stack and applications**
    -   Minor fixes and stability improvements
    -   Documentation updates

-   **Bluetooth LE controller**
    -   Added support for Bluetooth LE Channel Sounding
    -   Minor fixes and stability improvements

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

    -   **Minor Changes (no impact on application)**

        - [Platform]
            - Ignore the secure bit from RAM addresses when comparing used ram bank in bank retention mechanism
        - [OTA] 
            - Add choice name to OtaSupport flash selection in Kconfig
        - [NVM]
            - Add gNvmErasePartitionWhenFlashing_c feature support to gcc toolchain
        - [SecLib_RNG]
            - Misra fixes

-   **Zigbee and IEEE 802.15.4**
    -  Minor fixes for Zigbee PRO R22 configuration.
    -  Zigbee Pro 2023 Configuration is not supported in this release.
    