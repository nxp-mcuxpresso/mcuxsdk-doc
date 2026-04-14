# What is new 

The following updates were implemented with respect to the previous SDK release version \(26.03.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   RTT zero-meter calibration support in applications.
	-   Support for CS Enhancements at the Host level: 
		- Inline PCT Transfer.
		- RTT 2M PHY.
	-   New connection event 'gConnEvtRemoteFeaturesRead_c', providing the 'peer feature bitmask' via the Read Remote Features procedure.
	-   Support for up to five advertising sets in the Bluetooth LE Host.
	-   Method to specify GATT handles on the client, avoiding repeated service discovery.
	-   Experimental CS slope calibration algorithm (disabled by default), computing distance and quality indicators per antenna path.
	-   Handover broadcast time synchronization, allowing one connected anchor to synchronize multiple target anchors simultaneously.
	-   Added the common configuration header 'app_localization_config.h', overridable by the user.

    ### Improved
	-   Updated handling of 'Procedure_Results_Start' to correctly process multiple subevents in a single message.
	-   Improved CS temperature polling mechanism.
	-   BTCS Server now explicitly notifies the PSM channel via 'AppLocalization_SetPsmChannelId' function upon handover connection.
	-   RAS/BTCS clients can disable algorithm execution via 'gRunAlgo_d'.
	-   Updated and cleaned 'app_preinclude.h' for sample applications.
	-   Documentation and configuration updates for LCE enable/disable.
	-   Documentation updates.
	-   Miscellaneous minor application bug fixes.

    ### Fixed
	-   If the LE Set Periodic Adv Subevent Data command finishes with an error, use 'gInternalError_c' with 'gLeSetPeriodicAdvSubeventData_c' as the source and the command complete status as the error code.
	-   Corrected handling of AddrType values in MonAdvReport generated from XML.

    ### Changed
	-   Disabled the use of Random Static Address for all applications except: digital_key_car_anchor and digital_key_car_anchor_cs.
	-   Set the maximum CS procedure duration to: (procedure interval x connection interval x 2 - 1) slots.

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE Controller**
    -   Fixed extended connection establishment failure when peer advertising address is on primary channel.

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

