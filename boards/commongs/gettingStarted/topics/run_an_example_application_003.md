# Run an example application

This section describes steps to run a demo application using J-Link GDB Server application. To update the onboard LPC-Link2 debugger to Jlink firmware, see [Updating debugger firmware](updating_debugger_firmware.md).

**Note:** J-Link GDB Server application is not supported for TFM examples. Use CMSIS DAP instead of J-Link for flashing and debugging TFM examples.

After the J-Link interface is configured and connected, follow these steps to download and run the demo applications:

1.  Connect the development platform to your PC via USB cable between the LPC-Link2 USB connector \(may be named OSJTAG for some boards\) and the PC USB connector. If using a standalone J-Link debug pod, connect it to the SWD/JTAG connector of the board.
2.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configurations.png "Terminal (PuTTY) configurations")

|

    **Note:** Make sure that the board is set to FlexSPI flash boot mode \(ISP2: ISP1: ISP0 = ON, OFF, ON\) before use GDB debug.

3.  To launch the application, open the Windows **Start** menu and select **Programs** \> **SEGGER** \> **J-Link <version\> J-Link GDB Server**.

    **Note:** It is assumed that the J-Link software is already installed.

    The **SEGGER J-Link GDB Server Config** settings dialog appears.

4.  Make sure to check the following options.
    1.  **Target interface**: The debug connection on board uses internal SWD signaling. In case of a wrong setting J-Link is unable to communicate with device under test.
    2.  **Script file**: If required, a J-Link init script file can be used for board initialization. The file with the “`.jlinkscript`” file extension is located in the `<install_dir>/boards/<board_name>/` directory.
    3.  Under the **Server settings**, check the GDB port for connection with the gdb target remote command. For more information, see step [9](#commandsgdb).
    4.  There is a command line version of J-Link GDB server “`JLinkGDBServerCL.exe`”. Typical path is `C:\Program Files\SEGGER\JLink\`. To start the J-Link GDB server with the same settings as are selected in the UI, you can use these command line options.

        ![](../images/run_an_example_UI.png "SEGGER  J-Link GDB server configuration settings")

5.  After it is connected, the screen should look like this figure:

    |![](../images/segger_jlink_gdb_server_screen_successful_connecti.png "SEGGER J-Link GDB Server screen after successful
											connection")

|

6.  If not already running, open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system Start menu, go to **Programs** - **GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

    |![](../images/launch_command_prompt_20.jpg "Launch command prompt")

|

7.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/debug
    ```

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/release
    ```

    For this example, the path is:

    ```
    <install_dir>/boards/frdmk32l3a6/demo_apps/hello_world/cm4/armgcc/debug
    ```

8.  Run the `arm-none-eabi-gdb.exe <application_name>.elf` command. For this example, it is `arm-none-eabi-gdb.exe hello_world.elf`.

    |![](../images/run_arm_none_eabi_gdb_20.png "Run arm-none-eabi-gdb")

|

9.  Run these commands:
    1.  `target remote localhost:2331`
    2.  `monitor reset`
    3.  `monitor halt`
    4.  `load`
    5.  `monitor reset`
10. The application is now downloaded and halted at the watchpoint. Execute the `monitor go` command to start the demo application.

    The `hello_world` application is now running and a banner is displayed on the terminal. If this does not appear, check your terminal settings and connections.

    |![](../images/text_display_hello_world_demo.png "Text display of the hello_world demo")

|


**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm__gcc.md)

