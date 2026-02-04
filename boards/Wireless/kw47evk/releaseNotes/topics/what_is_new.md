# What is new 

The following changes have been implemented compared to the previous SDK release version \(26.03.00-pvw1\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Implemented Bluetooth LE Host Transient Application Key feature (experimental).
	-   Added Bluetooth LE Host Transient Application Key in ble_shell, loc_reader and loc_user_device.
	-   Added Channel Sounding phase calibration, with 0.5m compensation for all boards.
	-   Added Vendor Specific Command to enable Link Layer experimental features.
	-   Added `gAppCsTimeInfo_d` define in app_preinclude.h for digital_key_car_anchor_cs on KW47EVK.
	-   Added Channel Sounding **phase calibration** logic and updates in RAS CS Procedure Timing Measurement.

    ### Improved
	-   Updated RADE algorithm source files license description with NXP proprietary license.
	-   Improved data logging for digital key application.
	-   Updated CCC enumeration values to align with CCC v4.0.0 specification.
	-   Updated Intrusion Detection System documentation with event details.
	-   Documentation miscellaneous updates.

    ### Fixed
	-   Fixed ranging data body parser on the client side — aborted steps are now counted correctly to prevent subevent misalignment.
	-   Fixed handling of CS Procedure Disable at Host and application level.
	-   Fixed app_localization timer blocking when sensors were disabled.
	-   Fixed setting of `gCsTimeInfo.transferStart` for BTCS Client L2CAP transfer.
	-   Removed unused `gAppRealTimeDataTransfer_c` define from digital_key_car_anchor_cs.
	-   Fixed issues in data transfer and event updates related to timing measurement.

    ### Changed
	-   Updated `(SHELL_MAX_ARGS = 20)` in `app_preinclude.h` for localization applications.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    Periodic Advertising with Responses (PAwR):
    -  Fixed Periodic Advertising Subevent Data mechanism when handling more than five subevents.
    -  Fixed a problem preventing PAwR from being enabled while another advertising activity was active.
    Channel Sounding:
    -  Fixed an issue where an incorrect “Procedure Done Status” was reported after disabling and re‑enabling a Channel Sounding procedure.
    -  Fixed a condition where Channel Map Indication and CS Indication occurring within the same connection event caused incorrect behavior.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

    - **Major Changes**
        - [wireless_mcu][ble] Refactored BLE platform into separate core HCI and utilities modules for improved modularity and Zephyr compatibility. Core HCI transport functions remain in `fwk_platform_ble.c` while utility functions (BD address generation, security, TX power, timestamps) moved to new `fwk_platform_ble_utils.c` module. This enables minimal HCI-only builds without hardware parameter, RNG, or controller API dependencies.
        - [wireless_mcu][ble] Aligned HCI platform APIs with Zephyr driver requirements. `PLATFORM_SetHciRxCallback()` now returns an int value instead of void. Added new `PLATFORM_StartHci()` API, and enhanced `PLATFORM_InitBle()` with initialization guard to prevent multiple initialization attempts.
        - [wireless_mcu][ble] Made optional initialization steps configurable in `PLATFORM_InitBle()` with new flags `gPlatformSetBleMaxTxPowerAtInit_d`, `gPlatformSetSfcConfigAtInit_d`, and `gPlatformSetWakeUpDelayAtInit_d` to enable cleaner integration with Zephyr and minimal configurations.
        - [wireless_mcu][wireless_nbu] Added new APIs: `PLATFORM_TSTMR_GetBase()`, `PLATFORM_TSTMR_Enable()`, and modified `PLATFORM_TSTMR_ReadTimeStamp()` to use TSTMR instance ID rather than pointer. Removed dependencies on MCUX component tstmr.
        - [SecLib_RNG] Removed legacy SecLib and RNG mbedtls framework implementations now replaced by PSA. Removed deprecated SecLib AES-MMO implementation.
        - [RNG] Introduced `gRngEnableAutoReseed_d` feature flag to control automatic reseeding via WorkQ. Default values are enabled for platforms with NBU; otherwise they are disabled. This allows single-core platforms to use RNG without WorkQ dependency when handling reseeding manually.

    - **Minor Changes**
        - [wireless_mcu][ot] Conditionally exclude MCUXpresso-specific dependencies (board_platform.h, pin_mux.h, SecLib.h, RNG_Interface.h, HWParameter.h) when building for Zephyr, with stubbed IEEE 802.15.4 address generation functions.
        - [wireless_mcu] Made TRDC driver dependency optional based on `gPlatformNbuDebugGpioDAccessEnabled_d` usage, changing from mandatory (select) to optional (imply) in Kconfig.
        - [wireless_nbu] Added new NBU APIs `PLATFORM_GetSharedMemConfig()` and `PLATFORM_GetDMemConfig()` to retrieve size of SMU/DMEM.
        - [NVM] Added `Nv_GetPartitionAddressAndSize()` API to retrieve NVM partition characteristics.
        - [DBG] Added warning ID tracking support with enhanced `NBUDBG_StateCheck()` to monitor NBU warnings. Added `PLATFORM_IsNbuWarningSet()` API with callback support for proactive warning monitoring.
        - [DBG] Added HCI vendor event transmission support with `NBUDBG_ConfigureHciVendorEvent()` API to enable/disable debug structure transmission over HCI.
        - [DBG] Added coredump support on fault handler with `gFaultHandlerCoredumpEnabled_d` conditional compilation.
        - [DBG] Initialized .debugbuf from flash into sqram_debug_region for GCC builds with `INIT_BLE_DEBUG_DAT`.
        - [Sensors] Added initialization guard to prevent redundant sensor initialization calls with `PLATFORM_InitSensors()`.
        - [Platform] Added missing localization dependency to XCVR in Kconfig.
        - [Platform] Fixed missing Kconfig dependencies for KW47 core1 variants (KW47B42ZB2, KW47B42ZB3, KW47B42ZB6, KW47B42Z96, KW47B42Z97).
        - [OTA] Improved OTA coverage by allowing static functions to be invoked from unit tests.
        - [FSCI] Added UUID retrieval via `PLATFORM_GetMCUUid()` abstraction in `FSCI_ReadNbuVer()` API.
        - [Common] Made services CMakeLists optional to allow integration of only required services into Zephyr's hal_nxp.
        - [Platform] Made timer manager optional with configuration flag.
        - [wireless_mcu][lcl] Corrected FEM & COEX API functions with proper NBU wake-up handling and RF_GPO pin conflict checks.
        - [wireless_mcu] Consolidated `KB()` and `MB()` macro definitions by using `fwk_hal_macros.h` instead of platform-specific definitions to prevent conflicts and ensure Zephyr compatibility.
        - [Common] Added Zephyr RTOS compatibility to `fwk_hal_macros.h` by including <zephyr/sys/util.h> when `__ZEPHYR__` is defined and guarding `_DO_CONCAT` and `CONTAINER_OF` macros to prevent redefinition conflicts.

    - **Bug Fixes**
        - [SecLib_RNG][PSA] Fixed RNG and PSA context release in `RNG_Deinit()` by invoking `mbedtls_psa_crypto_free()` and resetting `rng_ctx.mRngInitialized` to ensure proper reinitialization in `RNG_ReInit()`.
        - [NVM] Fixed `GetFlashTableVersion()` function to prevent recursion.
        - [NVM] Treated missing error case in `NvCopyRecord()` if failed to find record.
        - [SecLib] Initialized CMAC context before using it to prevent usage of uninitialized memory.
        - [WorkQ] Increased workqueue stack size when coverage is enabled.
        - [wireless_mcu] Fixed build issue when ICS WorkQ is disabled.
        - [MISRA] Various MISRA and CERT-C compliance fixes in NVM, HWParameter, DBG (including platform dbg), LowPower, SecLib, Platform modules (platform_ics, platform_sensors), FSCI, FunctionLib, wireless_mcu, and Common modules.

