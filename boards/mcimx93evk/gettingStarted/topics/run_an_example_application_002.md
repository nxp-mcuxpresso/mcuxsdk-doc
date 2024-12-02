# Run an example application

To download and run the application, perform these steps:

1.  This board supports the J-Link PLUS debug probe. Before using it, install SEGGER J-Link software, which can be downloaded from [http://www.segger.com/downloads/jlink/](http://www.segger.com/downloads/jlink/).
2.  Connect the development platform to your PC via USB cable between the DBG USB connector \(J1401\) and the PC USB connector.
3.  Connect 12 V ~ 20 V power supply and J-Link Plus to the device.
4.  Switch SW1301\[3:0\] to the M core boot and ensure that the image is not available on the boot source. For example, 0b1010 for MicroSD boot. Keep the SD slot empty.
5.  Open the terminal application on the PC, such as PuTTY or TeraTerm, connect to the debug COM port, see [How to determine COM port](how_to_determine_com_port.md#), and configure the terminal with these settings:
    1.  115,200 baud rate
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

|

6.  In IAR, click **Download and Debug** to download the application to the target.

    |![](../images/download_and_debug_button_imx8mq.png "Download and Debug button")

|

7.  The application then downloads to the target and automatically runs to the `main()` function.

    |![](../images/stop_at_main_when_running_debugging_imx8mq.png "Stop at main() when running
											debugging")

|

8.  Run the code by clicking **Go** to start the application.

    |![](../images/go_button_imx8mq.png "Go button")

|

9.  The `hello_world` application is now running and a banner is displayed on the terminal. If the application does not run or the banner is not displayed, check your terminal settings and connections.

    |![](../images/text_display_hello_world.png "Text display of the hello_world
											demo")

|

    **Note:** If the software is already running on the M core, the debugger loading image into TCM may get HardFault or a data verification issue. NXP recommends you to follow the steps above to use the debugger. Repowering the board is required to restart the debugger.


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

