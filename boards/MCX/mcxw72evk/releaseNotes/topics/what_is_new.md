# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   Added an API to update local synchronization parameters after PAwR is already established on the scanner side.
	-   Added Connection Subrating feature (experimental) in the Bluetooth LE Host.
	-   Added Connection Subrating feature in ble_shell sample application.

    ### Improved
	-   Improved localization applications timer mechanism to reduce the number of wakeups.
	-   Updated localization timeout values to be overridable by the application.
	-   Retain the subevent_done_status local and remote values for all subevents and pass them to the algorithm.
	-   Documentation miscellaneous updates.

    ### Fixed
	-   Fixed L2CAP credit-based channel disconnection where the channel's timer ID would be set to `0` instead of `gTmrInvalidTimerID_c`.
	-   Fixed Channel Sounding applications issue: clear the Indication Pending flag for a peer device on disconnect.
	-   ble_shell sample application: Set maximum arguments in command (SHELL_MAX_ARGS = 20) in app_preinclude.h. 

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Fixed an issue where the procedure timeout was not stopped once the LL_PAUSE_ENC_RSP PDU is received on the peripheral side.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

      **Major Changes**
        -   [wireless_mcu][ot] Removed `gPlatformUseOuiFromIfr` configuration flag. OUI will now be read from IFR by default on mcxw72 platform, with a fallback to the static OUI if no value is found in IFR.
        -   [wireless_mcu][ble] Enabled `gPlatformUseUniqueDeviceIdForBdAddr_d = 2` on kw47/mcxw72 platforms to read the complete BD address from IFR. If no address is found in IFR, the system will fall back to generating one using the RNG method.
        -   [SecLib] Removed unused cryptographic implementations (SHA1, AES-EAX, AES-OFB) and obsolete `FSL_FEATURE_SOC_AES_HW` option to reduce code size and complexity.
      **Minor Changes**
        -   [wireless_mcu][ble] Added callback registration for HCI log. Users can register a callback to log the HCI commands sent/received on the platform using new wrapper API.
        -   [wireless_nbu][CS][COEX] Added Channel Sounding (CS) coexistence enablement support.
      **Bug fixes**
        -   [wireless_nbu][lowpower] Fixed NBU low-power timing issue by forcing LPO delay to 0 during active NBU window. The delay is restored to the default parameter right before re-entering low-power mode to guarantee accurate Link Layer timing calculations.
        -   [platform] Removed `PLATFORM_GetClockFreq()` API which contained MISRA violations, was unused, and duplicated `PLATFORM_GetNbuFreq()` functionality.
        -   [MISRA] Various MISRA compliance fixes in SFC, SecLib, Platform (including platform_ics and platform low power), FSCI, and PDUM modules.

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
