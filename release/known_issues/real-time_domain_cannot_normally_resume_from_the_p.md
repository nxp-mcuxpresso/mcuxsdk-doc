# Real-Time Domain cannot normally resume from the power-down mode due to EdgeLock secure enclave \(S400\) failure

There is an issue in EdgeLock secure enclave \(S400\) during state restoring phase for silicon A0.1. When Real Time Domain \(RTD\) is about to enter the power-down mode, S400 is promoted to save the current state to the memory. However, once RTD wakes up, S400 encounters an error when trying to restore the state.

This error can cause S400 decide to reset RTD, which means RTD cannot normally resume from the power-down mode.
