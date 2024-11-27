# What is new

The following is the list of new features and improvements in this release.

-   **Bluetooth LE host stack and applications:**

    -   Early Access Release.
    -   Periodic advertising with responses - experimental.
    -   Encrypted Advertising Data - experimental.
    -   Documentation update.
    -   Minor fixes and stability improvements.

-   **Bluetooth LE controller:**
    -   Fixed a case of connection initiation retry failure after AUX\_CONNECT\_RSP with CRC error is received \(and peer device is using privacy\).

    -   Fixed RPA address generation not refreshed properly in the case of non-connectable undirected advertising.

    -   Fixed a timing issue in case of concurrent activities \(connection and extended advertising\).

    -   Fixed a case of race condition between incoming and outgoing connection updates.

    -   Fixed some invalid fields in advertising reports.

    -   Fixed channel selection, algorithm 2 is not properly disabled.

    -   Fixed a case of connection drop when slave latency is enabled.

    -   Fixed a case of encrypted packet being sent before `LL_START_ENC_RSP`.

    -   Optimized real-time processing \(related to critical sections\) for advertising and direct test mode \(DTM\).

    -   Optimized connection event occupation in some cases of packets retransmission.

    -   Added advertising address in the enhanced notification messages.

-   **Connectivity framework:**
    -   Optimized \`\`PLATFORM\_RemoteActiveReq\(\)\`\` execution time.
    -   Optimized critical sections for Radio Subsystem \(NBU\) firmware.
-   **Low-power reference design applications \(central and peripheral\):**
    -   Solved build issues in case Pairing and Bonding are disabled.

