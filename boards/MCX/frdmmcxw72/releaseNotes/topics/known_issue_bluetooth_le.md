# Bluetooth LE 

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the app\_preinclude.h header file.

#   Bluetooth LE controller:

Max number of connections supported : 8

Potential instabilities particularly with short Connection Intervals

Channel Sounding (CS) not supported: 
-   RTT with Random sequence
-   RTT Random sequence NADM
-   TX SNR
-   LE 2M 2BT PHY
-   More than one CS procedure in parallel
-   Potential instabilities with small CS offset or small subevent interval
-   TQI not accurate

Periodic Avdertising with Responses (PAwR):
-   Incorrect data in Periodic Advertising Response is reported if AUX_SYNC_SUBEVENT_RSP contained an extended header.
-   Sync device cannot synchronize on more than 32 subevents.
-   Connection establishment using PAwR in LE Coded PHY can potentially fail.
-   Data report can potentially be truncated on the first AUX_ADV_IND of an extended advertising train containing an ACAD field.

**Parent topic:**[Known issues](../topics/known_issues.md)

