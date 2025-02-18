# Build an example application

To build an example application, follow these steps.

1.  Change the directory to the example application project directory, which has a path similar to the following:

    `<install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc`.

    For this example, the exact path is: `<install_dir>/boards/mcimx93evk/ demo_apps/hello_world/armgcc`.

2.  Run the `build_debug.sh` script on the command line to perform the build. The output is shown as below:

    ```
    $ ./build_debug.sh
    -- TOOLCHAIN_DIR: /work/platforms/tmp/gcc-arm-none-eabi-9-2019-q4-major
    -- BUILD_TYPE: debug
    -- TOOLCHAIN_DIR: /work/platforms/tmp/gcc-arm-none-eabi-9-2019-q4-major
    -- BUILD_TYPE: debug
    -- The ASM compiler identification is GNU
    -- Found assembler: /work/platforms/tmp/gcc-arm-none-eabi-8-2019-q3-update/bin/arm-none-eabi-gcc
    -- Configuring done
    -- Generating done
    -- Build files have been written to:
    /work/platforms/tmp/nxp/SDK\_2.12.0\_MCIMX93\_EVK/boards/mcimx93evk/demo\_apps/hello\_world/armgcc/demo\_apps/hello\_world/armgcc
    Scanning dependencies of target hello_world.elf
    \[ 6%\] Building C object CMakeFiles/hello\_world.elf.dir/work/platforms/tmp/nxp/SDK\_2.12.0\_MCIMX93\_EVK/boards/mcimx93evk/demo\_apps/hello\_world/hello\_world.c.obj
     < -- skipping lines -- >
    [100%] Linking C executable debug/hello_world.elf
    [100%] Built target hello_world.elf
    ```


**Parent topic:**[Linux OS host](../topics/linux_os_host.md)

