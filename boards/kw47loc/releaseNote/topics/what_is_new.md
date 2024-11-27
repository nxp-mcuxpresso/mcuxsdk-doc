# What is new 

The following changes have been implemented compared to the previous SDK release version.

-   Bluetooth LE
    -   Early Access Release.
    -   Bluetooth LE sample application: `w_uart`.
    -   Bluetooth LE Channel Sounding applications: `digital_key_car_anchor_cs`, `digital_key_device_cs`, `loc_reader`, `loc_user_device`, `wireless_ranging`.
    -   Bluetooth LE Channel Sounding applications are controlled access.
    -   Added LCE support.
	-   Enable CS antenna array.
	-   Documentation update.
    -   Other minor fixes and stability improvements.
-   Bluetooth LE controller:
    -   Early Access Release
    -   Channel Sounding (controlled Access)
    -   Minor fixes and stability improvements
-   XCVR API:

    -   Fixed PA power off transient bug in `XCVR_ForcePAPower()`.

-   **Connectivity framework**

    -   **Major Changes (User Applications may be impacted)**

        -   mcux github support with cmake/Kconfig from sdk3 user shall now use CmakeLists.txt and Kconfig files from root folder. Compilation should be done using west build command. In order to see the Framework Kconfig, use command >west build -t guiconfig
        -   Board files and linker scripts moved to examples repository

    -   **Bugfixes**

        -   [platform lowpower]
            -   Entering Deep down power mode will no longer call PLATFORM_EnterPowerDown(). This API is now called only when going to Power down mode

    -   **Platform specific**

        -   Early access release only:
            -   Deep sleep power mode not fully tested. User can experiment deep sleep and deep down modes using low power reference design applications
            -   XTAL32K-less support using FRO32K not tested

    -   **Overal folder restructuring for SDK3**

        -   [Platform]:
            -   Rename platform_family from connected_mcu/nbu to wireless_mcu/nbu
            -   platform family have now a dedicated fwk_config.h, rpmsg_config.h and SecLib_mbedtls_config.h
        -   [Services]:
            -   Move all framework services in a common directory "services/"



