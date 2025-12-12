# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   The maximum Advertising data length is limited to 800 bytes.
-   The scanner may sporadically miss some chained packets.

Periodic Advertising with Responses (PAwR):
-   Periodic Advertising with Response (PAwR) is not supported with the configuration "Subevent Interval = Number of Response Slots x Response Slot Spacing with Response Slot Spacing = 0x2".
-   Periodic Advertising placement with connection events is unoptimized.
-   The feature is not functional with the Free-Running Oscillator (FRO32K); it requires a 32 KHz Crystal Oscillator with accuracy less than 50 ppm.


KW45/MCXW71:
No specific issues.

KW47/MCXW72:
Channel Sounding (CS): 
Limitations:
-   RTT with Sounding Sequence is not supported.
-   LE 2M 2BT PHY is not supported.
-   Maximum 6 Channel Sounding procedures are supported in parallel.
-   Scheduling of activities may be non optimal when multiple Channel Sounding procedures are running in parallel.
-   Phase measurement bias is within certification range (<1.7x2πns) with KW47 EVK board. However, if different PCB or antenna matching is used, some bias may appear due to increased delay.
Known issues:
-   When CS Subevents are configured very close from each other (<700us), some Subevents may be aborted with reason 0x3.
-   When CS offset is configured too close from ACL anchor point, the anchor point may not be served (TX on central or RX on peripheral will not happen). Ideally, CS Offset should be configured greater than 1ms.
-   RTT bias compensation:
    - For parts not properly configured at production (IFR blank), RTT bias may not be compensated properly. Consequently, an inaccuracy of +/-2m may be observed.