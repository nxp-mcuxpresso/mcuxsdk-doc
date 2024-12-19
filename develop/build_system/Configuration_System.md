# Configuration System(Kconfig)

## Overview

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) is a selection-based configuration system originally developed for the Linux kernel which now found more and more use in other projects beyond the Linux kernel. In MCUXpresso SDK, Kconfig is used to config the build in run time which includes component selection with dependency resolve, component configuration with feature enable, disable and customization.

You can interact with Kconfig via a curses or graphical menu interface, usually invoked by running `west build -t guiconfig` after you have already run passed the CMake configuration process. In this interface, the user selects the options and features desired, and saves a configuration file, which is then used as an input to the
build process.

## Kconfig Usage

1. Please install python3 before installing kconfiglib. For kconfiglib, you can run with the command

   ```bash
   pip install -U kconfiglib
   ```
2. Make sure that `mcu-sdk-boards`, `mcu-sdk-components`, `mcux-devices-kinetis`, `mcux-devices-lpc`, `mcux-devices-rt` projects are cloned because there are Kconfig data inside these repos for boards/components/devices. Only with all these data included, then you can enjoy full feature of kconfig.

3. Run

   Inside Kconfig files, there are board/device variables included in referenced paths, so it cannot be directly run, so Kconfig shall be run inside whole cmake process.

    - Run cmake configuration

      ```bash
      west build -b frdmk22f examples/demo_apps/hello_world --cmake-only
      ```

      `--cmake-only` only executes BS configuration stage and generation stage.You can ignore `--cmake-only`, then the project will be built.
    - Run guiconfig target

      ```bash
      west build -t guiconfig
      ```

      Then you will get the Kconfig GUI launched, like

      ![kconfig_gui](./_doc/kconfig_gui.png)

      You can select/deselect and modify to do reconfiguration and remember to save.

      After you save and close, you can directly run "west build" to do the build.

## Kconfig Interface

menuconfig and guiconfig are 2 available interactive configuration interfaces to start a GUI to do run time selection and configuration for Kconfig options.

menuconfig is a curses-based interface that runs in the terminal while guiconfig is a graphical configuration interface.

Since the Kconfig data has variable inside, they need to be processed. BS has integrated this process into the build process. You can use west cmdline to start the GUI.

1. Run cmake configuration

   ```bash
   west build -b frdmk64f examples/demo_apps/hello_world --cmake-only
   ```

   You can ignore "--cmake-only", then the projecrt will be built.
2. Run guiconfig target

   ```bash
   west build -t guiconfig
   ```

   Then you will get the Kconfig GUI launched, like

   ![kconfig_gui](./_doc/kconfig_gui.png)

   You can select/deselect and modify to do reconfiguration and remember to save.

   After you save and close, you can directly run "west build" to do the build.

## Kconfig Process Flow

The Kconfig files and related prj.conf with priority are put into the Kconfig processor.

The direct output is the .config and config headers. Any updates in input Kconfig, output .config and config header will trigger a Kconfig process in next build cmd

![Kconfig_process_flow](./_doc/Kconfig_process_flow.PNG)

### prj.conf

As illustrated previously, prj.conf is the pre set value for Kconfig symbols. It is the input for the Kconfig process. Unlike the CMake which shall be explicitly included, the proj.conf will be loaded implicitly with different priority.

The prj.conf search paths can be provided through 3 ways with priority.

- Fixed prj.conf search paths

  For all project build, the following path prj.conf will anyway be collected into the build. They are related to device, board and example board specific part. The priority is from low to high. High priority prj.conf data will override low priority prj.conf data.
      1. devices/prj.conf
      2. devices/\<soc_series>/prj.conf
      3. devices/\<soc_series>/\<device>/prj.conf
      4. devices/\<soc_series>/\<device>/\<core_id>/prj.conf
      5. examples/prj.conf
      6. examples/_boards/prj.conf
      7. examples/_boards/\<board>/prj.conf
      8. examples/_boards/\<board>/\<core_id>/prj.conf
      9. examples/\<example_category>/prj.conf
      10. examples/\<example_category>/\<example\>/prj.conf
      11. examples/_boards/\<board>/\<example_category>/prj.conf
      12. examples/_boards/\<board>/\<example_category>/\<example>/prj.conf
      13. examples/_boards/\<board>/\<example_category>/\<example>/\<core_id>/prj.conf

  For shield case, it is generally the same as board:

      1. devices/prj.conf
      2. devices/\<soc_series>/prj.conf
      3. devices/\<soc_series>/\<device>/prj.conf
      4. devices/\<soc_series>/\<device>/\<core_id>/prj.conf
      5. examples/prj.conf
      6. examples/_boards/prj.conf
      7. examples/_boards/\<board>/prj.conf
      8. examples/_boards/\<board>/\<core_id>/prj.conf
      9. examples/\<shield_example_category>/prj.conf
      10. examples/\<shield_example_category>/\<example\>/prj.conf
      11. examples/_boards/\<board>/\<shield>/prj.conf
      12. examples/_boards/\<board>/\<shield>/\<shield_example_category>/prj.conf
      13. examples/_boards/\<board>/\<shield>/\<shield_example_category>/\<example>/prj.conf
      14. examples/_boards/\<board>/\<shield>/\<shield_example_category>/\<example>/\<core_id>/prj.conf

  If the "project" macro is with "NO_DEFAULT_CONFIG" like the following, then build system will skip all the fixed prj.conf search paths, since the input prj.conf cannot be empty, so the prj.conf must be provided with CUSTOM_PRJ_CONF_PATH or DCONF_FILE.

  ```cmake
  project(hello_world LANGUAGES C CXX ASM NO_DEFAULT_CONFIG)
  ```

