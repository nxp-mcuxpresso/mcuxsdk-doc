# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.03.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Test mode functionality for the Intrusion Detection System.
	-   Added GAP API for HCI LE_Set_Local_Slave_Latency_Enable vendor command.
	-   `gRasUseNotifOrInd_c` to allow configuration of Indication or Notification on RAS.
	-   `cs_sync_phy` argument to `setcsconfig` shell command.
	-   `snr_control_init` and `snr_control_refl` arguments to `setcsproc` shell command.
	-   Detailed description for `setcsconfig` and `setcsproc` command arguments to the CCC w/ CS and Localization applications notes.
	-   Mode0 step information parsing for both RAS and BTCS, made available for the export module.

    ### Improved
	-   ATT Write Commands can now be sent at any time, as per specification.
	-   Enhanced CCC and RAS Channel Sounding by incorporating real-time local and remote data decompression.
	-   Localization applications now record the PHY used for establishing the connection and incorporate it into the CS procedure parameters configuration.
	-   Localization applications keep the `subevtStopIdx` for the remote data and provide it to the algorithm.
	-   Localization applications now pass remote mode map to algorithm.
	-   Eliminated the dependency on `hci_interface.h` in localization files.
	-   Documentation updates.
	-   Miscellaneous minor application bug fixes.

    ### Fixed
	-   Wrong data field type in `GAP2GenericEventVendorSpecificDebugFatalError`.
	-   Localization application now processes CS results only when local data is available.
	-   Digital key car anchor application issue related to setting the GAP role prior to any use.
	-   Error in the definition of a CCC PSM VDBT Version GATT characteristic.
	-   Issue with PACKET_NADM byte not being packed correctly into the TOF buffer for mode-3 steps.
	-   MISRA fixes.

    ### Changed
	-   Modified linker section names, comments, and RAM layout in the `connectivity.icf` and `connectivity_ble_loc.ld` files for every KW47 and MCXW72 board.
	-   Set the default CS submode and default `rtt_type` to 3.
	-   Set the default radio core speed for the Channel Sounding application to 48 MHz.
	-   Localization applications configured to use the extended heap as the final segment of DATA1.
	-   Deleted the `gcGapMaximumActiveConnections_c` definition from applications.
	-   Eliminated unused fields related to CS Test Mode.
	-   Deleted initializations of range settings that were subsequently overwritten.

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

