# Bluetooth LE 

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the app\_preinclude.h header file.

#   Bluetooth LE controller:

Max number of connections supported : 8

Potential instabilities particularly with short Connection Intervals

Channel Sounding (CS) not supported: 
-	RTT with Random sequence
-	RTT Random sequence NADM
-   TX SNR
-   LE 2M 2BT PHY
-	More than one CS procedure in parallel
-   Potential instabilities with small CS offset or small subevent interval

**Parent topic:**[Known issues](../topics/known_issues.md)

