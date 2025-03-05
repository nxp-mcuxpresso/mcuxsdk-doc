# Bluetooth LE

-   In case more than 8 Bluetooth LE connections are configured, sporadic packet loss or disconnection events may be observed.

-   Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the app\_preinclude.h header file.

-   TX data path integrity is not guaranteed during the Bluetooth LE handover.

#   Bluetooth LE controller:

-   Max number of connections supported : 8 

-   Potential instabilities particularly with short Connection Intervals 

**Parent topic:**[Known issues](../topics/known_issues.md)

