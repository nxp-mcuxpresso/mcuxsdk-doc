# Build System Based on CMake

## Build Process Flow

Broadly speaking, the build process flow can be divided into Kconfig process and CMake process.

When you run a build, build system starts from the example CMakelists.txt to work:

```cmake
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)
## In mcux.cmake, build system does the following work
# 1. Load used extension modules like python.cmake, ruby.cmake, sysbuild.cmake, etc
# 2. Clean cached cmake compiler flags variable
# 3. Load toolchain.cmake
# 4. Load board variable
# 5. Load device variable
# Kconfig needs board and device variables to work. With board and device variable, cmake has the environment to start Kconfig. This execution will be done in the following "project"

project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH ${board_root}/${board}/demo_apps/hello_world)
## In this "project" macro, build system does the following work
# 6. Add execution cmake target
# 7. Add pristine cmake target
# 8. Execute Kconfig process to get .config and config headers
# 9. Process .config to get 
#  a. All used variables in cmake files so that all cmake files can be included
#  b. component and project segment if-endif guard condition value so that CMake knows whether include or skip the component or project segment
#     config headers with compiler macros inside which are in the build tree
# 10. Add run cmake target 
# 11. Add GUI generation cmake target

include(${SdkRootDirPath}/CMakeLists.txt)
# ${SdkRootDirPath}/CMakeLists.txt is the assembly point for all device/board, drivers, components, middlewares cmake data.
# After the include(${SdkRootDirPath}/CMakeLists.txt), the project has got the environment setup and all depended data included

# If needed, load other customized cmake
include(${SdkRootDirPath}/examples/demo_apps/reconfig.cmake OPTIONAL)
include(${SdkRootDirPath}/${project_board_port_path}/reconfig.cmake OPTIONAL)

# Add the project self source and include
mcux_add_source(
    SOURCES hello_world.c
)

mcux_add_include(
    INCLUDES .
)

# get board porting sources and configuration data
include(${SdkRootDirPath}/${board_root}/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)

# Convert binary to bin format
mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
```

## Toolchains Support

MCUXpresso SDK supports all mainstream toolchains in the embedded world beyond traditional armgcc.

The toolchain list supported by our build system is armgcc, iar, mdk, xtensa, codewarrior, riscvllvm and zephyr. The CMake toolchain setting files are placed in `mcuxsdk/cmake/toolchain` folder.

```
cmake
    ├── toolchain
            ├── armgcc.cmake # zephyr shares the same armgcc.cmake
            ├── codewarrior.cmake
            ├── iar.cmake
            ├── mdk.cmake
            ├── riscvllvm.cmake
            ├── xtensa.cmake
```

All toolchain files generally follow the same pattern, here is the iar.cmake:

```cmake
set(CMAKE_EXECUTABLE_SUFFIX ".elf")
set(TOOLCHAIN_ROOT $ENV{IAR_DIR})
string(REGEX REPLACE "\\\\" "/" TOOLCHAIN_ROOT "${TOOLCHAIN_ROOT}")

if(NOT TOOLCHAIN_ROOT)
    message(FATAL_ERROR "***Please set IAR_DIR in environment variables***")
endif()

SET(TARGET_TRIPLET "arm/bin")

set(AS "iasmarm")
set(CC "iccarm")
set(CXX "iccarm")
set(LD "ilinkarm")
set(AR "iarchive")
set(CPP "iccarm")
set(OC "ielftool")
set(OD "objdump")

set(AS ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${AS}${TOOLCHAIN_EXT})
set(CC ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${CC}${TOOLCHAIN_EXT})
set(CXX ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${CXX}${TOOLCHAIN_EXT})
set(LD ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${LD}${TOOLCHAIN_EXT})
set(AR ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${AR}${TOOLCHAIN_EXT})
set(CPP ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${CPP}${TOOLCHAIN_EXT})
set(OC ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${OC}${TOOLCHAIN_EXT})
set(OD ${TOOLCHAIN_ROOT}/${TARGET_TRIPLET}/${OD}${TOOLCHAIN_EXT})

set(CMAKE_ASM_COMPILER "${AS}")
set(CMAKE_C_COMPILER "${CC}")
set(CMAKE_CXX_COMPILER "${CXX}")
set(CMAKE_OBJCOPY "${OC}")
set(CMAKE_OBJDUMP "${OD}")
set(OBJDUMP_OUT_CMD "")
set(OBJDUMP_BIN_CMD "--bin")
```

