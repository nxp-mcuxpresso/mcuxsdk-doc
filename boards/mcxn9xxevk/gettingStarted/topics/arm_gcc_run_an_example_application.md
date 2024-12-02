# Run an example application 
This section describes steps to run a demo application using J-Link GDB Server application.

To complete the set-up check if your board supports OpenSDA, see [Default debug interfaces](default_debug_interfaces.md).

-   If your board supports OpenSDA:

    -   The OpenSDA interface on your board is pre-programmed with the J-Link OpenSDA firmware.
    -   For instructions on reprogramming the OpenSDA interface.
-   If your board does not support OpenSDA:

    -   A standalone J-Link pod is required which should be connected to the debug interface of your board.

        **Note:** Some hardware platforms require hardware modification in order to function correctly with an external debug interface.

        **Note:** J-Link GDB Server application is not supported for TFM examples. Use CMSIS DAP instead of J-Link for flashing and debugging TFM examples.

    -   After the J-Link interface is configured and connected, follow these steps to download and run the demo applications:

        1.  Connect the development platform to your PC via USB cable between the LPC-Link2 USB connector \(may be named OSJTAG for some boards\) and the PC USB connector. If using a standalone J-Link debug pod, connect it to the SWD/JTAG connector of the board.
        2.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug serial port number \(to determine the COM port number, see [How to determine com port](how_to_determine_com_port.md).
        3.  Configure the terminal with these settings:

            a. 115200 or 9600 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in `board.h` file\)

            b. No parity

            c. 8 data bits

            d. 1 stop bit

            ![](../images/arm_gcc_run_example_terminal_putty_configuration.png "Terminal (PuTTY) configurations")

            **Note:** Make sure the board is set to FlexSPI flash boot mode \(ISP2: ISP1: ISP0 = ON, OFF, ON\) before use GDB debug.

        4.  Open the J-Link GDB Server application. Assuming the J-Link software is installed, the application can be launched by going to the Windows operating system Start menu and selecting **Programs** -\> **SEGGER** -\> **J-Link <version\> J-Link GDB Server**.
        5.  Modify the settings as shown below. The target device selection chosen for this example is **MCXN947\_cm33\_core0**.
        6.  After it is connected, the screen should look like [Figure 2](#SEGGER).

            ![](../images/arm_gcc_run_example_segger_jlink_success.png "SEGGER J-Link GDB Server screen after successful
                                                    connection")

        7.  If not already running, open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system Start menu, go to **Programs** -\> **GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

            ![](../images/arm_gcc_run_example_launch_command_prompt.png "Launch command prompt")

        8.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

            ```
            <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/debug
            ```

            ```
            <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/release
            ```

            For this example, the path is:

            ```
            <install_dir>/boards/mcxn9xxevk/demo_apps/hello_world/cm4/armgcc/debug
            ```

        9.  Run the `arm-none-eabi-gdb.exe <application_name>.elf` command. For this example, it is `arm-none-eabi-gdb.exe hello_world.elf`.

            ![](../images/arm_gcc_run_example_run_arm_none.png "Run arm-none-eabi-gdb")

        10. Run these commands:

            a. `target remote localhost:2331`

            b. `monitor reset`

            c. `monitor halt`

            d. `load`

            e. `monitor reset`

        11. The application is now downloaded and halted at the watch point. Execute the `monitor go` command to start the demo application.

            The `hello_world` application is now running and a banner is displayed on the terminal. If this does not appear, check your terminal settings and connections.

            ![](../images/iar_run_example_text_display_hello_world.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo using Arm GCC](../topics/arm_gcc_run_a_demo_application.md)

