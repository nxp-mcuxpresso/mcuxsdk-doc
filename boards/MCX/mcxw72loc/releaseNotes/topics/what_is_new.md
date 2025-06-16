# What is new 

The following changes have been implemented compared to the previous SDK release version \(25.06.00\).


-   **Bluetooth LE Host Stack and Applications**
    ### Added
    -   **Gap_SetBondedDeviceName()** to set device name using NVM index.
    -   **RAS** queue for GATT indications sent.
    -   **gHciStatusBase_c** to **csError** status.
    -   Option to use statically allocated **memory** for dynamic **GATT database** (prevents heap fragmentation).
    -   Checks for **controller** supported features and setting **PAST bits** accordingly.
    -   **Shell commands** to list peer devices and trigger connection handover.
    -   **cs_sync_phy** parameter to mDefaultRangeSettings (**renamed** from outdated RTTPhy).

    ### Improved
    -   **Stack Host** now saves the most recently set **random address** after successful controller response.
    -   Miscellaneous **minor** application **updates**.

    ### Fixed
    -   Compilation issue in **loc_reader app** with real-time RAS transfer.
    -   **RAS** uses correct bit for data overwrite preference.

    ### Changed
    -   Updated **Bluetooth LE Host Documentation**.
    -   **BLE_Shell** Tx timer interval adjusted for **max throughput** on 1M PHY.
    -   **CS_ConfigVendorCommand** updated with **Inline Phase Return** field.
    -   Renamed **tx_pwr_phy** to **phy** and removed obsolete rtt_phy field.
    -   Updated **documentation** to clarify **Controller Privacy** restrictions .

    -   Details can be found in **CHANGELOG.md**.
-   **Bluetooth LE controller**
    -   HADM, PAwR fixes and stability improvements.

-   **Transceiver drivers (XCVR)**
    -   Added support for Bluetooth LE Channel Sounding
    -   Added API to control PA ramp type and duration.

-   **Connectivity framework**

    -   **Major Changes**
        -   [KW47/MCXW72] NBU: Add new fwk_platform_dcdc.[ch] files to allow DCDC stepping by using SPC high power mode. This requires new API in board_dcdc.c files. Please refer to new compilation MACROs gBoardDcdcRampTrim_c and gBoardDcdcEnableHighPowerModeOnNbu_d in board_platform.h files located in kw47evk, kw47loc, mcxw72loc, frdmmcxw72 board folders.
        -   [KW45/MCXW71/KW47/MCXW72] Trigger an interrupt each time App core calls PLATFORM_RemoteActiveReq() to access NBU power domain in order to restart NBU core for domain low power process
    -   **Minor Changes (no impact on application)**

        -   **Services**
            - [SecLib_RNG]
              Rename mSecLibMutexId mutex to mSecLibSssMutexId in SecLib_sss.c
              Remove MEM_TRACKING flag from RNG.c
              Implement port to fsl_adapter_rng.h API using gRngUseRngAdapter_c compil Macro from RNG.c
              Add support for BLE debug Keys in SecLib and SecLib_sss.c with gSecLibUseBleDebugKeys_d - for Debug only
            - [FSCI] Add queue mechanism to prevent corruption of FSCI global variableAllow the application to override the trig sample number parameter when gFsciOverRpmsg_c is set to 1
            - [DBG][btsnoop] Add a mechanism to dump raw HCI data via UART using SBTSNOOP_MODE_RAW
            - [OTA]
              OtaInternalFlash.c: Take into account chunks smaller than a flash phrase worth
              fwk_platform_ot.c: dependencies and include files to gpio, port, pin_mux removed

        -   **Platform specific**
		    - [kw45_mcxw71][kw47_mcxw72]
              fwk_platform_reset.h : add compil Macro gUseResetByLvdForce_c and gUseResetByDeepPowerDown_c to avoid compile the code if not supported on some platforms
              New compile Flag gPlatformHasNbu_d
              Rework FRO32K notification service for MISRA fix

Details can be found in [CHANGELOG.md](../../../../../../middleware/wireless/framework/CHANGELOG.md)

