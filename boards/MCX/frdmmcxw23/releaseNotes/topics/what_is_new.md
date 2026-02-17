# What is new

The following changes have been implemented compared to the previous SDK release version \(26.03.00-pvw2\).

- **Bluetooth Synopsys controller**
    - Fix scan response not always sent when filtering duplicates is enabled
    - Avoid network privacy if Peer IRK is all zero
    - Take also SID into account when adding a unique entry in the periodic advertiser list
    - Reject peer random static addresses in the resolving list when it does not contain 11 as MSb

- **Bluetooth LE**
    - **Major Changes**
        - Added support for switching to the coded PHY mode.
    - **Minor Changes**
        - [PSA] Added the project_segment Kconfig option to enable selection of an optimized PSA configuration for Bluetooth LE applications.

-   **Connectivity framework**

    - **Major Changes**
        - [wireless_mcu][ble] Refactored BLE platform into separate core HCI and utilities modules for improved modularity and Zephyr compatibility. Core HCI transport functions remain in `fwk_platform_ble.c` while utility functions (BD address generation, security, TX power, timestamps) moved to new `fwk_platform_ble_utils.c` module. This enables minimal HCI-only builds without hardware parameter, RNG, or controller API dependencies.
        - [wireless_mcu][ble] Aligned HCI platform APIs with Zephyr driver requirements. `PLATFORM_SetHciRxCallback()` now returns an int value instead of void. Added new `PLATFORM_StartHci()` API, and enhanced `PLATFORM_InitBle()` with initialization guard to prevent multiple initialization attempts.
        - [SecLib_RNG] Removed legacy SecLib and RNG mbedtls framework implementations now replaced by PSA. Removed deprecated SecLib AES-MMO implementation.
        - [RNG] Introduced `gRngEnableAutoReseed_d` feature flag to control automatic reseeding via WorkQ. Default values are enabled for platforms with NBU; otherwise they are disabled. This allows single-core platforms to use RNG without WorkQ dependency when handling reseeding manually.

    - **Minor Changes**
        - [NVM] Added `Nv_GetPartitionAddressAndSize()` API to retrieve NVM partition characteristics.
        - [Sensors] Added initialization guard to prevent redundant sensor initialization calls with `PLATFORM_InitSensors()`.
        - [MCXW23] Enabled `gSecLibUseDspExtension_d` to leverage CM33 DSP extensions for ultra-fast cryptographic library.
        - [MCXW23] Changed temperature dummy value for sensors to support application enablement.
        - [OTA] Improved OTA coverage by allowing static functions to be invoked from unit tests.
        - [FSCI] Added UUID retrieval via `PLATFORM_GetMCUUid()` abstraction in `FSCI_ReadNbuVer()` API.
        - [Common] Made services CMakeLists optional to allow integration of only required services into Zephyr's hal_nxp.
        - [Platform] Made timer manager optional with configuration flag.
        - [wireless_mcu] Consolidated `KB()` and `MB()` macro definitions by using `fwk_hal_macros.h` instead of platform-specific definitions to prevent conflicts and ensure Zephyr compatibility.
        - [Common] Added Zephyr RTOS compatibility to `fwk_hal_macros.h` by including <zephyr/sys/util.h> when `__ZEPHYR__` is defined and guarding `_DO_CONCAT` and `CONTAINER_OF` macros to prevent redefinition conflicts.

    - **Bug Fixes**
        - [SecLib_RNG][PSA] Fixed RNG and PSA context release in `RNG_Deinit()` by invoking `mbedtls_psa_crypto_free()` and resetting `rng_ctx.mRngInitialized` to ensure proper reinitialization in `RNG_ReInit()`.
        - [NVM] Fixed `GetFlashTableVersion()` function to prevent recursion.
        - [NVM] Treated missing error case in `NvCopyRecord()` if failed to find record.
        - [WorkQ] Increased workqueue stack size when coverage is enabled.
        - [MISRA] Various MISRA and CERT-C compliance fixes in NVM, HWParameter, DBG (including platform dbg), LowPower, SecLib, Platform modules (platform_ics, platform_sensors), FSCI, FunctionLib, wireless_mcu, and Common modules.
