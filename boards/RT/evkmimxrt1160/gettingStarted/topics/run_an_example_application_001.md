# Run an example application

To download and run the application, perform these steps:

1.  This board supports the CMSIS-DAP/mbed/DAPLink debug probe by default. Visit [MBED](https://os.mbed.com/handbook/Windows-serial-configuration) and follow the instructions to install the Windows® operating system serial driver. If running on Linux OS, this step is not required.
2.  Connect the development platform to your PC via USB cable. Connect the USB cable to J11 and make sure SW1\[1:4\] is **0010b**.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE`variable in the *board.h*file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/iar_terminal_putty_configuration.png "Terminal (PuTTY) configuration")

4.  In IAR, click the **Download and Debug** button to download the application to the target.

    ![](../images/iar_download_and_debug_button.png "Download and Debug button")

    -   When using CMSIS-DAP to debug cm4 project on IAR, an extra option needs to be specified in debugger settings. Check and fill in **--macro\_param enable\_core=1** in **Debugger** -\> **Extra Options** -\> **Command line options**, as shown in [Figure 3](run_an_example_application_001.md#FIG_COMMANDLINE).

        ![](../images/iar_options_for_node.png "Selecting Command line options")

    -   If debugging with JLINK as probe, `jlinkscript` file is needed.

        -   When downloading the `cm7` project, check **Use command line options**, as shown in [Figure 4](run_an_example_application_001.md#FIG_CHECK).

            ![](../images/iar_check_use_command_line_options.png "Check Use command line options")

        -   When downloading the `cm4` project, uncheck **Use flash loader\(s\)**, as shown in [Figure 5](run_an_example_application_001.md#FIG_UNCHECK), and change the contents of command line options as below:

            -   Target with SDRAM

                ```
                --jlink_script_file=$PROJ_DIR$/../evkmimxrt1160_connect_cm4_cm4side_sdram.jlinkscript
                ```

            -   Other target

                ```
                --jlink_script_file=$PROJ_DIR$/../evkmimxrt1160_connect_cm4_cm4side.jlinkscript
                ```

            ![](../images/iar_uncheck_use_flash_loaders.png "Uncheck Use flash loader(s)")

5.  The application is then downloaded to the target and automatically runs to the `main()` function.

    ![](../images/iar_stop_at_main.png "Stop at main() when running debugging")

6.  Run the code by clicking the **Go** button to start the application.

    ![](../images/iar_go_button.png "Go button")

7.  The `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    ![](../images/iar_text_display_of_hello_world.png "Text display of the hello_world demo")


**Note:** There are some limitations on MCUXpresso IDE debugging. For details, see **Section 8.6 IAR debug limitation** in *MCUXpresso SDK Release Notes for MIMXRT1160-EVK* \(document MCUXSDKMIMXRT116XRN\).

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

