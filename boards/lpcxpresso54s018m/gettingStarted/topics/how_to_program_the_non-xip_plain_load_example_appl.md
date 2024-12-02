# How to program the non-XIP \(plain load\) example application to external flash using J-Link

1.  Click the configure target option button and select the “Normal” reset option.

    ![](../images/select_normal_reset_option_lpc540xx.png "Select “Normal” reset option")

2.  Select the “Flash Download” option and click the “Add” button.

    ![](../images/select_flash_download_option_j-link_lpc540xx.png "Select “Flash Download” option")

3.  Select the “LPC540xx W25Q128JVFM SPIF” for the LPCXpresso54018 board , select "LPC540xx MX25L12835FM2I" for the LPC54018-IoT-Module option, and click the “Add” button.

    ![](../images/select_lpc540xx_w25q128jvfm_spif_option_j-link_lpc.png "Select “LPC540xx W25Q128JVFM SPIF” option")

    **Note:** Select "LPC540xx MX25L12835FM2I" for the LPC54018-IoT-Module.

4.  Set 0x00000000 as the start address and click the “OK” button.

    ![](../images/set_0x0000000_as_start_address_j-link_lpc540xx.png "Set 0x00000000 as the start address")

5.  Click the “LOAD” button.

    **Note:** If 'LOAD' fails, press the SW4 button on the board, then repower the board or reset the board \(get into ISP mode\). Keep pressing SW4 when clicking the 'LOAD' button again to program the application into the external flash.

    ![](../images/click_load_button_j-link_lpc540xx.png "Click the “LOAD” button.")

6.  Press the reset button on the board to run the example.

    The hello\_world application is now running and a banner is displayed on the terminal. If this is not the case, check your terminal settings and connections.

    ![](../images/text_display_hello_world.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo using Keil® MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

