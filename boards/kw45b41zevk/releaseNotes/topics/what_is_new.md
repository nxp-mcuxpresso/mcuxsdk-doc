# What is new

The following changes have been implemented compared to the previous SDK release version \(2.16.100\).

-   **Bluetooth LE host stack and applications**

    -   Early Access Release.
    -   Periodic advertising with responses - experimental.
    -   Encrypted Advertising Data - experimental.
    -   Documentation update.
    -   Minor fixes and stability improvements.
	
-   **Bluetooth LE controller**

    - Early Access Release
    - Periodic Advertising with Response (PAwR) – Experimental
    - Minor fixes and stability improvements
    - Channel Sounding (controlled Access)

-   **XCVR**

    -   Removed support for A0 silicon version.
-   **Connectivity framework**

    -   **Major Changes (User Applications may be impacted)**

        -   Supporting cmake/Kconfig for SDK 24.12.00: user shall now use CmakeLists.txt and Kconfig files from root folder. Compilation should be done using west build command. In order to see the Framework Kconfig, use command >west build -t guiconfig
        -   Board files and linker scripts moved to examples repository

    -   **Bugfixes**

        -   [platform lowpower]
            -   Entering Deep down power mode will no longer call PLATFORM_EnterPowerDown(). This API is now called only when going to Power down mode

    -   **Platform specific**

        -   Deep sleep mode is supported. Power down mode is supported in low power reference design applications as experimental only
        -   XTAL32K-less support using FRO32K is experimental 
        -   FRO32K notifications callback is debug only and should not be used for mass production firmware builds

    -   **Overal folder restructuring for SDK 24.12.00**

        -   [Platform]:
            -   Renamed platform_family from connected_mcu/nbu to wireless_mcu/nbu
            -   platform family have now a dedicated fwk_config.h, rpmsg_config.h and SecLib_mbedtls_config.h
        -   [Services]:
            -   Moved all framework services in a common directory "services/"

-   **GenFSK link layer**

    -   No fixes or changes.

