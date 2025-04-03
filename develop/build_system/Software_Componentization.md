# Software Componentization

This chapter illustrates the MCUXpresso SDK Componentization concept and composition supported by the build system.

## Componentization

To improve software component integration and portability, all MCUXpresso SDK components including drivers, components, utilities and middlewares are recorded and used in a componentized way instead of fragment code lines.

In addition to the sources, one MCUXpresso SDK software component always contains CMakeLists.txt and Kconfig files. CMake part defines the sources, includes, static configurations, versions, etc while Kconfig part defines the dynamic configurations and dependencies.

The following shows a typical MCUXpresso SDK component composition:

```
  uart
    ├── fsl_uart.h
    ├── fsl_uart.c
    ├── CMakeLists.txt
    ├── Kconfig
```

All MCUXpresso SDK components have an ID across the CMakeLists.txt and Kconfig. The ID starts with `MCUX_COMPONENT_` to indicate this component is a ready MCUXpresso SDK component. Briefly, in CMakeLists.txt the ID is like `CONFIG_MCUX_COMPONENT_<component name>` while in Kconfig it is like `MCUX_COMPONENT_<component name>`, you will see details in next chapters.

> According to [Introduce Component, Project Segment and Dependency Definition Symbols](../build_system/Configuration_System.md#introduce-component-project-segment-and-dependency-definition-symbols), all Kconfig symbols with naming prefix MCUX_ will be intentionally removed out of the generated config header file, so they won't affect example build.

For external customers enabling a software functionality, it is not required to follow and use this componentization way to organize the sources and data. You can still use the traditional cmake and Kconfig syntax to work, but it is recommended that you could put your sources and data into a component instead of keeping them in a scattered way.

## CMakeLists.txt

In CMakeLists.txt, component data is recorded inside a `if-endif` guard. The condition of the `if` statement is the combination of the `CONFIG_MCUX_COMPONENT_` prefix and the component name which indicates everything insides the `if-endif` section belongs to a software component. The combination name is the component ID.
The nested `if-endif` is not supported, and the `if` condition shall only contain one component name, combined condition with `||` or `&&` is not supported either.

Here is the driver.uart CMakeLists.txt:

```cmake
if (CONFIG_MCUX_COMPONENT_driver.uart) # component name is driver.uart

    # component version
    mcux_component_version(2.5.1)
  
    # component data
    mcux_add_source(
        SOURCES fsl_uart.h 
                fsl_uart.c
    )
    mcux_add_include(
        INCLUDES .
    )
endif()
```

If a component definition is split into several cmake files, the same `if(CONFIG_MCUX_COMPONENT_<component name>)-endif` guards should be used in all files data.

## Kconfig

In Kconfig, the symbol for a component also starts with `MCUX_COMPONENT_` to be identical with cmake component name. Component configuration and dependency are recorded in Kconfig following the below pattern:

```bash
config MCUX_HAS_COMPONENT_driver.uart
    bool
    default y if MCUX_HW_IP_DriverType_UART # such MCUX_HW_IP_DriverType_UART is defined in device Kconfig.chip

config MCUX_COMPONENT_driver.uart
    bool "Use driver uart"
    select MCUX_COMPONENT_driver.common
    depends on MCUX_HAS_COMPONENT_driver.uart # component dependency

# Configuration for driver.uart shall be put into the if-endif so that only driver.uart is selected, the configuration will be showed
    if MCUX_COMPONENT_driver.uart 
     # Configuration for driver.uart
    endif
```

About the dependency, please refer [Complex Dependency](../build_system/Dependency.md) chapter for details.

For multiple components belonging to one middleware set, `menu` is used to gather them together, like

```
menu "freertos-kernel(FreeRTOSConfig.h)"
    config MCUX_COMPONENT_middleware.freertos-kernel
        bool "middleware.freertos-kernel"
        select MCUX_COMPONENT_middleware.freertos-kernel.extension
  
    ......
  
    config MCUX_COMPONENT_middleware.freertos-kernel.cm33_non_trustzone
        bool "cm33 non trustzone port"
        default n
        depends on (MCUX_HW_CORE_CM33 || MCUX_HW_CORE_CM33F)
    config MCUX_COMPONENT_middleware.freertos-kernel.cm33_trustzone.non_secure
        bool "cm33 trustzone, non secure port"
        default n
        depends on (MCUX_HW_CORE_CM33 || MCUX_HW_CORE_CM33F)

    config MCUX_COMPONENT_middleware.freertos-kernel.tfm_ns
        bool "TF-M NS support"
        select MCUX_COMPONENT_middleware.freertos-kernel.cm33_non_trustzone
        select MCUX_COMPONENT_middleware.tfm.ns
        default n
        help
            OS wrapper for running inside TF-M non secure world

    config MCUX_COMPONENT_middleware.freertos-kernel.extension
        default n
        bool "Task Aware Debugger (TAD) support"
    ......
endmenu
```

Component macro definitions will be generated in header files. Please refer to [Config Headers](../build_system/Configuration_System.md#config-headers) chapter for details.

## Supported Components

There are following components which are already enabled in MCUXpresso SDK: drivers, components/utilities, middlewares and RTOS. They are located under `mcuxsdk/drivers`, `mcuxsdk/components`, `mcuxsdk/middlewares` and `mcuxsdk/rtos`.

> Base device and board specific drivers and components are located in the target device and board folder.

All software components are involved into build tree through the root `mcuxsdk/CMakeLists.txt` and `mcuxsdk/Kconfig.mcuxpresso`. You can check them with Kconfig GUI and select needed components into your example.

## Component Naming

As you can see, in our build system, all components naming is in format `MCUX_COMPONENT_<name>` . The `MCUX_COMPONENT_` prefix indicates that the data section is a software component. About the specific component name, currently they are generally following the format `<major type>.<minor types>.<name>`. The dot is used to separate component type and name. The minor type(s) is **optional** and can be more than one like `driver.uart` , `middleware.fatfs` and `middleware.fatfs.mmc`.
Most frequently used major types are:

| Major Types | Explanation            | Examples                                 |
| ----------- | ---------------------- | ---------------------------------------- |
| driver      | Base SDK drivers       | driver.uart, driver.clock                |
| component   | SDK components         | component.serial_manager,  component.serial_manager_spi |
| utilities   | SDK utility            | utilities.gcov,  utilities.unity         |
| middleware  | Middlewares and RTOSes | middleware.fatfs, middleware.freertos-kernel |

The above naming convention applies to both cmakes and Kconfigs. For Kconfig, normally all Kconfig symbols will be generated into header files as macros, so there will be macros like `CONFIG_MCUX_COMPONENT_component.serial_manager=1` in the generated header file which will cause build failure because C language identifiers cannot contain punctuation mark dot. To resolve this, our build system intentionally remove such component naming symbols from generated header file. Please check [MCUXpresso SDK Customized Kconfig Rules](../build_system/Configuration_System.md#mcuxpresso-sdk-customized-kconfig-rules) for more rules and details.