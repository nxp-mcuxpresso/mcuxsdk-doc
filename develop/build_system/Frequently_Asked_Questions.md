# Frequently Asked Questions

## CMake

1. How to get detailed cmake configuration log about from which cmake files the include/source/configuration is added.

   You can use `--log-level=debug` to get detailed steps of cmake adding source/include/configuration. A cmd example is like

   ```bash
   west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm4 --log-level=debug
   ```

   The logs look like

   ![cmake_debug_log](./_doc/cmake_debug_log.PNG)

2. How to replace the default linker file with the customized one?

   Generally, when you type `--config=<CMAKE_BUILD_TYPE>` in the command line, the cmake settings inside `mcuxsdk/arch/arm/target` folder will take effect. The link file for the corresponding config is then used.
   If running with "--log-level=debug" in the command line, you can find the log, such as:
   ```text
   -- DEBUG: Add -T C:/git_repo/migrate_sdk_repo/mcuxsdk/devices/Kinetis/MK64F12/gcc/MK64FN1M0xxx12_flash.ld to LD flags, load from CMakefile: C:/git_repo/migrate_sdk_repo/mcuxsdk/arch/arm/target/flash.cmake
   ```

   To replace the default linker file with the customized one, you need to remove the default linker file and add the customized one by `mcux_remove_<toolchain>_linker_script` and `mcux_add_<toolchain>_linker_script` in reconfig.cmake.
   For example:
   ```cmake
   # mcuxsdk/examples/frdmk64f/demo_apps/hello_world/reconfig.cmake
   mcux_remove_armgcc_linker_script(
       TARGETS debug release
       BASE_PATH ${SdkRootDirPath}
       LINKER devices/${soc_portfolio}/${soc_series}/${device}/gcc/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.ld
   )

   mcux_add_armgcc_linker_script(
       TARGETS debug release
       BASE_PATH ${SdkRootDirPath}
       LINKER examples/frdmk64f/demo_apps/hello_world/hello_world_flash.ld
   )
   ```
   If running with "--log-level=debug", you can find the log:
   ```text
   -- DEBUG: Add linker flag -T C:/git_repo/migrate_sdk_repo/mcuxsdk/devices/Kinetis/MK64F12/gcc/MK64FN1M0xxx12_flash.ld into TO_BE_REMOVED_FLAGS list, load from CMakefile: 1171
   -- DEBUG: Remove linker flag -T C:/git_repo/migrate_sdk_repo/mcuxsdk/devices/Kinetis/MK64F12/gcc/MK64FN1M0xxx12_flash.ld, load from CMakefile: 1182
   -- DEBUG: Add -T C:/git_repo/migrate_sdk_repo/mcuxsdk/examples/frdmk64f/demo_apps/hello_world/hello_world_flash.ld to LD flags, load from CMakefile: C:/git_repo/migrate_sdk_repo/mcuxsdk/examples/frdmk64f/demo_apps/hello_world/reconfig.cmake
   ```

## Kconfig

1. How are the Kconfig symbols(configurations) handled and integrated into the build?

   1. All Kconfig symbols will first be generated into .config with Kconfig process lib. We do some updates on the Kconfig process lib to meet our needs

   2. Macro Symbols starting with `MCUX_` are used by cmake to determine which components/drivers/project_segments are included in a build.

   3. Macro Symbols are generated into config header files

        3.1 In the Kconfig menu, if the header is specified, like menu **freertos-kernel(FreeRTOSConfig.h)**, then all symbols under this menu are generated into *FreeRTOSConfig.h*

        3.2 In the Kconfig menu, if there is no specified header, then all symbols are generated into *mcux_config.h*.

        3.3 All generated config header files are placed under the project root path. (i.e. /boards/frdmk64f/demo_apps/hello_world) These header files are expected to be included in the sources/headers in advance.

        3.4 By default, Kconfig will add a CONFIG_ prefix to macros. If you need it, then add **No prefix in generated macro** in the help, like:

        ```bash
            if MCUX_COMPONENT_middleware.freertos-kernel

                config configUSE_PREEMPTION
                    bool "configUSE_PREEMPTION"
                    default y
                    help
                        No prefix in generated macro
                config configUSE_TICKLESS_IDLE
                    bool "configUSE_TICKLESS_IDLE"
                    default 0
                    help
                        No prefix in generated macro
        ```

2. Kconfig files provide the default board device variant selection. Developers can explicitly specify it in *prj.conf* found in **/boards/`<board>`/** , like

   ![board_select_device_part](./_doc/board_select_device_part.PNG)

## GUI Project

1. Why do I get an "wrong argument type nil (expected Regexp)" error when running `-t guiproject`?

   That's because you have run west command for armgcc toolchain, so that the script will get build information from cache, but there is no GUI project for armgcc. In this case, you need to add "-p always" to run a pristine build.

   We have updated the script, if you get the latest commit, you will get more explicit error message:

   ```bash
   Currently supported toolchain: ["iar", "mdk"], but script get armgcc, please check --toolchain in west command, or try run with -p always to prevent setting by cache.
   ```

2. Why the IDE can not identify the MCU when I open the project?

    For Keil MDK, if you get build error like:

    ![board_select_device_part](./_doc/gui_project_mdk_device_not_found.png)

    For IAR, if the error like `Fatal Error[Pe035]: #error directive: "Unknown target."` And no device setting:

    ![board_select_device_part](./_doc/gui_project_undefined_device.png)

    Please check the variable `MCUX_TOOLCHAIN_IAR_CPU_IDENTIFIER` and `MCUX_TOOLCHAIN_MDK_CPU_IDENTIFIER` in `mcuxsdk/devices/${soc_series}/${device}/Kconfig.chip`, make sure it's a valid device identifier. 

## BUILD

1. Why does GUI project build pass but fail on the command line?

    To create GUI project, the script parses `build.ninja` and set them in project template file. There may be some presets in the template file that make your project compile successfully, but they will not be used by CMake. So you need to compare the build options in the GUI project with those in `build.ninja` and add missing assembler/compiler/linker flags in CMake.

    For IAR project, you can check build options by setting log level to `All`.
    ![board_select_device_part](./_doc/IAR_GUI_all_build_option.png)

    For MDK project, you can check build options in  `C/C++(AC6)`/`Asm`/`Linker`  option tab.
    ![board_select_device_part](./_doc/MDK_GUI_all_build_option.png)

2. Why does IAR GUI project run pass but fail on the command line?

    There are two possible causes for this. The first one is caused by wrong compiler/linker flags, please refer to previous question `Why does GUI project build pass but fail on the command line?`.

    If the flags are identical, please check the version of CMake and Ninja. The IAR IDE GUI project will use `.o` extension for object name, developer may relocate these object in linker file. For example:
    ```
    initialize by copy {
        readwrite,
        /* Place in RAM flash and performance dependent functions  */
        readonly object fsl_flexspi_nor_flash.o,
        readonly object nor_flash_ops.o,
        readonly object fsl_flexspi.o,
        readonly object fsl_clock.o,
        readonly object ABImemclr4.o,
        section .textrw,
        section CodeQuickAccess,
        section DataQuickAccess
        };
    ```
    However, meta build system use CMake and Ninja, in some of low version CMake and Ninja, the generated object has `.c.o` extesion name. This misalignment will cause the link configuration not to take effect. So please make sure the minimum version for CMake is `3.30.0`, and `1.12.1` for Ninja.