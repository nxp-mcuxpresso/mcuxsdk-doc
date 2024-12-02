# Run an example application

To download and run the application, perform these steps:

1.  This board supports the `CMSIS-DAP/mbed/DAPLink` debug probe by default. Visit [MBED](https://os.mbed.com/handbook/Windows-serial-configuration) serial-configuration and follow the instructions to install the Windows® operating system serial driver. If running on Linux OS, this step is not required.
2.  Connect the development platform to your PC via USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number. To determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE`variable in the *board.h*file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/keil_terminal_putty_configuration.png "Terminal (PuTTY) configurations")

4.  To debug the application, click **load** or press the **F8** key for flexspi target which need to download the program to flash memory. Then, click the **Start/Stop Debug Session**button, highlighted in red in [Figure 2](run_an_example_application_003.md#FIG_STOPATMAIN). If using **J-Link**as the debugger, click **Project option**\>**Debug**\>**Settings**\>**Debug** \>**Port**, and select **SW**.

    **Note:** If debugging with JLINK, device selection window will be popped when you click the **Settings** button under the **Debug** tab. Users need to choose **MIMXRT1165/MIMXRT1166** device manually.

    **Note:**

    When using jlink in MDK for cm4 projects, it expects one jlinkscript file named JLinkSettings.JLinkScript in the folder where the uVision project files are located. Please refer to [Segger Wiki](https://wiki.segger.com/Keil_MDK-ARM) for more information.

    For the contents in this `JlinkSettings.JLinkScript`, use contents in `evkmimxrt1160_connect_cm4_cm4side.jlinkscript` \(non-sdram targets\) and `evkmimxrt1160_connect_cm4_cm4side_sdram.jlinkscript` \(sdram targets\).

    ![](../images/keil_stop_at_main.png "Stop at main() when run debugging")

5.  Run the code by clicking **Run** to start the application, as shown in [Figure 3](run_an_example_application_003.md#FIG_RUNBUTTON).

    ![](../images/keil_run_button.png "Run button")

    The `hello_world` application is now running and a banner is displayed on the terminal, as shown in [Figure 4](run_an_example_application_003.md#FIG_TEXTDISPLAY). If this is not true, check your terminal settings and connections.

    ![](../images/keil_text_display.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo using Keil® MDK/μVision](../topics/run_a_demo_using_keil_mdk_vision.md)

