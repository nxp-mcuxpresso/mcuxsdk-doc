# Application Development

## Example Types

In MCUXpresso SDK, based on whether supporting the hierarchical configuration for board porting, we can distinguish 2 types examples: repository and freestanding examples.

| Example Type | Support hierarchical configuration for board porting | CMakeLists.txt Location                  |
| ------------ | ---------------------------------------- | ---------------------------------------- |
| Repository   | Yes                                      | Under sdk-root/examples sdk-root/examples_int |
| freestanding | No                                       | No restriction.                          |

### Repository Example

Repository example CMakelists.txt is located inside `mcu-sdk-3.0/examples/<example-category>/<example>`or `mcu-sdk-3.0/examples_int/<example-category>/<example>` folder, like the hello_world CMakelists.txt is located in `mcu-sdk-3.0/examples/demo_apps/hello_world`.

```
sdk_next/
├─── .west/
│    └─── config
└─── mcu-sdk-3.0/
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
```

#### Hierarchical Configuration For Board Porting

For MCUXpresso SDK officially supported boards, the board porting are done for all board supported examples in a hierarchical way. In any repository example CMakeLists.txt "project" macro, the "PROJECT_BOARD_PORT_PATH" is provided to specify the root board porting path. All the prj.conf files inside each sub folder of PROJECT_BOARD_PORT_PATH will be processed during the example build, they are hierarchically configuring the example in different levels.

Take evkmimxrt1170 hello_world porting for example, in the hello_world CMakeLists.txt, we have "PROJECT_BOARD_PORT_PATH" as "examples/_boards/${board}/demo_apps/hello_world" as the following:

```cmake
project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH examples/_boards/${board}/demo_apps/hello_world)
```

So following prj.conf files are taken into examples to do different level configurations.

| prj.conf                                 | Application scope of configuration       |
| ---------------------------------------- | ---------------------------------------- |
| examples/prj.conf                        | Apply for all examples                   |
| examples/\_boards/prj.conf               | Apply for all NXP official boards examples |
| examples/\_boards/evkmimxrt1170/prj.conf | Apply for all evkmimxrt1170 examples     |
| examples/\_boards/evkmimxrt1170/demo_apps/prj.conf | Apply for all evkmimxrt1170 demo apps examples |
| examples/\_boards/evkmimxrt1170/demo_apps/hello_world/prj.conf | Apply for evkmimxrt1170 hello_world examples |