- Specify customized prj.conf search path in project CMakelists.txt "project" with "CUSTOM_PRJ_CONF_PATH"

  The "CUSTOM_PRJ_CONF_PATH" argument can be used in project CMakelists.txt "project" macro to specify the customized prj.conf search paths and they have higher priority than the fixed prj.conf search paths.

  It could be either relative path or absolute path. For relative path, the root is the SDK repo root path.

  Here is one example:

  ```cmake
  project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH examples/_boards/${board}/demo_apps/hello_world CUSTOM_PRJ_CONF_PATH subfolder e:/sdk_next/subfolder)
  ```

  The `sdk-root/subfolder/prj.conf` and `e:/sdk_next/subfolder/prj.conf` will be added into build if existed.

- -DCONF_FILE=\<customized config file>

  You can directly provide customized prj.conf with -DCONF_FILE=\<customized config file>, like

  ```bash
  west build -b evkmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm4 -DCONF_FILE=./examples/prj.conf
  ```

  The customized project config file has the highest priority over all.

### .config

.config will be filtered to get the component and project segment dependency symbol values, such symbol values will be put into cmake process so that cmake knows which component and project segment data shall be included into the build process.

For example, if `CONFIG_MCUX_COMPONENT_driver.uart` is `y` in .config, then the following sources and includes will be added into the build during cmake process, otherwise not.

```cmake
if (CONFIG_MCUX_COMPONENT_driver.uart)
    mcux_add_source(
        SOURCES fsl_uart.h 
                fsl_uart.c
    )
    mcux_add_include(
        INCLUDES .
    )
endif()
```

### config headers

The Kconfig symbols and the values will be generated into config headers placed in build binary folder.

If you want your components Kconfig symbols and values to be generated into customized header, you can set Kconfig menu with (header name). Here is an example with Freertos kernel.

```bash
menu "Configuration (FreeRTOSConfig_Gen.h)"  # All freertos kernel Kconfig symbols and values will be generated into FreeRTOSConfig.h

#******************************************************************************#
#* Hardware description related definitions. **********************************#
#******************************************************************************#
        config configCPU_CLOCK_HZ
            string "configCPU_CLOCK_HZ"
            default "(SystemCoreClock)"
            help
                No prefix in generated macro
```

If it is not set, then all Kconfig symbols and values will be generated header named `mcux_config.h`, it is a preinclude file which means developer doesn't need to include it in source file explicitly.

For customized header files, there are 2 ways to include them into build tree:

1.  The build binary folder is added into search path by default, developer just need to include the config headers in the source in advance.  So that all config headers will be added into build tree. This is the default way.
2.  If run with "-DPREINCLUDE=1", then all generated header files will be included into build tree in a preinclude way.

## Specific config value

As previously described, the Kconfig symbols will be saved into header files as C macro. By default, there is a "CONFIG_" prefix for the macro, and macro value is set by prj.conf or "default" setting in Kconfig symbol.

For example, there are Kconfig symbols

```bash
    config FLASH_BASE_ADDRESS
        hex "Flash base address for the application"
        default 0x0
    config MPU_SUPPORT
        bool "MPU wrappers"
        default y
    config DSP_SUPPORT
        bool "DSP Support"
        default n
```

They will be generated in header file as the format:

```c
#define CONFIG_FLASH_BASE_ADDRESS 0x0
#define CONFIG_MPU_SUPPORT 1    /* Bool type y will be translated to 1 */
// #define CONFIG_DSP_SUPPORT 0 /* Bool type n will not be generated */
```

However, this rule may not satisfy some specific requirement, therefore some rules are provided for special handling of macro values, you can describe the rules in Kconfig help:

1. Keep quotes for string type macro value

   If the macro value is string type, for C language, it must be wrapped with quotes. This requires that strings set in Kconfig's default or prj.conf be escaped from quotes using `\`, which is not convenient. For example:

   ```bash
   config CHIP_DEVICE_PRODUCT_NAME
       string "Product name"
       default "\"not-specified\""
       help
           Provides a human-readable product name
   ```

   To get rid of the escape symbols, please add `Macro value is in quotes` in Kconfig `help` information, it can be identified by scripts to generate header files correctly.

2. Keep `U` suffix for unsigned integer type macro value

   Unlike C, Kconfig only provides integer data types. If you want to mark data as unsigned integer, please add `type unsigned` keyword in Kconfig `help` information

3. Remove `CONFIG_` prefix for macro name

   The default macro name has a `CONFIG_` prefix, it's a common rule of Kconfig. However, if you just want to keep the original name of Kconfig symbol as macro name, please add `No prefix` as the keyword in Kconfig `help` information.

Note: The rules above can be combined. For example, if you want to generate a macro without `CONFIG_` prefix, but has an unsigned value, you can record both keyword in Kconfig help information. 

```Bash
        config ERPC_MESSAGE_LOGGERS_COUNT
            int "ERPC_MESSAGE_LOGGERS_COUNT"
            default 0
            help
                Set amount of message loggers objects used simultaneously.
                No prefix in generated macro, type unsigned   
```

