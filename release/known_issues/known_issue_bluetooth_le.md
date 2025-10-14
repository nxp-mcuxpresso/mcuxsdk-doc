# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   The maximum Advertising data length is limited to 800 bytes.
-   Missing chained packets during scanning.
-   Need to add a dummy nbu request to wake-up NBU core during asynchronous wakeup to avoid low power race condition issue (ie: for NBU ramlog dump from shared memory).

Periodic Advertising with Responses (PAwR):
-   Periodic Advertising with Response (PAwR) is not supported with the configuration "Subevent Interval = Number of Response Slots * Response Slot Spacing".
-   Unoptimized Periodic Advertising placement with Connection events.


KW45/MCXW71:
No specific issues.

KW47/MCXW72:
Channel Sounding (CS): 
Limitations:
-   RTT with Sounding Sequence is not supported.
-   TX SNR is not supported.
-   LE 2M 2BT PHY is not supported.
-   Maximum 6 Channel Sounding procedures are supported in parallel.
-   Scheduling of activities may be non optimal when multiple Channel Sounding procedures are running in parallel.
-   Phase measurement bias is within certification range (<1.7x2πns) with KW47 EVK board. However, if different PCB or antenna matching is used, some bias may appear due to increased delay.
-   Channel Sounding is not supported with internal FRO32.
Known issues:
-   When CS_SYNC=2Mbps, sensitivity drops at –85dBm (vs –95dBm for 1Mbps).
-   NADM may report false positive attacks when using localization board at 2Mbps.
-   When CS Subevents are configured very close from each other (<700us), some Subevents may be aborted with reason 0x3.
-   When CS offset is configured too close from ACL anchor point, the anchor point may not be served (TX on central or RX on peripheral will not happen). Ideally, CS Offset should be configured greater than 1ms.
-   Wireless_ranging stability issue in test mode 2Mbps with RTT random sequence payload 128 bits.
-   RTT bias compensation:
    - For parts not properly configured at production (IFR blank), RTT bias may not be compensated properly. Consequently, an inaccuracy of +/-2m may be observed.
    - Temperature variation: RTT variation of +/-2m is observed based on temperature.