# Example Development

## Overview

In addition to the sources, one example contains CMakeLists.txt, Kconfig, prj.conf and example.yml.

```
hello_world
    ├── hello_world.c
    ├── CMakeLists.txt
    ├── Kconfig
    ├── prj.conf
    ├── example.yml
```

## CMakeLists.txt

CMakeLists.txt defines the sources, includes and static configurations.

Based on the cmake built-in macro `project`, we customize the `project` to provide the following additional arguments:

| Argument Name            | Argument Type | Explanation                              |
| ------------------------ | ------------- | ---------------------------------------- |
| PROJECT_BOARD_PORT_PATH  | Single        | Path for board porting files and data.<br />Only applied for examples with board-specific configuration. |
| PROJECT_DEVICE_PORT_PATH | Single        | Path for device porting files and data.<br />Only applied for examples with device-specific configuration. |
| PROJECT_TYPE             | Single        | Specify the project type, can be `EXECUTABLE` or `LIBRARY` or `LIBRARY_OBJECT`.<br />The default is `EXECUTABLE`. |
| CUSTOM_PRJ_CONF_PATH     | Multiple      | Specify customized prj.conf search paths. |

Here is the hello_world CMakeLists.txt:

```
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

# Specify the project
project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH ${board_root}/${board}/demo_apps/hello_world)

# Include device, board, drivers, components, middlewares, RTOS
include(${SdkRootDirPath}/CMakeLists.txt)

mcux_add_source(
    SOURCES hello_world.c
)
RTOSRTOS
mcux_add_include(
    INCLUDES .
)

# convert binary to .bin. 
mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
```

## Kconfig

Kconfig defines the dynamic configurations.

It is not required to always provide example specific Kconfig. If your example has specific Kconfig, then please follow the pattern to add it:

```
rsource "../../../Kconfig.mcuxpresso"

mainmenu "Hello world Example Run Time Configuration"

config HELLO_WORLD_EXAMPLE_MACRO
    bool "Hello world example macro"
    default y
    help
        "Hello world example macro"
```

1. `rsource "../../../Kconfig.mcuxpresso"` must be added to load all device, board and other components Kconfigs.
2. Set `mainmenu` to give the GUI title
3. Set the example specific configurations

> The Kconfig process will take example specific Kconfig as entry point with priority. If not provided, then it will take the mcuxsdk/Kconfig.mcuxpresso instead.

## prj.conf

prj.conf here specifies the example specific configuration values for Kconfig symbols. It will be merged together with other prj.conf values from device, board and shield to produce the final configurations.

