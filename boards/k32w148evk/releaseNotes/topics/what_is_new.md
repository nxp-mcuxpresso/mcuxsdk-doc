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

    -   **Major Changes (User Applications may be impacted)**

        -  Supporting CMake/Kconfig for SDK 24.12.00: user shall now use `CmakeLists.txt` and `Kconfig` files from root folder. Compilation should be done using `west build` command. In order to see the Framework Kconfig, use command `west build -t guiconfig`
        -   Board files and linker scripts moved to examples repository

    -   **Bugfixes**

        -   [platform lowpower]
            -   Entering Deep down power mode will no longer call `PLATFORM_EnterPowerDown()`. This API is now called only when going to Power down mode

    -   **Platform specific**
        -   Deep sleep mode is supported. 
        -   Power down mode is supported in low power reference design applications as experimental.
        -   XTAL32K-less support using FRO32K is experimental 
        -   FRO32K notifications callback is debug only and should not be used for final product firmware builds

    -   **Overal folder restructuring for SDK 24.12.00**
        -   [Platform]:
            -   Renamed platform family from `connected_mcu/nbu` to `wireless_mcu/nbu`
            -   Platform families have now dedicated `fwk_config.h`, `rpmsg_config.h` and `SecLib_mbedtls_config.h`
        -   [Services]:
            -   Moved all framework services in a common directory `services`

-   **Zigbee and IEEE 802.15.4**
    -  Minor fixes for Zigbee PRO R22 configuration.
    -  Zigbee Pro 2023 Configuration is not supported in this release.
    

