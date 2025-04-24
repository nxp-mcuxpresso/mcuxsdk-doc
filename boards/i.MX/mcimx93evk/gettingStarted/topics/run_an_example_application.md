# Run an example application

To download and run the application via UUU, perform these steps:

1.  Connect the development platform to your PC via USB cable between the DBG USB connector \(J1401\) and the PC. It provides console output while using UUU.
2.  Connect the J403 \(USB1\) connector and the PC. It provides the data path for UUU.
3.  Open the terminal application on the PC, such as PuTTY or TeraTerm, and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:

    1.  115200 baud rate
    2.  No parity
    3.  8 data bits
    4.  1 stop bit
    |![](../images/flash_xip_terminal_putty_configuration_8mm.png "Terminal (PuTTY) configuration")

|

4.  Get the boot images and the imx-mkimage source repository from corresponding Linux BSP release. The boot images required to be put into imx-mkimage/i.MX9 are:

    `- u-boot-imx93evk.bin-sd (rename to u-boot.bin)`

    `- u-boot-spl.bin-imx93evk-sd (rename to u-boot-spl.bin)`

    `- bl31-imx93.bin (rename to bl31.bin)`

    `- mx93a0-ahab-container.img`

    `- lpddr4_dmem_1d_v202201.bin`

    `- lpddr4_dmem_2d_v202201.bin`

    `- lpddr4_imem_1d_v202201.bin`

    `- lpddr4_imem_2d_v202201.bin`

5.  Make flash.bin with imx-mkimage.

    `make SOC=iMX9 flash_singleboot_m33 (for single boot mode)`

    or

    `make SOC=iMX9 flash_lpboot (for low power boot mode)`

6.  Type the UUU command to the flash image.

    `uuu -b emmc flash.bin (for single boot on eMMC)`

    `uuu -b sd flash.bin (for single boot on SD)`

    For low power boot, a single boot flash.bin is needed besides the target flash.bin.

    `uuu -b emmc <singleboot flash.bin> flash.bin (for lowpower boot on eMMC)`

    `uuu -b sd <singleboot flash.bin> flash.bin (for lowpower boot on SD)`

    The UUU puts the platform into fast boot mode and automatically flashes the target bootloader to emmc/sd. The command line and fast boot console is as shown in [Figure 2](run_an_example_application.md#COMMANDLINSEFASTBOOT).

    |![](../images/command_line_fast_boot_console_output_executing_uu.png "Command line and fast boot console output when
											executing UUU")

|

7.  Then, power off the board and change the boot mode to the corresponding one.
    -   For single-boot mode:
        -   when boot device is emmc, then `SW1301[3:0] = 0000`;
        -   when boot device is sd, then `SW1301[3:0] = 0010`.
    -   For low-power boot mode:
        -   when boot device is emmc, then `SW1301[3:0] = 1000`;
        -   when boot device is sd, then `SW1301[3:0] = 1010`.
8.  Power on the board again.

**Parent topic:**[Program flash.bin to SD/eMMC with UUU](../topics/run_a_flash_target_demo_by_uuu.md)

