# What is new

The following changes have been implemented compared to the previous SDK release version \(24.12.00-pvw2\).


-   **Bluetooth LE host stack and applications**
    -  Minor fixes and stability improvements
    -  Documentation updates

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
            - [Settings] Add new macro gSettingsRedefineApiName_c to avoid multiple definition of settings API when using connectivity framework repo

        -   **Platform specific**
            - [wireless_mcu] [wireless_nbu] Use new WorkQ service to process framework intercore messages

    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)

-   **Zigbee and IEEE 802.15.4**
    -  Added Zigbee Pro 2023 and examples applications for ZC, ZR, ZED
    -  Introduced experimental support for MAC split architecture with FreeRTOS host stack and examples applications for ZC, ZR, ZED 
    -  Fixed PHY low power timer cancellation
    -  Minor fixes for Zigbee PRO R22 configuration
    -  Minor fixes and stability improvements for connectivity_test example application
    -  Fixed the size of TLVs for Node_desc_req in R23 examples
    -  Added experimental Zigbee NCP: coprocessor application and coordinator & router applications for imx8 and x86 platforms


