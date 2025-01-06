# Run an example application

To download and run the application, perform these steps:

1.  Reference the table in [Default debug interfaces](default_debug_interfaces.md) to determine the debug interface that comes loaded on your specific hardware platform.
2.  Connect the development platform to your PC via USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    |![](../images/terminal_putty_configuration_001.png "Terminal (PuTTY) configurations")

|

4.  To debug the application, click **load** \(or press the F8 key\). Then, click the **Start/Stop Debug Session** button.

    |![](../images/49_rt600.png "Stop at main() when run
											debugging")

|

5.  Run the code by clicking **Run** to start the application.

    |![](../images/50_rt600.png "Run button")

|

    The `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/hello_world_lowercase.png "Text display of the hello_world
											demo")

|


**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

