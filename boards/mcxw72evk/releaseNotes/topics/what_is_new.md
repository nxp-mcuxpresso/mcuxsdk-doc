# What is new 

The following changes have been implemented compared to the previous SDK release version..

-   Bluetooth LE
    -   Early Access Release.
    -   Bluetooth LE sample applications.
    -   Bluetooth LE Channel Sounding applications: `loc_reader`, `loc_user_device`, `wireless_ranging`.
    -   Bluetooth LE Channel Sounding applications are controlled access.
    -   Added LCE support.
	-   Documentation update.
    -   Other minor fixes and stability improvements.
-   XCVR API:
    -   Fixed PA power off transient bug in `XCVR_ForcePAPower()`.
-   IEEE 802.15.4 and Zigbee

    -   Minor updates and stability improvements.

-   Connectivity Framework:

    -   SDK build environment\] Added Cmake/Kconfig support.
    -   \[Sensors\] Sensors API renaming: `SENSORS_InitAdc()` renamed to `SENSORS_Init()`, `SENSORS_DeinitAdc()` renamed to `SENSORS_Deinit()`.
    -   \[HWParams\] Added support to repair PROD\_DATA sector if there is ECC error \(implies loss of previous contents of sector\).
    -   \[NVM\} Linker script modification for armgcc whenever the `gNvTableKeptInRam_d` option is used placement of NVM\_TABLE\_RW in the data initialized section, providing start and end address symbols. For details see NVM\_Interface.h comments.
    -   \[Platform\] Updated macro values for MCX W72: `BOARD_32MHZ_XTAL_CDAC_VALUE` from 12U to 10U, `BOARD_32MHZ_XTAL_ISEL_VALUE` from 7U to 11U, `BOARD_32KHZ_XTAL_CLOAD_DEFAULT` from 8U to 4U, `BOARD_32KHZ_XTAL_COARSE_ADJ_DEFAULT` from 1U to 3U.
    -   \[NBU\] New `PLATFORM_RegisterNbuTemperatureRequestEventCb()` API: register a function callback when NBU requests new temperature measurement. API provides the interval request for the temperature measurement.
    -   \[NBU\] Update `PLATFORM_IsNbuStarted()` API to return true only if the NBU firmware has been started.
    -   \[platform low-power\] Moved RAM layout values in `fwk_platform_definition.h` and update RAM retention API.

