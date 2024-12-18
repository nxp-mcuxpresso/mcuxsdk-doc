# Run an example application

Perform the following steps to download and run the application.

1.  Connect the MC56F80000-EVK USB port J12 to PC via micro USB cable. It setups the debugger multilink and USB to UART bridge.
2.  Install the multilink and USB to UART bridge driver as PC hint if it is the first time you run it on your PC. The MultiLink driver is provided by CodeWarrior by default.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md)\). Configure the terminal with these settings:

    1.  115200, defined by `BOARD_DEBUG_UART_BAUDRATE` in the *board.h* file
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    ![](../images/terminal_putty_configurations.jpg "Terminal (PuTTY) configuration")

4.  For this example, click **Debug** in the **Commander** pane, and select the **hello\_world\_flash\_sdm\_lpm\_debug\_PnE U-MultiLink** launch configuration.

    ![](../images/debug_button.jpg "Debug button")

    ![](../images/debug_configuration_selection.jpg "Debug configuration selection")

    Then the application is downloaded onto target board and automatically runs to the `main()` function.

    Click **Run** on the toolbar to run the code.

    **Note:**

    1.  Generally there are four build configurations for DSC SDK 2.12.0: `flash_sdm_lpm_debug`, `flash_sdm_lpm_release`, `flash_ldm_lpm_debug` and `flash_ldm_lpm_release`.

        `debug` uses optimization level 1 and `release` uses optimization level 4. `sdm` means small data memory model. `ldm` means large data memory model. `lpm` means large program memory model.

    2.  Check each demo `readme` document, which includes detail instructions for HW and SW settings.
    ![](../images/run_button.jpg "Run button")

5.  The `hello_world` application is now running and a banner is displayed on the terminal, as shown in [Figure 5](#FIG_TEXTDISPLAYHELLOWORLD). If it does not appear, check your terminal settings and connections.

    ![](../images/text_display_hello_world.jpg "Text display of the hello_world demo")


**Parent topic:**[Run a demo application using CodeWarrior](../topics/run_a_demo_application_using_codewarrior.md)
