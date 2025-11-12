# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw1\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
    -   Threshold for the invalid number of Anchor Monitor events received by the target anchor
    -   **Experimental Monitoring Advertisers** feature in Bluetooth LE Host
    -   **Experimental Randomized RPA** feature in Bluetooth LE Host
    -   Application defines for default connection and default advertising tx power

    ### Improved
    -   Miscellaneous applications updates
    -   Central applications now wait for status of Encrypt procedure in case of bonded device
    -   Logging data on localization applications
    -   PCT rotation calibration added to localization apps
    -   Configured CS Reflector to start the CS procedure with the tdm command and updated the documentation
    -   Populated the optionalSubfeaturesSupported field correctly
    -   Prevented CORE 0 from entering deep sleep while LCE is computing by setting the low power mode constraint to PWR_WFI during LCE computation and releasing it afterwards
    -   Implemented in CCC_CS, Channel Sounding data transfer from the anchor to the device
    -   Documentation miscellaneous updates
    -   Updated armgcc ld linker files to take gUseInternalStorageLink_d flag value into consideration

    ### Fixed
    -   Memory issue when setting scan response data would return an error status from the LL
    -   Set advertises with the public address, overwritten by a previously used random address on receiving the Advertising Set Terminated event

    ### Changed
    -   Updated memory configuration: replaced the extended heap area in the available SMU2 memory with a 24KB array in the data1
    -   Removed redundant cached remote capabilities write on reflectors, as the initiator will always trigger a capabilities exchange and trying to write cached capabilities afterwards results in an HCI error

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Channel sounding updates:
        -   Fixed cases where the procedure was dropped due to connection collisions.
        -   Fixed an issue where the CSSubeventResultIndication event was missing during the second CS procedure.
        -   Fixed CS termination procedure collision handling.
        -   Added phase rotation vendor command.

    - Fixed an issue where the procedure timeout did not expire in some cases, causing the device to remain connected if the peer device did not respond to the procedure initiated by the device.
    - Fixed connection establishment issues with LE Coded PHY when the scan window interval was set to 2.5 ms.
    - Fixed connection establishment issues with LE Coded PHY when four peripheral devices attempted to connect to a single central device, resulting in connection collisions.
    - Fixed connection parameter request that was incorrectly rejected when the minimum and maximum connection intervals differed, and no preferred periodicity or offset was set.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework (compared to 25.09.00 release)**

      **Major Changes**
        -   [wireless_mcu] Reduced RPMSG buffer payload size from 496 to 270 bytes on KW43/KW47 platforms, saving 226 bytes per buffer (1808 bytes total with 4 buffers on each core). This optimization is possible as rpmsg-lite no longer requires buffer sizes to be powers of two.
        -   [configs] Introduced RL_ALLOW_CUSTOM_SHMEM_CONFIG flag in rpmsg_config.h to enable connectivity applications to use platform_set_static_shmem_config() and platform_get_custom_shmem_config().
      **Minor Changes**
        -   [wireless_mcu] Updated radio power management configuration with PLATFORM_InitRadio() API on kw47/mcxw72 platforms
        -   [DBG] Added NBU assert indication support to host with line/file info using debug structure.
        -   [DBG] Enhanced NBU debug framework with warning detection and notification capabilities. Extended NBUDBG_StateCheck() to monitor NBU warnings via PLATFORM_IsNbuWarningSet() with callback support for proactive warning monitoring.
        -   [Sensors] Added periodic temperature measurement support allowing app/host to request periodic temperature measurement.
        -   [Sensors] Added markdown documentation explaining periodic measurement functionality upon NBU requests.
        -   [SecLib_RNG] Added documentation for asynchronous seed handling using RNG_NotifyReseedNeeded() and SecLib implementation flavors (Software, EdgeLock, PSA Crypto, MbedTLS).
        -   [PSA] Simplified PSA configuration files and reduced imports/definitions for wireless MCU platforms.
        -   [NVS] Enhanced debug capabilities by adding CONFIG_NVS_LOG_LEVEL and improved LOG macros to adapt to PRINTF limitations.
        -   [wireless_mcu][wireless_nbu] Migrated TSTMR implementation to use SDK fsl_tstmr driver for better maintainability and consistency. This migration replaces custom TSTMR register definitions with official SDK driver APIs while maintaining existing PLATFORM_* API compatibility.
      **Bug fixes**
        -   [wireless_mcu] Fixed FRO32K as 32 kHz clock source with deferred OSC32K switching to improve initialization performance after warm reset.
        -   [wireless_mcu] Added wait loop for NBU power domain readiness in PLATFORM_InitNbu() to prevent race conditions when accessing NBU power domain in applications without NBU images.
        -   [wireless_mcu] Fixed external flash blank check procedure for LSPI external NOR Flash by correcting PLATFORM_ExternalFlashAreaIsBlank() to read from RAM buffer and perform erase pattern comparison in RAM with optimized 4-byte step loops.
        -   [NVS] Removed mflash dependency from NVS external flash port and fixed internal flash blank check of unaligned flash data.
        -   [SecLib_RNG][mbedtls] Enhanced ECDH context preservation across low-power transitions on KW45_MCXW71 and KW47_MCXW72 platforms using export/import APIs to ensure cryptographic context is retained when hardware accelerator loses internal memory during power-down mode.
        -   [wireless_nbu] Fixed incorrect FRODIV values that were causing reduced peripheral clocks by updating PLATFORM_FroDiv[] mapping array to prevent over-division of flash APB and RF_CMC clocks.

Details can be found in [CHANGELOG.md](/middleware/wireless/framework/CHANGELOG.md)

