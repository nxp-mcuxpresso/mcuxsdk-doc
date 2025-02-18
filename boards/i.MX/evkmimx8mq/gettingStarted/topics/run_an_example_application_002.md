# Run an example application

This section describes steps to run a demo application using J-Link GDB Server application.

After the J-Link interface is configured and connected, follow these steps to download and run the demo applications:

1.  Connect the development platform to your PC via USB cable between the USB-UART connector and the PC USB connector. If using a standalone J-Link debug pod, also connect it to the SWD/JTAG connector of the board.
2.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see Appendix A\). Configure the terminal with these settings:
    1.  115200 baud rate
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configurations.png "Terminal (PuTTY) configurations")

|

3.  Open the J-Link GDB Server application. Assuming the J-Link software is installed, the application can be launched by going to the Windows operating system Start menu and selecting “Programs -\> SEGGER -\> J-Link <version\> J-Link GDB Server”.
4.  Modify the settings as shown below. The target device selection chosen for this example is the MIMX8MQ6\_M4.
5.  After it is connected, the screen should resemble this figure:

    |![](../images/5_2_3segger_j-link_gdb_server_configuration_imx8mq.png "SEGGER J-Link GDB server configuration")

|

    |![](../images/5_2_3_segger_j-link_gdb_server_screen_after_succes.png "SEGGER J-Link GDB server screen after successful connection")

|

6.  If not already running, open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system Start menu, go to “Programs -\> GNU Tools ARM Embedded <version\>” and select “GCC Command Prompt”.

    |![](../images/launch_command_prompt_20.jpg "Launch command prompt")

|

7.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

    *<install\_dir\>/boards/<board\_name\>/<example\_type\>/<application\_name\>/armgcc/debug*

    *<install\_dir\>/boards/<board\_name\>/<example\_type\>/<application\_name\>/armgcc/release*

    For this example, the path is:

    *<install\_dir\>/boards/evkmimx8mq/demo\_apps/hello\_world/armgcc/debug*

8.  Run the command “arm-none-eabi-gdb.exe <application\_name\>.elf”. For this example, it is “arm-none-eabi-gdb.exe hello\_world.elf”.

    |![](../images/5_2_3_run_arm_none_eabi_gdb_imx8mq.png "Run arm-none-eabi-gdb")

|

9.  Run these commands:
    1.  "target remote localhost:2331"
    2.  "monitor reset"
    3.  "monitor halt"
    4.  "load"
10. The application is now downloaded and halted at the reset vector. Execute the “monitor go” command to start the demo application.

    The hello\_world application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/text_display_hello_world_demo.png "Text display of the hello_world demo")

|


**Parent topic:**[Windows OS host](../topics/windows_os_host.md)

