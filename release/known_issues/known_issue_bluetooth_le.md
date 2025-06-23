# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   The maximum advertising data length is limited to 800 bytes.
-   Potential instabilities particularly with short Connection Intervals.

Periodic Advertising with Responses (PAwR):
-   Connection establishment using PAwR in LE Coded PHY can potentially fail.
-   Data report can potentially be truncated on the first AUX_ADV_IND of an extended advertising train containing an ACAD field.
-   Periodic Advertising with Response (PAwR) is not supported with the configuration "Subevent Interval = Number of Response Slots * Response Slot Spacing".

KW45/MCXW71:
No specific issues.


KW47/MCXW72:
Channel Sounding (CS): 
Limitations:
-	RTT with sounding sequence not supported
-	RTT sounding sequence NADM not supported
-   TX SNR not supported
-   LE 2M 2BT PHY not supported
-   Maximum 2 Channel Sounding procedures supported in parallel.
Known issues:
-   Potential instabilities with small CS offset or small subevent interval
-   Channel Sounding measurement performance at 2Mbps is affected by a sensitivity issue (shall be fixed in next release).
-   Link Layer is not able to trigger autonomous Feature Exchange procedure before initiating the Channel Sounding Capability Exchange procedure (shall be fixed in next release).
-   Link Layer does not properly manage collisions between Channel Sounding and other non-Channel Sounding procedures. This may lead to some LLCP timeout.