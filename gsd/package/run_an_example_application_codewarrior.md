# Run an example application

To download and run the application, perform the following steps:

1.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(see [How to determine COM port](/gsd/package/how_to_determine_com_port.md)\). Configure the terminal with these settings:

    - 115200, defined by `BOARD_DEBUG_UART_BAUDRATE` in the *board.h* file
    - No parity
    - 8 data bits
    - 1 stop bit
    ![](/gsd/package/images/terminal_putty_configurations.jpg "Terminal (PuTTY) configuration")

2.  For this example(TWR-MC56F8400 hello_world), click **Debug** in the **Commander** pane, and select the `hello_world_flash_sdm_lpm_debug_OSJTAG` launch configuration.
    Then the application is downloaded onto target board and automatically runs to the `main()` function.
    ![](/gsd/package/images/codewarrior_debug_button.jpg "Debug button")
    ![](/gsd/package/images/codewarrior_debug_configuration_selection.png "Debug configuration selection")

    **Note:**
    - Generally there are four build configurations for DSC SDK examples: `flash_sdm_lpm_debug`, `flash_sdm_lpm_release`, `flash_ldm_lpm_debug`, and `flash_ldm_lpm_release`.
      * `*_debug`: uses optimization level 1
      * `*_release`: uses optimization level 4
      * `sdm`: small data memory model
      * `ldm`: large data memory model
      * `lpm`: large program memory model
    - Select corresponding launch configuration based on build target and debugger type.
    - Some examples may require specific hardware settings, check each demo `readme` document, which includes detail instructions for HW and SW settings.

3.  To run the code, click **Run** on the toolbar.
    ![](/gsd/package/images/codewarrior_run_button.jpg "Run button")

4.  The `hello_world` application is now running and a banner is displayed on the terminal.
    ![](/gsd/package/images/text_display_hello_world.png "Text display of the hello_world demo")
