# Running an application from QSPI flash

This section describes the steps to write a bootable SDK image to QSPI flash with the prebuilt U-Boot image for the i.MX processor. The following steps describe how to use the U-Boot:

1.  Connect the “DEBUG UART” slot on the board to your PC through the USB cable. The Windows OS installs the USB driver automatically, and the Ubuntu OS finds the serial devices as well.
2.  On Windows OS, open the device manager, find “USB serial Port” in “Ports \(COM and LPT\)”. Assume that the ports are COM9 and COM10. One port is for the debug message from the Cortex-A7 and the other is for the Cortex-M4. The port number is allocated randomly, so opening both is beneficial for development. On Ubuntu OS, find the TTY device with name /dev/ttyUSB\* to determine your debug port. Similar to Windows OS, opening both is beneficial for development.

    |![](../images/determine_com_port_target_board.png "Determining the COM port of target
												board")

|

3.  Build the application \(for example, hello\_world\) and copy the built binary \(sdk20-app.bin file\) to the *<install\_dir\>/tools/imgutil/evkmcimx7ulp* folder.
4.  In the *<install\_dir\>/tools/imgutil/evkmcimx7ulp*p folder, run mkimg.sh in mingw32 shell to get bootable image file sdk20- app.img.
    -   If the image is built with RAM link file, use "mkimg.sh ram" to create the bootable image.
    -   If the image is built with flash link file, use "mkimg.sh flash" to create the bootable XIP.
5.  Prepare an SD card with the prebuilt U-Boot image and copy the sdk20-app.img generated into the SD card \(as shown in Step 4\). Then, insert the SD card to the target board. Make sure to use the default boot SD slot and check the DIP switch configuration.
6.  Open your preferred serial terminals for the serial devices, setting the speed to 115200 bit/s, 8 data bits, 1 stop bit \(115200, 8N1\), no parity, then power on the board.
7.  Power on the board and hit any key to stop autoboot in the terminals, then enter to U-Boot command-line mode. You can then write the image and run it from QSPI Flash with the following commands \(Assume that image size is less than 0x20000, otherwise the sf erase and write command size parameter must be enlarged. If the image size is bigger than 0x20000 \(128 kB\), change 0x20000 to a number larger or equal to the image size.\):
    -   sf probe.
    -   sf erase 0x0 0x20000.
    -   fatload mmc 0:1 0x62000000 sdk20-app.img.
    -   sf write 0x62000000 0x0 0x20000.

        |![](../images/u_boot_cmd_run_application_qspi.png "U-Boot command to run application on
												QSPI")

|

8.  Open another terminal application on the PC, such as PuTTY and connect to the debug COM port \(to determine the COM port number, see Appendix A\). Configure the terminal with these settings:
    -   115200
    -   No parity
    -   8 data bits
    -   1 stop bit
9.  Power off and repower on the board.
10. The hello\_world application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    |![](../images/hello_world_demo_running_on_cortex_m4_core.png "Hello world demo running on Cortex-M4
												core")

|