The CMake variable for toolchain is `CONFIG_TOOLCHAIN`.

If you need to enable new toolchain, please follow the existing toolchain file to prepare the new one and place it in  `mcuxsdk/cmake/toolchain`.

## CMake Extension

MCUXpresso SDK is a comprehensive product including hundred of boards and devices, thousands of components and ten thousands of examples, all mainstream toolchains. The MCUXpresso CMake extensions aims to greatly reduce SDK data development and maintenance efforts.

Following extensions are provided for you to facilitate component, example and misc data record for all toolchains. All extension functions start with prefix `mcux_`

### Source and Include

#### mcux_add_source/mcux_add_include

Adding source can be done with `mcux_add_source`.

For include path, the following functions are provided:

- `mcux_add_include`

  Set include path for all source code
- `mcux_add_asm_include`

  Set include path for assembly code
- `mcux_add_c_include`

  Set include path for C code
- `mcux_add_cpp_include`

  Set include path for CPP code

Here is the argument table:

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final source path equals `BASE_PATH` + `SOURCES`. <br /> If not provided, the final source path equals `${CMAKE_CURRENT_LIST_DIR}` + `SOURCES`. <br />This is usually used in abstracted `.cmake` files which are not placed together with real sources. For sources or includes in CMakeLists.txt which are usually put together with real sources, no need to add it. |
| CONFIG        | Single        | `true` or `false`, case insensitive. <br />Specify that the source is a config file. If build system finds a file with the same name, it will replace the config file. Please note if the config file is a header file, you need to record the file in `TARGET_FILES` when adding the path for that header file with `mcux_add_include`. |
| PREINCLUDE    | Single        | `true` or `false`, case insensitive. Specify that the header is a preinclude header. This is only for `mcux_add_source`. |
| EXCLUDE       | Single        | `true` or `false`, case insensitive. Specify the source shall be excluded from build. This is only for `mcux_add_source` |
| SOURCES       | Multiple      | The sources. This is only for `mcux_add_source`. If there are multiple sources, please separate them with whitespace. |
| SCOPE         | Single        | Specify the source scope, can be INTERFACE/PUBLIC/PRIVATE. This is only for `mcux_add_source` and take same effect as target_sources scope. The default scope is PRIVATE. |
| INCLUDES      | Multiple      | The includes. This is only for `mcux_add_include`. If there are multiple includes, please separate them with whitespace. |
| TARGET_FILES  | Multiple      | This is only for `mcux_add_include`, which indicates the path is for the target header file. The base name of the file without parent folder path is accepted. Please note target header files must be added by `mcux_add_source` and marked `CONFIG TRUE`. |
| COMPILERS     | Multiple      | The compilers. It means the source or include only supports the listed compilers.<br />The supported compilers include armclang, iar, gcc, xcc, mwcc56800e, riscvllvm. |
| TOOLCHAINS    | Multiple      | The toolchains. It means the source or include only supports the listed toolchains.<br />The supported toolchains include iar, mdk, armgcc, xcc, codewarrior, riscvllvm. |
| CORES         | Multiple      | The cores. It means the source or include only supports the listed cores.<br />The supported cores include cm0, cm0p, cm3, cm4, cm4f, cm7, cm7f, cm33, cm33f, cm23, ca7, dsp56800ex, dsp56800ef, dsp, etc. |
| CORE_IDS      | Multiple      | The core_ids. It means the source or include only supports the listed core_ids. This is usually to distinguish the support for core in multicore device. |
| DEVICES       | Multiple      | The devices. It means the source or include only supports the listed device, like MIMXRT1176. |
| DEVICE_IDS    | Multiple      | The device ids. It means the source or include only supports the listed device id, like MIMXRT1176xxxxx. |
| FPU           | Multiple      | The fpu. It means the source or include only supports the listed fpu. fpu enum values are  NO_FPU,  SP_FPU and  DP_FPU. |
| DSP           | Multiple      | The dsp. It means the source or include only supports the listed dsp. dsp enum values are NO_DSP and HAS_DSP. |
| TRUSTZONE     | Multiple      | The trustzone, enum values are TZ and  NO_TZ. TZ means the source or include are only enabled on device with SAU, NO_TZ means they are only enabled on device without SAU. |
| COMPONENTS    | Multiple      | The components. It means the source or include only supports the listed components. |

