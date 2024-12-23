# Software Component

## Componentization

To improve software component integration and portability, all MCUXpresso SDK components including drivers, components, utilities and middlewares are recorded and used in a componentized way instead of fragment code lines.

In addition to the sources, one software component always contains CMakeLists.txt and Kconfig files. CMake part defines the sources, includes, static configurations, versions, etc while Kconfig part defines the dynamic configurations and dependencies.

## CMakeLists.txt

In CMakeLists.txt, component data shall be recorded inside a `if-endif` guard. The `if `condition shall be with prefix `CONFIG_MCUX_COMPONENT `to specify the following data belongs to a software component. The component name is right next to it. Please note that nested `if-endif` is not supported, and the `if` condition shall only contain one component name, combined condition with `||` or `&&` is not supported either.

Here is the driver.uart CMakeLists.txt:

```cmake
if (CONFIG_MCUX_COMPONENT_driver.uart) # component name

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

If a component definition is split into several cmake files, please use the same `if-endif` guard in all files data.

## Kconfig

In Kconfig, the symbol for a component shall also start with `MCUX_COMPONENT_` to be identical with cmake component name. Component configuration and dependency shall be recorded in Kconfig following the below pattern:

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

For multiple components belonging to one middleware set, please use `menu` to gather them together, like

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

## Supported Components

There are following components which are already enabled in MCUXpresso SDK: drivers, components/utilities, middlewares and RTOS. They are located under `mcuxsdk/drivers`, `mcuxsdk/components`, `mcuxsdk/middlewares` and `mcuxsdk/rtos`.

> Base device and board specific drivers and components are located in the target device and board folder.

All software components are involved into build tree through the root `mcuxsdk/CMakeLists.txt` and `mcuxsdk/Kconfig.mcuxpresso`. You can check them with Kconfig GUI and select needed components into your example.
