# Sysbuild

Sysbuild is a higher-level build system that can be used to combine multiple other build systems together. It's ported from [Sysbuild (System build) — Zephyr Project](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-zephyr-application). In MCUXpresso SDK build system, it's mainly used for multi-project example build.

## Sysbuild files

To include sub projects into building system, you must prepare `sysbuild.cmake` into main project folder. Sub projects can be located anywhere which are imported by `ExternalMCUXProject_Add` command inside `sysbuild.cmake`. 

Take multicore hello_world for example:

```cmake
# examples/multicore_examples/hello_world/primary/sysbuild.cmake

ExternalMCUXProject_Add(
        APPLICATION hello_world_secondary_core
        SOURCE_DIR  ${APP_DIR}/../secondary
        board ${SB_CONFIG_secondary_board}
        core_id ${SB_CONFIG_secondary_core_id}
        config ${SB_CONFIG_secondary_config}
        toolchain ${SB_CONFIG_secondary_toolchain}
)

# Let's build the secondary application first
add_dependencies(${DEFAULT_IMAGE} hello_world_secondary_core)
```

The `${APP_DIR}` means the build directory of primary project and `${DEFAULT_IMAGE}` indicates the primary project target. The build sequence can be determined by [add_dependencies](https://cmake.org/cmake/help/latest/command/add_dependencies.html#add-dependencies) function in `sysbuild.cmake`.

The variables with `SB_` prefix in `sysbuild.cmake` can be defined before adding sub projects. Or you can pass them with west command `-D`.

In practice it is more common to set these variables automatically via kconfig to support multiple platforms in a more flexible way. For example, you can prepare a `Kconfig.sysbuild` in main project folder:

```bash
# examples/middleware/multicore/multicore_examples/hello_world/primary/Kconfig.sysbuild

config secondary_board
    string
    default "$(board)"

config secondary_core_id
    string
    default "cm4" if $(board) = "evkbmimxrt1170" && $(core_id) = "cm7"
    default "cm33_core1" if $(board) = "lpcxpresso55s69" && $(core_id) = "cm33_core0"

config secondary_config
    string
    default "debug" if $(config) = "debug"
    default "debug" if $(config) = "flexspi_nor_debug"

config secondary_toolchain
    string
    default "$(toolchain)"
```

Sysbuild is used to organize project build sequence, about how images are linked together is set by the project's own CMakeLists.txt. For example, you must import the secondary core binary in the CMakeLists.txt of primary project:

```cmake
# examples/multicore_examples/hello_world/secondary/CMakeLists.txt
mcux_convert_binary(
    TOOLCHAINS armgcc mdk iar
    BINARY ${APPLICATION_BINARY_DIR}/${CONFIG_TOOLCHAIN}/core1_image.bin
)

# examples/multicore_examples/hello_world/primary/CMakeLists.txt
mcux_add_iar_configuration(
    LD "--image_input=${APPLICATION_BINARY_DIR}/../hello_world_secondary_core/iar/core1_image.bin,_core1_image,   __core1_image,4 "
)
```

## Build command

To enable sysbuild, only `--sysbuild` is needed when you build the main project:

```bash
west build -b evkbmimxrt1170 --sysbuild ./examples/multicore_examples/hello_world/primary -Dcore_id=cm7  --config flexspi_nor_debug --toolchain=armgcc -p always
```

You can set Kconfig options via command as `-DCONFIG_<var>=<value>` for main project or `-D<namespace>_CONFIG_<var>=<value>` for other projects.
The namespace is the project name declared in `project()` from CMakeLists.txt file, to imply the config option is for which project. For example:
```bash
west build -b evkmimxrt1160 --sysbuild examples/multicore_examples/hello_world/primary -d build -Dcore_id=cm7 --toolchain iar -DCONFIG_MCUX_COMPONENT_driver.lpi2c=y -Dhello_world_secondary_core_CONFIG_MCUX_COMPONENT_driver.lpi2c=y  -p always
```

You can set up a separate config file for each projects via command as `-DCONF_FILE=<path/to/config_file>` for main project or `-D<namespace>_CONF_FILE=<path/to/config_file>` for other projects. The namespace is the project name declared in `project()` from CMakeLists.txt file, to imply the config file is for which project. The config file path can be either an absolute path or a relative path to the current command invocation path. For example:
```bash
west build -b evkmimxrt1160 --sysbuild examples/multicore_examples/hello_world/primary -d build -Dcore_id=cm7 --toolchain iar -DCONF_FILE="./examples/multicore_examples/hello_world/prj-static.conf" -Dhello_world_secondary_core_CONF_FILE="./examples/multicore_examples/hello_world/prj-static.conf" -p always
```
This config file has the highest priority over all.

## Kconfig GUI

The sysbuild projects can be configured with Kconfig GUI just like a normal project in the build system. The only difference is the target name, for main project, they're menuconfig or guiconfig, for sub project, you must add project name prefix to differ each target. 

For example:

```bash
west build -t guiconfig
west build -t hello_world_secondary_core_guiconfig
```

## Standalone project

When using sysbuild command, if you want to generate [Standalone project](./../sdk/example_development.md#standalone-examples) for sharing, you can add "-t standalone_project". Then the standalone projects will be generated in the `<build directory>/<toolchain>` folder. The default build directory is "build", and can be set to other path by adding "-d" parameter.
For example: 
```bash
west build -b evkmimxrt1160 --sysbuild ./examples/multicore_examples/rpmsg_lite_pingpong/primary -Dcore_id=cm7 --toolchain iar -p always -t standalone_project -d build_rpmsg_lite_pingpong
```