Wildcard `*.<extension>` and `**` is supported in `mcux_add_source`, frequently used ones are `*.*`, `*.c` and `*.h`. 

`**` will add alll kinds of files in all sub folders recursively into build.

If the number of files is relatively small, it is not recommended to use wildcards because it is implicit and time-consumed in build.

Here is one example:

```cmake
# In drivers/uart/CMakelists.txt
if(CONFIG_MCUX_COMPONENT_driver.uart)
    # with wildcard, it can be this way
    mcux_add_source(
        SOURCES *.*
    )
    mcux_add_include(
        INCLUDES .
    )
endif()
```

#### mcux_add_codewarrior_sys_include

Add header files search path for codewarrior system libraries.

| Argument Name        | Argument Type | Explanation                              |
| -------------------- | ------------- | ---------------------------------------- |
| TARGETS              | Multiple      | The build targets, like debug release    |
| SYS_SEARCH_PATH      | Multiple      | The path to be searched for header files |
| SYS_PATH_RECURSIVELY | Multiple      | The path and all the subdirectories to be searched recursively for header files |

Here is one example

```cmake
mcux_add_codewarrior_sys_include(
    SYS_SEARCH_PATH 
    "\"${MCUToolsBaseDir}/DSP56800x_EABI_Tools/M56800E Support/runtime_56800E/include\""
    "\"${MCUToolsBaseDir}/DSP56800x_EABI_Tools/M56800E Support/msl/MSL_C/MSL_Common/Include\""
    "\"${MCUToolsBaseDir}/DSP56800x_EABI_Tools/M56800E Support/msl/MSL_C/DSP_56800E/prefix\""
    SYS_PATH_RECURSIVELY 
    "\"${MCUToolsBaseDir}/DSP56800x_EABI_Tools/M56800E Support\""
)
```

#### mcux_add_library

Specify the library to be linked.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final library path equals `BASE_PATH` + `LIB`s.<br />If not provided, the final library path equals `${CMAKE_CURRENT_LIST_DIR}` + `LIBS`. <br />This is usually used in abstracted `.cmake` files which are not placed together with real libraries. For CMakeLists.txt which is usually put together with real libraries, no need to add it. |
| LIBS          | Multiple      | The libraries to be added                |
| SCOPE         | Single        | Specify the library scope, can be INTERFACE/PUBLIC/PRIVATE. This is only for `mcux_add_library` and take same effect as target_link_libraries scope. The default scope is PRIVATE. |
| TOOLCHAINS    | Multiple      | The toolchains. It means the library only supports the listed toolchains.<br />The supported toolchains include iar, mdk, armgcc, xcc, codewarrior. |
| CORES         | Multiple      | The cores. It means the library only supports the listed cores.<br />The supported cores include cm0, cm0p, cm3, cm4, cm4f, cm7, cm7f, cm33, cm33f, cm23, ca7, dsp56800ex, dsp56800ef, dsp. |
| CORE_IDS      | Multiple      | The core_ids. It means the library only supports the listed core_ids. This is usually to distinguish the support for core in multicore device. |
| DEVICES       | Multiple      | The devices. It means the library only supports the listed device, like MIMXRT1176. |
| DEVICE_IDS    | Multiple      | The device ids. It means the library only supports the listed device id, like MIMXRT1176xxxxx. |
| FPU           | Multiple      | The fpu. It means the library only supports the listed fpu. fpu enum values are  NO_FPU,  SP_FPU and  DP_FPU. |
| DSP           | Multiple      | The dsp. It means the library only supports the listed dsp. dsp enum values are NO_DSP and HAS_DSP |
| TRUSTZONE     | Multiple      | The trustzone, enum values are TZ and  NO_TZ. TZ means the libraries are only enabled on device with SAU, NO_TZ means they are only enabled on device without SAU. |
| COMPONENTS    | Multiple      | The components. It means the library only supports the listed components. |
| GENERATED     | Single        | `TRUE` or `FALSE`<br />Specify the library is generated by other project. This is necessary for KEX package. |
| EXCLUDE       | Single        | `TRUE` or `FALSE`<br />Specify the library is exclude from linking. |
| HIDDEN        | Single        | `TRUE` or `FALSE`<br />Specify the library is hidden from GUI project. |
| TARGETS       | Multiple      | Specify the library is for designated build configuration targets. |

