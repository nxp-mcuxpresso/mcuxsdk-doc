# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   CCC and IoT Channel Sounding Localization applications on the GitHub repository
	-   Local average and remote average RSSI values to the CS measurement report
	-   The "-Os" optimization flag to the ARMGCC release configuration for the NCP applications

    ### Improved
	-   Enabled low power support in the 'loc_reader_host' application

    ### Fixed
	-   'loc_reader_host' application event set issue
	-   Missing handler for Version2 of the Set RPA Timeout command

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Fixed an issue where the procedure timeout was not stopped once the LL_PAUSE_ENC_RSP PDU is received on the peripheral side.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

      **Major Changes**
        -   [wireless_mcu][ble] Enabled `gPlatformUseUniqueDeviceIdForBdAddr_d = 2` on kw47/mcxw72 platforms to read the complete BD address from IFR. If no address is found in IFR, the system will fall back to generating one using the RNG method.
        -   [SecLib] Removed unused cryptographic implementations (SHA1, AES-EAX, AES-OFB) and obsolete `FSL_FEATURE_SOC_AES_HW` option to reduce code size and complexity.
      **Minor Changes**
        -   [wireless_mcu][ble] Added callback registration for HCI log. Users can register a callback to log the HCI commands sent/received on the platform using new wrapper API.
        -   [wireless_nbu][CS][COEX] Added Channel Sounding (CS) coexistence enablement support.
      **Bug fixes**
        -   [wireless_nbu][lowpower] Fixed NBU low-power timing issue by forcing LPO delay to 0 during active NBU window. The delay is restored to the default parameter right before re-entering low-power mode to guarantee accurate Link Layer timing calculations.
        -   [platform] Removed `PLATFORM_GetClockFreq()` API which contained MISRA violations, was unused, and duplicated `PLATFORM_GetNbuFreq()` functionality.
        -   [MISRA] Various MISRA compliance fixes in SFC, SecLib, Platform (including platform_ics and platform low power), FSCI, and PDUM modules.

