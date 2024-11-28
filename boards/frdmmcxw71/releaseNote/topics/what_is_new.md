# What is new

The following changes have been implemented compared to the previous SDK release version.

-   **Bluetooth LE host stack and applications:**

    -   Early Access Release.
    -   Periodic advertising with responses - experimental.
    -   Encrypted Advertising Data - experimental.
    -   Documentation update.
    -   Minor fixes and stability improvements.

-   **Bluetooth LE controller**

    - Early Access Release
    - Periodic Advertising with Response (PAwR) – Experimental
    - Minor fixes and stability improvements
    - Channel Sounding (controlled Access)

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
    -   Platform MCXW71 crypto support for deprecated API.
    -   R23 ZPSAPL Prevent DLK state START for joiners with ZB3.0 key negotiation.
    -   ZPSNWK Allow Device Annce which seems ours to ZDP for address conflict verification.
    -   R23 ZPSAPL Fix `zps_pvAesHash` wrapper to support text longer than 128 bits.
    -   ZPSAPL Use the length parameter of `zps_pvAesHash`.
    -   R23 ZPSAPL Implement on-network DLK triggered by Node Desc Rsp.
    -   Platform common crypto support for block random bytes generation.
    -   Platform crypto header support for block random bytes generation.
    -   Platform MCXW71 crypto support for block random bytes generation.
    -   R23 ZPSAPL Define DLK\_DISALLOWED for dev permissions configured on TC.
    -   Examples: Add TRDC driver include.
    -   Platform crypto.c changed to rename z`bPlatCryptoAesDecrypt`.
    -   BDB renamed `zbPlatCryptoAesDecrypt`.
    -   Platform header renamed to `zbPlatCryptoAesDecrypt`.
    -   R23 ZPSAPL `Node Desc Rsp` with `SelectedKeyNegotiationMethod` TLV.
    -   R23 ZPSNWK `SetCommissionAppendix` sets the source MAC address field.
    -   R23 ZPSAPL Implement Simple Password Exponential Key Exchange \(SPEKE\) over Curve25519 MBEDTLS.
-   **Connectivity framework:**

    -   Optimized \`\`PLATFORM\_RemoteActiveReq\(\)\`\` execution time.

    -   Optimized critical sections for Radio Subsystem \(NBU\) firmware.


