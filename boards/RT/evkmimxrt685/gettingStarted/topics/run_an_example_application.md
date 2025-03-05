# Run an example application

For more information on debug probe support in the MCUXpresso IDE, see [community.nxp.com](https://community.nxp.com/message/630901).

To download and run the application, perform the following steps:

1.  See the table in [Default debug interfaces](default_debug_interfaces.md) to determine the debug interface that comes loaded on your specific hardware platform.
    -   For boards with CMSIS-DAP/mbed/DAPLink interfaces, visit [developer.mbed.org/handbook/Windows-serial-configuration](http://developer.mbed.org/handbook/Windows-serial-configuration) and follow the instructions to install the Windows operating system serial driver. If running on Linux OS, this step is not required.
    -   For boards with a P&E Micro interface, see [PE micro](http://www.pemicro.com/support/downloads_find.cfm) to download and install the P&E Micro Hardware Interface Drivers package.
2.  Connect the development platform to your PC via a USB cable.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    |![](../images/terminal_putty_configurations.png "Terminal (PuTTY) configurations")

|

4.  On the **Quickstart Panel**, click **Debug `evkmimxrt685_hello_world [Debug]`** to launch the debug session.

    |![](../images/debug_hello_world_case_mimxrt600.jpg "Debug hello_world case")

|

5.  The first time you debug a project, the **Debug Emulator Selection** dialog is displayed, showing all supported probes that are attached to your computer. Select the probe through which you want to debug and click **OK**. \(For any future debug sessions, the stored probe selection is automatically used, unless the probe cannot be found.\)

    |![](../images/attached_probes_debug_emulator_selection_mimxrt600.jpg "Attached Probes: debug emulator selection")

|

    **Note:** If the debug probe is CMSIS-DAP and the debugging application is running in flash, make sure that the board is set to FlexSPI flash boot mode \(ISP2: ISP1: ISP0 = ON, OFF, ON\). Otherwise, you should not set to FlexSPI boot mode when debugging the application. If the debug probe is J-Link, **Reset before running** must be disabled. Double click the `<example> J-Link Debug.launch` file, and deselect this option under **JLink Debugger -\>Additional Options** menu.

    |![](../images/figure12_rt600.png "Disabling Reset before running")

|

6.  The application is downloaded to the target and automatically runs to `main()`.

    |![](../images/stop_at_main_when_running_debugging_mcuxpresso_ide.jpg "Stop at main() when running
											debugging")

|

7.  Start the application by clicking **Resume**.

    |![](../images/resume_button.png "Resume button")

|


The `hello_world` application is now running and a banner is displayed on the terminal. If not, check your terminal settings and connections.

|![](../images/hello_world_demo.png "Text display of the hello_world demo")

|

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

