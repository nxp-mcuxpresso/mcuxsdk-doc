# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   The maximum advertising data length is limited to 800 bytes.

Periodic Advertising with Responses (PAwR):
-   Connection establishment using PAwR in LE Coded PHY can potentially fail.
-   Periodic Advertising with Response (PAwR) is not supported with the configuration "Subevent Interval = Number of Response Slots * Response Slot Spacing".

KW45/MCXW71:
No specific issues.


KW47/MCXW72:
Channel Sounding (CS): 
Limitations:
-   RTT w/ Sounding Sequence is not supported
-   Phase-based NADM - Sounding Sequence is not supported
-   TX SNR not supported
-   LE 2M 2BT PHY not supported
-   Scheduling of activities may be non optimal when multiple Channel Sounding procedures are running in parallel.
Known issues:
-   Potential instabilities with small CS offset or small subevent intervals.
-   Channel Sounding measurement performance at 2Mbps is affected by a sensitivity issue.
-   Link Layer is not able to trigger autonomous Feature Exchange procedure before initiating the Channel Sounding Capability Exchange procedure.