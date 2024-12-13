# What is new

MCUXpresso SDK version 24.12.00-pvw2 is an early adopter release provided as preview for early development.

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