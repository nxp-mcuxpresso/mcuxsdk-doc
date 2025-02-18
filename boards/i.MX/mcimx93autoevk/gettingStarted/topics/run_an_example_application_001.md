# Run an example application

To run a demo application using J-Link GDB Server application, perform the following steps.

1.  Connect the development platform to your PC via USB cable between the DBG USB connector \(J26\) and the PC USB connector.
2.  Connect 12 V ~ 20 V power supply and J-Link Plus to the device.

3.  Switch SW5\[1:4\] to the M core boot and ensure that the image is not available on the boot source. For example, 0b0101 for MicroSD boot. Keep the SD slot empty.
4.  Open the terminal application on the PC, such as PuTTY or TeraTerm, connect to the debug COM port, see [How to determine COM port](how_to_determine_com_port.md#), and configure the terminal with these settings:
    1.  115200 baud rate, depending on your board \(reference `BOARD_DEBUG_UART_BAUDRATE` variable in the `board.h` file\)
    2.  No parity
    3.  8 data bits
    4.  1 stop bit

        |![](../images/terminal_putty_configurations.png "Terminal (PuTTY) configurations")

|

5.  Power on the board.
6.  Open the J-Link GDB Server application. Assuming the J-Link software is installed, the application can be launched from a new terminal for the MIMX9352\_M33 device:

    ```
    $ JLinkGDBServer -jlinkscriptfile /opt/SEGGER/JLink/Devices/NXP/iMX93/NXP_iMX93_Connect_CortexM33.JLinkScript -device MIMX9352_M33 -if SWD
    -----GDB Server start settings-----
    GDBInit file:                  none
    GDB Server Listening port:     2331
    SWO raw output listening port: 2332
    Terminal I/O port:             2333
    Accept remote connection:      localhost only
    Generate logfile:              off
    Verify download:               off
    Init regs on start:            off
    Silent mode:                   off
    Single run mode:               off
    Target connection timeout:     5000 ms
    ------J-Link related settings------
    J-Link Host interface:         USB
    J-Link script:                 Devices\NXP\iMX93\NXP_iMX93_Connect_CortexM33.JLinkScript
    J-Link settings file:          none
    ------Target related settings------
    Target device:                 MIMX9352_M33
    Target interface:              SWD
    Target interface speed:        4000kHz
    Target endian:                 little
    
    Connecting to J-Link...
    J-Link is connected.
    Firmware: J-Link V9 compiled May  7 2021 16:26:12
    Hardware: V9.60
    S/N: 59611220
    Feature(s): RDI, GDB, FlashDL, FlashBP, JFlash
    Checking target voltage...
    Target voltage: 1.98 V
    Listening on TCP/IP port 2331
    Connecting to target...
    Connected to target
    Waiting for GDB connection...
    ```

7.  Change to the directory that contains the example application output. The output can be found in using one of these paths, depending on the build target selected:

    `<install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/debug`

    `<install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc/release`

    For this example, the path is:

    `*<install\_dir\>/boards/mcimx93autoevk/demo\_apps/hello\_world/armgcc/debug*`

8.  Start the GDB client:

    ```
    $ arm-none-eabi-gdb hello_world.elf
    GNU gdb (GNU Tools for Arm Embedded Processors 9-2019-q4-major) 8.3.0.20190709-git
    Copyright (C) 2019 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    Type "show copying" and "show warranty" for details.
    This GDB was configured as "--host=i686-w64-mingw32 --target=arm-none-eabi".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
       <http://www.gnu.org/software/gdb/documentation/>.
    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from hello_world.elf...
    (gdb)
    ```

9.  Connect to the GDB server and load the binary by running the following commands:

    1.  `target remote localhost:2331`
    2.  `monitor reset`
    3.  `monitor halt`
    4.  `load`
    ```
    
    (gdb) target remote localhost:2331
    Remote debugging using localhost:2331
    0x00000008 in \_\_isr\_vector \(\)
    (gdb) monitor reset
    Resetting target
    (gdb) monitor halt
    (gdb) load
    Loading section .interrupts, size 0x240 lma 0x0
    Loading section .text, size 0x3ab8 lma 0x240
    Loading section .ARM, size size 0x8 lma 0x3cf8
    Loading section .init\_array, size 0x4 lma 0x3d00
    Loading section .fini\_array, size 0x4 lma 0x3d04
    Loading section .data, size 0x64 lma 0x3d08
    Start address 0x2f4, load size 15724
    Transfer rate: 264 KB/sec, 2620 bytes/write.
    \(gdb\)
    
    
    ```


The application is now downloaded and halted at the reset vector. Execute the `monitor go` command to start the demo application.

```
(gdb) monitor go
```

The `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

|![](../images/text_display_hello_world_demo.png "Text display of the hello_world demo")

|

**Note:** If the software is already running on the M core, the debugger loading image into TCM may get HardFault or a data verification issue. NXP recommends you to follow the steps above to use the debugger. Repowering the board is required to restart the debugger.

**Parent topic:**[Linux OS host](../topics/linux_os_host.md)

