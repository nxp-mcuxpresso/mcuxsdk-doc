# Bluetooth LE Controller

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

    -   Simultaneous scanning 1 Mbps and Long Range
    -   Scanning and advertising in parallel
    -   24 connections as a central role
    -   24 connections as a peripheral role
    -   Any combination of central and peripheral roles \(24 connections maximum\)
    -   8 connections with a 7.5 ms connection interval
    -   Two advertising sets in parallel
    -   26 Accept List entries
    -   36 Resolvable Private Address \(RPA\) entries
    -   Up to six Chain Packets per Extended Advertising set
    -   Enhanced Notification on end of - Scanning/Advertising/Connection events
    -   Connection event counters associated to Bluetooth LE packet reception
    -   Timestamp associated to Bluetooth LE packet reception
    -   RF channel info associated to Bluetooth LE packet reception
    -   NXP proprietary Bluetooth LE Handover feature
    -   Decision Based Advertising Filtering \(DBAF\) - Experimental feature. See [Note](#note) below.
    -   Advertising Coding Selection \(ACS\) - Experimental feature. See [Note](#note) below.
    -   Periodic Advertising with Responses \(PAwR\) - Experimental feature. See [Note](#note) below.
    Additional features supported for KW47 and MCX W72 devices:
    -   Channel Sounding - Experimental feature

        
        **Note:**
        Project configuration enabling Experimental features on KW45 and MCX W71 requires the Radio Subsystem \(NBU\) 
        Firmware to be reprogrammed with the firmware provided in the SDK under *\\middleware\\wireless\\ble\_controller\\bin\\experimental\\*.
        For NBU programming steps, see the *EVK Quick Start Guide* and Secure Provisioning SDK \(SPSDK\) documentation.

        Project configurations that require usage of the Bluetooth LE controller including all Bluetooth LE examples require the Radio Subsystem \(NBU\) Firmware to be re-programmed with the firmware provided in the SDK under middleware\\wireless\\ble\_controller\\bin.

