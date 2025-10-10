# MCUXpresso SDK Integration

## McuxSDK CMake Package

MCUXpresso SDK can be used as a standard McuxSDK [CMake package](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html) . It ensures that CMake can automatically find the MCUXpresso SDK and use it to build the example.

There are 2 ways to use the McuxSDK CMake package:

1. Export the MCUXpresso SDK to system standard CMake user package registry and directly use `find_package(McuxSDK)`.

   Here is the table about the standard CMake user package registry in different OSes.

   | OS      | CMake user package registry                               |
   | ------- | --------------------------------------------------------- |
   | Windows | HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\McuxSDK |
   | Linux   | ~/.cmake/packages/McuxSDK                                 |
   | MacOS   | ~/.cmake/packages/McuxSDK                                 |

   There are 2 ways to export MCUXpresso SDK repo.


   1. You can use west cmd `west mcuxsdk-export` to export.
   2. You can directly use cmake cmd `cmake -P <sdk repo root>/share/mcuxsdk-package/cmake/mcuxsdk_export.cmake`  to export.
2. Directly add the MCUXpresso SDK root as `HINT` for `find_package(McuxSDK HINT <repo root>)`

### Create Example With `find_package(McuxSDK)`

When using McuxSDK CMake package, you just simply needs to write `find_package(McuxSDK)`  at the beginning of the application `CMakeLists.txt` file, then build system will get all needed drivers, components and middlewares for designated devices and boards and build them into a static library called `McuxSDK`.  This `McuxSDK` has been linked to target `app` in advance, you only need to add the example specific sources/include/configuration.

Here is an example:

```cmake
cmake_minimum_required(VERSION 3.30.0)
find_package(McuxSDK 25.12.00 EXACT REQUIRED)
project(hello_world LANGUAGES C CXX ASM)
mcux_add_source(
  SOURCES   
    hello_world.c
    hardware_init.c
    app.h
)
mcux_add_include(
  INCLUDES 
    .
)
```

If you use native cmake `target_` function with target `app`, then the sources/includes/configurations are added for target `app`. If you use NXP cmake extension to add sources/includes/configurations, then the data and files are added into target `McuxSDK`, a static library, which will be linked to `app` finally.

If there is no special instruction, the app target will use default provided linker script by MCUXpresso SDK if it is an executable. If it doesn't satisfy your needs, then please add `CUSTOM_LINKER TRUE` in the `project` like the following and then add your own linker script.

```cmake
project(hello_world LANGUAGES C CXX ASM CUSTOM_LINKER TRUE)
```

There is no `PROJECT_BOARD_PORT_PATH` support in this `find_package(McuxSDK)`way which means you need to provide your own board port files, typically `hardware_init.c` and `app.h`, and disable the original ones in prj.conf. So the example dedicated prj.conf will have following lines:

```
CONFIG_MCUX_HAS_PRJSEG_project.use_hw_app=n
CONFIG_MCUX_PRJSEG_project.hw_app_project_folder=n
CONFIG_MCUX_PRJSEG_module.board.pinmux_board_folder=y
```

The `CONFIG_MCUX_PRJSEG_module.board.pinmux_board_folder=y` guarantee that the example is using board level pin_mux because default enabled is pin_mux located in project root.

We provide a frdmmcxa346 hello_world `find_package(McuxSDK)` [example](../../_static/build_system/McuxSDK_CMake_package_freestanding_example.zip) for reference.

for reference.

### McuxSDK CMake Package Version

`find_package(McuxSDK)` supports to specify MCUXpresso SDK version number in `x.y.z` format which is very useful as it ensures the example is built with a minimal MCUXpresso SDK version. An explicit version also helps CMake to select the correct MCUXpresso SDK to use for building when there are multiple MCUXpresso SDK repositories in the system.

Here is an example with version:

```cmake
find_package(McuxSDK 25.12.00)
project(hello_world)
```

This requires hello_world project to be built with MCUXpresso SDK version 25.12.00 as minimum.

`find_package` supports the keyword `EXACT` to ensure an exact version is used.

```cmake
find_package(McuxSDK 25.12.00 EXACT)
project(hello_world)
```

## Integrated Into Other Build System

### Import as CMake package

