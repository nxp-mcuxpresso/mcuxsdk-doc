# Run an example application

This section describes steps to run a demo application using J-Link GDB Server application. To perform this exercise, make sure that a standalone J-Link pod is connected to the debug interface of your board.

After the J-Link interface is configured and connected, follow these steps to download and run the demo applications:

1.  This board supports the J-Link debug probe. Before using it, install SEGGER software, which can be downloaded from [SEGGER](http://www.segger.com/).
2.  Connect the development platform to your PC via USB cable between the OpenSDA USB connector and the PC USB connector.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE`variable in the *board.h* file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/armgcc_terminal_putty_configuration.jpg "Terminal (PuTTY) configurations")

4.  Open the J-Link GDB Server application. Go to the SEGGER install folder. For example, *C:\\Program Files\(x86\)\\SEGGER\\JLink\_Vxxx*. Open the command windows. To debug CM33, run the following command:

    ```
    JLinkGDBServer.exe -device MIMXRT1186_M33 -if SWD -speed 4000 -jlinkscriptfile <frdmimxrt1186_cm33.jlinkscript> -stayontop -ir
    ```

    To debug CM7, run the following command:

    ```
    JLinkGDBServer.exe -device MIMXRT1186_M33 -if SWD -speed 4000 -jlinkscriptfile <frdmimxrt1186_cm7.jlinkscript> -stayontop -ir
    ```

    **Note:** The supporting `jlinkscript` file can be found in */boards/frdmimxrt1186/demo_apps/hello\_world/cm33*.

5.  After it is connected, the screen should resemble [Figure 2](#FIG_SEGGERJLINK).

    ![](../images/armgcc_segger_jlink_gdb_server_screen.png "SEGGER J-Link GDB Server screen after successful connection")

6.  If not already running, open a GCC ARM Embedded tool chain command window. To launch the window, from the Windows operating system **Start menu**, go to **Programs**\> **GNU Tools ARM Embedded <version\>**and select **GCC Command Prompt**.

    ![](../images/armgcc_launch_command_prompt.png "Launch command prompt")

7.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

    *<install\_dir\>/boards/<board\_name\>/<example\_type\>/<application\_name\>/<core\>/armgcc/<target\>*

    For this example, the path is:

    *<install\_dir\>/boards/frdmimxrt1186/demo\_apps/hello\_world/<core\>/armgcc/debug*

8.  Run the `arm-none-eabi-gdb.exe <application_name>.elf`. For this example, it is `arm-none-eabi-gdb.exe hello_world.elf`.

    ![](../images/armgcc_run_arm-none-eabi-gdb.png "Run arm-none-eabi-gdb")

9.  Run these commands:

    ```
    target remote localhost:2331
    monitor reset
    monitor halt
    load
    ```

10. The application is now downloaded and halted at the reset vector. Execute the `continue` or `monitor go` command to start the demo application.

    The `hello_world`application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    ![](../images/armgcc_text_display.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm_gcc.md)

