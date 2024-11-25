# What is new

The following changes have been implemented compared to the previous SDK release version \(2.15.000\).

-   **Bluetooth LE host stack and applications**

    -   New Features and Improvements:

        -   Miscellaneous updates in sample applications.

        -   Updated Handover to transfer pending packets in the controller from the source anchor to the destination anchor.

        -   Documentation updates.

    -   Bug fixing:

        -   Fixed issue in HCI frame length fragmentation check.
        -   GATT caching refactorization for multiple connection support.
        -   Fixed MISRA issues in sample applications.
        -   Fixed memory leak in `wireless_uart` sample application.
        -   Set `identityHeaderList` before `resetActiveDeviceSlot()` call.
        -   Fixed issue with the `AttMTU` value requested by the application GATT client following the response from a GATT server.
        -   Fixed possible memory overflow in `gap_checkForAutoConnect` results.
-   **Bluetooth LE controller**

    -   Improved Connection Handover feature.

    -   Optimized Passive Scan and Scan Initiating states.

    -   Optimized Critical Sections duration.

    -   Improved robustness of Rx packets filtering.

    -   Optimized throughput.

    -   Improved reliability of hardware deadlock detection mechanism.

    -   Improved scheduling of shorter Connection Intervals when Connection Intervals are multiple of each other.

    -   Fixed a Link Layer real time issue causing a case of disconnection cause 0x3E \(CONNECTION FAIL TO ESTABLISH\).

    -   Fixed a case of disconnection cause 0x1F \(UNSPECIFIED ERROR\), due to collision of Connection Update and PHY Update procedures.

    -   Fixed a case of connection establishment failure erroneously aborted by lower priority activities. For example, the Advertising activity.

    -   Fixed a case of Peripheral connection establishment failure due to undetected collision with already established connections.

    -   Fixed a case of "Connection Failed to be Established \(0x3E\)" caused by wrong Access Address used when Central establishes the connection.

    -   Fixed MISRA issues.

    -   Fixed the mechanism for disabling enhanced notifications for connection-related events.
-   **XCVR**

    -   Removed support for A0 silicon version.
-   **Connectivity framework**

    -   **\[HWparams\]**:
        -   Support for location of HWParameters and Application Factory Data IFR in IFR1.

        -   Default is still to use HWparams in Flash to keep backward compatibility.

        -   \[RNG\]: API updates:

            -   New APIs `RNG_IsReseedneeded()`, `RNG_SetSeed()` to provide seed to PRNG. See `BluetoothLEHost_ProcessIdleTask()` in `app_conn.c`.

            -   New APIs `RNG_SetExternalSeed()`: User can provide external seed. Typically used by Radio Subsystem \(NBU\) firmware for App core to set a seed to RNG.

        -   \[NVS\] Wear statistics counters added. Fixed `nvs_file_stat()` function.

        -   \[NVM\] fixed. `Nv_Shutdown()` API.

-   **Low-power reference design applications \(central and peripheral\)**

    -   Disabled power down experimental feature on peripheral application in advertising as better performance has been observed in deep sleep.
-   **GenFSK link layer**

    -   No fixes or changes.

