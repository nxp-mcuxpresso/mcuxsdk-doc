# Enable MCU UARTs

1.  Connect usb typec cable from pc to typec port J15 of board.(It will emulate four serial ports[e.g. COM0 - LPUART8, COM1, COM2 - LPUART1, COM3 - LPUART2] in pc)

    - COM0(LPUART8 - use as uart of cortex-m33 core1), please perform the following steps,

      a. Enable BCU,

        - Change SW7-1 from OFF.(For imx943evk proto2 board, base board version: REV B1)

        - Change SW7-1 from ON.(For imx943evk proto1 board)

      b. Enable the serial port via bcu command,

        - `bcu set_gpio fta_jtag_host_en 0 -board=imx943evk19b1` or `bcu set_gpio fta_jtag_host_en 0 -board=imx943evk19a0`

        - `bcu set_gpio fta_jtag_uart_sel 1 -board=imx943evk19b1` or `bcu set_gpio fta_jtag_uart_sel 1 -board=imx943evk19a0`

    - COM2(LPUART1 - use as uart of Cortex-A)

    - COM3(LPUART2 - use as uart of Cortex-m33 core0)

2.  Connect two usb2uart converter from pc to arduino interface of board.(It will emulate two serial ports[e.g. COM4 - LPUART11, COM5 - LPUART12] in pc)

    -   COM4(LPUART11 - use as uart of cortex-m7 core0)

        J48-2(M2_UART11_RXD) -- TX of usb2uart converter  -- pc

        J48-4(M2_UART11_TXD) -- RX of usb2uart converter  -- pc

        GND   ----------------- GND of usb2uart converter -- pc

    -   COM5(LPUART12 - use as uart of cortex-m7 core1)

        J44-4(M1_UART12_RXD) -- TX of usb2uart converter  -- pc

        J44-2(M1_UART12_TXD) -- RX of usb2uart converter  -- pc

        GND   ----------------- GND of usb2uart converter -- pc

    **Note:**

    -   mx943evk for `m33_image.bin` is used for `rpmsg str echo`, `rpmsg ping pong` and `power_mode_switch_rtos`.

    -   mx943alt for `m33_image.bin` is used for almost other examples.

    -   JTAG cannot be used when LPUART8 is used.

    -   Pls change uart from LPUART8 to LPUART1 and generate m33_image.bin with command `make config=mx94alt all` when debugging with jtag.

        -   For MCUXPresso SDK
	```
	_boards/imx943evk/board.h
        #define BOARD_DEBUG_UART_INSTANCE 8 -> #define BOARD_DEBUG_UART_INSTANCE 1
	```

**Parent topic:**[Run a demo application](../topics/run_a_demo_application.md)

