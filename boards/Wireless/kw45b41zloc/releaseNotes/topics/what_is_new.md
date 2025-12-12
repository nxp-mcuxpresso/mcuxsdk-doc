# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   'Monitoring Advertisers' support in the 'fsci_black_box' and 'ble_shell' applications

    ### Fixed
	-   Missing handler for Version2 of the Set RPA Timeout command

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Periodic Advertising updates:
        -   Fixed PerAdvSync skip scheduling.
        -   Improved PAwR Responses (TX & RX) instant.
        -   Fixed calculation of the count parameters in Periodic Advertising Subevent Data Request.

    - Fixed a corner case where LL_CONNECTION_PARAM_REQ is immediately followed by LL_TERMINATE_IND.

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework (compared to 25.09.00 release)**

      **Major Changes**
        -   [configs] Introduced RL_ALLOW_CUSTOM_SHMEM_CONFIG flag in rpmsg_config.h to enable connectivity applications to use platform_set_static_shmem_config() and platform_get_custom_shmem_config().
      **Minor Changes**
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
