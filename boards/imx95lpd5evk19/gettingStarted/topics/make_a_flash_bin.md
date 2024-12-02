# Make a flash.bin 

1.  Get the boot images and the imx-mkimage source repository from corresponding Linux BSP release. The boot images required to be put into imx-mkimage/i.MX95 are:

    `- oei-m33-tcm.bin`

    `- oei-m33-ddr.bin`

    `- m33_image.bin (m33_image-mx95alt.bin/m33_image-mx95evk.bin/m33_image-mx95netc. bin)`

    `- lpddr5_dmem_qb_v202311.bin (lpddr4x_dmem_qb_v202311.bin for IMX95LP4XEVK-15)`

    `- lpddr5_dmem_v202311.bin (lpddr4x_dmem_v202311.bin for IMX95LP4XEVK-15)`

    `- lpddr5_imem_qb_v202311.bin (lpddr4x_imem_qb_v202311.bin for IMX95LP4XEVK-15)`

    `- lpddr5_imem_v202311.bin (lpddr4x_imem_v202311.bin for IMX95LP4XEVK-15)`

    `- u-boot.bin`

    `- u-boot-spl.bin`

    `- bl31.bin`

    `- tee.bin`

    `- mx95a0-ahab-container.img`

    **Note:**

    -   mx95evk for `m33_image.bin` is used for `rpmsg str echo`, `rpmsg ping pong` and `power_mode_switch_rtos`.

    -   mx95netc for `m33_image.bin` is used for `netc_share_sm`.

    -   mx95alt for `m33_image.bin` is used for almost other examples.

2.  Copy binary built by ARMGCC/IAR into imx-mkimage/i.MX95, and rename it to m7\_image.bin.
3.  make image for ram target.

    1.  Make flash.bin with imx-mkimage.

        `make SOC=iMX95 OEI=YES flash_all LPDDR_TYPE=lpddr5` \(boot A core and M7\)

        or

        `make SOC=iMX95 OEI=YES flash_lpboot_sm_m7 LPDDR_TYPE=lpddr5` \(does not boot A core, just boot M7\)

    2.  Make image for ddr target:

        `make SOC=i.MX95 OEI=YES flash_m7_ddr LPDDR_TYPE=lpddr5`

        `make SOC=iMX95 OEI=YES flash_lpboot_sm_m7 LPDDR_TYPE=lpddr5`

    **Note:** For IMX95LP4XEVK-15, LPDDR\_TYPE=lpddr4x.

4.  Burn flash.bin to MicroSD/eMMC at 32 K\(0x8000\) offset with dd or HxD or UUU and then plug the MicroSD card to the board.

    For example:

    -   Burn flash.bin to Micro SD card with dd

        `dd if=flash.bin of=/dev/sdh bs=1k seek=32 && sync`

    -   Burn flash.bin to SD/eMMC with UUU

        1.  Connect USB Type-C port to PC through the USB cable. It is used for downloading firmware of the board.
        2.  Switch to serial downloader mode; boot core is cortex-m33. `sd: uuu -b sd imx-boot-imx95-19x19-lpddr5-evk-sd.bin-flash_all new-flash.bin`
        3.  Burn flash.bin with uuu.

            `emmc: uuu -b emmc imx-boot-imx95-19x19-lpddr5-evk-sd.bin-flash_all new-flash.bin`

        **Note:**

        -   `imx-boot-imx95-19x19-lpddr5-evk-sd.bin-flash_all (imx-boot-imx95-15x15-lpddr4x-evk-sd.bin-flash_all for IMX95LP4XEVK-15 and imx-boot-imx95-19x19-verdin-sd.bin-flash_all for imx95verdinevk)`. Get it from linux bsp.
        -   `new-flash.bin`. Generate it yourself.
5.  Change the boot mode to `SW7[1:4] = 1011` for sd boot, `SW7[1:4] = 1010` for emmc boot.
6.  Power on the board .

**Parent topic:**[Run a demo application](../topics/run_a_demo_application.md)

