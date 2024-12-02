# Run an example application

To download and run the application via UUU, perform these steps:

1.  Connect the development platform to your PC via USB cable between the J23 USB DEBUG connector and the PC. It provides console output while using UUU.
2.  Connect the J6 USB Type-C connector and the PC. It provides the data path for UUU.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:

    1.  115200 baud rate
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    |![](../images/flash_xip_terminal_putty_configuration_8mm.bmp "Terminal (PuTTY) configuration")

|

4.  Get the fspi version U-Boot image named **imx-boot-imx8mpevk-fspi.bin-flash\_evk\_flexspi** from the linux release package.
5.  In the command line, execute uuu to get script for qspi: `uuu -bshow qspi > qspi_auto.sh`.
    
	Then edit qspi_auto.sh, repleace this line:

   	`FB: ucmd if qspihdr dump ${fastboot_buffer}; then setenv qspihdr_exist yes; else setenv qspihdr_exist no; fi;` 

    with the below line:

   	`FB: ucmd setenv qspihdr_exist no`
	|![](../images/qspi_auto_modification.png "Modify qspi_auto script")
6. rename file imx-boot-imx8mpevk-fspi.bin-flash_evk_flexspi with `_flexspi.bin`,

   rename hello_world.bin with `_image`

7. In the command line, execute uuu with the qspi_auto.sh:

   `uuu qspi_auto.sh`

    The UUU puts the platform into fast boot mode and automatically flashes the target bin to QSPI. The command line and fast boot console is as shown 
	(run_an_example_application.md#COMMANDLINSEFASTBOOT).

    |![](../images/command_line_fast_boot_console_output_executing_uu.png "Command line and fast boot console output when
											executing UUU")

|

8. Then, power off the board and change the boot mode to eMMC/SDHC3 [SW0010[1-4]], and power on the board again.

9.  Use following command in U-Boot to kickoff m7:

    ```
    sf probe
    sf read ${loadaddr} 0 4
    bootaux 0x8000000
    ```


**Parent topic:**[Run a flash target demo by UUU](../topics/run_a_flash_target_demo_by_uuu.md)

