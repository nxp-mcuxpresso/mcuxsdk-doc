# What is new

The following changes have been implemented compared to the previous SDK release version \(2.16.100\).

-   **Bluetooth LE host stack and applications**

    -   Early Access Release.
    -   Periodic advertising with responses - experimental.
    -   Encrypted Advertising Data - experimental.
    -   Documentation update.
    -   Minor fixes and stability improvements.
	
-   **Bluetooth LE controller**

    - Early Access Release
    - Periodic Advertising with Response (PAwR) – Experimental
    - Minor fixes and stability improvements
    - Channel Sounding (controlled Access)

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

