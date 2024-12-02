# Run an example application

To download and run the application, perform these steps:

1.  Download and install LPCScrypt or the Windows® operating systems driver for LPCXpresso boards from [www.nxp.com/lpcutilities](http://www.nxp.com/lpcutilities). This installs the required drivers for the board.
2.  Connect the development platform to your PC via USB cable between the Link2 USB connector \(named Link for some boards\) and the PC USB connector. If you are connecting for the first time, allow about 30 seconds for the devices to enumerate.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see Appendix A\). Configure the terminal with these settings:
    1.  115200 baud rate \(reference BOARD\_DEBUG\_UART\_BAUDRATE variable in board.h file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        ![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configuration")

4.  In IAR, click the "Download and Debug" button to download the application to the target.

    ![](../images/download_and_debug_button.png "Download and Debug button")

5.  The application is then downloaded to the target and automatically runs to the main\(\) function.

    **Note:** The application is programmed to the external on board flash, then jumped to SRAM to run

    ![](../images/stop_at_main_running_debugging.png "Stop at main() when running debugging")

6.  Run the code by clicking the "Go" button to start the application.

    ![](../images/go_button_001.png "Go button")

7.  The hello\_world application is now running and a banner is displayed on the terminal. If this does not occur, check your terminal settings and connections.

    ![](../images/text_display_hello_world_001.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

