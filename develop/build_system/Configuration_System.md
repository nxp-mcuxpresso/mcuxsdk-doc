# Configuration System(Kconfig)

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
menu "freertos-kernel(FreeRTOSConfig.h)" # All freertos kernel Kconfig symbols and values will be generated into FreeRTOSConfig.h
    config MCUX_COMPONENT_middleware.freertos-kernel
        bool "middleware.freertos-kernel"
        select MCUX_COMPONENT_middleware.freertos-kernel.extension

    config MCUX_COMPONENT_middleware.freertos-kernel.extension
    ......
endmenu
```

If it is not set, then all Kconfig symbols and values will be generated header named `mcux_config.h`.

There are 2 ways to include the generated config headers into build tree.

1. The config headers shall be included in the source in advance and the build binary folder will be added into includes so that all config headers will be added into build tree. This is the default way.
2. If run with "-DPREINCLUDE=1", then all generated header files will be included into build tree in a preinclude way.