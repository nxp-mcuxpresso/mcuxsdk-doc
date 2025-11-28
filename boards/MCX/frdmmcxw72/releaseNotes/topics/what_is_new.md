# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.12.00-pvw2\).

-   **Bluetooth LE Host Stack and Applications**

    ### Added
	-   IoT Channel Sounding Localization applications on the GitHub repository
	-   'Monitoring Advertisers' support in the 'fsci_black_box' and 'ble_shell' applications
	-   Local average and remote average RSSI values to the CS measurement report
	-   The "-Os" optimization flag to the ARMGCC release configuration for the NCP applications

    ### Improved
	-   Enabled low power support in the 'loc_reader_host' application

    ### Fixed
	-   'loc_reader_host' application event set issue
	-   Missing handler for Version2 of the Set RPA Timeout command

    -   Details can be found in github repository **nxp-mcuxpresso/mcuxsdk-middleware-bluetooth-host/CHANGELOG.md**.

-   **Bluetooth LE controller**
    - Channel sounding updates:
        -   Fixed HCI_LE_CS_Config_Complete event which was not sent when rejecting the peripheral's request in case of colliding procedure.
        -   Adjusted RTT vs temperature compensation.

    - Periodic Advertising updates:
        -   Fixed PerAdvSync skip scheduling.
        -   Improved PAwR Responses (TX & RX) instant.
        -   Fixed calculation of the count parameters in Periodic Advertising Subevent Data Request.

    - Fixed a corner case where LL_CONNECTION_PARAM_REQ is immediately followed by LL_TERMINATE_IND.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding.
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

      **Major Changes**
        -   [wireless_mcu][wireless_nbu] Replaced interrupt masking macros with static inline functions `PLATFORM_SetInterruptMask()` and `PLATFORM_ClearInterruptMask()` to ensure consistent BASEPRI value handling across all compilers. This addresses compiler-dependent behavior issues with the previous macro implementation.
        -   [wireless_mcu] Added BASEPRI-based interrupt masking in `PLATFORM_RemoteActiveRel()` to allow high-priority IRQs while ensuring only IMU0 or thread context can call this function.
        -   [wireless_mcu] Introduced `gPlatformUseHwParameter_d` compile flag to allow builds without HWParameter section. When undefined or set to 0, crystal trimming functions conditionally access HWParameters only when required.
      **Minor Changes**
        -   [kw47_mcxw72] Introduced platform-specific library for KW47/MCXW72 platforms.
        -   [kw47_mcxw72] Removed SH_MEM_TOTAL_SIZE override as it is now automatically calculated to match rpmsg-lite configuration.
        -   [wireless_mcu] Set RL_BUFFER_PAYLOAD_SIZE to word-aligned value as expected by rpmsg-lite.
        -   [wireless_mcu] Added system-generated HCI vendor events capability for debug and diagnostic purposes.
        -   [DBG] Added debug structure transmission over HCI vendor events with `NBUDBG_ConfigureHciVendorEvent()` API to enable/disable the feature.
        -   [DBG] Added debug structure versioning and logging buffer address/size information to debug structure.
        -   [DBG] Added stack overflow detection for armv8_m_mainline architecture.
        -   [Platform] Simplified enablement of reset features via pin detection 
            - Automatically selects `gUseResetByLvdForce_c` when `gAppForceLvdResetOnResetPinDet_d` is enabled.
            - Automatically select `gUseResetByDeepPowerDown_c` when `gAppForceDeepPowerDownResetOnResetPinDet_d` is enabled.
        -   [RNG] Replaced `gRngHasSecLibDependency_d` compilation switch with `gRngUseSecLib_d`.
      **Bug fixes**
        -   [wireless_mcu] Fixed race condition in `PLATFORM_RemoteActiveRel()` by adding verification loop to confirm NBU core execution before releasing power domain.
        -   [wireless_mcu] Added instruction synchronization barrier (__ISB()) after interrupt re-enable in `PLATFORM_RemoteActiveRel()` to ensure pending interrupts execute between critical sections.
        -   [wireless_mcu] Fixed external IO voltage isolation issue during low-power initialization - isolation is now cleared at init to ensure proper behavior.
        -   [wireless_mcu] Replaced spin-wait loops with event-based synchronization in NBU communication APIs. Added mutex protection to `PLATFORM_NbuApiReq()` and `PLATFORM_GetNbuInfo()` to prevent race conditions and deadlocks when multiple tasks call these APIs concurrently.
        -   [wireless_mcu] Fixed OSA bare metal event race condition in ICS where auto-clear event feature could cause tasks to become permanently stuck. Disabled auto-clear feature in bare metal builds and manually clear event flags after `OSA_EventWait()` returns successfully.
        -   [NVM] Fixed `NvIdle()` to prevent looping for more operations than the queue size.
        -   [NVS] Fixed blank check procedure to return false (non-blank) when checking a 0 length area.
        -   [NVS] Made external and internal flash ports consistent.
        -   [DBG] Fixed debug structure size and callback access issues - corrected memory placement overlap between reg_info and assert_info.
        -   [MISRA] Various MISRA compliance fixes in NVM, HWParameter, LowPower, SecLib, Platform modules and IFR offset definitions.

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
