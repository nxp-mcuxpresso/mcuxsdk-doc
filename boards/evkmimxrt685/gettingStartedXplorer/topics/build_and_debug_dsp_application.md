# Build and Debug DSP Application

The Xtensa command-line toolchain is installed as part of the Xplorer IDE. The tools can be optionally installed on a new Windows or Linux system without the IDE using the redistributable compressed file found at: `<XTENSA_ROOT>/XtDevTools/downloads/RI-2023.11/tools/`. For more information, see [Install Xtensa On Chip Debugger Daemon](install_xtensa_on_chip_debugger_daemon.md).

In order to use the command-line tools, some environment variables must be set up for use with the cmake build scripts:

```
# Add tools binaries to PATH.  Assume ~/xtensa/ is install root - please adjust accordingly.
export PATH=$PATH:~/xtensa/XtDevTools/install/tools/RI-2023.11-linux/XtensaTools/bin
# (Optional) Use environment variable to control license file
# NOTE: ~/.flexlmrc will override this selection.  Please delete that file before proceeding.
export LM_LICENSE_FILE=~/RT600.lic
# Setup env vars needed for compile and linking
export XCC_DIR=~/xtensa/XtDevTools/install/tools/RI-2023.11-linux/XtensaTools
export XTENSA_SYSTEM=~/xtensa/XtDevTools/install/builds/RI-2023.11-linux/
nxp_rt600_RI23_11_newlib/configexport XTENSA_CORE=nxp_rt600_RI23_11_newlibb
```

**Note:** On Windows, you can use the ‘setx’ command instead of the ‘export’ command to set the environment variables.

1.  Use the batch/shell script to build out the DSP application from the command line, in the ‘xcc’ directory:

    ```
    user@linux:~/SDK/boards/evkmimxrt685/dsp_examples/xaf_record/dsp/xcc$ ./build_debug.sh
    ...
    [100%] Built target dsp_xaf_record_hifi4.elf
    ```

    **Note:** Some warnings during the linking process \(floating-point ABI\) may appear. However, the warnings may be ignored.

2.  Launch xt-ocd debugging server \(replace topology.xml with your custom version – see section 1.5 of this document\):

    ```
    user@linux:/opt/Tensilica/xocd-14.11$ ./xt-ocd.exe -c topology.xml
    ```

    **Note:** If the Arm core fails to initialize the DSP, the xt-ocd daemon may fail to start. Therefore, the Arm core must initialize the DSP first.

3.  Connect with Xtensa GDB to the device and execute the DSP application:

    ```
    user@linux:/SDK/boards/evkmimxrt685/dsp_examples/xaf_record/dsp/xcc$ xt-gdb
    debug/dsp_xaf_record_hifi4.elf
    GNU gdb (GDB) 7.11.1 <Xtensa Tools VERSION NUMBER>
    ...
    Reading symbols from debug/dsp_xaf_record_hifi4.elf...done.
    (xt-gdb)
    (xt-gdb) target remote localhost:20000
    Remote debugging using localhost:20000
    _DoubleExceptionVector ()
        at /home/xpgcust/tree/RI-2023.11/ib/tools/swtools-x86_64-linux/xtensa-elf/src/xos/src/xos_vectors.S:216
    216 /home/xpgcust/tree/RI-2023.11/ib/tools/swtools-x86_64-linux/xtensa-elf/src/xos/src/xos_vectors.S: No such file or directory.
    (xt-gdb) reset
    _ResetVector ()
        at /home/xpgcust/tree/RI-2023.11/ib/tools/swtools-x86_64-linux/xtensa-elf/src/xtos/xea2/reset-vector-xea2.S:71
    71  /home/xpgcust/tree/RI-2023.11/ib/tools/swtools-x86_64-linux/xtensa-elf/src/xtos/xea2/reset-vector-xea2.S: No such file or directory.
    (xt-gdb) load
    Loading section .rtos.rodata, size 0x80 lma 0x200000
    Loading section .rodata, size 0x17d50 lma 0x200080
    Loading section .text, size 0x633f0 lma 0x217dd0
    Loading section .rtos.percpu.data, size 0x4 lma 0x27b1c0
    Loading section .data, size 0x110c lma 0x27b1d0
    Loading section NonCacheable, size 0x2960 lma 0x20040000
    Loading section .Level3InterruptVector.literal, size 0x4 lma 0x24000000
    Loading section .DebugExceptionVector.literal, size 0x4 lma 0x24000004
    Loading section .NMIExceptionVector.literal, size 0x4 lma 0x24000008
    Loading section .ResetVector.text, size 0x13c lma 0x24020000
    Loading section .WindowVectors.text, size 0x16c lma 0x24020400
    Loading section .Level2InterruptVector.text, size 0x1c lma 0x2402057c
    Loading section .Level3InterruptVector.text, size 0xc lma 0x2402059c
    Loading section .DebugExceptionVector.text, size 0xc lma 0x240205bc
    Loading section .NMIExceptionVector.text, size 0xc lma 0x240205dc
    Loading section .KernelExceptionVector.text, size 0xc lma 0x240205fc
    Loading section .UserExceptionVector.text, size 0x18 lma 0x2402061c
    Loading section .DoubleExceptionVector.text, size 0x8 lma 0x2402063c
    Start address 0x24020000, load size 520016
    Transfer rate: 8 KB/sec, 10612 bytes/write.
    (xt-gdb) b main
    Breakpoint 1 at 0x21ab5b: file /SDK/boards/src/dsp_examples/xaf_record/hifi4/xaf_main_hifi4.c, line 366.
    (xt-gdb) c
    Continuing.
    Breakpoint 1, main ()
        at /SDK/boards/src/dsp_examples/xaf_record/hifi4/xaf_main_hifi4.c:366
    366     xos_start_main("main", 7, 0);
    (xt-gdb) c
    Continuing.
    ```

    **Note:** You can use the gdb command ‘set substitute-path’ to map the missing symbols from the toolchain libraries. For example:

    ```
    set substitute-path /home/xpgcust/tree/RI-2023.11/ib/tools/swtools-x86_64-linux ~/xtensa/tools/RI-2023.11-linux/XtensaTools
    ```

    For more information on xt-gdb, see the Cadence GNU Debugger User’s Guide and the Cadence Xtensa Debug Guide. The documents are available at:

    -   `~/xtensa/XtDevTools/downloads/RI-2023.11/docs/gnu_gdb_ug.pdf`
    -   `~/xtensa/XtDevTools/downloads/RI-2023.11/docs/xtensa_debug_guide.pdf`

**Parent topic:**[Run and Debug from Command-Line Environment / LINUX](../topics/run_and_debug_from_command-line_environment_linux.md)

