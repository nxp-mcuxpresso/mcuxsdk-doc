# Run an example application 

For more information on debug probe support in the MCUXpresso IDE, see [Community](https://community.nxp.com/message/630901).

To download and run the application, perform the following steps:

1.  See [Table 1](default_debug_interfaces.md#TABLE_HARDWAREPLATFORM) to determine the debug interface that comes loaded on your specific hardware platform.
    -   For boards with the CMSIS-DAP/mbed/DAPLink interface, visit [Windows serial configuration](https://developer.mbed.org/handbook/Windows-serial-configuration) and follow the instructions to install the Windows operating system serial driver. If running on Linux operating system, this step is not required.
    -   For boards with a P&E Micro interface, visit [PE micro](http://www.pemicro.com/support/downloads_find.cfm) and download and install the P&E Micro Hardware Interface Drivers package.
    -   If using J-Link either a standalone debug pod or OpenSDA, install the J-Link software \(drivers and utilities\) from [Segger](https://www.segger.com/).
2.  Connect the development platform to your PC via a USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/terminal_putty_configuration.png "Terminal (PuTTY) configurations")

4.  On the **Quickstart Panel**, click **Debug `frdmke17z512_demo_apps_hello_world [Debug]`** to launch the debug session.

    ![](../images/ide_debug_hello_world_case.JPG "Debug hello_world case")

5.  The first time you debug a project, the **Debug Emulator Selection** dialog is displayed, showing all supported probes that are attached to your computer. Select the probe through which you want to debug and click **OK**. \(For any future debug sessions, the stored probe selection is automatically used, unless the probe cannot be found.\)

    ![](../images/ide_attached_probes_debug_emulator_selection.png "Attached Probes: debug emulator selection")

6.  The application is downloaded to the target and automatically runs to `main()`.

    ![](../images/ide_stop_at_main_when_running_debugging_mcuxpresso.png "Stop at main() when running debugging")

7.  Start the application by clicking **Resume**.

    ![](../images/ide_resume_button.png "Resume button")


The `hello_world` application is now running and a banner is displayed on the terminal. If this is not the case, check your terminal settings and connections.

![](../images/text_display_hello_world.png "Text display of the hello_world demo")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