See [prj.conf](../build_system/Configuration_System.md#prjconf) for more details.

## example.yml

example.yml contains data specifying example category, description, supported devices, boards and shields, etc. It is mainly for tool and CI usage.

### Overview

```yaml
# yaml-language-server: $schema=../../../../scripts/data_schema/example_description_schema.json
hello_world:
  section-type: application
  contents:
    meta_path: examples/demo_apps/hello_world
    project-root-path: boards/${board}/demo_apps/hello_world/${multicore_foldername}
    document:
      name: hello_world${core_id_suffix_name}
      category: demo_apps
      brief: The HelloWorld demo prints the "Hello World" string to the terminal using
        the SDK UART drivers and repeat what user input. The purpose of this demo
        is to show how to use the UART, and to provide a simple project for debugging
        and further development.
      example_readme:
      - examples/demo_apps/hello_world/readme.md
      - ${board_root}/${board}/demo_apps/hello_world/example_board_readme.md
      - ${board_root}/${board}/examples_shared_readme.md
  boards:
    evk9mimx8ulp@cm33: []
    evkbimxrt1050:
    - +armgcc@flexspi_nor_sdram_debug
    - +armgcc@flexspi_nor_sdram_release
    - +armgcc@sdram_txt_debug
    - +armgcc@sdram_txt_release
    - +iar@flexspi_nor_sdram_debug
    - +iar@flexspi_nor_sdram_release
    - +iar@ram_0x1400_debug
    - +iar@ram_0x1400_release
    - +iar@sdram_txt_debug
    - +iar@sdram_txt_release
    - +mdk@flexspi_nor_sdram_debug
    - +mdk@flexspi_nor_sdram_release
    - +mdk@ram_0x1400_debug
    - +mdk@ram_0x1400_release
    - +mdk@sdram_txt_debug
    - +mdk@sdram_txt_release
```

### Example Toolchains and Targets

The supported toolchains and build configuration targets for an example can be got in the following way:

1. Get the designated board example.yml to get the board default supported toolchains and build configuration targets from [board.toolchains](device_board_shield_definition.md#board).

   > This is for board examples. For device examples, it should be the device example.yml. We don't have such cases public yet.
   >
2. Get the designated board from `boards` data attribute

   1. If the data attribute is empty, then the board level toolchains and build configuration targets are the example ones.
   2. If the data attribute exists, `+` to add extra toolchains and build configuration targets pairs with the board ones. `-` to reduce extra ones from board ones.

The `mcuxsdk/scripts/data_schema/example_decription_schema.json` is provided to specify detailedly the data attributes for the example.yml.

## Example Types

### Board Examples and Device Examples

MCUXpresso SDK supports both board examples and device examples. The board examples are based on board and the mounted device while device examples only use target device without board. For [hierarchical configuration for porting](#hierarchical-configuration-for-board-porting), board examples use PROJECT_BOARD_PORT_PATH, device examples use PROJECT_DEVICE_PORT_PATH.

> Since most examples are board examples, we will focus on board examples for illustration in later chapters.

### Repository Examples and Freestanding Examples

In MCUXpresso SDK, based on example location we distinguish 2 example types: repository and freestanding examples.

| Example Type | Example Location(where CMakeLists.txt is placed) |
| ------------ | ---------------------------------------- |
| Repository   | MCUXpresso SDK repository                |
| Freestanding | Other locations                          |

#### Repository Examples

Most repository examples CMakelists.txts are located inside `mcuxsdk/examples/<example-category>/<example>` folder, like the hello_world CMakelists.txt is located in `mcuxsdk/examples/demo_apps/hello_world`.

```
sdk_next/
├─── .west/
│    └─── config
└─── mcuxsdk/
     ├── arch/
     ├── cmake/
     ├── examples
     │   	├── demo_apps
     │              ├── reconfig.cmake
     │              ├── prj.conf
     │  	        ├── hello_world
     │                     ├── CMakeLists.txt
     │                     ├── Kconfig
     │                     ├── prj.conf
     │                     ├── hello_world.c
     │                     ├── example.yml
```

##### Hierarchical Configuration

MCUXpresso SDK build system supports hierarchical configuration for repository examples by involving different levels of project configuration (prj.conf) files, each with its own priority. These prj.conf files are organized into four groups: device, board, example category/example, and example board-specific parts. For more details, see [prj.conf](../build_system/Configuration_System.md#prjconf).

When you run the following build command:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 -p
```

The following prj.conf files are included for configuration, if present:

| prj.conf                                                           | Configuration Level    | Application Scope                                 |
| ------------------------------------------------------------------ | ---------------------- | ------------------------------------------------- |
| device/prj.conf                                                    | Device                 | All examples of all devices                       |
| device/RT/prj.conf                                                 | Device                 | All the examples of all the RT devices                    |
| device/RT/RT1170/prj.conf                                          | Device                 | All the examples of all the RT1170 devices                |
| device/RT/RT1170/MIMXRT1176/prj.conf                               | Device                 | All the examples of all the RT1176 devices                |
| device/RT/RT1170/MIMXRT1176/cm7/prj.conf                           | Device                 | All the examples of all the RT1176 device cm7 cores        |
| examples/prj.conf                                                  | Example                | All the examples                                      |
| examples/_boards/prj.conf                                          | Board                  | All the examples of all the boards                        |
| examples/_boards/evkbmimxrt1170/prj.conf                           | Board                  | All the examples of the evkbmimxrt1170 board              |
| examples/_boards/evkbmimxrt1170/cm7/prj.conf                       | Board                  | All the examples of the evkbmimxrt1170 board cm7 core     |
| examples/demo_apps/prj.conf                                        | Example Category       | All the demo_apps category examples                   |
| examples/demo_apps/hello_world/prj.conf                            | Example                | hello_world example for all the boards                |
| examples/_boards/evkbmimxrt1170/demo_apps/prj.conf                 | Example Board-Specific | All the evkbmimxrt1170 demo_apps examples             |
| examples/_boards/evkbmimxrt1170/demo_apps/hello_world/prj.conf     | Example Board-Specific | evkbmimxrt1170 hello_world example for both the cores |
| examples/_boards/evkbmimxrt1170/demo_apps/hello_world/cm7/prj.conf | Example Board-Specific | evkbmimxrt1170 hello_world example for the cm7 core   |

The deeper the prj.conf file is in the directory structure, the higher its priority.

This hierarchical approach allows shared configuration for the same device, board, example category/example, and example board-specific part without duplication. It also enables customization for board examples. For instance, most boards use debug console lite by default. If your example for a specific board needs to use the full debug console, you can disable debug console lite and enable the full debug console in the example board-specific prj.conf.

For device and board configuration, the build system determines prj.conf locations from the `-b` board argument.

> The build system directly retrieves board and device folder names from board and device variable.cmake.

For example category/example prj.conf locations, the build system uses the example CMakeLists.txt root directory (e.g., `examples/demo_apps/hello_world`) from the command line. All search paths start with the keyword `examples`, such as `examples/demo_apps` and `examples/demo_apps/hello_world`.

For example board-specific prj.conf locations, the build system uses the `PROJECT_BOARD_PORT_PATH` argument in the project CMakeLists.txt:

```bash
project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH examples/_boards/${board}/demo_apps/hello_world)
```

Starting from the board name (for example, evkbmimxrt1170), all subfolder prj.conf files will be included, such as `examples/_boards/evkbmimxrt1170/demo_apps/prj.conf`, `examples/_boards/evkbmimxrt1170/demo_apps/hello_world/prj.conf`, and `examples/_boards/evkbmimxrt1170/demo_apps/hello_world/cm7/prj.conf`.

If your examples are located in a folder other than `examples` and you still want to use hierarchical configuration, place all your examples under an `examples` subfolder in your new location. For example, if you have a `middleware/<middleware>` directory for all contents including examples, your folder layout could be:

```text
middleware/<middleware>/examples
  ├── _boards
  │   ├── <board1>
  │   │   └── <example1>
  │   └── <board2>
  │       ├── <example1>
  │       └── <example2>
  ├── <example1>
  └── <example2>
```

> The example category layer is optional in this case.

#### Freestanding Examples

Freestanding example points examples located outside MCUXpresso SDK repository. Here is a typical freestanding example layout:

```
<home>/
├─── sdk_next/
│     ├─── .west/
│     │    └─── config
│     ├── mcuxsdk/
│     └── ...
│
└─── app/
     ├── CMakeLists.txt
     ├── prj.conf
     └── src/
         └── main.c
```

Freestanding examples share the same build and run way as repository examples. You can still use `west build` to work.

##### Configuration

All freestanding examples still share the default configuration of the target device, board and the full scope example configuration just as the repository example: The default prj.conf list is like:

```
1. devices/prj.conf
2. devices/<soc_series>/prj.conf
3. devices/<soc_series>/<device>/prj.conf
4. devices/<soc_series>/<device>/<core_id>/prj.conf
5. examples/prj.conf # full scope example configuration
6. examples/_boards/prj.conf
7. examples/_boards/<board>/prj.conf
8. examples/_boards/<board>/<core_id>/prj.conf
9. <example location>/prj.conf # The example itself configuration
```

If `PROJECT_BOARD_PORT_PATH` is provided inside `project` macro, a freestanding example can additionally shares the same board hierarchical configuration, then its configuration is same as the repository example except itself part.

The freestanding examples may don't need the default pin mux and hardware_init/app prj.conf setting, you can disable them in `<example location>/prj.conf`:

```
CONFIG_MCUX_PRJSEG_module.board.pinmux_project_folder=n
CONFIG_MCUX_PRJSEG_module.board.pinmux_board_folder=n
CONFIG_MCUX_HAS_PRJSEG_project.use_hw_app=n
CONFIG_MCUX_HAS_PRJSEG_module.board.pinmux_sel=n
```

##### Ways to Get MCUXpresso SDK Contents

For freestanding example, there are 2 ways to get the MCUXpresso SDK contents.

###### Explicitly include root CMakeLists.txt

The CMakeLists.txt shall explicitly include mcux.cmake to get the NXP cmake extension and include the root CMakeLists.txt to get MCUXpresso SDK contents.

```cmake
include(${SdkRootDirPath}/cmake/extension/mcux.cmake)
# No PROJECT_BOARD_PORT_PATH in project
project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH ${board_root}/${board}/<example_category>)
include(${SdkRootDirPath}/CMakeLists.txt)
```

###### Use McuxSDK CMake package

Since the MCUXpresso SDK can be exported to be a standard CMake package, so you can directly use find_package(McuxSDK) way to get MCUXpresso SDK contents:

```cmake
cmake_minimum_required(VERSION 3.30.0)
find_package(McuxSDK 24.12.00 EXACT REQUIRED)
project(hello_world LANGUAGES C CXX ASM)
```

Please refer [McuxSDK CMake Package](./integration.md#mcuxsdk-cmake-package) for details.

#### Standalone Examples

The build system provides a feature to collect and copy all the components and example self configurations and sources into an individual folder so that the example can build and run just with the stuff in the folder without depending on the mcuxsdk repository.

With this feature, it could be very convenient to zip and share examples between developers.

To build the standalone examples, an individual build system is provided in the location folder.

- For toolchains with GUI tool support like IAR/MDK/Codewarrior/Xtensa, the example files like .ewp file for IAR, .uvprojx for MDK, will be generated to use. You can directly use corresponding IDE to work.
- For toolchain without GUI tool support like Armgcc, all the examples files and configurations will be flattened into a complete CMakeLists.txt. Build target specific shell and windows cmd batch will be provided to do the build.

  > There is no Kconfig file in the standalone folder, so there is no Kconfig GUI feature in the standalone example.
  >

The standalone example can be generated with west command line parameters `-t standalone_project` like:

```bash
west build -b evkbmimxrt1170 ./examples/demo_apps/hello_world -Dcore_id=cm7 -p always --toolchain iar -t standalone_project
```

You can find IAR project is generated in build folder with all the sources. The default destination folder is "build" and can be specified by `-d` parameter.

![iar_standalone_project](../build_system/_doc/iar_standalone_project.png)

**The standalone example feature supports repository examples and freestanding examples using the explicitly include root CMakeLists.txt. Freestanding examples using McuxSDK CMake package do not have standalone example feature.**

If your example already has generated build artifacts, you can directly type `west build -t standalone_project` to generate the standalone example.

### Convert a Repository Example to a Freestanding Example

If you find one repository example functions are similar to your example and want to copy it from SDK repository into your own workspace as a freestanding example to start the development, you can use `west export_app` command to do it. Take hello_world as an example:

```bash
west export_app examples/demo_apps/hello_world -o <new workspace>/hello_world
```

Then you can get output like this:

```bash
=== Successfully create the freestanding project, see <new workspace>/hello_world/CMakeLists.txt.
=== you can use following command to build it.
west build -b <board_id> --toolchain armgcc -p always <new workspace>/hello_world -d <new workspace>/hello_world/build
```

```{note}
`--build` parameter can tell the extension build the freestanding example after convertion. It only works with explicit `board` or `core_id`.

`-Dcore_id=<core_id>` is needed for multicore board.
When use `--build` parameter, `west export_app` extension accepts other parameters passed to `west build`. So you can use `west export_app -b <board_id> examples/demo_apps/hello_world -o <new workspace>/hello_world --build --toolchain armgcc --config release `.
```

For non-sysbuild example, all files will be generated to the output directory specified by `-o`. For sysbuild, it will keep the last parent folder name in repo.

```bash
non-sysbuild example
    output_dir/
        ├── CMakeLists.txt
        └── main.c

sysbuild example
    output_dir/
        └── primary
            ├── CMakeLists.txt
            ├── main.c
            ├── sysbuild.cmake
        └── secondary
            ├── CMakeLists.txt
            ├── main.c
```

Technically, the freestanding example generated by the above command can support any board.

If you want to specify the target board, you can use `-b` argument like

```bash
west export_app -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 -o <new workspace>
```

Then you can use the following command to build

```bash
west build -b evkbmimxrt1170 --toolchain armgcc -p always <new workspace>/hello_world -d <new workspace>/hello_world/build -Dcore_id=cm7
```

```{note}
For freestanding examples exported with explicit `board` or `core_id`, you can only build it with that `board` and`core_id`.
```

#### Copy board related files

Sometimes the developer may also want to export board related files like pin_mux.c/.h, clock_config.c/.h, etc. Hence, the `export_app` extension provided an optional argument `--bf` to help developers got all board related files defined in `CONFIG_MCUX_PRJSEG_xxx`. Currently, it will scan all files in `examples` directory. With this argument, you can get a freestanding project like this:

```bash
output_dir/
    └── <board_id> or <board_id>_<core_id>
        ├── board_files.cmake (Record all copiled board related files)
        ├── board sources
        ├── prj.conf
    ├── CMakeLists.txt
    ├── Kconfig (Will forcely select promptless symbols)
    └── main.c
```

#### How Export_App extension works

`west export_app` extension uses a static cmake file parser to analyze the example's CMakeLists.txt file. It will looks up all `mcux_add_source` and `mcux_add_include` in the list file and copy the recorded source/header files to the output directory.
For sysbuild examples, `sysbuild.cmake` is also involved to get the list file or linked application.
After copying all files, the paths in the list file will be updated to that in the output directory. It will also collected all example level `prj.conf` files and combine them into one.
If user use `--bf` option, the extension will call cmake configuration step to get trace log and a final `.config` file and then analyze which project segments and files are used.
Hence, to ensure a SDK repository example can be successfully exported to a freestanding exmaple, it have to comply with following rules:

1. Record files with mcuxsdk provided cmake extensions [`mcux_add_source/mcux_add_include`](../build_system/Build_System.md#source-and-include).
2. Explicitly add example common sources in the example's `CMakeLists.txt`. Do not add them in `reconfig.cmake` or another cmake file.
3. Do not add board related files like pin mux and clock config in example's `CMakeLists.txt`.
4. Do not record duplicated source files in `reconfig.cmake`.
5. Do not record duplicated source files in `CMakelists.txt` and project segments used in the `prj.conf`.
6. For sysbuild examples, `ExternalMCUXProject_Add` is expected in the root `sysbuild.cmake` file. For board with multiple different core ids, we only allow one level `include`. That means, you can `include` another `sysbuild.cmake` file in your board folder, but you cannot `include` again in that board specific `sysbuild.cmake`. Here is an example:

    ```cmake
    mcuxsdk/examples/dsp_examples/hello_world_usart/cm/sysbuild.cmake
    include(${SdkRootDirPath}/${board_root}/${board}/dsp_examples/hello_world_usart/${core_id}/sysbuild.cmake)

    mcuxsdk/examples/_boards/mimxrt700evk/dsp_examples/hello_world_usart/cm33_core0/sysbuild.cmake
    ExternalZephyrProject_Add(
            APPLICATION hello_world_usart_hifi4
            SOURCE_DIR  ${APP_DIR}/../dsp
            board ${SB_CONFIG_dsp_board}
            core_id ${SB_CONFIG_primary_dsp_core_id}
            config ${SB_CONFIG_dsp_config}
            toolchain ${SB_CONFIG_dsp_toolchain}
    )

    ExternalMCUXProject_Add(
            APPLICATION hello_world_usart_hifi1
            SOURCE_DIR  ${APP_DIR}/../dsp
            board ${SB_CONFIG_dsp_board}
            core_id ${SB_CONFIG_secondary_dsp_core_id}
            config ${SB_CONFIG_dsp_config}
            toolchain ${SB_CONFIG_dsp_toolchain}
    )

    ExternalZephyrProject_Add(
            APPLICATION hello_world_usart_cm33_core1
            SOURCE_DIR  ${APP_DIR}/../cm_core1
            board ${SB_CONFIG_secondary_board}
            core_id ${SB_CONFIG_secondary_core_id}
            config ${SB_CONFIG_secondary_config}
            toolchain ${SB_CONFIG_secondary_toolchain}
    )

    # Let's build the hifi4 application first
    add_dependencies(hello_world_usart_cm33_core1 hello_world_usart_hifi1)

    add_dependencies(${DEFAULT_IMAGE} hello_world_usart_hifi4)

    add_dependencies(${DEFAULT_IMAGE} hello_world_usart_cm33_core1)
    ```

Additionally, the extension now supports:
- Copying extra files or folders defined in the example metadata, with `extra_files` field. This can support setting custom destination paths for those copied files.
- Applying simple replacements to update paths or values in exported files.

These enhancements make it easier to customize and adapt examples during export. For example you can define in the example.yml :

```yaml
hello_world_virtual_com:
  section-type: application
  contents:
    # hello_world_virtual_com content
    extra_files:
      - source: ${SdkRootDirPath}/examples/_boards/${board}/demo_apps/hello_world_virtual_com/reconfig.cmake
      - destination: reconfig.cmake
    replacements:
      - file: CMakeLists.txt
        replace:
          - from: "include(${SdkRootDirPath}/${board_root}/${board}/demo_apps/hello_world_virtual_com/reconfig.cmake OPTIONAL)"
            to: "include(${CMAKE_CURRENT_SOURCE_DIR}/reconfig.cmake OPTIONAL)"
```
In this example, this will:
- Copy the example's `reconfig.cmake` under the freestanding folder to be customized.
- Update the CMakeLists.txt to reflect the new path.

### Example with different build configurations

An example may have different build configuration(usually for test), see [prj.conf](../sdk/example_development.md#prjconf). It is easy for developer to add different configurations in `example.yml`to make it be visiable to `list_project` and `build` extension.
Here is an example:

```yaml
# examples/demo_apps/hello_world/example.yml+

hello_world:
  hello world content
# The example with custom configuration must end with '@config_name'
hello_world@custom1:
  section-type: custom_application # MUST BE custom_application
  contents:
    document:
      extra_build_args:
      - -DCONF_FILE=examples/demo_apps/hello_world/new.conf
  boards:
    # define your scope for this custom_application
```

```{note}
Currently, `custom_application` only support contents -> document -> extra_build_args, do not add other fields.
```

## Component Configuration in Project Construction and Build

There are following ways to do component configuration in the project construction and build

1. Use Kconfig to do configuration for the component set
2. Use the prepared customized configuration header file for the component set in the example root
3. Use the component default provided configuration header file

   ```{note}
   For a component, it must be defined in Kconfig, otherwise the component won't be involved into the build tree anyway, but it is not required that component Kconfig item must have concrete configurations. You can still put configurations like macro definitions in the header file.
   ```

To make the above ways coexist in a component set, a component set(especially middleware components) shall do the following steps:

1. Prepare a `config` component to hold the default configuration file for the component set. `config` component means the component files shall be marked with `CONFIG: TRUE`, and if the config file is a header file, the include path shall use `TARGET_FILES` to identify the file that corresponds to the path.  The `config` header file has lowest priority in the build system, if any same name header file is provided in the example root, then it won't be included. This `config` component shall be selected by the core component of the component set, then it can always be selected. So if the customized configuration is not provided for that component, the project can still build with default configuration provided by `config` component.
2. Prepare a project segment in Kconfig file to hold all Kconfig configuration symbols for the component set. All the configuration symbols shall be set to be generated into a designated header file with the same name as component default configuration file.

If you want to use Kconfig to do configuration, then the project segment shall be set to `y`. The generated configuration header name shall be set in Kconfig and be the same with component default configuration header file so that it will override the component default one. The project segment can depend on the core component of the component set so that it  can involve core component of the set.
If you don't want to use Kconfig but want to directly provide a configuration header, then project segment should be set to `n`, the directly provided configuration header shall be put in the root of project.

## Create an Example

Firstly, you should make sure that the target device and board data are ready, secondly, you need to follow the above [CMakeLists.txt](#cmakeliststxt), [Kconfig](#kconfig), [prj.conf](#prjconf) and [example.yml](#exampleyml) chapters to prepare the build and configuration files, then it should be ok.

If the default board and device data and configuration cannot satisfy your needs, then you need to do customization for the certain device or board or both.

There are following ways to do the customization.

1. Reconfig CMake

   In the example CMakeLists.txt, there is such line

   ```cmake
   include(${SdkRootDirPath}/${board_root}/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)
   ```

   This is the board port cmake. Any board specific configurations can be added in it.
2. prj.conf

   For component selection and configuration, you can use different scope prj.conf to achieve it. Refer the priority of prj.conf in [prj.conf](../build_system/Configuration_System.md#prjconf) chapter to set the data.

## Build The Example

Run `west build -h` to see help information for west build command.
Compared to zephyr's west build, MCUXpresso SDK build command provides following additional options for examples:

- `--toolchain`: specify the toolchain for this build, default armgcc.
- `--config`: value for CMAKE_BUILD_TYPE, default debug.

Here are some typical usage for generating a SDK example is:

```bash
# Build example
west build -b frdmk22f examples/demo_apps/hello_world
# multcore device must be specified with core_id
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7

# Just print cmake commands, do not execute it
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 --dry-run

# Build iar
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 --toolchain iar

# Build flexspi_nor_debug target
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 --config flexspi_nor_debug

# Switch device
west build -b frdmk22f examples/demo_apps/hello_world --device MK22F12810
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --device=MIMXRT1175 -Dcore_id=cm7 --config flexspi_nor_debug
```

For shield, please use the `--shield` to specify the shield to build, like

```bash
west build -b mimxrt700evk --shield a8974 examples examples/issdk_examples/sensors/fxls8974cf/fxls8974cf_poll -Dcore_id=cm33_core0
```

If you want to get available commands for different build config combinations supported by the example and the toolchain, you can run the command below. Please note that `@${core_id}` suffix for board is only needed for multicore devices.

```bash
west list_project -p examples/mbedtls_examples/mbedtls_selftest -b evkbmimxrt1170@cm7 -t mdk
```

Here is the output:

```bash
INFO: [   1][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config debug -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   2][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config flexspi_nor_debug -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   3][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config flexspi_nor_release -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   4][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config release -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   5][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config sdram_debug -b evkbmimxrt1170 -Dcore_id=cm7]
INFO: [   6][west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config sdram_release -b evkbmimxrt1170 -Dcore_id=cm7]
```

```{tip}
You can use `west config list_project.list_format silent_cmd` to remove useless log wrapper of the list_project output. It will directly output the build command `west build -p always examples/mbedtls_examples/mbedtls_selftest --toolchain mdk --config debug -b evkbmimxrt1170 -Dcore_id=cm7`
```

For multi-projects example build, you can build all projects by adding `--sysbuild` for main project. For example:

```bash
west build -b evkbmimxrt1170 --sysbuild ./examples/multicore_examples/hello_world/primary -Dcore_id=cm7 --config flexspi_nor_debug -p always
```

For more details, please refer to [System build](../build_system/Sysbuild.md#sysbuild).

## Flash and Debug The Example

### Flash

For an example that have been compiled successfully, use the command to flash the image:

```bash
west flash
```

To specify the build directory, use `--build-dir` (or `-d`).

### Debug

Here are the typical supported debugger servers:

1. [LinkServer](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/linkserver-for-microcontrollers:LINKERSERVER)
2. [JLink](https://www.segger.com/downloads/jlink/)

Please install LinkServer or JLink and add it to PATH environment variable firstly, then specify debug server with `-r`.
If you want to configure debug server, please refer to [Flash and Debug Data](#flash-and-debug-cmake-configuration-data).

Flash the hello_world example:

```bash
west flash -r linkserver
```

Start a gdb interface by following command:

```bash
west debug -r linkserver
```

> All of the above west commands can only be run in mcuxsdk west workspace. If you want to use them outside the workspace, please run `mcuxsdk/mcux-env.cmd` in Windows Command Prompt or `source mcuxsdk/mcux-env.sh` in Linux terminal to activate the commands.

### Flash and Debug CMake Configuration Data

MCUXpresso SDK supports to set up customized configuration for board flash runners. Such configuration is stored in `${SdkRootDirPath}/examples/_boards/<board>/board_runner.cmake`. It is loaded by `${SdkRootDirPath}/cmake/extension/run.cmake` which is used to get runner type and arguments.

Here is an example:

```cmake
# set runner speicfic arguments
board_runner_args(jlink "--device=${CONFIG_MCUX_TOOLCHAIN_JLINK_CPU_IDENTIFIER}")
board_runner_args(linkserver "--device=${CONFIG_MCUX_HW_DEVICE_ID}:MIMXRT1170-EVKB")
board_runner_args(linkserver "--core=${core_id}")

# load board supported runner cmake file
include(${SdkRootDirPath}/cmake/extension/runner/jlink.board.cmake)
include(${SdkRootDirPath}/cmake/extension/runner/linkserver.board.cmake)
```

In this example, `board_runner_args` is used to pass runner-specific arguments, runner cmake files are load from `${SdkRootDirPath}/cmake/extension/runner/` which indicates the supported runners.

**The first included runner cmake will be set as the default runner for both flash and debug**.

If you want to choose a different runner, you can set following variables in the board variable.cmake:

```cmake
mcux_set_variable(BOARD_FLASH_RUNNER "linkserver")
mcux_set_variable(BOARD_DEBUG_RUNNER "jlink")
```

To make the runner get correct flash address, the Kconfig option `FLASH_BASE_ADDRESS` shall be set correct value for each device core in `devices/${soc_portfolio}/${soc_series}/${device}/(${core_id})/prj.conf`:

```bash
CONFIG_FLASH_BASE_ADDRESS=0x30000400
```

If your example has different flash base address, please override the above value in your example specific prj.conf.

### Size Report of the generated ELF

Run `west build -t ram_report` or `west build -t rom_report`

Sample for ram size report:

```bash
Path                                                                                             Size       %  Address    Section    
==========================================================================================================================================
Root                                                                                             3264 100.00%  - 
├── (hidden)                                                                                     3107  95.19%  - 
├── (no paths)                                                                                     28   0.86%  - 
│   ├── SystemCoreClock                                                                             4   0.12%  0x20000000 .data
│   ├── s_lpuartHandle                                                                             12   0.37%  0x20000084 .bss
│   └── s_lpuartIsr                                                                                12   0.37%  0x20000090 .bss
├── /                                                                                              96   2.94%  - 
│   └── Volumes                                                                                    96   2.94%  - 
│       └── data                                                                                   96   2.94%  - 
│           └── jenkins                                                                            96   2.94%  - 
│               └── workspace                                                                      96   2.94%  - 
│                   └── GNU-toolchain                                                              96   2.94%  - 
│                       └── arm-11                                                                 96   2.94%  - 
│                           └── src                                                                96   2.94%  - 
│                               └── newlib-cygwin                                                  96   2.94%  - 
│                                   └── newlib                                                     96   2.94%  - 
│                                       └── libc                                                   96   2.94%  - 
│                                           └── reent                                              96   2.94%  - 
│                                               └── impure.c                                       96   2.94%  - 
│                                                   └── impure_data                                96   2.94%  0x20000008 .data
└── SDK_BASE                                                                                       33   1.01%  - 
    ├── components                                                                                 20   0.61%  - 
    │   └── debug_console_lite                                                                     20   0.61%  - 
    │       └── fsl_debug_console.c                                                                20   0.61%  - 
    │           └── s_debugConsole                                                                 20   0.61%  0x200000a4 .bss
    ├── devices                                                                                     4   0.12%  - 
    │   └── MCX                                                                                     4   0.12%  - 
    │       └── MCXA                                                                                4   0.12%  - 
    │           └── MCXA153                                                                         4   0.12%  - 
    │               └── drivers                                                                     4   0.12%  - 
    │                   └── fsl_clock.c                                                             4   0.12%  - 
    │                       └── s_Ext_Clk_Freq                                                      4   0.12%  0x20000004 .data
    ├── drivers                                                                                     8   0.25%  - 
    │   └── ostimer                                                                                 8   0.25%  - 
    │       └── fsl_ostimer.c                                                                       8   0.25%  - 
    │           ├── s_ostimerHandle                                                                 4   0.12%  0x2000009c .bss
    │           └── s_ostimerIsr                                                                    4   0.12%  0x200000a0 .bss
    └── examples                                                                                    1   0.03%  - 
        └── driver_examples                                                                         1   0.03%  - 
            └── ostimer                                                                             1   0.03%  - 
                └── ostimer_example.c                                                               1   0.03%  - 
                    └── matchFlag                                                                   1   0.03%  0x200000b8 .bss
==========================================================================================================================================
                                                                                                 3264
```

To get JSON RAM/ROM usage report in build directory, just run `west build -t footprint`

### Usage for Cmake Targets

To see all accessible cmake targets, run `west build -t usage`, then you can get a more readable help information

```bash
Cleaning targets:
  clean     - Remove most generated files but keep configuration and backup files
  pristine  - Remove all files in the build directory

Kconfig targets:
  menuconfig - Update .config using a console-based interface
  guiconfig  - Update .config using a graphical interface

Other generic targets:
  all          - Build a mcuxsdk application
  run          - Build a mcuxsdk application and run it if the board supports emulation
  flash        - Run "west flash"
  debug        - Run "west debug"
  ....
  other targets
```

## Project Segment

MCUXpresso SDK is composed of hundreds of devices and boards, thousands of components and ten thousands of examples. Examples on the devices and boards have many shared data like core related settings, common build target settings,  device headers and configurations, board files, clock and pin mux. Project segment data section is an abstraction of common shared project data. It is introduced to avoid data duplication.

### CMake

Like the component, in cmake files, project segment data shall be recorded inside a `if-endif` guard. The if condition shall be with prefix `CONFIG_MCUX_PRJSEG_`, right after it is the project segment name.

Here is one project segment cmake example:

```cmake
if (CONFIG_MCUX_PRJSEG_module.board.clock)  # project segment name is module.board.clock
    # project segment data
    mcux_add_source(
        BASE_PATH ${SdkRootDirPath}
        SOURCES boards/${board}/clock_config.h
                boards/${board}/clock_config.c
    )
    mcux_add_include(
        BASE_PATH ${SdkRootDirPath}
        INCLUDES boards/${board}
    )
endif()
```

### Kconfig

In Kconfig, symbol for a project segment shall start with `MCUX_PRJSEG_` to be identical with cmake project segment name. Project segment configuration and dependency shall be recorded following the below pattern:

```bash
config MCUX_PRJSEG_module.board.clock
    bool "Use default clock files"
    imply MCUX_COMPONENT_driver.clock
    if MCUX_PRJSEG_module.board.clock
    endif
```

Unlike the component dependency, the dependency for project segment is simple, just several parallel `imply` to state that the project segment depends on some components and maybe other project segment to work. Since it is frequently occuring cases that some examples on certain boards need to modify some predefined project segment dependencies, please use `imply` instead of `select` for project segment dependencies because `select` once is set to true then cannot be deselected anymore.

### Predefined Project Segments

There are already many project segments defined in mcuxsdk, here is the frequently used project segments table.

| Location         | Functionality                            |
| ---------------- | ---------------------------------------- |
| arch             | The predefined settings and configurations of different SOC architectures |
| examples/_common | Commonly shared example board modules like board file, pinmux, clock config, etc.<br />Commonly shared example board components like flash, etc. |
