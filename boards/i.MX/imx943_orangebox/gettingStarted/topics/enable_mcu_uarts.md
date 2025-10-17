# Enable MCU UARTs

1.  Connect the USB Type C cable from the pc to tthe Type C port J24 of the board.(It emulates four serial ports[for example, COM0 - LPUART3, COM1 - LPUART11 Or LPUART12, COM2 - LPUART1, COM3 - LPUART2] on the PC.)

    - COM0(LPUART3 - use as UART of the Cortex-m33 core1)

    - COM1(LPUART11 - use as UART of the Cortex-m7 core0, LPUART12 - use as UART of the Cortex-m7 core1; Both cannot be used at the same time)

      - Select LPUART11: Insert jumpers into J1306(route LPUART11 to FTB UART) and J1307(Select the FTB UART).

      - Select LPUART12: Remove jumper from J1306(route LPUART12 to FTB UART) and insert jumper into J1307(Select the FTB UART).

    - COM2(LPUART1 - use as UART of the Cortex-A)

    - COM3(LPUART2 - use as UART of the Cortex-m33 core0: System Manager runs on this core)

**Parent topic:**[Run a demo application](../topics/run_a_demo_application.md)

