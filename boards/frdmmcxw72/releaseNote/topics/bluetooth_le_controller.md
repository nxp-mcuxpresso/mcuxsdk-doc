# Bluetooth LE controller

-   Main features supported:

    -   Peripheral Role
    -   Central Role
    -   Multiple PHYs \(1 Mbps, 2 Mbps, Coded PHY\)
    -   Asymmetric Connections
    -   Public/Random/Static Addresses
    -   Network/Device Privacy Modes
    -   Extended Advertising
    -   Extended Scanning
    -   Passive/Active Scanning
    -   LE Encryption
    -   LE Ping Procedure
    -   HCI Test Interface
    -   UART Test Interface
    -   Randomized Advertising Channel Indexing
    -   Sleep Clock Accuracy Update - Mechanism
    -   ADI Field in Scan Response Data
    -   HCI Support for Debug Keys in LE - Secure Connections
-   Main capabilities supported:

    -   Simultaneous Scanning 1 Mbps and Long Range
    -   Scanning and Advertising in parallel
    -   24 connections as central role
    -   24 connections as peripheral role
    -   Any combination of central and peripheral roles \(24 connections maximum\)
    -   Eight connections with 7.5 ms connection interval
    -   Two advertising sets in parallel
    -   26 Accept List entries
    -   36 Resolvable Private Address \(RPA\) entries
    -   Up to six Chain Packets per Extended Advertising set
    -   Enhanced Notification on end of - Scanning/Advertising/Connection events
    -   Connection event counter associated to Bluetooth LE packet reception
    -   Timestamp associated to Bluetooth LE packet reception
    -   RF channel info associated to Bluetooth LE packet reception
    -   NXP proprietary Bluetooth LE Handover feature
    -   Support experimental features **Advertising Coding Selection** and **Decision Based Advertising Filtering \(DBAF\)**. See [Note](#note) below.

**Note:** Project configurations that require usage of the Bluetooth LE Controller including all Bluetooth LE examples and Matter over Thread configurations require the Radio Subsystem \(NBU\) Firmware to be re-programmed with the firmware provided in the SDK under *middleware\\wireless\\ble\_controller\\bin* \(Bluetooth LE only\) or *middleware\\wireless\\ieee-802.15.4\\bin\\k32w1* \(Bluetooth LE and IEEE 802.15.4 multiprotocol targeting Matter\). For NBU programming steps, see the *EVK Quick Start Guide* and Secure Provisioning SDK \(SPSDK\) documentation.

**Note:** Project configuration enabling Experimental features requires the Radio Subsystem \(NBU\) Firmware to be reprogrammed with the firmware provided in the SDK under *\\middleware\\wireless\\ble\_controller\\bin\\experimental\\*. For NBU programming steps, see the *EVK Quick Start Guide* and Secure Provisioning SDK \(SPSDK\) documentation.

**Parent topic:**[Wireless connectivity middleware summary](../topics/wireless_connectivity_middleware_summary.md)

