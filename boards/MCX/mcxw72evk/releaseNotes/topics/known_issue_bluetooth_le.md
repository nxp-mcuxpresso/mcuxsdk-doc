# Bluetooth LE 

TX data path integrity is not guaranteed during the Bluetooth LE handover.

Some instabilities may occur in demanding Bluetooth LE connection scenarios \(such as mutiple Bluetooth LE connection, very short Connection Intervals\), and in some Channel Sounding configurations.

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

**Note:** Documentation may not be fully updated to refer to MCX W72 devices.

**Parent topic:**[Known issues](../topics/known_issues.md)

