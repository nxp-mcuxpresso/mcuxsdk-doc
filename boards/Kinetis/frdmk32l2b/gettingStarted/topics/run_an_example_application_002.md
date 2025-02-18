# Run an example application

To download and run the application, perform these steps:

1.  See the table in [default\_debug\_interfaces.md\#](default_debug_interfaces.md#) to determine the debug interface that comes loaded on your specific hardware platform.
    -   For boards with CMSIS-DAP/mbed/DAPLink interfaces, visit [developer.mbed.org/handbook/Windows-serial-configuration](http://developer.mbed.org/handbook/Windows-serial-configuration) and follow the instructions to install the Windows® operating system serial driver. If running on Linux® OS, this step is not required.
    -   The user should install LPCScrypt or MCUXpresso IDE to ensure LPC board drivers are installed.
    -   For boards with P&E Micro interfaces, visit [www.pemicro.com/support/downloads\_find.cfm](http://www.pemicro.com/support/downloads_find.cfm) and download the P&E Micro Hardware Interface Drivers package.
2.  Connect the development platform to your PC via USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        ![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

4.  In IAR, click the **Download and Debug** button to download the application to the target.

    ![](../images/download_and_debug_button.png "Download and Debug button")

5.  The application is then downloaded to the target and automatically runs to the `main()` function.

    ![](../images/stop_at_main_running_debugging_k32l2a4s.png "Stop at main() when running debugging")

6.  Run the code by clicking the **Go** button.

    ![](../images/go_button.png "Go button")

7.  The `hello_world` application is now running and a banner is displayed on the terminal. If it does not appear, check your terminal settings and connections.

    ![](../images/text_display_hello_world_001.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

