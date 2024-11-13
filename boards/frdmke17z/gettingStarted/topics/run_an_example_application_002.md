# Run an example application

To download and run the application, perform these steps:

1.  See the table in [Default debug interfaces](default_debug_interfaces.md) to determine the debug interface that comes loaded on your specific hardware platform.
2.  Connect the development platform to your PC via USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

4.  In IAR, click the **Download and Debug** button to download the application to the target.

    ![](../images/download_and_debug_button.png "Download and Debug button")

5.  The application is then downloaded to the target and automatically runs to the `main()` function.

6.  Run the code by clicking the **Go** button.

    ![](../images/go_button_001.png "Go button")

7.  The `hello_world` application is now running and a banner is displayed on the terminal. If it does not appear, check your terminal settings and connections.

    ![](../images/text_display_hello_world_001.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