The deeper path of prj.conf, the higher priority it has. You can refer the chapter [prj.conf.](#Kconfig-Process-Flow).

Note, such hierarchical configuration must be specified with "PROJECT_BOARD_PORT_PATH" and only supports examples under "examples" folder, that is the standard repository example.

### Freestanding Example

Unlike standard repository examples, freestanding examples don't support hierarchical configuration for board porting, so there is no "PROJECT_BOARD_PORT_PATH" in "project" macro and there is no location restriction for freestanding example which means it can be placed anywhere.

- Inside mcu-sdk-3.0 repo

  ```yaml
  sdk_next/
  ├─── .west/
  │    └─── config
  └─── mcu-sdk-3.0/
       ├── arch/
       ├── cmake/
       ├── <any folder>/
       │   ├── hello_world
       │       ├── CMakeLists.txt
       │       ├── Kconfig
       │       ├── prj.conf
       │       ├── hello_world.c
  ```
- Outside mcu-sdk-3.0 repo

  ```
  <home>/
  ├─── sdk_next/
  │     ├─── .west/
  │     │    └─── config
  │     ├── mcu-sdk-3.0/
  │     └── ...
  │
  └─── app/
       ├── CMakeLists.txt
       ├── prj.conf
       └── src/
           └── main.c
  ```

Freestanding examples share the same build and run way as repository examples. You can still use `west build` to work.

#### Configuration

All freestanding examples still share the default configuration of the target board and device and the full scope example configuration.

The default prj.conf list is like

```yaml
1. devices/prj.conf
2. devices/<soc_series>/prj.conf
3. devices/<soc_series>/<device>/prj.conf
4. devices/<soc_series>/<device>/<core_id>/prj.conf
5. examples/prj.conf
6. examples/_boards/prj.conf
7. examples/_boards/<board>/prj.conf
8. examples/_boards/<board>/<core_id>/prj.conf
9. <example location>/prj.conf # The example itself configuration
```

Note, the freestanding project may don't need the default pin mux and hardware_init/app prj.conf setting, you can disable them by

```
CONFIG_MCUX_PRJSEG_module.board.pinmux_project_folder=n
CONFIG_MCUX_PRJSEG_module.board.pinmux_board_folder=n
CONFIG_MCUX_HAS_PRJSEG_project.use_hw_app=n
CONFIG_MCUX_HAS_PRJSEG_module.board.pinmux_sel=n
```

#### Ways To Get MCUXpresso SDK Contents

For freestanding project, there are 2 ways to get the MCUXpresso SDK contents.

##### Explicitly include root CMakeLists.txt

The CMakeLists.txt shall explicitly include mcux.cmake to get the NXP cmake extension and include the root CMakeLists.txt to get MCUXpresso SDK contents.

```cmake
include(${SdkRootDirPath}/cmake/extension/mcux.cmake)
# No PROJECT_BOARD_PORT_PATH in project
project(hello_world LANGUAGES C CXX ASM)
include(${SdkRootDirPath}/CMakeLists.txt)
```

##### Use McuxSDK CMake package

Since the MCUXpresso SDK can be export to be a standard CMake package, so you can directly use find_package(McuxSDK) way to get MCUXpresso SDK contents:

```cmake
cmake_minimum_required(VERSION 3.30.0)
find_package(McuxSDK 24.12.00 EXACT REQUIRED)
project(hello_world LANGUAGES C CXX ASM)
```

Please refer [McuxSDK CMake Package](#McuxSDK-CMake-Package) for details.

### Standalone Example

The build system provides a feature to collect and copy all the components, project segments and example self configurations and sources into an individual folder so that the example can build and run just with the stuff in the folder without depending on the sources, configurations and the build system inside the west repos.

With this feature, it could be very convenient to zip and share examples between customers and developers.

To build the standalone examples, an individual build system is provided in the location folder.

- For toolchains with GUI tool support like IAR/MDK/Codewarrior/Xtensa, the project files, like .ewp file for IAR, .uvprojx for MDK, will be generated to use. Developers and customers can directly use corresponding IDE to work.


- For toolchain without GUI tool support like Armgcc, all the examples files and configurations will be flattened into a complete CMakeLists.txt. Build target specific shell and windows cmd batch will be provided to do the build.

  **There is no Kconfig file in the standalone folder, so there is no Kconfig GUI feature in the standalone example.**

The standalone project can be generated with west command line parameters "-t standalone_project". For example:

```bash
west build -b frdmk64f ./examples/demo_apps/hello_world -p always --config debug --toolchain iar -t standalone_project
```

You can find IAR project in build folder with source code.

![iar_standalone_project](./_doc/iar_standalone_project.png)

Note:

1. **The standalone project supports repository examples and freestanding examples using the explicitly include root CMakeLists.txt. Freestanding examples using McuxSDK CMake package do not have standalone project feature.**
2. The default destination folder is mcu-sdk-3.0/build/${toolchain}. You can also specify the destination folder with command line parameter "-d" .
3. You can only create a project for a specific toolchain and config in one CMake configuration context. You should remove CMake build folder or run with "-p always" if changing toolchain or config
4. If the CMake has generated build artifacts, you can directly type "west build -t standalone_project" to generate.

## Convert A Repository Example To A Freestanding Example

If you find one repository example functions are similar to your project and want to copy it from SDK repository into your own workspace as an freestanding example to start the development, here are the steps with evkbmimxrt1170 hello_world as an example:

1. Copy hello_world specific sources and cmakes into your workspace folder: `SDK-root/examples/demo_apps/hello_world/*` =>  `<new workspace>/hello_world/*`

2. Update CMakeLists.txt: adjust paths and remove the "PROJECT_BOARD_PORT_PATH" from "project" macro.

    - If using explicitly include SDK root CMakeList.txt way, then the CMakeLists.txt is

      ```cmake
      cmake_minimum_required(VERSION 3.30.0)
      include(${SdkRootDirPath}/cmake/extension/mcux.cmake)
      # No PROJECT_BOARD_PORT_PATH in project
      project(hello_world LANGUAGES C CXX ASM)
      include(${SdkRootDirPath}/CMakeLists.txt)
      mcux_add_source(
          SOURCES hello_world.c
              pin_mux.c
              hardware_init.c
      )
      mcux_add_include(
          INCLUDES .
      )
      include(${SdkRootDirPath}/examples/_boards/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)
      mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
      ```

      For `include(${SdkRootDirPath}/examples/_boards/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)`, it is board specific reconfiguration cmake, you can move it to your workspace or keep it in the SDK-root. If you move it to your workspace, please also move the related sources inside it and update the path accordingly

    - If using the McuxSDK CMake package way, then the CMakeLists.txt is

      ```cmake
       cmake_minimum_required(VERSION 3.30.0)
       find_package(McuxSDK 3.0.0 EXACT REQUIRED)
       project(hello_world LANGUAGES C CXX ASM)
       mcux_add_source(
        SOURCES
          hello_world.c
          pin_mux.c
          pin_mux.h
          hardware_init.c
          app.h
       )
       mcux_add_include(
        INCLUDES
          .
       )
       include(${SdkRootDirPath}/examples/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)
       mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
      ```


3. Update Kconfig

   If your example has its specific Kconfig, then adjust the "source" path and  "project_board_port_path"

   The "project_board_port_path" can be updated with true value like `"examples/_boards/evkbmimxrt1170/demo_apps/hello_world"`. Here is the updated Kconfig:

   ```
   # It is optional to provide example specific Kconfig.
   mainmenu "Hello World"

   # Need to refer the root Kconfig.mcuxpreso to get all Kconfig data
   source "${SdkRootDirPath}/Kconfig.mcuxpresso"

   # Board example specific Kconfig can be linked in this way if needed
   osource "${SdkRootDirPath}/examples/_boards/evkbmimxrt1170/demo_apps/hello_world/Kconfig"

   ```

   For `${SdkRootDirPath}/examples/_boards/evkbmimxrt1170/demo_apps/hello_world/Kconfig`, you can move it to your workspace or keep it there in SDK repo.


4. Collect extra prj.conf

   For a freestanding example, no matter using explicitly include root CMakeLists.txt or using McuxSDK CMake package way, the default configuration for device, board and general-Mcuxpresso-SDK-example are anyway involved. Here is the prj.conf table

   ```yaml
   1. devices/prj.conf
   2. devices/<soc_series>/prj.conf
   3. devices/<soc_series>/<device>/prj.conf
   4. devices/<soc_series>/<device>/<core_id>/prj.conf
   5. examples/prj.conf
   6. examples/_boards/prj.conf
   7. examples/_boards/<board>/prj.conf
   8. examples/_boards/<board>/<core_id>/prj.conf
   ###### The example itself configuration
   9. <example location>/prj.conf
   ```

   For a repository example, it has extra category example configurations and  board porting configurations in the corresponding prj.conf:

   ```yaml
   1. devices/prj.conf
   2. devices/<soc_series>/prj.conf
   3. devices/<soc_series>/<device>/prj.conf
   4. devices/<soc_series>/<device>/<core_id>/prj.conf
   5. examples/prj.conf
   6. examples/_boards/prj.conf
   7. examples/_boards/<board>/prj.conf
   8. examples/_boards/<board>/<core_id>/prj.conf
   ###### category example configurations and  board porting configurations
   9. examples/<example_category>/prj.conf
   10. examples/<example_category>/<example>/prj.conf
   11. examples/_boards/<board>/<example_category>/prj.conf
   12. examples/_boards/<board>/<example_category>/<example>/prj.conf
   13. examples/_boards/<board>/<example_category>/<example>/<core_id>/prj.conf

   ```

   When converting a repository example to freestanding example, the 9-13 prj.conf of repository example shall be collected and merged into the freestanding 9 prj.conf

5. Run the example

   There 2 ways to run the example:

    1. Using west:

       ```bash
       west build -b evkbmimxrt1170 <new workspace>/hello_world -Dcore_id=cm7 --toolchain=iar
       ```

       Please run west cmd inside SDK-root. If you want to run west from your workspace, you can run `SDK-root/mcux-env.cmd` or `SDK-root/mcux-env.sh` to set up the environment variable otherwise west cannot find SDK-root.

    2. Using native cmake cmd in your workspace:

       ```bash
       cmake -S <new workspace>/hello_world -B build -G Ninja -Dboard=evkbmimxrt1170 -Dcore_id=cm7 -DCMAKE_BUILD_TYPE=debug -DCONFIG_TOOLCHAIN=iar -DSdkRootDirPath=SDK-root
       ```

       The "-S" specify the example folder containing CMakeLists.txt.

       The "-Dboard=evkbmimxrt1170" specify the target board, equal with "-b evkbmimxrt1170" in west cmd.

       The "-Dcore_id=cm7" specify the core id of multicore device.

       The "-B build" specify the binary output directory is "build". In west cmd, "build" folder is the default binary output folder.

       The "-G Ninja" specify the cmake generator is Ninja. In west cmd, Ninja is the default selected generator.

       The "-DCMAKE_BUILD_TYPE=debug" specify the build target is "debug". In west cmd, "debug" is the default build target.

       The "-DCONFIG_TOOLCHAIN=iar" specify the toolchain is iar, equal with "--toolchain=iar" in west cmd.

       The "-DSdkRootDirPath=SDK-root" specify the SDK root location. In west cmd, build system will automatically get the SDK root.

       After, you can cd into "build" and run "ninja"

## Enable An Example

Please firstly make sure that the target board and device data are ready, then follow the example CMakelists.txt pattern in [Project](#project) chapter and make your own one.

If the default board and device data and configuration cannot satisfy, then you need to do customization for the certain board or device or both.

BCS provides following ways to do the customization.

1. Reconfig CMake

   For example, the hello_world example CMakelists.txt is defined in "examples/demo_apps/hello_world". Inside it, there are 2 optional included reconfig.cmake, like

   ```cmake
   include(${SdkRootDirPath}/examples/demo_apps/reconfig.cmake OPTIONAL)
   # project_board_port_path here means examples/_boards/frdmk64f/demo_apps/hello_world
   include(${SdkRootDirPath}/${project_board_port_path}/reconfig.cmake OPTIONAL)
   ```

   You can add reconfig.cmake in any sub folder of the above 2 optional cmake path to different level reconfig.cmake and remember to include it recursively in deeper level cmake.

   For example, if you add a examples/_boards/frdmk64f/demo_apps/reconfig.cmake, then you should be awared of that this reconfig.cmake shall apply for all demo_apps in frdmk64f.

   In these reconfig.cmake, [remove](#remove) extensions can be used to remove board/device common data and settings. After removing the previous data and settings, customization data and settings can be added.
2. prj.conf

   For component selection and configuration, you can use different level prj.conf to achieve it. Refer the priority level in [prj.conf](#prj-conf) to set the data.

Remember to register the example in example.yml so that build system, CI and IDE will know that the examples are enabled in certain boards.

Here is one example:

```yaml
# in examples/_boards/frdmk64f/example.yml

hello_world:
  required: true
```

## Component Configuration In Project Construction

There are following ways to do component configuration in the project construction and build

1. Use the provided default configuration header of the component set
2. Use Kconfig to do RTE configuration for the component set
3. Prepare customized configuration header for the component set.

To achieve the above way, a component set(especially middleware components) shall do the following steps:

1. Prepare a "config" component to hold the default configuration file for the component set. The configuration file shall be marked with CONFIG: TRUE and the include shall be with "TARGET_FILES".  The "config" header file has lowest priority in the build system, if any same name header file is provided, then it won't be included. This "config" component shall be selected by the root component of the component set, then it can always be selected. So if the customized configuration is not provided for that component, the project can still build with default configuration.


2. Prepare a project segment to hold all Kconfig configuration symbols for the component set. All the configuration symbols shall be set to generated into designated header file with the same name as component default configuration.

If you want to use Kconfig to do RTE configuration, then the project segment shall be set to 'y'. The generated configuration header name shall be set in Kconfig and be the same with component default configuration head file so that it will override the component default one. The project segment can depend on the root component of the component set so that it  can involve root component of the set.
If you don't want to use Kconfig but want to directly provide a configuration header, then project segment should be set to 'n', the directly provided configuration header shall be put in the root of project.