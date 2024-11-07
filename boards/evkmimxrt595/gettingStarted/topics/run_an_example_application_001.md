# Run an example application

This section describes steps to run a demo application using J-Link GDB Server application. To perform this exercise, make sure that either:

-   The OpenSDA interface on your board is programmed with the J-Link OpenSDA firmware. To determine if your board supports OpenSDA, see [Default debug interfaces](default_debug_interfaces.md#). For instructions on reprogramming the OpenSDA interface, see [Updating debugger firmware](updating_debugger_firmware.md#). If your board does not support OpenSDA, a standalone J-Link pod is required.
-   You have a standalone J-Link pod that is connected to the debug interface of your board. Note that some hardware platforms require hardware modification in order to function correctly with an external debug interface.

After the J-Link interface is configured and connected, follow these steps to download and run the demo applications:

1.  Connect the development platform to your PC via USB cable between the OpenSDA USB connector and the PC USB connector. If using a standalone J-Link debug pod, also connect it to the SWD/JTAG connector of the board.
2.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:
    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configurations.png "Terminal (PuTTY) configurations")

|

3.  Open the J-Link GDB Server application. Assuming the J-Link software is installed, the application can be launched by going to the Windows operating system **Start** menu and selecting **Programs**-\>**SEGGER**-\>**J-Link <version\> J-Link GDB Server**.
4.  Modify the settings as shown in [Figure 2](run_an_example_application_001.md#FIG_SEGGERJLINKGDBSERVER). The target device selection chosen for this example is **MIMXRT595\_M33**.

    |![](../images/fig38.png "SEGGER J-Link GDB Server configuration")

|

5.  After it is connected, the screen should be as shown in [Figure 3](run_an_example_application_001.md#FIG_SEGGERJLINKGDBSERVERSCREEN).

    |![](../images/fig39.png "SEGGER J-Link GDB Server screen after successful
											connection")

|

6.  If not already running, open a GCC Arm Embedded tool chain command window. To launch the window, from the **Start** menu of the Windows operating system, go to **Programs**-\>**GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

    |![](../images/launch_command_prompt_20.jpg "Launch command prompt")

|

7.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

    *<install\_dir\>/boards/<board\_name\>/<example\_type\>/<application\_name\>/armgcc/debug*

    *<install\_dir\>/boards/<board\_name\>/<example\_type\>/<application\_name\>/armgcc/release*

    For this example, the path is: *<install\_dir\>/boards/evkmimxrt595/demo\_apps/hello\_world/armgcc/debug*

8.  Run the `arm-none-eabi-gdb.exe <application_name>.elf` command. For this example, it is `arm-none-eabi-gdb.exe hello_world.elf`.

    |![](../images/fig41.png "Run arm-none-eabi-gdb")

|

    **Note:** Make sure that the board is set to FlexSPI flash boot mode before debugging.

9.  Run these commands:
    1.  `target remote localhost:2331`
    2.  `monitor reset`
    3.  `monitor halt`
    4.  `load`
    5.  `monitor reset`
10. The application is now downloaded and halted. Execute the `c` command to start the demo application.

    The `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/text_display_hello_world_demo.png "Text display of the hello_world
											demo")

|


**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm__gcc.md)

