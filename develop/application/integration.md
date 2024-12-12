# MCUXSDK Integration

## Integrated Into Other Build System

### Import as CMake package

If you want to integrate the mcuxsdk to your project by CMake find_package feature, please refer [McuxSDK CMake Package](#McuxSDK-CMake-Package).

### Import manually

The mcuxsdk can also be integrated by adding CMake file manually. You need to load `${SdkRootDirPath}/cmake/extension/mcux.cmake` before project declaration, and load `${SdkRootDirPath}/CMakeLists.txt` after project declaration. For example:

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

Furthermore, If you encounter an error like below with west build command, possible reason is the project is added to other project by `add_subdirectory`, that's the limitation from west, please skip the sanity check by adding west parameter `-nsc` or `--no_sanity_check`
  ```bash
  Build directory <A> is for application <B>, but source directory <C> was specified; please clean it, use --pristine, or use --build-dir to set another build directory
  ```

**Note**: Currently GUI project and standalone project generation are not supported for other build system which uses McuxSDK CMake Package.

## Integrate Other CMake build system

The meta build system is based on CMake, theoretically, it supports the integration of other third-party software based on the CMake compilation system.

There are two ways for this requirement:

1. If the third-party software will be built as a library and linked to the project from meta build system, you can add the software path to CMake variable "EXTRA_MCUX_MODULES". The The directory of the path will be regarded as module's name. You need to create a folder named `mcux` in this path, and  prepare files below:

    - module.yml

      module.yml must be put into `mcux` folder. It records the relative path of CMakeLists.txt and Kconfig file. Note that the base path is the path form EXTRA_MCUX_MODULES. For example:

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

      At least one Kconfig item `MCUX_COMPONENT_`${module_name} should be recorded to help enable/disable the third-party software from building. For example:

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

   The software will use assembler/compiler/linker flags provided by meta build system, you can also set specific options for the third-party software in `PRIVATE` scope. If the module is a library project, meta build system can link the library automatically.

   **Note**: Due to the loading sequence of CMake, the compilation settings in reconfig.cmake are not available, so if necessary, you need to set them yourself in cmakelists.txt of the module.

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