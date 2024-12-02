# Run an XIP example application

1.  Use the J-FLASH-Lite \(with version higher than V6.22\) to erase the chip.

    ![](../images/erase_external_flash_jflashlite_lpc54018.png "Erase the external flash")

2.  Wait for the flash erase finish.

    ![](../images/erase_in_progress_jlinkflash_lpc54018.png "Erase in progress")

    **Note:** If you cannot erase, press the SW4 button then press the reset button to enter ISP mode. Then, click erase again \(keep pressing the SW4 button all the time\).

3.  Program the binary file into external flash.

    ![](../images/binary_built_armgcc_qspi_lpc54018.png "Binary built by armgcc")

    ![](../images/program_binary_external_flash_jflashlite_lpc54018.png "Program the binary to external flash")

    **Note:** Make sure the ‘.bin/Erase Start’ address is 0x10000000 \(the external flash base address\).

4.  After programming, press the reset button to run.

    ![](../images/hello_world_qspi_lpc54018.png "Text display of the hello_world_qspi_xip demo")


**Parent topic:**[Run a demo using Arm® GCC](../topics/run_a_demo_using_arm__gcc.md)

