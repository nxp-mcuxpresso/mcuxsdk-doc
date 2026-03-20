# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.03.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Test mode functionality for the Intrusion Detection System.
	-   Added GAP API for HCI LE_Set_Local_Slave_Latency_Enable vendor command.
	-   `gRasUseNotifOrInd_c` to allow configuration of Indication or Notification on RAS.
	-   `cs_sync_phy` argument to `setcsconfig` shell command.
	-   `snr_control_init` and `snr_control_refl` arguments to `setcsproc` shell command.
	-   Mode0 step information parsing for both RAS, made available for the export module.

    ### Improved
	-   ATT Write Commands can now be sent at any time, as per specification.
	-   Enhanced RAS Channel Sounding by incorporating real-time local and remote data decompression.
	-   Localization applications now record the PHY used for establishing the connection and incorporate it into the CS procedure parameters configuration.
	-   Localization applications keep the `subevtStopIdx` for the remote data and provide it to the algorithm.
	-   Localization applications now pass remote mode map to algorithm.
	-   Eliminated the dependency on `hci_interface.h` in localization files.
	-   Documentation updates.
	-   Miscellaneous minor application bug fixes.

    ### Fixed
	-   Wrong data field type in `GAP2GenericEventVendorSpecificDebugFatalError`.
	-   Localization application now processes CS results only when local data is available.
	-   Issue with PACKET_NADM byte not being packed correctly into the TOF buffer for mode-3 steps.
	-   MISRA fixes.

    ### Changed
	-   Modified linker section names, comments, and RAM layout in the `connectivity.icf` and `connectivity_ble_loc.ld` files.
	-   Set the default CS submode and default `rtt_type` to 3.
	-   Set the default radio core speed for the Channel Sounding application to 48 MHz.
	-   Localization applications configured to use the extended heap as the final segment of DATA1.
	-   Deleted the `gcGapMaximumActiveConnections_c` definition from applications.
	-   Eliminated unused fields related to CS Test Mode.
	-   Deleted initializations of range settings that were subsequently overwritten.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    No update.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

    - **Major Changes**
        - [SecLib] Refactored SecLib functions with improved error handling and naming conventions. Added return status codes for better testing, added the `SecLib_` prefix for all functions with backward compatibility maintained via `#define` stubs. Added parameter checks on all functions and improved test coverage for all SecLib flavors.
        - [SecLib] Updated CryptoLibSW APIs by removing unused pMultiplicationBuffer argument from `Ecdh_ComputeDhKeyUltraFast()`, `ECP256_GeneratePublicKeyUltraFast()`, and `ECP256_GenerateKeyPairUltraFast()`. Renamed `ECP256_GeneratePublicKey()` to `ECP256_GeneratePublicKeySeg()` in legacy implementation. Added new `ECP256_GeneratePublicKey()` API for SPAKE2+ ComputeL procedure.

    - **Minor Changes**
        - [FunctionLib] Enhanced `FLib_StrLen()` to return an error value when the string size exceeds maximum limit (4096 bytes), adopting strnlen behavior.
        - [Common] Cleaned deprecated mbedtls2x Kconfig configurations.
        - [wireless_mcu][lcl] Updated FEM API to send configuration to NBU for proper XCVR timing adaptation during Channel Sounding activity. XCVR register backup and restore uses current mechanism with config sent through `PLATFORM_NbuApiReq()`.
        - [SecLib_RNG] Removed support for deprecated devices including `FSL_FEATURE_SOC_SIM_COUNT` for RNG and QN908x platforms.
        - [FactoryDataProvider] Removed deprecated FactoryDataProvider service as it is no longer used following mbedtls2.x deprecation.

    - **Bug Fixes**
        - [wireless_mcu] Fixed FRO6M calibration failure in OEM closed lifecycle by replacing inaccessible DWT cycle counter with SysTick timer. The implementation saves/restores SysTick state to maintain FreeRTOS compatibility.
        - [wireless_mcu][ble] Removed redundant assert in `PLATFORM_SendHciVendorEvent()` as invalid parameters are already sanitized with the error returned to the caller.
        - [SecLib] Fixed `CMakeLists.txt` lib_crypto variant dependency.
        - [MISRA] Various MISRA compliance fixes in OTA, flash related files, FSCI, NVM, platform files, and ICS modules. Fixed potential flash blank check issue with unaligned pointers and split `OTA_PostWriteToFlash()` to match the `HIS_LEVEL` constraint. Also prevented infinite loop in `FLib_StrLen()` and ensured that unions have a consistent non-zero size across compilers.

-   **IEEE 802.15.4**
     - API cleanup: remove unmaintained slotted support
     - support for MAC split architecture
       - fix condition to enter low power
     - minor fixes and stability improvements for connectivity_test example application
     - experimental support for mcxw72 NBU core

-   **Zigbee**
      - NCP Host Updates and fixes
      - R23 fixes
        - Device can't establish a new TCLK through ZDO Start Key Update procedure
        - Security Start Key Update Request is not relayed to joining ZED in multi hop key negotiation
      - propagate APS ACK to end-user application
      - documentation updates