Here is one example:

```cmake
mcux_add_library(
    LIBS lib/kw45b41/kw45b41_nbu_libthreadx.a
    TOOLCHAINS iar
)
```

The library can also be added by `mcux_add_configuration`. However it requires the absolute path and does not support source level dependency condition. Therefore, `mcux_add_library` is preferred for library adding.

#### mcux_convert_binary

Specify the output binary format

| Argument Name | Argument Type | Explanation                   |
| ------------- | ------------- | ----------------------------- |
| TOOLCHAINS    | Multiple      | Supported toolchains          |
| BINARY        | Single        | The target output binary type |

Here is one example:

```cmake
mcux_convert_binary(
    TOOLCHAINS armgcc mdk iar
    BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin
)
```

#### mcux_add_iar_linker_script/mcux_add_mdk_linker_script/mcux_add_armgcc_linker_script/mcux_add_codewarrior_linker_script/mcux_add_riscvllvm_linker_script

Add linker for toolchain.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | The build targets, like debug release.   |
| BASE_PATH     | Single        | If provided, the final linker path equals `BASE_PATH` + `LINKER`. This is usually used in abstracted .cmake files which are not placed together with real linker. |
| LINKER        | Single        | The linker path                          |

Here is one example

```cmake
mcux_add_iar_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/iar/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.icf
)

mcux_add_armgcc_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/gcc/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.ld
)

mcux_add_mdk_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/arm/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.scf
)
```

Please remember to set `TARGETS` for the linker, otherwise the linker will be enabled for all targets.

### MACRO

#### mcux_add_macro

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets. |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains. |
| AS            | Single        | The assemble compiler macros.            |
| CC            | Single        | The c compiler macros.                   |
| CX            | Single        | The cxx compiler macros.                 |

**Note**:

1. `mcux_add_macro` automatically prefixes the macros that do not have the `-D` prefix and duplicated macros will be removed

   Here is one example

   ```cmake
   mcux_add_macro(
       CC "FOO -DFOO -DBAR=1" # Equals -DFOO -DBAR=1
   )
   ```
2. For all macros added by `mcux_add_configuration` or `mcux_add_macro`, if there are the duplicated macro names without value, like `-DA -DA`, or with the same value, like `-DC=3 -DC=3`, only one macro will be kept. If there are duplicated macro name with different values, build system will use the last one.
3. If you want to set macro for assembler, c compiler and cpp compiler at the same time, there is an easy way to omit AS/CC/CX parameters:

   ```cmake
   mcux_add_macro(
      "-DFOO -DBAR=1"
   )
   ```
4. If the vaule of macro contains quotation marks, please use the escape symbol for them, for example:

   ```cmake
   mcux_add_macro(
       CC "-DMBEDTLS_CONFIG_FILE=\\\"ksdk_mbedtls_config.h\\\""
   )
   ```

#### mcux_add_linker_symbol

The CMake function `mcux_add_configuration` requires the complete toolchain setting. For linker macro setting, you have to add prefix for linker symbol. The prefix may be different for each linker. For example, `--config_def=` for iar, `--predefine=` for mdk. To be convenient to set linker symbol for all toolchains, `mcux_add_linker_symbol` is provided.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets. |
| SYMBOLS       | Multiple      | The linker symbols.                      |

For example:

```cmake
mcux_add_linker_symbol(
    SYMBOLS gUseNVMLink_d=1
           gEraseNVMLink_d=1
           _ram_vector_table_=1
           gFlashNbuImage_d=1
           gUseProdInfoLegacyMode_d=1
)
```

For compatibility, it's also supported to wrap all symbols in double quotes.

### Configuration

#### mcux_add_configuration

Add configuration for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| LIB           | Multiple      | The library, the full path               |
| AS            | Single        | The assemble compiler flag               |
| CC            | Single        | The c compiler flags                     |
| CX            | Single        | The cxx compiler flags                   |
| LD            | Single        | The linker flags                         |

