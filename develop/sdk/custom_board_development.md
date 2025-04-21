# Custom Board Development

## Enable a Custom Board

To enable a custom board outside mcuxsdk repository, you need to prepare the following files

```
<CUSTOM_BOARD_ROOT>
        ├── <BOARD>
                ├── CMakeLists.txt
                ├── Kconfig
                ├── prj.conf
                ├── variable.cmake
                ├── board_runner.cmake
                ├── board sources
```

> `CUSTOM_BOARD_ROOT` is the root directory holding your custom board folder and all the contents. It shall be passed into build command so that build system can know your board location.

If you have a custom board which is built upon frdmmcxa346(Let's call it `frdmmcxa346_custom`) and placed under your own folder outside mcuxsdk repository, let's go with the following steps to integrate it into MCUXpresso SDK.

### Board Files

Firstly you need to prepare the board level files to provide basic functionalities like debug console output, clock configuration, pin mux, etc.

You can directly copy the board.h,board.c,clock_config.h,clock_config.c,pin_mux.h,pin_mux.c under `mcuxsdk/examples/_boards/frdmmcxa346` into your `frdmmcxa346_custom` folder and update them.

### CMakeLists.txt

The CMakeLists.txt contains the board basic build configuration data. Copy the `mcuxsdk/examples/_boards/frdmmcxa346/CMakeLists.txt` into your `frdmmcxa346_custom` and edit it.

1. Remove the `include` lines with project_segments cmake files. Those cmake files are for sources under `mcuxsdk/examples/_boards` which doesn't work for board in custom locations. You can leave them because they don't affect build.

2. Add new custom board.h,board.c,clock_config.h,clock_config.c,pin_mux.h,pin_mux.c. To make those files selectable  in the Kconfig system, we can use the [project segment](example_development.md#project-segment) way. Of curse you can directly use native cmake syntax to add these files.


The updated CMakeLists.txt is like:

```cmake
include(${SdkRootDirPath}/arch/arm/target/flash.cmake)
include(${SdkRootDirPath}/examples/_common/project_setting/arm_common.cmake)

## Custom board modules
if(CONFIG_MCUX_PRJSEG_module.custom_board.boardfile)
    mcux_add_source(SOURCES board.h board.c)
    mcux_add_include(INCLUDES .)
endif()

if(CONFIG_MCUX_PRJSEG_module.custom_board.clock)
    mcux_add_source(SOURCES clock_config.h clock_config.c)
    mcux_add_include(INCLUDES .)
endif()

if(CONFIG_MCUX_PRJSEG_module.custom_board.pinmux)
    mcux_add_source(
      SOURCES
        pin_mux.h
        pin_mux.c
    )
    mcux_add_include(INCLUDES .)
endif()

## Custom board project hardware_init.c/app.h
# Use PROJECT_NAME to distinguish between different projects
if(CONFIG_MCUX_PRJSEG_project.custom_board.hw_app)
  mcux_add_source(
    SOURCES examples/${PROJECT_NAME}/hardware_init.c
            examples/${PROJECT_NAME}/app.h
  )
  mcux_add_include(INCLUDES examples/${PROJECT_NAME})
endif()
```

The custom board CMakeLists.txt is added into the build tree through the `mcuxsdk/examples/CMakeLists.txt`:

```cmake
# Board cmakelist
# External repository board, exclusive to the internal repository board
mcux_add_cmakelists(${CUSTOM_BOARD_ROOT}/${board} OPTIONAL)

# Internal repository board, exclusive to the external repository board
mcux_add_cmakelists(${SdkRootDirPath}/${board_root}/${board} OPTIONAL)

# Project segment
include(${SdkRootDirPath}/examples/_common/project_segments/common/prjseg.cmake)
```

### Kconfig

Copy the `mcuxsdk/examples/_boards/frdmmcxa346/Kconfig` into your `frdmmcxa346_custom` and edit it. Several things to update:

1. `MCUX_HW_BOARD_<board name>` is used to provide the default used components by all board examples.
2. Add the newly added project segments corresponding to the CMakeLists.txt.
3. Remove unused Kconfig.defconfig and Kconfig.prjseg.


The updated Kconfig is like

```
# Copyright 2025 NXP
#
# SPDX-License-Identifier: BSD-3-Clause

config MCUX_HW_BOARD_frdmmcxa346_custom
    bool
    default y
    imply MCUX_HW_DEVICE_MCXA346
    imply MCUX_COMPONENT_driver.clock
    imply MCUX_COMPONENT_driver.common
    imply MCUX_COMPONENT_driver.gpio
    imply MCUX_COMPONENT_driver.lpuart
    imply MCUX_COMPONENT_driver.port
    imply MCUX_COMPONENT_driver.mcx_spc
    imply MCUX_COMPONENT_driver.reset

    ## Board project segment dependency data

    select MCUX_COMPONENT_driver.port if MCUX_PRJSEG_module.custom_board.pinmux
    select MCUX_COMPONENT_driver.gpio if MCUX_PRJSEG_module.custom_board.pinmux
    select MCUX_COMPONENT_driver.inputmux if MCUX_PRJSEG_module.custom_board.pinmux
    select MCUX_COMPONENT_driver.clock if MCUX_PRJSEG_module.custom_board.clock
    select MCUX_COMPONENT_driver.reset if MCUX_PRJSEG_module.custom_board.clock
    select MCUX_COMPONENT_driver.mcx_spc if MCUX_PRJSEG_module.custom_board.clock
    select MCUX_COMPONENT_component.lpuart_adapter if MCUX_PRJSEG_module.board.console_lite
    select MCUX_COMPONENT_driver.lpuart if MCUX_PRJSEG_module.board.console_lite

## Custom board modules
config MCUX_PRJSEG_module.custom_board.boardfile
    bool "Board file"
    help
        The custom board file.

config MCUX_PRJSEG_module.custom_board.clock
    bool "Clock"
    help
        The custom board clock file.

config MCUX_PRJSEG_module.custom_board.pinmux
    bool "Pinmux"
    help
        The custom board pinmux file.

## Custom board project hardware_init.c/app.h
config MCUX_PRJSEG_project.custom_board.hw_app
    bool "app.h/hardware_init.c"
    help
        The custom board app/hardware_init.c file.
```

The custom board Kconfig is added into the build tree through the `mcuxsdk/examples/Kconfig`:

```
# External repository board, exclusive to the internal repository board
osource "${CUSTOM_BOARD_ROOT}/${board}/Kconfig"

# Internal repository board, exclusive to the external repository board
orsource "../${board_root}/${board}/Kconfig"

rsource "_common/Kconfig.interfaces"

menu "Project Segments"
rsource  "./_common/project_segments/common/Kconfig.prjseg"
orsource "../${board_root}/${board}/Kconfig.prjseg"
endmenu
```

### prj.conf

In your custom board prj.conf, you need to disable the mcuxsdk repository board/clock_config/pin_mux project segments and enable your custom ones:

```
CONFIG_MCUX_HW_DEVICE_PART_MCXA346VLQ=y

# Mcuxsdk internal board project basic segments all should be set to n
CONFIG_MCUX_PRJSEG_module.board.boardfile=n
CONFIG_MCUX_PRJSEG_module.board.use_board_clock=n
CONFIG_MCUX_PRJSEG_module.board.clock=n
CONFIG_MCUX_PRJSEG_module.board.pinmux_project_folder=n
CONFIG_MCUX_PRJSEG_project.hw_app_project_folder=n
CONFIG_MCUX_HAS_PRJSEG_module.board.pinmux_sel=n
CONFIG_MCUX_PRJSEG_project.hw_app_project_core_folder=n
CONFIG_MCUX_HAS_PRJSEG_project.use_hw_app=n

# Custom board basic segments
CONFIG_MCUX_PRJSEG_module.custom_board.boardfile=y
CONFIG_MCUX_PRJSEG_module.custom_board.clock=y
CONFIG_MCUX_PRJSEG_module.custom_board.pinmux=y
```

###  variable.cmake

variable.cmake file is the connection file for a board to the build system. It tells the board and device related variable names:

```K
mcux_set_variable(board frdmmcxa346_custom)

if (NOT DEFINED device)
    mcux_set_variable(device MCXA346)
endif()

if (NOT DEFINED soc_series)
    mcux_set_variable(soc_series MCXA)
endif()

include(${SdkRootDirPath}/devices/MCX/${soc_series}/${device}/variable.cmake)
```

### board_runner.cmake

board_runner.cmake is used to enable board example download and debug. For jlink it is mainly with device related information, so you can copy `mcuxsdk/examples/_boards/frdmmcxa346/board_runner.cmake` into your `frdmmcxa346_custom` folder and keep the runner that works for your case:

```cmake
board_runner_args(jlink "--device=${CONFIG_MCUX_TOOLCHAIN_JLINK_CPU_IDENTIFIER}")

include(${SdkRootDirPath}/cmake/extension/runner/jlink.board.cmake)
```

### Full Picture Of a Custom Board

After you have done all the above steps, you will get the following files in your `CUSTOM_BOARD_ROOT/frdmmcxa346_custom`:

```
<CUSTOM_BOARD_ROOT>
        ├── frdmmcxa346_custom
                ├── board.h
                ├── board.c
                ├── clock_config.h
                ├── clock_config.c
                ├── pin_mux.h
                ├── pin_mux.c
                ├── CMakeLists.txt
                ├── Kconfig
                ├── prj.conf
                ├── variable.cmake
                ├── board_runnder.cmake
```

They make up your custom board contents.

Here are 2 examples of custom boards `frdmmcxa346_custom` based on frdmmcxa346 and `evkbmimxrt1170_custom` based on evkbmimxrt1170 for you to reference.

- [frdmmcxa346_custom](../../_static/build_system/frdmmcxa346_custom.zip)
- [evkbmimxrt1170_custom](../../_static/build_system/evkbmimxrt1170_custom.zip)

## Build With Repository Example

You can build a repository example with your custom board contents ready. Let's start with the hello_world. 

Before we build it we should notice that nearly all the MCUXpresso SDK examples use hardware_init.c and app.h to provide BOARD_InitHardware and some other board specific settings. In MCUXpresso SDK, we use some project segments like `MCUX_PRJSEG_project.hw_app_project_core_folder` and `MCUX_PRJSEG_project.hw_app_project_folder` to hold hardware_init.c and app.h. They both point to sources under `mcux/examples/_boards/<board>` folder which doesn't work for your custom board, so you need to provide your own hardware_init.c and app.h for your board for all repository examples. To make the data usable for all examples, we can use a project segment.
In `frdmmcxa346_custom/CMakeLists.txt`, adding:

```cmake
## Custom board project hardware_init.c/app.h
# Use PROJECT_NAME to distinguish between different projects
if(CONFIG_MCUX_PRJSEG_project.custom_board.hw_app)
  mcux_add_source(
    SOURCES examples/${PROJECT_NAME}/hardware_init.c
            examples/${PROJECT_NAME}/app.h
  )
  mcux_add_include(INCLUDES examples/${PROJECT_NAME})
endif()
```

Correspondingly, in `frdmmcxa346_custom/Kconfig`, adding:

```
## Custom board project hardware_init.c/app.h
config MCUX_PRJSEG_project.custom_board.hw_app
    bool "app.h/hardware_init.c"
    help
        The custom board app/hardware_init.c file.
```

In `frdmmcxa346_custom/prj.conf`, adding:

```
# Custom board project hardware_init.c/app.h for all mcuxsdk repository examples
CONFIG_MCUX_PRJSEG_project.custom_board.hw_app=y
```

After enabling the `MCUX_PRJSEG_project.custom_board.hw_app`, under mcuxsdk workspace you can use following command to build the hello_world example:

```bash
west build -b frdmmcxa346_custom examples/demo_apps/hello_world -DCUSTOM_BOARD_ROOT=<your custom board root(could be absolute path or relative path)>
```

If your custom board is multicore board and you want to try repository multi-project example, you can still use `--sysbuild` like

```bash
west build -b evkbmimxrt1170_custom examples/multicore_examples/hello_world/primary/ -Dcore_id=cm7 -DCUSTOM_BOARD_ROOT=<your custom board root(could be absolute path or relative path)> --sysbuild
```

> For multi-project example, there are many customized project segments that are used which are all pointing to mcuxsdk board specific contents, you need to disable them all and prepare your own board ones.

## Build With Freestanding Example

If you are working with your custom board and freestanding example, you could use your own downstream west workspace to hold your board(s) and examples:

```
root/my_downstream/
    ├── .west/                          # west directory
    ├── mcuxsdk/
    └── my_project/                     # your downstream repository
        ├── west.yml                    # west importing mcuxsdk related repos
        ├── examples
                └── demo_apps
                        └── hello_world # freestanding example
        └── _boards
                └── frdmmcxa346_custom
```

Since you have imported the mcuxsdk repositories into your own workspace, you can directly use `west build` under your workspace folder.

For freestanding example, you can use [west export_app ](./example_development.md#convert-a-repository-example-to-a-freestanding-example)  to export interesting repository example to be the freestanding example like

```bash
# under my_project folder
# export repository example to be freestanding example
west export_app ../mcuxsdk/examples/demo_apps/hello_world -o root/my_downstream/my_project
# after preparing the hardware_init.c and app.h, build the project
west build -b frdmmcxa346_custom examples/demo_apps/hello_world -DCUSTOM_BOARD_ROOT=/root/my_downstream/myproject/_boards/ -DPrjRootDirPath=root/my_downstream/myproject -p
```

> DPrjRootDirPath is used by west export_app to specify destination and used in the updated freestanding example CMakeLists.txt, so you need to specify it in the command line argument. We plan to remove such variable in next release.

For exported freestanding example, it is still needed that you provide the hardware_init.c and app.h for the example for your custom board. The previous `MCUX_PRJSEG_project.custom_board.hw_app` way still applies.

## Notifications

The custom board doesn't support [IDE Project Generation](./../build_system/IDE_Project.md#ide-project-generation) related feature including standalone project generation.

The custom board doesn't support `west list_project` feature.