# Make a flash.bin 

1.  Get the boot images and the imx-mkimage source repository from corresponding Linux BSP release. The boot images required to be put into imx-mkimage/i.MX937 are:

    `- m33-oei-ddrfw.bin`

    `- oei-m33-ddr.bin`

    `- m33_image.bin`

    `- lpddr5_dmem_qb_v202409.bin`

    `- lpddr5_dmem_v202409.bin`

    `- lpddr5_imem_qb_v202409.bin`

    `- lpddr5_imem_v202409.bin`

    `- u-boot.bin`

    `- u-boot-spl.bin`

    `- bl31.bin`

    `- tee.bin`

    `- mx937a0-ahab-container.img`

    **Note:**

    -   mx937evk for `m33_image.bin` is used for `rpmsg str echo`, `rpmsg ping pong` and `power_mode_switch_rtos`.

    -   mx937alt for `m33_image.bin` is used for almost other examples.

2.  Copy binary built by ARMGCC/IAR into imx-mkimage/iMX937, and rename it to m7\_image.bin.
3.  make image for ram target.

    1.  Make flash.bin with imx-mkimage.

        `make SOC=iMX937 OEI=YES flash_all LPDDR_TYPE=lpddr5` \(boot A core and M7\)

        or

        `make SOC=iMX937 OEI=YES flash_lpboot_sm_m7 LPDDR_TYPE=lpddr5` \(does not boot A core, just boot M7\)

4.  Burn flash.bin to MicroSD/eMMC at 32 K\(0x8000\) offset with dd or HxD or UUU and then plug the MicroSD card to the board.

    For example:

    -   Burn flash.bin to Micro SD card with dd

        `dd if=flash.bin of=/dev/sdh bs=1k seek=32 && sync`

    -   Burn flash.bin to SD/eMMC with UUU

        1.  Connect USB Type-C port to PC through the USB cable. It is used for downloading firmware of the board.
        2.  Switch to serial downloader mode; boot core is cortex-m33. `sd: uuu -b sd imx-boot-imx937-19x19-lpddr5-evk-sd.bin-flash_all new-flash.bin`
        3.  Burn flash.bin with uuu.

            `emmc: uuu -b emmc imx-boot-imx937-19x19-lpddr5-evk-sd.bin-flash_all new-flash.bin`

5.  Change the boot mode to `SW1[1:2] = 11` for sd boot, `SW1[1:2] = 10` for emmc boot.
6.  Power on the board .

**Parent topic:**[Run a demo application](../topics/run_a_demo_application.md)