If you want to integrate the MCUXpresso SDK to your project by CMake find_package feature, please refer the above  [McuxSDK CMake Package](#mcuxsdk-cmake-package).

### Import manually

The MCUXpresso SDK can also be integrated by adding cmake file manually. You need to load `${SdkRootDirPath}/cmake/extension/mcux.cmake` before project declaration, and load `${SdkRootDirPath}/CMakeLists.txt` after project declaration. For example:

```cmake
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

project(hello_world LANGUAGES C CXX ASM)

include(${SdkRootDirPath}/CMakeLists.txt)

mcux_add_source(
  SOURCES   
    hello_world.c
    pin_mux.c
    pin_mux.h
    hardware_init.c
    app.h
)

mcux_add_include(
  INCLUDES .
)
```

### Build the project

There are 2 ways to build the project:

1. With cmake command

```bash
  cmake -B ./build -G Ninja -Dboard=<board> -DCONF_FILE=<Absolute path to project folder>/prj.conf -DCMAKE_BUILD_TYPE=debug -DCONFIG_TOOLCHAIN=armgcc

  ninja -C build
```

2. With west command

```bash
  west build -b <board> <Absolute/relative path to project folder> -DCONF_FILE=<Absolute path to project folder>/prj.conf --config=debug --toolchain=armgcc
```

Furthermore, if you encounter an error like below with west build command, one possible reason is the project is added to other project by `add_subdirectory`, that's the limitation from west, please skip the sanity check by adding west parameter `-nsc` or `--no_sanity_check`

```bash
Build directory <A> is for application <B>, but source directory <C> was specified; please clean it, use --pristine, or use --build-dir to set another build directory
```

> Currently GUI project and standalone project generation are not supported for other build system which uses McuxSDK CMake Package.

## Integrate Other CMake Build System

The MCUXpresso SDK build system is based on CMake, so theoretically, it supports the integration of other third-party software based on the CMake compilation system.

There are two ways for this requirement:

1. If the third-party software needs to be built as a library and linked to the project from MCUXpresso SDK build system, you can add the software path to cmake variable `EXTRA_MCUX_MODULES`. The directory of the path will be treated as the module's name. You need to create a folder named `mcux` in this path, and prepare files below:

   - module.yml

     module.yml must be put into `mcux` folder. It records the relative path of CMakeLists.txt and Kconfig file. Note that the base path is the path form `EXTRA_MCUX_MODULES`. For example:

     ```yaml
     name: zcbor #optional, must be set only if module folder name is different with module name
     build:
       # if the base path is ~/zcbor
       cmake: mcux/.             #full path ~/zcobr/mcux/CMakeLists.txt
       kconfig: mcux/Kconfig     #full path ~/zcobr/mcux/Kconfig
       depends:                 # optional, dependent module will be included into the build system and be processed before current module.
         - <module>
     ```
   - Kconfig

     At least one Kconfig item `MCUX_COMPONENT_${module_name}` should be recorded to help enable/disable the third-party software from building. For example:

     ```
     config MCUX_COMPONENT_ZCBOR
         bool "zcbor CBOR library"
         help
           zcbor CBOR encoder/decoder library

     if MCUX_COMPONENT_ZCBOR

     config ZCBOR_CANONICAL
         bool "Produce canonical CBOR"
         help
           Enabling this will prevent zcbor from creating lists and maps with
           indefinite-length arrays (it will still decode them properly).
     endif # MCUX_COMPONENT_ZCBOR  
     ```
   - CMakeLists.txt

     All content should be wrapped by `if(CONFIG_MCUX_COMPONENT_${module_name}) ... endif()`. Then we can enable/disable the third-party software according to kconfig setting. There is no strict format for CMakeLists.txt. The module project will be linked to application code automatically by build system if it is a static library.

     For example:

     ```cmake
     cmake_minimum_required(VERSION 3.20.0)

     if(CONFIG_MCUX_COMPONENT_ZCBOR)
         add_library(zcbor) # declare a zcbor library 

         target_sources(zcbor PRIVATE # add files to zcbor library
                 ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_common.c
                 ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_decode.c
                 ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_encode.c
         )

         target_include_directories(zcbor PUBLIC # add include path to zcbor library
                 ${MCUX_ZCBOR_MODULE_DIR}/include
         )

         target_compile_definitions(zcbor PUBLIC _POSIX_C_SOURCE=200809L) # add macro to zcbor library and the targets which links this library

         if(CONFIG_ZCBOR_CANONICAL)
             target_compile_definitions(zcbor PRIVATE ZCBOR_CANONICAL) # # add macro only for zcbor library 
         endif ()

     endif()
     ```

The software will use assembler/compiler/linker flags provided by MCUXpresso SDK build system, you can also set specific options for the third-party software in `PRIVATE` scope. If the module is a library project, MCUXpresso SDK build system can link the library automatically.

> Due to the loading sequence of cmake files, the compilation settings in reconfig.cmake are not available, so if necessary, you need to set them yourself in CMakeLists.txt of the module.

2. If the other software is a standalone project which has separated configuration, it can be imported by sysbuild.

   For example, you can provide a sysbuild.cmake:

   ```cmake
   ExternalMCUXProject_Add(
           APPLICATION my_library
           SOURCE_DIR  path/to/my_library
           CMAKE_ARGS -DCMAKE_BUILD_TYPE=debug -DCMAKE_TOOLCHAIN_FILE=path/to/toolchain.cmake
   )

   # Let's build the secondary application first
   add_dependencies(${DEFAULT_IMAGE} my_library)
   ```
