# What is new

The following changes have been implemented compared to the previous SDK release version.

-   **Bluetooth LE host stack and applications:**
    -   Early Access Release.
    -   Bluetooth LE sample applications: `ble_shell`, `w_uart`.
    -   Bluetooth LE Channel Sounding applications: `loc_reader`, `loc_user_device`, `wireless_ranging`.
    -   Bluetooth LE Channel Sounding applications are controlled access.
    -   Added LCE support.
	-   Documentation update.
    -   Other minor fixes and stability improvements.
 
-   **Bluetooth LE controller:**
    -   Early Access Release
    -   Channel Sounding (controlled Access)
    -   Minor fixes and stability improvements

-   **Zigbee:**
    -   R23 ZPSAPL BDB uses `eAplZdoJoinNetwork` with TLVs for JoinerEncaps.
    -   R23 examples of ZC, ZR with R23\_UPDATES guard for DLK enable.
    -   R23 examples of ZR joining with off network key DLK.
    -   R23 examples of ZR with default cluster enabled to process the new clusters.
    -   R23 ZPSAPL handle DLK joiner with default TCLK.
    -   R23 examples of ZC configuring the DLK pass phrase.
    -   R23 ZPSAPL set function to configure the DLK pass phrase.
    -   R23 examples of ZC configuring the DLK AIB attributes.
    -   R23 ZPSAPL AIB set function to configure the DLK options
    -   R23 example of ZC with default cluster enabled to process the new clusters.
    -   R23 examples of ZC with DLK AES-128.
    -   R23 examples of ZC mandatory beacon appendix with NetworkWideTLVs.
    -   R23 ZPSAPL after off network key DLK process UpdateDevice to transport the network key.
    -   R23 ZPSAPL deny request to retrieve authentication token, if not supported in AIB.
    -   R23 ZPSAPL fix the use of well-known pass phrase identification 255.
    -   ZPSNWK cleanup inconsistent NT entries pointing to the same IEEE address.
    -   R23 ZPSAPL fix the test of the ZPS\_EVENT\_TLV\_FOUND flag.
    -   R23 AT-ZCP displays the BTR TP2 cluster number.
    -   R23 ZPSAPL set DLK state to COMPLETE only if it was started.
    -   Examples: `zigbee_ed_rx_off`: add missing TRDC path for MAC split.
    -   Platform MCXW72 crypto support for deprecated API.
    -   R23 ZPSAPL Prevent DLK state START for joiners with ZB3.0 key negotiation.
    -   ZPSNWK Allow Device Annce which seems ours to ZDP for address conflict verification.
    -   R23 ZPSAPL Fix `zps_pvAesHash` wrapper to support text longer than 128 bits.
    -   ZPSAPL Use the length parameter of `zps_pvAesHash`.
    -   R23 ZPSAPL Implement on-network DLK triggered by Node Desc Rsp.
    -   Platform common crypto support for block random bytes generation.
    -   Platform crypto header support for block random bytes generation.
    -   Platform MCXW72 crypto support for block random bytes generation.
    -   R23 ZPSAPL Define DLK\_DISALLOWED for dev permissions configured on TC.
    -   Examples: Add TRDC driver include.
    -   Platform crypto.c changed to rename z`bPlatCryptoAesDecrypt`.
    -   BDB renamed `zbPlatCryptoAesDecrypt`.
    -   Platform header renamed to `zbPlatCryptoAesDecrypt`.
    -   R23 ZPSAPL `Node Desc Rsp` with `SelectedKeyNegotiationMethod` TLV.
    -   R23 ZPSNWK `SetCommissionAppendix` sets the source MAC address field.
    -   R23 ZPSAPL Implement Simple Password Exponential Key Exchange \(SPEKE\) over Curve25519 MBEDTLS.

-   **Connectivity framework**

    -   **Major Changes (User Applications may be impacted)**

        -   mcux github support with cmake/Kconfig from sdk3 user shall now use CmakeLists.txt and Kconfig files from root folder. Compilation should be done using west build command. In order to see the Framework Kconfig, use command >west build -t guiconfig
        -   Board files and linker scripts moved to examples repository

    -   **Bugfixes**

        -   [platform lowpower]
            -   Entering Deep down power mode will no longer call PLATFORM_EnterPowerDown(). This API is now called only when going to Power down mode

    -   **Platform specific**

        -   Early access release only:
            -   Deep sleep power mode not fully tested. User can experiment deep sleep and deep down modes using low power reference design applications
            -   XTAL32K-less support using FRO32K not tested

    -   **Overal folder restructuring for SDK3**

        -   [Platform]:
            -   Rename platform_family from connected_mcu/nbu to wireless_mcu/nbu
            -   platform family have now a dedicated fwk_config.h, rpmsg_config.h and SecLib_mbedtls_config.h
        -   [Services]:
            -   Move all framework services in a common directory "services/"



