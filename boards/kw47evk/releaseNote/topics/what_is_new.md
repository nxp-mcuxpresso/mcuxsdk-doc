# What is new 

MCUXpresso SDK version 24.12.00-pvw2 is an early adopter release provided as preview for early development.

The following changes have been implemented compared to the previous SDK release version \(24.12.00-pvw1\).

-   **Bluetooth LE host stack and applications:**
    -   Added Bluetooth LE sample applications: `ble_shell`, `w_uart`.
    -   Added Bluetooth LE Channel Sounding applications with Localization Compute Engine \(LCE\) support:`digital_key_car_anchor_cs`, `digital_key_device_cs`, `loc_reader`, `loc_user_device`, `wireless_ranging`  \(Bluetooth LE Channel Sounding applications are provided with controlled access, contact your NXP representative for access\)
	-   Added support for OTA feature
    -   Minor fixes and stability improvements
    -   Documentation updates
 
-   **Bluetooth LE controller:**
    -   Added support for Bluetooth LE Channel Sounding
    -   Minor fixes and stability improvements

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding
    -   Added API to control PA ramp type and duration

-   **Connectivity framework**

    -   **Major Changes (User Applications may be impacted)**

        -   Supporting CMake/Kconfig for SDK 24.12.00: user shall now use `CmakeLists.txt` and `Kconfig` files from root folder. Compilation should be done using `west build` command. In order to see the Framework Kconfig, use command `>west build -t guiconfig`
        -   Board files and linker scripts moved to examples repository

    -   **Bugfixes**

        -   [platform lowpower]
            -   Entering Deep down power mode will no longer call `PLATFORM_EnterPowerDown()`. This API is now called only when going to Power down mode

    -   **Platform specific**

        -   Deep sleep power mode not fully qualified - User can experiment deep sleep and deep down modes using low power reference design applications
        -   XTAL32K-less support using FRO32K not qualified

    -   **Overall folder restructuring for SDK 24.12.00**

        -   [Platform]:
            -   Renamed platform_family from `connected_mcu/nbu` to `wireless_mcu/nbu`
            -   Platform families have now a dedicated `fwk_config.h`, `rpmsg_config.h` and `SecLib_mbedtls_config.h`
        -   [Services]:
            -   Moved all framework services in a common directory `services`
