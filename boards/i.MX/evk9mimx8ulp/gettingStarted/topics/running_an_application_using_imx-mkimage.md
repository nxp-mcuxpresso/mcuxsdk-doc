# Run an application using imx-mkimage

This section describes the steps to write a bootable SDK image to the eMMC/FlexSPI NOR flash for the i.MX processor.

**Note:** Attach core to debug code with J-Link probe.

The following steps describe how to write container image \(flash.bin\):

1.  Connect the DEBUG UART slot on the board to your PC through the USB cable. The Windows OS installs the USB driver automatically and the Ubuntu OS finds the serial devices as well.
2.  On Windows OS, open the device manager, find **USB serial Port** in **Ports \(COM and LPT\)**. Assume that the ports are COM9 and COM10. One port is for the debug message from the Cortex-A35 and the other is for the Cortex-M33. The port number is allocated randomly, so opening both is beneficial for development. On Ubuntu OS, find the TTY device with name `/dev/ttyUSB*` to determine your debug port. Similar to Windows OS, opening both is beneficial for development.

    |![](../images/determine_com_port_target_board.png "Determining the COM port of target
												board")

|

3.  Generate m33 firmware:

    -   **For RAM target**:

        ```
        $ ./build_debug.sh 
        ```

        or

        ```
        $ ./build_release.sh
        ```

    -   **For FLASH target\(XIP\)**:

        ```
        $ ./build_flash_debug.sh 
        ```

        or

        ```
        $ ./build_flash_release.sh
        ```

4.  Get `imx-mkimage`, `s400 firmware(mx8ulpa2-ahab-container.img)`, `OPTEE(tee.bin)`, `upower firmware(upower.bin)`, `uboot-spl(u-boot-spl.bin)`, `uboot(u-boot.bin)`, and `TF-A(bl31.bin)` from the Linux release package.
    1.  Clone the `imx-mkimage` from NXP public git.

        ```
        $ git clone https://github.com/nxp-imx/imx-mkimage
        ```

    2.  Check out the correct branch. The branch name is named after Linux release version which is compatible with the SDK. You can get the version information from corresponding Linux Release Notes document.

        ```
        $ cd imx-mkimage
        $ git checkout [branch name]
        ```

    3.  Get `s400 firmware(mx8ulpa2-ahab-container.img)`.

        ```
        $ cp mx8ulpa2-ahab-container.img iMX8ULP/
        ```

    4.  Get `upower firmware(upower.bin)`.

        ```
        $ cp upower.bin iMX8ULP/
        ```

    5.  Get `u-boot-spl.bin and u-boot.bin`.
        -   For EVK-MIMX8ULP:

            ```
            $ cp u-boot-spl.bin-imx8ulpevk-sd iMX8ULP/u-boot-spl.bin
            $ cp u-boot-imx8ulpevk.bin-sd iMX8ULP/u-boot.bin
            ```

        -   For EVK9-MIMX8ULP:

            ```
            $ cp u-boot-spl.bin-imx8ulp-9x9-lpddr4-evk-sd iMX8ULP/u-boot-spl.bin
            $ cp u-boot-imx8ulp-9x9-lpddr4-evk.bin-sd iMX8ULP/u-boot.bin
            ```

    6.  Get `bl31.bin`.

        ```
        $ cp bl31-imx8ulp.bin-optee iMX8ULP/bl31.bin
        ```

5.  Generate container image table with `imx-mkimage`:

    |boot type|A35|M33|SW5\[8:1\]|
    |---------|---|---|----------|
    |Single Boot|make SOC=iMX8ULP flash\_singleboot For RAM target:

make SOC=iMX8ULP flash\_singleboot\_m33 **Note:** Does not support pack Flash target into flash.bin when boot type is single boot type.

|1000\_xx00 Single Boot-eMMC|
    | |make SOC=iMX8ULP flash\_singleboot\_flexspiFor RAM target:

make SOC=iMX8ULP flash\_singleboot\_m33\_flexspi **Note:** Does not support pack Flash target into flash.bin when boot type is single boot type.

|1010\_xx00 Single Boot-Nor|
    |Dual Boot|make SOC=iMX8ULP flash\_dualboot|For RAM target: make SOC=iMX8ULP flash\_dualboot\_m33

For Flash target: make SOC=iMX8ULP flash\_dualboot\_m33\_xip

|1000\_0010 A35-eMMC/M33-Nor|
    | |make SOC=iMX8ULP flash\_dualboot\_flexspi|1010\_0010 A35-Nor/M33-Nor|
    |Low Power Boot|make SOC=iMX8ULP flash\_dualboot|1000\_00x1 A35-eMMC/M33-Nor|
    | |make SOC=iMX8ULP flash\_dualboot\_flexspi|1010\_00x1 A35-Nor/M33-Nor|

    **Note:**

    -   For details, see `imx-mkimage/iMX8ULP/README`.
    -   Does not support pack Flash target firmware to flash.bin when boot type is single boot type.

    -   RAM target: debug/release.

    -   Flash target: `flash_debug/flash_release`.

    -   Need generate two flash.bin and download to emmc/flexspi2 nor flash of a35 and flexspi0 nor flash of m33, one for A35, another one for M33 when boot type is dual boot type or low power boot type.

6.  Build the application \(for example, `hello_world`\), get binary image `sdk20-app.bin`, copy to `imx-mkimage` project folder `iMX8ULP/` and rename to `m33_image.bin`.

    ```
    cp sdk20-app.bin <imx-mkimage path>/iMX8ULP/m33_image.bin
    ```

7.  Under `imx-mkimage` project folder, execute the following command to generate m33 container image.
    1.  When boot type is dual boot/low power boot type:

        **For RAM \(TCM\) target:**

        ```
        make SOC=iMX8ULP flash_dualboot_m33 (write flash.bin to flexspi0 nor flash of m33; 
        ```

        **For Flash target:**

        ```
        make SOC=iMX8ULP flash_dualboot_m33_xip (write flash.bin to flexspi0 nor flash of m33); 
        ```

    2.  When boot type is single boot type:

        ```
        for RAM (TCM) target and sw5[8:1] = 1000_xx00 Single Boot-eMMC:
        make SOC=iMX8ULP flash_singleboot_m33 (write flash.bin to emmc); 
        ```

        ```
        for RAM (TCM) target and sw5[8:1] = 1010_xx00 Single Boot-Nor:
        make SOC=iMX8ULP flash_singleboot_m33_flexspi (write flash.bin to flexspi2 nor flash of
        a35);
        ```

8.  Copy the `flash.bin` image to your tftpboot server.
9.  Write `flash.bin to flexspi0 nor flash`. There are two ways:
    1.  Write `flash.bin to flexspi0 nor flash with uboot`.
        1.  Switch to single boot type \(`sw[8:1]=1000 0000`\) and boot the board, assuming your board can boot to U-Boot.
        2.  At the U-Boot console, execute following commands to download image \(from network\) and flash to FlexSPI0 NOR flash.

            ```
            setenv serverip <tftpboot server ip>
            dhcp
            tftpboot 0xa0000000 flash.bin
            setenv erase_unit 1000
            setexpr erase_size ${filesize} + ${erase_unit}
            setexpr erase_size ${erase_size} / ${erase_unit}
            setexpr erase_size ${erase_size} * ${erase_unit}
            sf probe 0:0
            sf erase ${erase_size}
            sf write  0xa0000000 0 ${filesize}
            ```

    2.  Write `flash.bin to flexspi0 nor flash with JLink`:

        ```
        J-Link>connect
        Device>
        TIF>s (Choose target interface as SWD, unless failed to do anything)
        Speed>
        J-Link>r
        J-Link>h
        J-Link>loadbin flash.bin 0x4000000
        ```

10. Write `flash.bin to emmc with uuu` \(only for the RAM target\):
    1.  Start `uuu`.

        ```
        uuu -b emmc workable-flash.bin flash.bin (workable-flash.bin: uboot and m33 image are workable)
        ```

    2.  Enter serial download mode.
        1.  Change SW5\[8:1\] to 01xx\_xxxx Serial Downloader.
        2.  Enter serial download mode with uboot.

            ```
            => fastboot 0
            ```

11. Open another terminal application on the PC, such as PuTTY and connect to the debug COM port \(to determine the COM port number, see [How to determine COM port](how_to_determine_com_port.md#)\). Configure the terminal with these settings:
    -   115200
    -   No parity
    -   8 data bits
    -   1 stop bit
12. Power off and switch to low-power boot mode \(`sw5[8:1]=1000 0001`\), then repower the board.
13. The `hello_world` application is now executed and a banner is displayed at the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/hello_world_demo_running_on_cortex_m4_core.png "Hello world demo running on Cortex-M33
												core")

|


