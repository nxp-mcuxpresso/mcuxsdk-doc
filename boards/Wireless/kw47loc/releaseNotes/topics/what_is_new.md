# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.03.00\).


-   **Bluetooth LE host stack and applications**
    ### Added
    -   Support for **disable UART** for **CS applications** for **low power measurements**.
    -   Support for **LCE (DSPV) non-blocking API** integration to **RADE**.
    -   **Intrusion Detection System** as **Experimental**.

    ### Improved
    -   **L2CAP command length validation** to cover all signaling commands.
	
    -   Details can be found in **CHANGELOG.md**.
-   **Bluetooth LE controller**
    -   HADM, PAwR, DBAF fixes and stability improvements.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

    -   **Minor Changes (no impact on application)**

        -   **General**
            - [General] Various MISRA/Coverity fixes in framework: NVM, RNG, LowPower, SecLib and platform files

        -   **Services**
            - [SecLib_RNG] fix return status from RNG_GetTrueRandomNumber() function: return correctly gRngSuccess_d when RNG_entropy_func() function is successful
            - [SFC] Allow the application to override the trig sample number parameter
            - [Settings] Re-define the framework settings API name to avoid double definition when gSettingsRedefineApiName_c flag is defined

        -   **Platform specific**
		    - [wireless_mcu] fwk_platform_sensors update :
                - Enable temperature measurement over ADC ISR
                - Enable temperature handling requested by NBU
            - [kw47_mcxw72] Change the default ppm_target of SFC algorithm from 200 to 360ppm

    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)

