# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   Max number of connections supported : 8 

-   Potential instabilities particularly with short Connection Intervals

Channel Sounding (CS): 
-	RTT with Random sequence not supported
-	RTT Random sequence NADM not supported
-   TX SNR not supported
-   LE 2M 2BT PHY not supported
-	2 CS procedures in parallel supported (some instabilities observed)
-   Potential instabilities with small CS offset or small subevent interval

Periodic Advertising with Responses (PAwR):
-   Connection establishment using PAwR in LE Coded PHY can potentially fail.
-   Data report can potentially be truncated on the first AUX_ADV_IND of an extended advertising train containing an ACAD field.