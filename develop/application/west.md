# West

West comes from [Zephyr’s meta-tool]([West (Zephyr’s meta-tool) — Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/index.html)). For MCUXSDK, we not only use its multiple repository management system, but also develop a series of auxiliary commands based on its pluggable features to facilitate the user's development.

## Format
| Command | Description                              |
| ------- | ---------------------------------------- |
| format  | Format specified files. Currently support cmake, c, c++, cuda, python, yaml files. |


## Build

Use `west build -h` to see help information for west build command.
Compared to zephyr's west build, MCUXSDK build command provides following additional options for mcux examples:

- --toolchain: specify the toolchain for this build, default armgcc.
- --config: value for CMAKE_BUILD_TYPE, default debug.

Here are some typical usage for generating a SDK example is:

```bash
# Generate example with default settings
west build -b frdmk22f examples/demo_apps/hello_world

# Just print cmake commands, do not execute it
west build -b frdmk22f examples/demo_apps/hello_world --dry-run

# Generate other toolchain like iar, default armgcc
west build -b frdmk22f examples/demo_apps/hello_world --toolchain iar

# Generate config type, default debug
west build -b frdmk22f examples/demo_apps/hello_world --config release

```

For multicore devices, you shall specify the corresponding core id by passing the command line argument "-Dcore_id". For example

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug
```

Remember to use "--config" to specify build target.

For shield, please use the "--shield" to specify the shield to run, like

```bash
west build -b mimxrt700evk --shield a8974 examples examples/issdk_examples/sensors/fxls8974cf/fxls8974cf_poll -Dcore_id=cm33_core0
```

If you want to get available commands for different build config combinations supported by the project and the toolchain, you can run the command below. Please note that "@${core_id}" suffix for board is only needed for multicore devices.
```bash
  west list_project -p examples/mbedtls_examples/mbedtls_selftest -b evkmimxrt1160@cm4 -t mdk
```
Here is the output:
```bash
INFO: [   1][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config debug -b evkmimxrt1160 -Dcore_id=cm4]
INFO: [   2][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config flexspi_nor_debug -b evkmimxrt1160 -Dcore_id=cm4]
INFO: [   3][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config flexspi_nor_release -b evkmimxrt1160 -Dcore_id=cm4]
INFO: [   4][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config release -b evkmimxrt1160 -Dcore_id=cm4]
INFO: [   5][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config sdram_debug -b evkmimxrt1160 -Dcore_id=cm4]
INFO: [   6][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config sdram_release -b evkmimxrt1160 -Dcore_id=cm4]
```

For multicore project building, you can build all projects by adding "--sysbuild" for main application. For example:

```bash
west build -b evkmimxrt1170 --sysbuild ./examples/middleware/multicore/multicore_examples/hello_world/primary -Dcore_id=cm7 --config flexspi_nor_debug -p always
```

For more details, please refer to [System build](../build_system/Sysbuild.md#sysbuild).

## Flash and debug

### Basic

For a project that have been compiled successfully, use the command to flash the image:

```bash
west flash
```

To specify the build directory, use `--build-dir` (or `-d`).

### Chose debug server

Typical supported debugger server:
1. [LinkServer](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/linkserver-for-microcontrollers:LINKERSERVER)
2. [JLink](https://www.segger.com/downloads/jlink/)

Please install LinkServer or JLink and add it to PATH environment variable firstly, then specify debug server with `-r`.
If you want to configure debug server, please refer to [Flash and Debug Data](../build_system/BCS_data.md#flash-and-debug-data).

Flash the hello_world example:

```bash
west flash -r linkserver
```

![flash](../build_system/_doc/flash.png)

### Debug

Start a gdb interface by following command:

```bash
west debug -r linkserver
```

![debug](../build_system/_doc/debug.png)

**Note**
All of the above west commands can only be run in mcuxsdk west workspace. If you want to use them outside the workspace, please run `SDK-root/mcux-env.cmd` in Windows Command Prompt or `source SDK-root/mcux-env.sh` in Linux terminal to activate the commands.


