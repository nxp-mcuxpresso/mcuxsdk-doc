# Run an example application

To download and run the application, perform these steps:

1.  This board supports the J-Link PLUS debug probe. Before using it, install SEGGER J-Link software, which can be downloaded from [http://www.segger.com/downloads/jlink/](http://www.segger.com/downloads/jlink/).
2.  Connect the development platform to your PC via USB cable between the USB-UART MICRO USB connector and the PC USB connector, then connect 12 V power supply and J-Link Plus to the device.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:
    1.  115200 baud rate
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

|

4.  In IAR, click **Download and Debug** to download the application to the target.

    |![](../images/download_and_debug_button_imx8mq.png "Download and Debug button")

|

5.  The application then downloads to the target and automatically runs to the `main()` function.

    |![](../images/stop_at_main_when_running_debugging_imx8mq.png "Stop at main() when running debugging")

|

6.  Run the code by clicking **Go** to start the application.

    |![](../images/go_button_imx8mq.png "Go button")

|

7.  The `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/text_display_hello_world.png "Text display of the hello_world demo")

|

    **Note:** For downloading the DDR target application, insert one TF card with U-Boot code. This requires both on IAR and GCC.


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

