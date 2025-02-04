# Run an example application

To download and run the application, perform the following steps:

1.  See [Table 1](default_debug_interfaces.md#TABLE_HWPLATFORMS) to determine the debug interface that comes loaded on your specific hardware platform.
    -   If using J-Link with either a standalone debug pod or OpenSDA, install the J-Link software \(drivers and utilities\) from [SEGGER](https://www.segger.com/downloads/jlink/).
    -   To use J-Link for debug, remove J5, J6, J7, J8 jumpers and attach external J-Link on J1.
    -   For boards with the OSJTAG interface, install the driver from [KEIL](https://www.keil.com/).
2.  Connect the development platform to your PC via a USB cable.
3.  Connect USB cable between J11 on EVKB and PC USB port.
4.  Open the terminal application on the PC, such as PuTTY or TeraTerm, J11 on EVKB, and connect to the debug serial port number. To determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md). Configure the terminal with these settings:

    1.  115200 baud rate or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the *board.h* file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/ide_terminal_putty_configurations.png "Terminal (PuTTY) configurations")

5.  On the **Quickstart Panel**, click **Debug 'evkbmimxrt1170\_demo\_apps\_hello\_world’ \[Debug\]**.

    ![](../images/ide_debugging_hello_world_case.png "Debug hello_world case")

6.  The first time you debug a project, the **Debug Emulator Selection** dialog is displayed, showing all supported probes that are attached to your computer. Select the probe through which you want to debug and click **OK**. \(For any future debug sessions, the stored probe selection is automatically used, unless the probe cannot be found.\)

    ![](../images/ide_attached_probes_debug_emulator_selection.png "Attached Probes: debug emulator selection")

7.  The application is downloaded to the target and automatically runs to `main()`.

    ![](../images/ide_stop_at_main_when_running_debugging.png "Stop at main() when running debugging")

8.  Start the application by clicking **Resume**.

    ![](../images/ide_resume_button.png "Resume button")


The `hello_world` application is now running and a banner is displayed on the terminal. If not , check your terminal settings and connections.

![](../images/ide_text_display_of_hello_world_demo.jpg "Text display of the hello_world demo")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

