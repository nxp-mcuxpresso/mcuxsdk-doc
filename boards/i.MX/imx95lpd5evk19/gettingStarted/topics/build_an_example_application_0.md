# Build an example application 

To build an example application, follow these steps.

1.  Change the directory to the example application project directory, which has a path similar to the following: `<install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc`. For example, the exact path is: `<install_dir>/boards/imx95lpd5evk19/demo_apps/hello_ world_sm/armgcc`.
2.  Run the `build_debug.sh` script at the command-line to perform the build. The output is shown as below:

    ```
    $ ./build_debug.sh
    -- TOOLCHAIN_DIR:
    -- BUILD_TYPE: debug
    -- TOOLCHAIN_DIR:
    -- BUILD_TYPE: debug
    -- The ASM compiler identification is GNU
    -- Found assembler:
    -- Configuring done
    -- Generating done
    -- Build files have been written to:
    Scanning dependencies of target hello_world.elf
    < -- skipping lines -- >
    [100%] Linking C executable debug/hello_world.elf
    [100%] Built target hello_world.elf
    ```

    **Note:** `build_debug/release.sh` are ram target, `build_ddr_debug/release.sh` are ddr target \(only imx95lpd5evk19 hello\_world\_sm support ddr target this release, the same as iar\).


**Parent topic:**[Linux OS host](../topics/linux_os_host_0.md)

