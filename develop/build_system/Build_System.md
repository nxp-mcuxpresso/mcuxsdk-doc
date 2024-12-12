# Build System Based on CMake

## Overview

MCUXpresso SDK build and configuration system is based on CMake and Kconfig.

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) is a selection-based configuration system originally developed for the Linux kernel which now found more and more use in other projects beyond the Linux kernel. In MCUXpresso SDK, Kconfig is used to config the build in run time which includes component selection with dependency resolve, component configuration with feature enable, disable and customization.

You can interact with Kconfig via a curses or graphical menu interface, usually invoked by running `west build -t guiconfig` after you have already run passed the CMake configuration process. In this interface, the user selects the options and features desired, and saves a configuration file, which is then used as an input to the
build process.

[CMake](https://cmake.org/) which is cross platform not only manages the software build process based on Kconfig result.

Beyond traditional CMake generation, MCUXpresso build system also integrates some useful functionalities like IDE project generation.


## Build and Configuration Process Flow

Broadly speaking, the build process flow can be divide into Kconfig process and CMake process.

When you run a build, BS start from the example CMakelists.txt to work:

```cmake
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)
## In this mcux.cmake, BS does the following work
# 1. Load used extension modules like python.cmake, sysbuild.cmake
# 2. Clean cached cmake compiler flags variable
# 3. Load toolchain.cmake
# 4. Load board variable
# 5. Load device variable
# With board and device variable, cmake has the environment to start Kconfig because Kconfig needs board and device variables to work. This execution will be done in following "project"

project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH examples/_boards/${board}/demo_apps/hello_world/${multicore_foldername})
## In this "project" macro, BS continuously does the following work
# 6. Add execution cmake target
# 7. Add pristine cmake target
# 8. Execute Kconfig process to get .config and config headers
# 9. Process .config to get 
#  a. All variables used in CMakes so that all cmakes can be included
#  b. component and project segment if-endif guard condition value so that cmake knows whether include or skip the component or project segment
#  config headers with compiler macros inside which are in the build tree
# 10. Add run cmake target 
# 11. Add GUI generation cmake target

include(${SdkRootDirPath}/CMakeLists.txt)
# ${SdkRootDirPath}/CMakeLists.txt is the assembly point for all board/device, drivers, components,  middlewares cmake data.
# Here is its contents
# # Load device CMakeLists.txt
# mcux_add_cmakelists(${SdkRootDirPath}/devices/${soc_portfolio}/${soc_series}/${device})
# Load board CMakeLists.txt
# mcux_add_cmakelists(${SdkRootDirPath}/boards/${board})
# Load all drivers
# mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)
# all components
# mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/components)
# CMSIS
# mcux_add_cmakelists(${SdkRootDirPath}/CMSIS)
# middlewares
# mcux_add_cmakelists(${SdkRootDirPath}/rtos/freertos/freertos-kernel OPTIONAL)
# mcux_add_cmakelists(${SdkRootDirPath}/middleware/fatfs OPTIONAL)
# mcux_add_cmakelists(${SdkRootDirPath}/middleware/multicore OPTIONAL)
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
```

## Toolchains Support

MCUXpresso SDK supports all mainstream toolchains in the embedded world beyond traditional armgcc.

The toolchain list supported by our build system is armgcc, iar, mdk, xtensa and zephyr. The CMake toolchain setting files are placed in `mcu-sdk-3.0/cmake/toolchain` folder. All toolchain files generally follow the same structure and loaded through `mcu-sdk-3.0/cmake/<toolchain>.cmake`. The CMake variable for toolchain is `CONFIG_TOOLCHAIN` which is used to cmdline to specify the toolchain to build.

If you need to enable new toolchain, please follow the existing toolchain file pattern and place it there.


## CMake Extension

MCUXpresso SDK is a comprehensive product including hundred of boards and devices, thousands of components and ten thousands of examples, all mainstream toolchains. The MCUXpresso CMake extensions aims to greatly reduce build data development and maintenance efforts.

Following extensions are provided for you to facilitate component, project and misc data record for all toolchains. All extension functions start with prefix `mcux_`

### Source And Include

#### mcux_add_source/mcux_add_include

Add the source can be done with `mcux_add_source`.

For include path, the following functions are provided:

- `mcux_add_include`

  Set include path for all source code
- `mcux_add_asm_include`

  Set include path for assembly code

- `mcux_add_c_include`

  Set include path for C code

- `mcux_add_cpp_include`

  Set include path for CPP code

Please see following table for the arguments

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final source path equals `BASE_PATH` + `SOURCES`.  If not provided, the final source path equals `${CMAKE_CURRENT_LIST_DIR}` + `SOURCES`. This is usually used in abstracted `.cmake` files which are not placed together with real sources. For sources or includes in CMakeLists.txt which is usually put together with real source, no need to add it. |
| CONFIG        | Single        | `true` or `false`, case insensitive. Specify that the source is a config file. If build system finds a file with the same name, it can replace the config file. Please note if the config file is a header file, you need to record the file in `TARGET_FILES` when adding the path for that header file with `mcux_add_include`. |
| PREINCLUDE    | Single        | `true` or `false`, case insensitive. Specify that the header is a preinclude header. This is only for mcux_add_source. |
| EXCLUDE       | Single        | `true` or `false`, case insensitive. Specify the source shall be excluded from build. This is only for mcux_add_source |
| SOURCES       | Multiple      | The sources. This is only for `mcux_add_source`. If there are multiple sources, please separate them with whitespace. |
| SCOPE         | Single        | Specify the source scope, can be INTERFACE/PUBLIC/PRIVATE. This is only for mcux_add_source and take same effect as target_sources scope. The default scope is PRIVATE if not set. |
| INCLUDES      | Multiple      | The includes. This is only for `mcux_add_include`. If there are multiple includes, please separate them with whitespace. |
| TARGET_FILES  | Multiple      | This is only for `mcux_add_include`, which indicates the path is for the target header file. The base name of the file without parent folder path is accepted. Please note target header files must be added by `mcux_add_source` and marked `CONFIG TRUE`. |
| COMPILERS     | Multiple      | The compilers. It means the source or include only supports the listed compilers.`<br>`Here are all the supported compilers: armclang, iar, gcc, xcc, mwcc56800e, riscvllvm. |
| TOOLCHAINS    | Multiple      | The toolchains. It means the source or include only supports the listed toolchains.`<br>`Here are all the supported toolchains: iar, mdk, armgcc, xcc, codewarrior, riscvllvm. |
| CORES         | Multiple      | The cores. It means the source or include only supports the listed cores.`<br>`Here are all the supported cores: cm0, cm0p, cm3, cm4, cm4f, cm7, cm7f, cm33, cm33f, cm23, ca7, dsp56800ex, dsp56800ef, dsp |
| CORE_IDS      | Multiple      | The core_ids. It means the source or include only supports the listed core_ids. This is usually to distinguish support for core in multicore platform. |
| DEVICES       | Multiple      | The devices. It means the source or include only supports the listed device, like MK64F12. |
| DEVICE_IDS    | Multiple      | The device ids. It means the source or include only supports the listed device id, like MK64FN1M0xxx12. |
| FPU           | Multiple      | The fpu. It means the source or include only supports the listed fpu. fpu enum values are  NO_FPU,  SP_FPU and  DP_FPU. |
| DSP           | Multiple      | The dsp. It means the source or include only supports the listed dsp. dsp enum values are NO_DSP and HAS_DSP |
| TRUSTZONE     | Multiple      | The trustzone. It means the source or include only supports the listed trustzone. trustzone enum values are TZ and  NO_TZ. |
| COMPONENTS    | Multiple      | The components. It means the source or include only supports the listed components |

Wildcard "\*.\<extension>" is supported in mcux\_add_source, frequently used would be "\*.*", "\*.c" and "\*.h".

If the number of files is relatively small, it is not recommended to use wildcards because it is implicit and time consumed.

Here is one example:

```cmake
# In drivers/uart/CMakelists.txt
if (CONFIG_MCUX_COMPONENT_driver.uart)
    mcux_add_source(
        SOURCES fsl_uart.h 
                fsl_uart.c
    )
    # with wildcard, it can be this way
    # mcux_add_source(
    # SOURCES *.*
    # )
    mcux_add_include(
        INCLUDES .
    )
endif()

# In examples/demo_apps/hello_world/CMakelists.txt
mcux_add_source(
    SOURCES hello_world.c
)

mcux_add_include(
    INCLUDES .
)
```

#### mcux_add_library

Specify the library to be linked.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final library path equals `BASE_PATH` + `LIB`. This is usually used in abstracted `.cmake` files which are not placed together with real library. For library in CMakeLists.txt which is usually put together with real library, no need to add it. |
| LIBS          | Multiple      | The libraries to be added                |
| SCOPE         | Single        | Specify the library scope, can be INTERFACE/PUBLIC/PRIVATE. This is only for mcux_add_library and take same effect as target_link_libraries scope. The default scope is PRIVATE if not set. |
| TOOLCHAINS    | Multiple      | The toolchains. It means the library only supports the listed toolchains.`<br>`Here are all the supported toolchains: iar, mdk, armgcc, xcc, codewarrior. |
| CORES         | Multiple      | The cores. It means the library only supports the listed cores.`<br>`Here are all the supported cores: cm0, cm0p, cm3, cm4, cm4f, cm7, cm7f, cm33, cm33f, cm23, ca7, dsp56800ex, dsp56800ef, dsp |
| CORE_IDS      | Multiple      | The core_ids. It means the library only supports the listed core_ids. This is usually to distinguish support for core in multicore platform. |
| DEVICES       | Multiple      | The devices. It means the library only supports the listed device, like MK64F12. |
| DEVICE_IDS    | Multiple      | The device ids. It means the library only supports the listed device id, like MK64FN1M0xxx12. |
| FPU           | Multiple      | The fpu. It means the library only supports the listed fpu. fpu enum values are  NO_FPU,  SP_FPU and  DP_FPU. |
| DSP           | Multiple      | The dsp. It means the library only supports the listed dsp. dsp enum values are NO_DSP and HAS_DSP |
| TRUSTZONE     | Multiple      | The trustzone. It means the library only supports the listed trustzone. trustzone enum values are TZ and  NO_TZ. |
| COMPONENTS    | Multiple      | The components. It means the library only supports the listed components |
| GENERATED     | Single        | Mark the library is generated by other project, should be TRUE or FALSE. This is necessary for KEX package |
| EXCLUDE       | Single        | Mark the library is exclude from linking, should be TRUE or FALSE. |
| HIDDEN        | Single        | Mark the library is hidden from GUI project, should be TRUE or FALSE. |
| TARGETS       | Multiple      | Mark the library is for designated build configuration targets. |

Here is one example

```cmake
    mcux_add_library(
        LIBS lib/kw45b41/kw45b41_nbu_libthreadx.a
        TOOLCHAINS iar
    )
```

Note, the library can be also added by mcux_add_configuration, however, it requires the absolute path and does not support file scope or dependency condition. Therefore, mcux_add_library is preferred.

#### mcux_convert_binary

Specify the Output binary format

| Argument Name | Argument Type | Explanation                   |
| ------------- | ------------- | ----------------------------- |
| TOOLCHAINS    | Multiple      | Supported toolchains          |
| BINARY        | Single        | The target output binary type |

Here is one example

```cmake
mcux_convert_binary(
        TOOLCHAINS armgcc mdk iar
        BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin
)
```

#### mcux_add_iar_linker_script/mcux_add_mdk_linker_script/mcux_add_armgcc_linker_script

Add linker for toolchain.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | The build targets, like debug release    |
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

Please remember to set "TARGETS" for the linker, otherwise the linker will be enabled for all targets.

### MACRO

#### mcux_add_macro

It is recommended to use `mcux_add_macro` to set macros.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| AS            | Single        | The assemble compiler macros             |
| CC            | Single        | The c compiler macros                    |
| CX            | Single        | The cxx compiler macros                  |

Note:

1. mcux_add_macro automatically prefixes macros that do not have the -D prefix, duplicated macros will be removed

   Here is one example

    ```cmake
    mcux_add_macro(
      CC "FOO -DFOO -D BAR=1" # Equals -DFOO -DBAR=1
    )
    ```

2. For all macros added by mcux_add_configuration or mcux_add_macro, the duplicated macro name without value, like -DA -DA, or with same value, like -DC=3 -DC=3, only one macro will be kept. If found duplicated macro name with different value, use the latest one. You can also get notice from log.

3. If you want to set macro for assembler, c compiler and cpp compiler at the same time, you can set them three times. Or there is an easy way to omit AS/CC/CX parameters. Here is an example:

   ```cmake
   mcux_add_macro(
     "-DFOO -DBAR=1"
   )
   ```

4. If the vaule of macro contains quotation marks, please use the escape symbol for them. For example:
    ```cmake
      mcux_add_macro(
          CC "-DMBEDTLS_CONFIG_FILE=\\\"ksdk_mbedtls_config.h\\\""
      )
    ```

#### mcux_add_linker_symbol

The CMake function mcux_add_configuration requires the complete toolchain setting. For linker macro setting, you have to add prefix for linker symbol. The prefix may be different for each linker. For example, `--config_def=` for iar, `--predefine=` for mdk. To be convenient for developer to set linker symbol once time for all toolchains, ``mcux_add_linker_symbol` is provided.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| SYMBOLS       | Multiple      | The linker symbols                       |

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
Note: For compatibility, it's also supported to wrap all symbols in double quotes.

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

Note, please use native compiler flags of the compilers.

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

#### mcux_add_iar_configuration\mcux_add_mdk_configuration\mcux_add_armgcc_configuration\mcux_add_xcc_configuration

Very similar with mcux_add_configuration, just target specified toolchain, not for all.

### Pre/Post Build Command

#### mcux_add_custom_command

CMake provide built-in function `add_custom_command`, this is useful for performing an operation before or after building the target by setting PRE_BUILD | PRE_LINK | POST_BUILD parameters. For more details, please refer to [CMake document]([add_custom_command — CMake 3.30.3 Documentation](https://cmake.org/cmake/help/latest/command/add_custom_command.html#add-custom-command)). It shall only be used in the project CMakelists.txt,  not the component one. Based on this function, meta build system provide customized CMake function mcux_add_custom_command to set pre/post build command for specific targets and toolchains.

| Argument Name     | Argument Type | Explanation                              |
| ----------------- | ------------- | ---------------------------------------- |
| TARGETS           | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS        | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| BUILD_EVENT       | Single        | Set the time when the command is executed, can be PRE_COMPILE/PRE_BUILD/PRE_LINK /POST_BUILD. If not provided, the default setting is POST_BUILD |
| BUILD_COMMAND     | Multiple      | Specify the command-line(s) to execute. The format is same as CMake built-in function add_custom_command, do not wrap the command with double quotes |
| BYPRODUCTS        | Multiple      | Specify the files to be generated by command. It can be omitted if the directory of  the generated files exist. |
| WORKING_DIRECTORY | Single        | Specify the working directory to execute the command. The default directory is  ${CMAKE_BINARY_DIR} if not set. |

Here is one example

```cmake
mcux_add_custom_command(
        TARGETS debug release
        TOOLCHAINS armgcc
        BUILD_EVENT  PRE_BUILD
        BUILD_COMMAND ${TOOLCHAIN_DIR}/bin/arm-none-eabi-gcc -E -P -xc -I${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/target/nxp/evkmimxrt685/partition -I${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common ${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common/gcc/tfm_common_ns.ld -o ${SdkRootDirPath}/middleware/tfm/tf-m/platform/ext/common/gcc/tfm_common_ns_pre.ld
)
```

Note: According to [add_custom_command — CMake 3.30.0 Documentation](https://cmake.org/cmake/help/latest/command/add_custom_command.html) , for Ninja and Make generator, the PRE_BUILD behaves the same as PRE_LINK. Therefore, If you want to create files which is used for compilation, meta build system has provided a specific build event parameter "PRE_COMPILE" to simplify and unify custom command setting. For example:

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

You will see the log:
```
-- west build: building application
[1/23] Pre-compile command: sh ../middleware/wireless/zigbee/tools/...g -o ../middleware/wireless/zigbee/examples/zigbee_coordinator/src 
```


### Remove

Besides adding data, the build system also supports removing defined data. For example, if in a common definition, a macro is defined for examples in the board, but your example cannot use it, then you can use following remove function to remove it.

#### mcux_remove_configuration

Remove configuration for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| LIB           | Multiple      | The library, the full path               |
| AS            | Single        | The assemble compiler flag               |
| CC            | Single        | The c compiler flags                     |
| CX            | Single        | The cxx compiler flags                   |
| LD            | Single        | The linker flags                         |

Note, please use native compiler flags of the compilers.

Here is one example

```cmake
mcux_remove_configuration(
        TARGETS release
        AS "-DMCUXPRESSO_SDK -DNDEBUG"
        CC "-DMCUXPRESSO_SDK -DNDEBUG"
        CX "-DMCUXPRESSO_SDK -DNDEBUG"
)
```

#### mcux_remove_iar_configuration/mcux_remove_mdk_configuration/mcux_remove_armgcc_configuration

Very similar with mcux_remove_configuration, just target specified toolchain, not for all.

#### mcux_remove_macro

Remove macros for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all targets |
| TOOLCHAINS    | Multiple      | Supported toolchains. If not provided, then supporting all toolchains |
| AS            | Single        | The assemble compiler macros             |
| CC            | Single        | The c compiler macros                    |
| CX            | Single        | The cxx compiler macros                  |

Note, mcux_remove_macro automatically prefixes macros that do not have the -D prefix
Here is one example

```cmake
mcux_remove_macro(CC "TESTMACRO")
```

#### mcux_remove_linker_symbol

Remove linker symbol for all toolchains with specified build targets.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | Supported build targets. If not provided, then supporting all target |
| SYMBOLS       | Single        | The linker symbols to be removed         |

Here is one example

```cmake
mcux_remove_linker_symbol(
    SYMBOLS "gFlashNbuImage_d=1"
)
```

#### mcux_remove_iar_linker_script/mcux_remove_mdk_linker_script/mcux_remove_armgcc_linker_script/mcux_remove_codewarrior_linker_script

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| TARGETS       | Multiple      | The build targets, like debug release    |
| BASE_PATH     | Single        | If provided, the final linker path equals BASE_PATH + LINKER. This is usually used in abstracted .cmake files which are not placed together with real linker. |
| LINKER        | Single        | The linker path                          |

Here is one example

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

Here is one example

```cmake
mcux_project_remove_source(
  SOURCES hello_world.c
)

mcux_project_remove_include(
  INCLUDES .
)
```

#### mcux_remove_library

Remove libraries. Whether the file was added before or after this statement, it will take effect.

| Argument Name | Argument Type | Explanation                              |
| ------------- | ------------- | ---------------------------------------- |
| BASE_PATH     | Single        | If provided, the final source path equals `BASE_PATH` + `LIBS`. Otherwise the actual path is relative to ${CMAKE_CURRENT_LIST_DIR} |
| LIBS          | Multiple      | The library files to be removed          |

Here is one example

```cmake
mcux_remove_library(
  BASE_PATH ${SdkRootDirPath}
  SOURCES devices/${soc_portfolio}/${soc_series}/${device}/iar/iar_lib_power.a
)
```

### Misc

#### mcux_set_variable

Set variable with **global scope**. It requests that variable defined by mcux_set_variable must be unique. Build system will give error if there are duplication variable defined with "mcux_set_variable".

Here is one example

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

Here is one example

```cmake
mcux_add_cmakelists(${SdkRootDirPath}/devices/Kinetis/MK64F12/drivers)
```

#### mcux_load_all_cmakelists_in_directory

Load all cmakelists under one directory

```cmake
mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)
```






## McuxSDK CMake Package

MCUXpresso SDK repo contents can be used as a standard McuxSDK [CMake package](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html) . The McuxSDK CMake package is a convenient way to create a SDK next repo based freestanding example. It ensures that CMake can automatically find the MCUXpresso SDK repo and use the contents to build the example.

There are 2 ways to use the McuxSDK CMake package:

1. Export the MCUXpresso SDK repo to system standard CMake User Package Registry and directly use `find_package(McuxSDK)`.

   Here is the table about the standard CMake user package registry in different OSes.

   | OS      | CMake user package registry              |
   | ------- | ---------------------------------------- |
   | Windows | HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\McuxSDK |
   | Ubuntu  | ~/.cmake/packages/McuxSDK                |
   | MacOS   | ~/.cmake/packages/McuxSDK                |

   There are 2 ways to export MCUXpresso SDK repo.

   1. You can use west cmd `west mcuxsdk-export` to export.
   2. You can directly use cmake cmd `cmake -P <sdk repo root>/share/mcuxsdk-package/cmake/mcuxsdk_export.cmake`  to export.

2. Directly add the MCUXpresso SDK repo root as `HINT` for `find_package(McuxSDK HINT <repo root>)`

### Create Example With "find_package(McuxSDK)"

When using McuxSDK CMake package, you just simply needs to write `find_package(McuxSDK)` in the beginning of the application `CMakeLists.txt` file, then build system will get all needed drivers, components and middlewares for designated devices and boards and build them into a static library called `McuxSDK`.  This `McuxSDK` has been linked to target "app" in advance, you only need to add the example specific sources/include/configuration. 

Here is an example:

```cmake
cmake_minimum_required(VERSION 3.30.0)
find_package(Mcuxsdk REQUIRED)
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
```

If you use native cmake target_ function with target `app`, then the sources/includes/configurations are added for target `app`. If you use NXP cmake extension to add sources/includes/configurations, then the data and files are added into target `McuxSDK`, a static library, which will be linked to `app` finally.

If there is no special instruction, the app target will use default provided linker by MCUXpresso SDK if it is an executable. If you want to use your own linker, then please add "CUSTOM_LINKER TRUE" in the "project" like 

```cmake
project(hello_world LANGUAGES C CXX ASM CUSTOM_LINKER TRUE)
```

then add your own  linker.

### McuxSDK CMake Package Version

`find_package(McuxSDK)` supports to specify MCUXpresso SDK version number in `x.y.z` format which is very useful as it ensures the example is built with a minimal MCUXpresso SDK version. An explicit version also helps CMake to select the correct MCUXpresso SDK to use for building when there are multiple MCUXpresso SDK repos in the system.

Here is an example with version:

```cmake
find_package(McuxSDK 3.0.0)
project(hello_world)
```

This requires hello_world project to be built with MCUXpresso SDK version 3.0.0 as minimum.

`find_package` supports the keyword `EXACT` to ensure an exact version is used. 

```cmake
find_package(McuxSDK 3.0.0 EXACT)
project(hello_world)
```
