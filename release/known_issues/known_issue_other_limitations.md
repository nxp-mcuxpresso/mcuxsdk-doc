# Other limitations

-   The following Connectivity Framework configurations are Experimental and not recommended for mass production:

    -   Power down on application power domain.

-   GenFSK `Connectivity_test` application is not operational with Low Power enabled.
-   Serial manager is only supported on UART \(not I2C nor SPI\).
-   If the FRO32K is configured as the clock source of the CM33 Core then the debug session will block in IAR CMSIS-DAP while debugging. Use a lower debug wire speed, for example 1 MHz instead of the default one.

    In IAR, the option is in **Runtime Checking** -\> **Debugger** -\> **CMSIS DAP** -\> **Interface** -\> **Interface speed**.
