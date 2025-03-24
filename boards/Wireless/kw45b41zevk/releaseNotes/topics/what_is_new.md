# What is new

The following changes have been implemented compared to the previous SDK release version \(25.03.00-pvw2\).


-   **Bluetooth LE host stack and applications**
    ### Added
    -   **L2CAP support** for Channel Sounding **IQ Sample Transfer** in CCC CS sample applications.


    ### Changed
    -   Updated **FSCI XML file**.
    -   Updated **Bluetooth LE Host Documentation**. 

    ### Fixed
    -   Cleared the **mpRemoteCachedCaps** entry when the peer disconnects (CS sample applications).
    -   Transfer **RAS subscription** data during connection handover (CCC CS sample applications).
    -   **EAD** - Updated advertising data length check to ensure encrypted data fits inside one AD.
    -   Updated **digital_key_car_anchor** and **digital_key_car_anchor_cs** applications to manage **Random Static address** from the application layer.
	
    -   Details can be found in **CHANGELOG.md**.
-   **Bluetooth LE controller**
    -  Minor fixes and stability improvements

-   **Transceiver Drivers (XCVR)**
    -   Added API to control PA ramp type and duration

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
            - [wireless_mcu] fwk_platform_lcl coex config update for KW45

    -   **Note**

	   - [HwParameter] By default, hardware parameters are located in both main flash and IFR. Main flash and IFR needs to be erased if you want to erase the actual hardware parameters.

    Details can be found in [CHANGELOG.md](../../../../../middleware/wireless/framework/CHANGELOG.md)
