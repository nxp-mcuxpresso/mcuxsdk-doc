# What is new

The following changes have been implemented compared to the previous SDK release version \(24.12.00-pvw2\).


-   **Bluetooth LE host stack and applications**
    
    #### Added
	- PAWR support in **BLE Shell** sample application.
	- PAWR support in **adv_ext_peripheral** and **adv_ext_central** sample applications.
	- New sample applications for **FRDM-MCXW72**.
	- **Gap_SetScanningCallback** API.
	- Support for handover connection interval update command.

	#### Changed
	- Updated HID Device for **Windows 11** compatibility.
	- Updated CCC demos to **Digital Key R4 spec version 1.0.0**.
	- Improved RPA resolution at the **Host level**, now performed synchronously.
	- Enhanced parsing of the **CS procedure** in Ranging Service.

    #### Fixed
	- Corrected parsing of the **PAST command** in FSCI GAP.
	- Fixed **scan event reporting** in PAST scenario.
	- Added an error case for `Gap_SetChannelMap` in the generic event handler.

	    
    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/bluetooth/CHANGELOG.md).

-   **Bluetooth LE controller**
    -  Added initial experimental support for Bluetooth LE Controller feature: Periodic Advertising with Responses \(PAwR)\
    -  Minor fixes and stability improvements

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration

-   **Connectivity framework**

    -   **Minor Changes (no impact on application)**

        -   **General**
            - [General] Various MISRA/Coverity fixes in framework: NVM, RNG, LowPower, FunctionLib and platform files

        -   **Services**
            - [SecLib_RNG] AES-CBC evolution:
              - added `AES_CBC_Decrypt()` API for sw, SSS and mbedtls variants.
              - Made AES-CBC SW implementation reentrant avoiding use of static storage of AES block.
              - fixed SSS version to update Initialization Vector within SecLib, simplifying caller's implementation.
              - modified `AES_128_CBC_Encrypt_And_Pad()` so as to avoid the constraint mandating that 16 byte headroom be available at end of input buffer.
            - [SecLib_RNG] RNG modifications:
              - `RNG_GetPseudoRandomData()` could return 0 in some error cases where caller expected a negative status.
              - Explicited RNG error codes
              - Added argument checks for all APIs and return `gRngBadArguments_d` (-2) when wrong
              - added checks of RNG initalization and return `gRngNotInitialized_d` (-3) when not done
              - fixed correcteness of `RNG_GetPrngFunc()` and `RNG_GetPrngContext()` relative to API description.
              - Added `RNG_DeInit()` function mostly for test and coverage purposes.
              - Improved RNG description in README.md
              - Unified the APIs behaviour between mbedtls and non mbedtls variants.
              - RNG/mbedtls : Prevent `RNG_Init()` from corrupting RNG entropy context if called more than once.
              - RNG/mbedtls: fixed `RNG_GetTrueRandomNumber()` to return a proper `mbedtls_entropy_func()` result.
            - [SecLib_RNG] Use defragmetation option when freeing key object in SecLib_sss to avoid leak in S200 memory
            - [SecLib_RNG] Add new API ECP256_IsKeyValid() to check whether a public key is valid
            - [OtaSupport] Update return status to OTA_Flash_Success when success at the end of InternalFlash_WriteData() and InternalFlash_FlushWriteBuffer() APIs
            - [WorQ] Implementing a simple workqueue service to the framework
            - [SFC] Keep using immediate measurement for some measurement before switching to configuration trig to confirm the calibration made
            - [DBG] Adding modules to framework DBG :
              - sbtsnoop
              - SWO
            - [Common] Fix HAL_CTZ and HAL_RBIT IAR versions
            - [LowPower] Fix wrong tick error calculation in case of infinite timeout

        -   **Platform specific**
            - [wireless_mcu] [wireless_nbu] Use new WorkQ service to process framework intercore messages

    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)
