# Build and Debug Arm Application

The Arm application requires the GNU Arm Embedded Toolchain and CMake version 3.x for command line compile and linking. See the ‘Getting Started with MCUXpresso SDK for RT500.pdf’ in the <SDK\_ROOT\>/docs/ directory for more information on installation and configuration of required build tools for command line development.

1.  Launch a command prompt / terminal and change directory to the xaf\_record application.

    ```
    user@linux:~/SDK/boards/evkmimxrt595/dsp_examples/xaf_record/cm33/Armgcc$ **ls -1**
    build_all.bat
    build_all.sh
    build_debug.bat
    build_debug.sh
    build_flash_debug.bat
    build_flash_debug.sh
    build_flash_release.bat
    build_flash_release.sh
    build_release.bat
    build_release.sh
    clean.bat
    clean.sh
    CMakeLists.txt
    ```

2.  Use .bat files to build the configuration on Windows, and .sh files on Linux/UNIX.

    ```
    user@linux:~/SDK/boards/evkmimxrt595/dsp_examples/xaf_record/cm33/Armgcc$ **./build\_debug.sh**
    ...
    [100%] Linking C executable debug/dsp_xaf_record_cm33.elf
    [100%] Built target dsp_xaf_record_cm33.elf
    ```

3.  Launch the GDB server \(NOTE: J-Link requires version \>= 6.46\).

    ```
    user@linux:/opt/JLink$ ./JLinkGDBServerCLExe -device MIMXRT595_M33 -if SWD
    SEGGER J-Link GDB Server V6.46j Command Line Version
    ...
    Listening on TCP/IP port 2331
    Connecting to target...Connected to target
    Waiting for GDB connection...
    ```

4.  Connect with GDB to the device and load Arm application.

    ```
    user@jlinux:~/SDK/boards/evkmimxrt595/dsp_examples/xaf_record/cm33/Armgcc$ Arm-none-eabi-gdb debug/dsp_xaf_demo_cm33.elf
            ...
            Reading symbols from debug/dsp_xaf_record_cm33.elf...
            (gdb) **target remote localhost:2331**
            Remote debugging using localhost:2331
            0x1301ec7a in ?? ()
            (gdb) **mon reset**
            Resetting target
            (gdb) **load**
            Loading section .flash_config, size 0x200 lma 0x7f400
            Loading section .interrupts, size 0x130 lma 0x80000
            Loading section .text, size 0xe330 lma 0x80130
            Loading section CodeQuickAccess, size 0x52c lma 0x8e460
            Loading section .Arm, size 0x8 lma 0x8e98c
            Loading section .init_array, size 0x4 lma 0x8e994
            Loading section .fini_array, size 0x4 lma 0x8e998
            Loading section .data, size 0x104 lma 0x8e99c
            Start address 0x801e4, load size 60576
            Transfer rate: 272 KB/sec, 5506 bytes/write.
            (gdb) **b main**
            Breakpoint 1 at 0x808f2: file /SDK/boards/src/dsp_examples/xaf_record/cm33/main_cm33.c, line 161.
            (gdb) **c**
            Continuing.
            Breakpoint 1, main ()
            at /SDK/boards/src/dsp_examples/xaf_record/cm33/main_cm33.c:161
            161     BOARD_InitHardware();
    ```


**Parent topic:**[Run and Debug from Command-Line Environment / LINUX](../topics/run_and_debug_from_command_line_environment_linux.md)