Please use native compiler flags of the compilers.

Here is one example

```cmake
mcux_add_configuration(
    TARGETS release
    TOOLCHAINS IAR
    AS "-M\"<>\" -w+ -s -j"
    CC "--diag_suppress=Pa082,Pa050 --endian=little -e --use_c++_inline --silent"
    CX "--diag_suppress=Pa082,Pa050 --endian=little -e --c++ --silent"
)
```

#### mcux_add_iar_configuration\mcux_add_mdk_configuration\mcux_add_armgcc_configuration\mcux_add_xcc_configuration\mcux_add_codewarrior_configuration

Very similar with `mcux_add_configuration`, just for specified toolchain.

### Pre/Post Build Command

#### mcux_add_custom_command

CMake provides built-in function `add_custom_command` which is useful for performing an operation before or after building the target by setting `PRE_BUILD` | `PRE_LINK` | `POST_BUILD` parameters. For more details, please refer to [add_custom_command](https://cmake.org/cmake/help/latest/command/add_custom_command.html#add-custom-command). Based on this function, build system provides customized CMake function `mcux_add_custom_command` to set pre/post build command for specific targets and toolchains.

It shall only be used in the project CMakelists.txt, not the component one.

| Argument Name     | Argument Type | Explanation                              |
| ----------------- | ------------- | ---------------------------------------- |
| TARGETS           | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS        | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| BUILD_EVENT       | Single        | Specify the time when the command is executed, can be `PRE_COMPILE`/`PRE_BUILD`/`PRE_LINK`/`POST_BUILD`. The default setting is `POST_BUILD` |
| BUILD_COMMAND     | Multiple      | Specify the command-line(s) to execute. The format is same as CMake built-in function `add_custom_command`, do not wrap the command with double quotes |
| BYPRODUCTS        | Multiple      | Specify the files to be generated by command. It can be omitted if the directory of the generated files exist. |
| WORKING_DIRECTORY | Single        | Specify the working directory to execute the command. The default directory is `${CMAKE_BINARY_DIR}`. |

Here is one example:

```cmake
mcux_add_custom_command(
    TARGETS debug release
    TOOLCHAINS armgcc
    BUILD_EVENT  PRE_BUILD
    BUILD_COMMAND ${TOOLCHAIN_DIR}/bin/arm-none-eabi-gcc -E -P -xc -I${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/target/nxp/evkmimxrt685/partition -I${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common ${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common/gcc/tfm_common_ns.ld -o ${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common/gcc/tfm_common_ns_pre.ld
)
```

According to [add_custom_command](https://cmake.org/cmake/help/latest/command/add_custom_command.html), for Ninja and Make generator, the `PRE_BUILD` behaves the same as `PRE_LINK`. Therefore, If you want to create files which is used for compilation, build system has provided a specific build event parameter `PRE_COMPILE` to simplify and unify custom command setting, for example:

```cmake
mcux_add_custom_command(
    BUILD_EVENT PRE_COMPILE
    BUILD_COMMAND 
    sh ../middleware/wireless/zigbee/tools/ZPSConfig/Source/ZPSConfig
    -n coordinator
    -e LITTLE_ENDIAN
    -t JN518x
    -l ../middleware/wireless/zigbee/platform/K32W1/libs/libZPSNWK.a
    -a ../middleware/wireless/zigbee/platform/K32W1/libs/libZPSAPL.a
    -f ../middleware/wireless/zigbee/examples/zigbee_coordinator/src/coordinator.zpscfg
    -o ../middleware/wireless/zigbee/examples/zigbee_coordinator/src/
    BYPRODUCTS
    ../middleware/wireless/zigbee/examples/zigbee_coordinator/src/zps_gen.c
    ../middleware/wireless/zigbee/examples/zigbee_coordinator/src/zps_gen.h
)
```

### Remove

Besides adding data, the build system also supports removing defined data. For example, if in a common definition, a macro is defined for examples in the board, but your example shall not use it, then you can use following remove function to remove it.

#### mcux_remove_configuration

Remove configuration for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| LIB           | Multiple      | The full path of the library             |
| AS            | Single        | The assemble compiler flags              |
| CC            | Single        | The c compiler flags                     |
| CX            | Single        | The cxx compiler flags                   |
| LD            | Single        | The linker flags                         |

Please use native compiler flags of the compilers.

Here is one example:

```cmake
mcux_remove_configuration(
    TARGETS release
    AS "-DMCUXPRESSO_SDK -DNDEBUG"
    CC "-DMCUXPRESSO_SDK -DNDEBUG"
    CX "-DMCUXPRESSO_SDK -DNDEBUG"
)
```

#### mcux_remove_iar_configuration/mcux_remove_mdk_configuration/mcux_remove_armgcc_configuration

Very similar with `mcux_remove_configuration`, just for specified toolchain.

#### mcux_remove_macro

Remove macros for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| AS            | Single        | The assemble compiler macros             |
| CC            | Single        | The c compiler macros                    |
| CX            | Single        | The cxx compiler macros                  |

`mcux_remove_macro` automatically prefixes macros that do not have the `-D` prefix
Here is one example:

```cmake
mcux_remove_macro(CC "TESTMACRO")
```

#### mcux_remove_linker_symbol

Remove linker symbol for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| SYMBOLS       | Single        | The linker symbols to be removed         |

Here is one example:

```cmake
mcux_remove_linker_symbol(
    SYMBOLS "gFlashNbuImage_d=1"
)
```

#### mcux_remove_iar_linker_script/mcux_remove_mdk_linker_script/mcux_remove_armgcc_linker_script/mcux_remove_codewarrior_linker_script

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | The build targets, like debug release    |
| BASE_PATH     | Single        | If provided, the final linker path equals `BASE_PATH` + `LINKER`. This is usually used in abstracted .cmake files which are not placed together with real linker. |
| LINKER        | Single        | The linker path                          |

Here is one example:

```cmake
mcux_remove_iar_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/iar/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.icf
)

mcux_remove_armgcc_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/gcc/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.ld
)

mcux_remove_mdk_linker_script(
    TARGETS debug release
    BASE_PATH ${SdkRootDirPath}
    LINKER devices/${soc_portfolio}/${soc_series}/${device}/arm/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.scf
)
```

#### mcux_project_remove_include\mcux_project_remove_source

Remove project source or include.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final source path equals `BASE_PATH` + `SOURCES`. This is usually used in abstracted .cmake files which are not placed together with real sources. For sources or includes in CMakeLists.txt which is usually put together with real source, no need to add it. |
| INCLUDES      | Multiple      | The include path.                        |
| SOURCES       | Multiple      | The source path.                         |

Here is one example:

```cmake
mcux_project_remove_source(
    SOURCES hello_world.c
)

mcux_project_remove_include(
    INCLUDES .
)
```

#### mcux_remove_library

Remove libraries. It will take effect no matter the library was added before or after this statement.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final source path equals `BASE_PATH` + `LIBS`. Otherwise the actual path is relative to `${CMAKE_CURRENT_LIST_DIR}` |
| LIBS          | Multiple      | The library files to be removed          |

Here is one example:

```cmake
mcux_remove_library(
    BASE_PATH ${SdkRootDirPath}
    SOURCES devices/${soc_portfolio}/${soc_series}/${device}/iar/iar_lib_power.a
)
```

### Misc

#### mcux_set_variable

Set variable with **global scope**. It requests that variable defined by `mcux_set_variable` must be unique. Build system will report error if there are duplicated variables defined with `mcux_set_variable`.

Here is one example:

```cmake
mcux_set_variable(soc_series Kinetis)
```

#### mcux_set_list

Set a cmake list.

Here is one example

```cmake
mcux_set_list(KW47_FAMILY "KW47B42Z83xxxA KW47B42Z96xxxA KW47B42Z97xxxA KW47B42ZB2xxxA KW47B42ZB3xxxA KW47B42ZB6xxxA KW47B42ZB7xxxA KW47Z42082xxxA KW47Z42092xxxA KW47Z420B2xxxA KW47Z420B3xxxA")
```

#### mcux_add_cmakelists

Add CMakelists.txt

Here is one example:

```cmake
mcux_add_cmakelists(${CMAKE_CURRENT_LIST_DIR}/drivers)
```

#### mcux_load_all_cmakelists_in_directory

Load all cmakelists under one directory

```cmake
mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)
```
