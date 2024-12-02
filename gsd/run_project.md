# Evaluate an Example Project

## Supported Boards

Use the west extension `west list_project` to understand the board support scope for a specified example

```base
west list_project -p examples/demo_apps/hello_world [-t armgcc]

INFO: [   1][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evk9mimx8ulp -Dcore_id=cm33]
INFO: [   2][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkbimxrt1050]
INFO: [   3][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkbmimxrt1060]
INFO: [   4][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkbmimxrt1170 -Dcore_id=cm4]
INFO: [   5][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   6][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkcmimxrt1060]
INFO: [   7][west build -p always examples/demo_apps/hello_world --toolchain armgcc --config release -b evkmcimx7ulp]
...

```

## Build the project

Use `west build -h` to see help information for west build command.
Compared to zephyr's west build, MCUXpresso SDK's west build command provides following additional options for mcux examples:

- --toolchain: specify the toolchain for this build, default armgcc.
- --config: value for CMAKE_BUILD_TYPE, default debug.
- --show-configs: show all supported build configurations for the project.

Here are some typical usage for generating a SDK example:

```bash
# Generate example with default settings
west build -b frdmk22f examples/demo_apps/hello_world

# Just print cmake commands, do not execute it
west build -b frdmk22f examples/demo_apps/hello_world --dry-run

# Generate other toolchain like iar, default armgcc
west build -b frdmk22f examples/demo_apps/hello_world --toolchain iar

# Generate config type, default debug
west build -b frdmk22f examples/demo_apps/hello_world --config release

# Show all supported build configurations
west build -b frdmk22f examples/demo_apps/hello_world --show-configs
```

For multicore devices, you shall specify the corresponding core id by passing the command line argument "-Dcore_id". For example

```bash
west build -b evkmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug
```

For shield, please use the "--shield" to specify the shield to run, like

```bash
west build -b mimxrt700evk --shield a8974 examples examples/issdk_examples/sensors/fxls8974cf/fxls8974cf_poll -Dcore_id=cm33_core0
```

### Sysbuild(System build)

To support multicore project building, we ported Sysbuild from Zephyr. It supports combining multiple projects for compilation. You can build all projects by adding "--sysbuild" for main application. For example:

```bash
west build -b evkmimxrt1170 --sysbuild ./examples/middleware/multicore/multicore_examples/hello_world/primary -Dcore_id=cm7 --config flexspi_nor_debug -p always
```

## Config a project

Example in MCUXpresso SDK is configured and tested with pre-defined configuraiton. You can follow this step to change the configuration.

Run cmake configuration

```bash
west build -b frdmk22f examples/demo_apps/hello_world --cmake-only
```

You can ignore `--cmake-only`, then the project will be built.
Run guiconfig target

```bash
west build -t guiconfig
```

Then you will get the Kconfig GUI launched, like

![kconfig_gui](./_doc/kconfig_gui.png)

You can select/deselect and modify to do reconfiguration and remember to save.

After you save and close, you can directly run "west build" to do the build.


## Flash

***Note***: Please refer [West Flash and Debug Support](#west-flash-and-debug-support) to enable west flash/debug support.

As we do not have a FRDM-K64F with JLink or other runners for test, we only ensure flash/debug commands can work for linkserver. Please install linkserver and add it to your PATH firstly.

Flash the hello_world example:

```bash
west flash -r linkserver
```

## Debug

Start a gdb interface by following command:

```bash
west debug -r linkserver
```