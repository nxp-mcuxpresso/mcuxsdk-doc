# Bluetooth LE

Most sensor applications have pairing and bonding disabled to allow a faster interaction with mobile applications. These two security features can be enabled in the `app_preinclude.h` header file.

#   Bluetooth LE controller:

-   The maximum Advertising data length is limited to 800 bytes.
-   The scanner may sporadically miss some chained packets.

Periodic Advertising with Responses (PAwR):
-   Periodic Advertising with Response (PAwR) is not supported with the configuration "Subevent Interval = Number of Response Slots x Response Slot Spacing with Response Slot Spacing = 0x2".
-   The feature is not functional with the Free-Running Oscillator (FRO32K); it requires a 32 KHz Crystal Oscillator with accuracy less than 50 ppm.
Decision Based Advertising Filtering (DBAF):
-   Fail to establish connection using extended create connection command if peer advertising address is on primary channel and if filter accept list and/or address resolution is being used. If the peer advertising address is on secondary, the connection establishment succeeds.

KW45/MCXW71:
No specific issues.

KW47/MCXW72:
Channel Sounding (CS):
Information:
-   RF Bandwidth Occupancy and Connections/Channel Sounding Activities:
The RF bandwidth occupancy is tightly coupled with configured activities, including the number of connections, connection event durations, the number of Channel Sounding (CS) procedures, and related CS parameters (e.g., subevent length, repeat mode).
The Link Layer Scheduler is responsible for allocating RF bandwidth to these activities, optimizing bandwidth utilization. However, because each activity operates on its own timing constraints, some RF collisions are expected. This is inherent to the Bluetooth LE protocol, particularly when peripheral roles are configured, as anchor placement is controlled by the central peer devices.
The application controls several timing parameters, such as connection interval and subevent length. To optimize user experience, the Link Layer expects the application to adjust these parameters to achieve the best RF bandwidth occupancy with the lowest occurrence of RF collisions.

Limitations:
-   RTT with Sounding Sequence is not supported.
-   Maximum 6 Channel Sounding procedures are supported in parallel.
-   Phase measurement bias is within certification range (<1.7x2πns) with KW47 EVK board. However, if different PCB or antenna matching is used, some bias may appear due to increased delay.

Known issues:
-   NADM RTT payload 96bits BT2.0 raises false positives.
-   When CS Subevents are configured very close from each other (<700us), some Subevents may be aborted with reason 0x3.
-   When CS offset is configured too close from ACL anchor point, the anchor point may not be served (TX on central or RX on peripheral will not happen). Ideally, CS Offset should be configured greater than 1ms.
-   RTT bias compensation:
    - For parts not properly configured at production (IFR blank), RTT bias may not be compensated properly. Consequently, an inaccuracy of +/-2m may be observed.