# Build and Configuration System Data

## SDK Data

### Data File Types

The SDK data is recorded in CMake and Kconfig. CMake holds most build data like sources, includes, static configurations while Kconfig holds component dependencies and run time configurations.

Since Kconfig data are configurable, then there are 3 ways to provide the configure values

1. Kconfig default value

   Inside the Kconfig file, for each symbol, default value must be provided. In this way, any symbol will anyway gets a default value in any cases if the symbol dependency has been satisfied.

2. prj.conf

   For **visible** Kconfig symbols, you can directly set symbol=value in `prj.conf` to do the configuration. The `prj.conf` is placed in designated places will be taken as Kconfig process input with priority. Please refer [prj.conf](./Configuration_System.md#prj-conf) for details.

3. Kconfig.defconfig

   For invisible Kconfig symbols, prj.conf won't take effect. Please use `Kconfig.defconf` to redefine the symbol without type but with new default value.

   Note, `Kconfig.defconfig` will is actually repeatedly define Kconfig symbols. They are only supported in board and device reconfiguration. Please don't use it in your examples customization.

### Principles

There are 2 principles for MCUXpresso SDK data

1. Componentization

   SDK data is recorded and used in a `component` way instead of fragment lines. There are several component types each of which in data record is a data section.  Please refer [Data Section](#data-section) chapter for details.

   In this way software is highly modularized thus greatly improve the integration.
2. Decoupling.

   There are many kinds SDK data: boards, devices, drivers, components, middlewares, examples, etc. Different type data are strictly decoupled from each other and prepared separately.

   In this way, migrability is highly addressed and achieved. When adding a driver, you don't need to care about examples. When adding an example, you don't need to care about board or device data like pinmux or clock.

   So please don't mix data during the developments.

### Data Section

Each data section is composed of CMake and Kconfig.

3 data section types are supported: component, project segment and project.

#### Component

"component" section is used for software components. Only source files/include path/libraries/flags/macros/version are valid data for component section. Please do not set other data like variable inside the component.

In CMake, component data shall be recorded inside a if-endif guard. The `if` condition shall be with prefix `CONFIG_MCUX_COMPONENT` to specify the following data belongs to a software component. The component name is right next to it. Please note nested if-endif is unsupported, and the `if` condition should only contains single cmake variable, combined condition is unsupported.

Here is one driver.uart component cmake data:

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

If a component definition is split into several CMake files, please use the same if-endif guard in all files data.

In Kconfig, symbol for a component shall also start with `MCUX_COMPONENT_` to be identical with CMake component name.

Component configuration and dependency shall be recorded in Kconfig with the following the below pattern:

```bash
config MCUX_HAS_COMPONENT_driver.uart
    bool
    default y if MCUX_HW_IP_DriverType_UART

config MCUX_COMPONENT_driver.uart
    bool "Use driver uart"
    select MCUX_COMPONENT_driver.common
    depends on MCUX_HAS_COMPONENT_driver.uart # component dependency

 # Configuration for driver.uart shall be put into the if-endif so that only driver.uart is selected, the configuration will be showed
    if MCUX_COMPONENT_driver.uart 
     # Configuration for driver.gpio
    endif
```

About the dependency, please refer [Complex Dependency In Kconfig](#dependency) chapter for details.

For multiple components belonging to one middleware set, please use Kconfig "menu" to gather them together, like

```bash
menu "freertos-kernel(FreeRTOSConfig.h)"
    config MCUX_COMPONENT_middleware.freertos-kernel
        bool "middleware.freertos-kernel"
        select MCUX_COMPONENT_middleware.freertos-kernel.extension
    config MCUX_COMPONENT_middleware.freertos-kernel.extension
        bool "tad extension"
    config MCUX_COMPONENT_middleware.freertos-kernel.heap_1
        bool "heap 1"
    config MCUX_COMPONENT_middleware.freertos-kernel.heap_2
        bool "heap 2"
    config MCUX_COMPONENT_middleware.freertos-kernel.heap_3
        bool "heap 3"
    config MCUX_COMPONENT_middleware.freertos-kernel.heap_4
        bool "heap 4"
    config MCUX_COMPONENT_middleware.freertos-kernel.heap_5
        bool "heap 5"
    ......
endmenu
```

#### Project Segment

MCUXpresso SDK is composed of hundreds of devices and boards, thousands of components and ten thousands of projects. Projects on these boards and devices have many shared data like core related settings, common build target settings,  device headers and configurations, board files, clock and pinmux. Project segment data section is an abstraction of common shared data. It is introduced to avoid data duplication.

Like the component, in CMake, project segment data shall also be recorded inside a if-endif guard. The if condition shall be with prefix `CONFIG_MCUX_PRJSEG_`, right after it is the project segment name.

Here is the frequently used and prepared project segments table.

| Project Segment Name                     | Location               | Functionality                            |
| ---------------------------------------- | ---------------------- | ---------------------------------------- |
| CONFIG_MCUX_PRJSEG_config.arm.shared     | arch/arm/configuration | The commonly shared configuration by all examples of ARM platforms |
| CONFIG_MCUX_PRJSEG_config.kinetis.shared | arch/arm/configuration | The commonly shared configuration by all examples of kinetis platforms |
| CONFIG_MCUX_PRJSEG_config.arm.core.`<core name>` | arch/arm/cortexm       | The ARM core settings                    |
| CONFIG_MCUX_PRJSEG_config.arm.core.fpu.`<fpu type>` | arch/arm/cortexm       | The ARM core fpu settings                |
| CONFIG_MCUX_PRJSEG_config.device_core.define | arch/arm/cortexm       | The core CPU macro definition            |
| CONFIG_MCUX_PRJSEG_target.`<buiild target name>` | arch/arm/target        | Build configuration target               |
| CONFIG_MCUX_PRJSEG_module.board.`<board module name>` | boards/common          | Commonly shared board modules like board file, pinmux, clock config, etc. |
| CONFIG_MCUX_PRJSEG_project.`<project module name>` | boards/common          | Commonly shared project modules like hardware init app. etc. |

Here is one project segment CMake example:

```cmake
if (CONFIG_MCUX_PRJSEG_module.board.clock)
    mcux_add_source(
        BASE_PATH ${SdkRootDirPath}
        SOURCES boards/${board}/clock_config.h
                boards/${board}/clock_config.c
    )
    mcux_add_include(
        BASE_PATH ${SdkRootDirPath}
        INCLUDES boards/${board}
    )
endif()
```

In Kconfig, symbol for a project segment shall start with `MCUX_PRJSEG_` to be identical with CMake project segment name. Project segment configuration and dependency shall be recorded following the below pattern:

```bash
config MCUX_PRJSEG_module.board.clock
    bool "Use default clock files"
    imply MCUX_COMPONENT_driver.clock
    if MCUX_PRJSEG_module.board.clock
    endif
```

Unlike the component dependency, the dependency for project segment is simple, just several parallel `imply` to state that the project segment depends on some components and maybe other project segment to work. Since it is frequently occuring cases that some examples on certain boards need to customize some project segment dependencies, please use `imply` instead of `select` for project segment dependencies because `select` once true then cannot be deselected anymore.

#### Project

Just like the native CMake way, all data inside CMakeLists.txt with `project` macro inside is a `project` segment.

Compared to the native `project`, the customized `project` provides the following additional  parameters:

| Argument Name           | Argument Type | Explanation                              |
| ----------------------- | ------------- | ---------------------------------------- |
| PROJECT_BOARD_PORT_PATH | Single        | Path for board-specific and project-specific files. Generally, this folder will contain hardware_init.c and app.h |
| PROJECT_TYPE            | Single        | Specify the project type, can be " EXECUTABLE" or "LIBRARY". The default type is " EXECUTABLE" if not set. |
| CUSTOM_PRJ_CONF_PATH    | Multiple      | Specify customized prj.conf search path. Please refer to[prj.conf](#prj.conf) |

Here is one project CMake example

```cmake
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

# Specify the project
project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH examples/_boards/${board}/demo_apps/hello_world)

# Include device, board, drivers/components, middlewares
include(${SdkRootDirPath}/CMakeLists.txt)

include(${SdkRootDirPath}/examples/demo_apps/reconfig.cmake OPTIONAL)
include(${SdkRootDirPath}/${project_board_port_path}/reconfig.cmake OPTIONAL)

mcux_add_source(
    SOURCES hello_world.c
)

mcux_add_include(
    INCLUDES .
)

# convert binary to .bin. 
mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
```

For project, it is not required to provide example specific Kconfig. If your example has specific Kconfig, then please follow the pattern to add it.

```bash
rsource "../../../Kconfig.mcuxpresso"

mainmenu "Hello world Example Run Time Configuration"

config HELLO_WORLD_EXAMPLE_MACRO
    bool
    default y
    help
        "Hello world example macro"
```

1. `rsource "../../../Kconfig.mcuxpresso"` must be added to load all repo Kconfigs because Kconfig.mcuxpresso is assembly point for Kconfigs.
2. Set `mainmenu` to give the GUI title
3. Set your example specific configurations

**Note, the Kconfig process will take example specific Kconfig as entry point with priority. If not provided, then take the <mcuxsdk>/Kconfig instead. So if your example doesn't have Kconfig contents, please don't keep it.**

### Dependency

BS provided dependencies record and resolve for both sections(project and components) and sources.

#### Section Level Dependency

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) dependency mechanism and tool is used to describe and resolve section level dependency.

##### Dependency Mechanisms

[Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) provides `depends on`, `select` and `choice` dependency mechanisms.

- "depends on"

  It defines a dependency for Kconfig symbol. If multiple dependencies are defined, they can be connected with ‘&&’, ‘||’, and ! for NOT.

  The Kconfig item won’t be showed if the “depends on” is not satisfied.
- "select"

  It forces a symbol to true which means the depended component is selected anyway no matter the dependency is
  satisfied or not.
- "choice"

  It defines a choice group. The single choice can only be of type bool or tristate. If no type is specified for a choice, its type will be determined by the type of the first choice element in the group or remain unknown if none of the choice elements have a type specified.

Kconfig processor in BCS will give detailed warnings about unsatisfied component selection so that  you can immediately find it and fix.

##### Practice Recommendation

- For software components depending on hardware related dependency items like board, device, device_id, please use `depends on`. If not satisfied, the related components will not be showed so that not bloat the Kconfig GUI list.
- For software components depending on software component, priority to use `select`. It helps to auto select component dependency.
- For cycle dependency case like FOO needs to "select" BAR and BAR needs to "select" FOO, since Kconfig doesn't support cycle dependency, so you cannot use mutually "select" between FOO and BAR. The recommendation is use both "select" and "depends on". For example, FOO "select" BAR and BAR "depends on" FOO. In this way, when you  tick FOO, then BAR will be automatically selected. When FOO dependency is not satisfied, BAR cannot be showed.
- If there are `any of` dependencies, `choice` can satisfy the needs, please see [Dependency Patterns](#dependency-patterns)

##### Dependency Items

Except for software components, following dependency items are provided.

| Dependency Item               | Illustration                             |
| ----------------------------- | ---------------------------------------- |
| MCUX_HW_DEVICE_\<device>      | Device, like MK64F12                     |
| MCUX_HW_DEVICE_ID_\<device_d> | Device id, like MK64FN1M0xxx12           |
| MCUX_HW_CORE_\<core_name>     | Core name, like cm4f                     |
| MCUX_HW_CORE_ID_\<core_id>    | Core id, like cm33_core0                 |
| MCUX_HW_BOARD_\<board name>   | Board name, like frdmk64f                |
| MCUX_HW_KIT_\<kit name>       | Kit name, like frdmk64f_agm01            |
| MCUX_HW_\<fpu type>           | fpu type name, like  MCUX_HW_FPV4_SP     |
| MCUX_HW_DSP                   | DSP                                      |
| MCUX_HW_MPU                   | MPU                                      |
| MCUX_HW_\<secure type>        | Secure or nonsecure, like MCUX_HW_SECURE, MCUX_HW_NONSECURE |
| MCUX_HW_\<trustzone type>     | Trustzone type, like MCUX_HW_TZ, MCUX_HW_NO_TZ |

**All these dependency items shall be defined in device Kconfig.chip.**

##### Dependency Patterns

Here are summarized frequently used dependency patterns.

- Pattern1: start with allOf, with one level anyOf and not

  ```yaml
  componentA:
    allOf:
      - component1
      - component2
      - anyOf:
        - component3
        - component4
      - anyOf:
        - component5
        - component6
      - not: 
          device:
          - MK64F12
          - MK63F12
  ```

  The recommended dependency patterns for this.

  ```bash
      config MCUX_COMPONENT_componentA
          bool "Component A, pattern 1"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on !MCUX_HW_DEVICE_MK64F12 && !MCUX_HW_DEVICE_MK63F12 # not
          choice
              prompt "Component A anyOf1"
              default MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_1
              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_1
                  bool "Select component3"
                  select MCUX_COMPONENT_component3

              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_2
                  bool "Select component4"
                  select MCUX_COMPONENT_component4
          endchoice  
          choice
              prompt "Component A anyOf2"
              default MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_3
              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_3
                  bool "Select component5"
                  select MCUX_COMPONENT_component5

              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_4
                  bool "Select component6"
                  select MCUX_COMPONENT_component6
          endchoice
  ```
- Pattern 2: start with allOf, with 2 level anyOf/allOf

  ```yaml
  componentB:
    dependency:
      allOf:
      - component1
      - component2
      - compiler:
        - iar
        - mdk
      - anyOf:
          - allOf:
            - component3
            - component4
            - device:
              - MK64F12
              - MK63F12
          - allOf:
            - component5
            - component6
            - device:
              - LPC54005
              - LPC54016
  ```

  The Kconfig dependency pattern is like

  ```bash
      config MCUX_COMPONENT_componentB
          bool "Component B, pattern 2 choise"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on MCUX_COMPILER_IAR || MCUX_COMPILER_MDK
          # All device scope shall be explicitly specified here, otherwise for a device which is not in the scope which means the dependency is not satisfied, but componentC is still showed and configurable
          depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12 || MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016

          if MCUX_COMPONENT_componentB
              choice
                  prompt "ComponentB anyOf"
                  default MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_1
                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_1
                      bool "Select component3 and component 4 in device MK64F12, MK63F12"
                      select MCUX_COMPONENT_component3
                      select MCUX_COMPONENT_component4
                      depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12

                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_2
                      bool "Select component5 and component4"
                      select MCUX_COMPONENT_component5
                      select MCUX_COMPONENT_component6
                      depends on MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016
              endchoice       
          endif
  ```

  If under each allOf, there is only one component, then you can use "select"

  ```yaml
  componentB:
    dependency:
      allOf:
      - component1
      - component2
      - compiler:
        - iar
        - mdk
      - anyOf:
          - allOf:
            - component3
            - device:
              - MK64F12
              - MK63F12
          - allOf:
            - component5
            - device:
              - LPC54005
              - LPC54016
  ```

  ```bash
     config MCUX_COMPONENT_componentB
          bool "Component B, pattern 2 select"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on MCUX_COMPILER_IAR || MCUX_COMPILER_MDK
          # All device scope shall be explicitly specified here, otherwise for a device which is not in the scope which means the dependency is not satisfied, but componentC is still showed and configurable
          depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12 || MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016
          select MCUX_COMPONENT_component3 if MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12
          select MCUX_COMPONENT_component5 if MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016 
  ```
- Pattern 3: start with anyOf, with one level allOf

  ```yaml
  componentE:
    dependency:
      anyOf:
      - allOf:
        - component1
        - component2
        - core:
          - cm4
          - cm4f
        - device:
          - MK64F12
          - MK63F12
      - allOf:
        - component3
        - component4
  ```

  The Kconfig dependency pattern is like

  ```bash
      config MCUX_COMPONENT_componentC
          bool "Component C, pattern 3"
          if MCUX_COMPONENT_componentC
              choice
                  prompt "Component C anyOf"
                  default MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component1_component2
                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component1_component2
                      bool "Select component1 and component2"
                      select MCUX_COMPONENT_component1
                      select MCUX_COMPONENT_component2
                      depends on MCUX_HW_CORE_CM4 || MCUX_HW_CORE_CM4F
                      depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12

                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component3_component4
                      bool "Select component3 and component4"
                      select MCUX_COMPONENT_component3
                      select MCUX_COMPONENT_component4
              endchoice       
          endif
  ```

#### Source Level Dependency

Source level dependency is achieved through the CMake extension, like

```cmake
    mcux_add_source(
        SOURCES portable/GCC/ARM_CM0/port.c
        # The following 2 lines mean port.c only supports cm0p core and toolchain armgcc, mcux and mdk
        CORES cm0p
        TOOLCHAINS armgcc mcux mdk
    )
```

Please refer the [mcux_add_source/mcux_add_include extension arguments](./Build_System.md#source-and-include) for supported dependency items.

### Variables

Variable mechanism is introduced to facilitate data record in both CMake and Kconfig for MCUXpresso SDK.

For example, in CMake with a `board` variable in the source, one copy of the following project segment data can be shared by all boards examples without any duplication.

```cmake
if (CONFIG_MCUX_PRJSEG_module.board.suite)
    mcux_add_source(
        BASE_PATH ${SdkRootDirPath}/examples/_boards/${board} # "board" variable shall be defined in each board so that each board can use this project segment
        SOURCES dcd.c dcd.h
    )
endif()
```

In Kconfig, the same `board` variable can set the board Kconfig path for all boards.

```bash
rsource "${board}/Kconfig"
```

There are some required variables which must be provided for each build to make the CMake configuration process run passed.

Besides, customized variables are allowed for some software data recorded although not suggested.

#### Required Variables

There are some required variables which shall be defined in advance to make the BCP workable. These variables are generally related to hardware related information.

In the BS, all these required variables can be defined in CMake to make the build work, but to enable the switch across device parts in run time in Kconfig, most hardware related variables are moved into Kconfig.chip because Kconfig mechanism can make sure that when you switch device part, all related variables can be switch at the same time.

Here is the CMake stored variable table:

| Variable Name        | Explanation               | Acquisition                              | Used in           | Usage                                    |
| -------------------- | ------------------------- | ---------------------------------------- | ----------------- | ---------------------------------------- |
| SdkRootDirPath       | SDK root directory        | Automatically set by BS                  | CMake             | Secify sdk root path like `include(${SdkRootDirPath}/devices/common/device_header.cmake)` |
| board                | board name, like frdmk64f | Provided in cmdline argument, also need to record it in board variable cmake | CMake and Kconfig | Specify the target board, like `${SdkRootDirPath}/boards/${board}` |
| device               | device name, like MK64F12 | Device variable cmake                    | CMake and Kconfig | Specify the target device, like `${SdkRootDirPath}/devices/\${soc_portfolio}/${soc_series}/${device}` |
| core_id              | Core id, like cm33_core0  | Device variable cmake. This is only required for multicore device. | Kconfig           | Specify the core_id, like `rsource "${core_id}/Kconfig`.`<br>`This is only needed for multiple core device Kconfig. |
| core_id_suffix_name  | Core id suffix name       | Device variable cmake                    | CMake             | Unify data record across single core and multicore device. For example, for the same hello_world project name, in multicore device, it is may called hello_world_cm4 and hello_world_cm7 while in single core device, it is may called hello_world, then "hello_world${core_id_suffix_name}" can work for all cases. For cm4 core, it can be "_cm4", for cm7 core, it can be "_cm7", for single core, it can be "" |
| multicore_foldername | multicore folder name     | Device variable cmake                    | CMake             | Unify data record across single core and multicore device. For example, for the same hello_world project root, in multicore device evkmimxrt1170, it is boards/evkmimxrt1170/demo_apps/hello_world/cm4 and boards/evkmimxrt1170/demo_apps/hello_world/cm7 while in single core board frdmk64f, it is boards/frdmk64f/demo_apps/hello_world, then "boards/evkmimxrt1170/demo_apps/hello_world/${multicore_foldername}" can work for all cases. For cm4 core, it can be "cm4", for cm7 core, it can be "cm7", for single core, it can be "." |
| soc_series           | soc series                | Soc series cmake                         | CMake             | Specify the soc series, like `${SdkRootDirPath}/devices/${soc_portfolio}/${soc_series}/${device}` |

The above variables shall anyway be provided in CMake because they are used before Kconfig process.

Here is the Kconfig stored variable table:

| Variable Name                            | Explanation                              | Acquisition     | Used in | Usage |
| ---------------------------------------- | ---------------------------------------- | --------------- | ------- | ----- |
| CONFIG_MCUX_HW_CORE                      | Core                                     | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_CORE_ID                   | Core id                                  | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_DEVICE_CORE               | device core. For single core, it is the device like MK64F12. For multicore, it is device+core like  MIMXRT1176_cm4 or  MIMXRT1176_cm7 | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_FPU                       | fpu                                      | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_FPU_TYPE                  | fpu type.                                | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_DEVICE_ID                 | Device id like  MK64FN1M0xxx12           | Kconfig process | CMake   |       |
| CONFIG_MCUX_HW_DEVICE_PART               | Device part like  MK64FN1M0VDC12         | Kconfig process | CMake   |       |
| CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX | MCUXpresso SDK provided device default linker file name prefix, like "LINKER devices/${soc_portfolio}/${soc_series}/${device}/gcc/${CONFIG_MCUX_TOOLCHAIN_LINKER_DEVICE_PREFIX}_flash.ld", for MK64F12, it is devices/Kinetis/MK64F12/gcc/MK64FN1M0xxx12_flash.ld | Kconfig process | CMake   |       |
| CONFIG_MCUX_TOOLCHAIN_IAR_CPU_IDENTIFIER | IAR IDE project device identifier        | Kconfig process | CMake   |       |
| CONFIG_MCUX_TOOLCHAIN_MDK_CPU_IDENTIFIER | MDK IDE project device identifier        | Kconfig process | CMake   |       |

Basically, all type string Kconfig symbol can be regarded as variable and used in CMake.

Except for the above variables, there are variables which are generated in the configuration stage:

| Variable Name          | Explanation                              |
| ---------------------- | ---------------------------------------- |
| MCUX_SDK_PROJECT_NAME  | The processed example name, it equals `PROJECT_NAME`+`core_id_suffix_name` |
| APPLICATION_SOURCE_DIR | Project CMakelists.txt directory like examples/demo_apps/hello_world |
| APPLICATION_BINARY_DIR | Output build directory like `<mcuxsdk>/build` |

#### Customized Variables

Besides the above variables, you can set your own variable in CMake to facilitate your data record with extension mcux_set_variable.

For the required variables, BCS will guarantee that they are defined before they are used.

For you customized variables, please make sure that your variables are defined before they are used by yourself.

#### Tips For Variable Usage

- Variable value replacement is invisible in CMake process, to avoid potential issues, please minimize the usage of variable.
- To make Kconfig integratable for other Kconfig system, please don't use variables in Kconfig data other than "rsource". "rsource" is only to load Kconfig files.

### Repo Data

MCUXpresso SDK repo CMake and Kconfig data are composed of arch, boards, devices, drivers, components, middlewares and examples. Based on the decoupling principle, all these different kinds data are placed under different folders of the MCUXpresso SDK repo.

#### Arch Data

MCUXpresso SDK support all mainstream soc architecture like ARM, Riscv, DSC. The soc architecture specific data are recorded in `<mcuxsdk>/arch/<arch>` folder.

Here is the hierarchy of arch data folder:

```yaml
arch:
  arm:
    target: Commonly shared build targets data like debug and release
    configuration: Commonly shared build configuration data
    cortexm: Core settings
    CMSIS: CMSIS headers
  dsp56800:
  xtensa:
```

#### Board Data

##### Structure

Board data stays in boards folder. Here is a hierarchy demonstrated with single core device board frdmk64f and multicore device board evkmimxrt1170:

```yaml
_boards:
  frdmk64f: # A single core device board
    CMakeLists.txt: Board specific contents like components and settings
    Kconfig: Board software Kconfig, mainly specify board specific component and project segment dependency
    Kconfig.defconfig: Board specific components selection and configuration for invisible Kconfig symbols
    prj.conf: Board specific components selection and configuration
    example.yml: The supported toolchains and build configuration targets
    variable.cmake: Board variables
    board_runner.cmake: Board debug settings
    shields: The shields, see next Shield Data chapter
    demo_apps:
      hello_world:
        reconfig.cmake: Board example reconfig, mainly replace, remove some default board settings
        prj.conf: Board example specific component selection and configuration
      reconfig.cmake: Board example category reconfig, mainly replace, remove some default settings
      prj.conf: Board example category specific component selection and configuration
    rtos_examples: # like above demo_apps
      freertos_hello:
        reconfig.cmake:
        prj.conf:
      reconfig.cmake:
      prj.conf:
  evkmimxrt1170: # A multicore device board
    cm4: Core specific contents folder 
      example.yml: Board core specific example list
      Kconfig: Board core software Kconfig, mainly specify board core specific component and project segment dependency
      Kconfig.defconfig: Board core specific components selection and configuration for invisible Kconfig symbols
      prj.conf: Board core specific components selection and configuration
      setting.cmake: Board core specific data and settings
      variable.cmake: Board core specific variables
    cm7: # Just like above cm4 core
      example.yml:
      Kconfig:
      Kconfig.defconfig:
      prj.conf: 
      setting.cmake:
      variable.cmake:
    CMakeLists.txt: Board specific contents like components and settings
    Kconfig: Board software Kconfig, mainly specify board specific component and project segment dependency
    Kconfig.defconfig: Board specific components selection and configuration for invisible Kconfig symbols
    prj.conf: Board specific components selection and configuration
    variable.cmake: Board variables
    board_runner.cmake: Board debug settings
    demo_apps:
      reconfig.cmake:  Board example category reconfig, mainly replace, remove some default board settings
      hello_world:
        cm4:
          reconfig.cmake: Board core specific example reconfig, mainly replace, remove some default board settings
          prj.conf: Board core example specific components selection and configuration
        cm7:
          reconfig.cmake:
          prj.conf:
        reconfig.cmake: Board example category reconfig, mainly replace, remove some default board settings
        prj.conf: Board example category specific component selection and configuration
  prj.conf: components selection and configuration by all boards
```

##### Example.yml

The board level supported toolchains and build configuration targets shall be recorded in the `example.yml`.

A typical board example.yml is like

```yaml
board.toolchains:
- +armgcc@debug
- +armgcc@release
- +iar@debug
- +iar@release
- +mdk@debug
- +mdk@release
```

All examples under the board share the toolchains and targets in the board example.yml.

#### Shield Data

Shield is an addon which is attached to a board to extend its features and functionalities. All shields are put under its mother board folder. The structure is like

```yaml
_boards:
  frdmk64f:
    shields:
      a8974:
        <example category>:
        CMakeLists.txt:
        Kconfig:
        prj.conf:
      <other_shield>:
        <example category>:
        CMakeLists.txt:
        Kconfig:
        prj.conf:
```

The shield shares the board example.yml for toolchains and targets support. The shield CMakelists.txt shall be added into the board CMakeLists.txt with mcux_add_cmakelists and the shield Kconfig shall be 'rsource' in the board Kconfig.

#### Device Data

Device data stays in devices folder. Here is the device data hierarchy demonstrated with single core device MK64F 2 and multicore device MIMXRT1176:

```yaml
devices:
  Kinetis: Device socs sery
    MK63F12:
      Kconfig: Device software Kconfig, mainly specify board specific component and project segment dependency
      Kconfig.chip: Device hardware Kconfig related to device and core
      Kconfig.defconfig: Device specific components selection and configuration for invisible Kconfig symbols
      CMakeLists.txt: Device specific contents like components and settings, usually, just load mainset cmakelist
      driver:
        CMakeLists.txt: Device specific drivers
        Kconfig: Device specific drivers Kconfig
      prj.conf: Device specific components selection and configuration for visible Kconfig symbols
    MK64F12:
      Kconfig: Device software Kconfig, mainly specify board specific component and project segment dependency
      Kconfig.chip: Device hardware Kconfig related to device and core
      Kconfig.defconfig: Device specific components selection and configuration for invisible Kconfig symbols
      CMakeLists.txt: Device specific contents like components and settings
      driver:
        CMakeLists.txt: Device specific drivers
        Kconfig: Device specific drivers Kconfig
      prj.conf: Device specific components selection and configuration   
    prj.conf: Components selection and configuration by all Kinetis series
  RT:
    MIMXRT1175:
      cm4:
        driver:
          CMakeLists.txt: Device core specific drivers
        Kconfig: Device core software Kconfig, mainly specify board specific component and project segment dependency
        Kconfig.chip: Device core hardware Kconfig related to device and core
        Kconfig.defconfig: Device core specific components selection and configuration for invisible Kconfig symbols
        setting.cmake: Device core specific data and settings
        variable.cmake: Device core specific variables
        prj.conf: Device core specific components selection and configuration
      cm7: # just like core cm4 
        driver:
          CMakeLists.txt:
        Kconfig:
        Kconfig.chip:
        Kconfig.defconfig:
        setting.cmake:
        variable.cmake:
        prj.conf:
      CMakeLists.txt: Device specific contents like components and settings, usually, just load mainset cmakelist
      driver:
        CMakeLists.txt: Device specific drivers
      Kconfig: Device 
      Kconfig.chip: Device software Kconfig, mainly specify board specific component and project segment dependency
      Kconfig.defconfig: Device specific components selection and configuration for invisible Kconfig symbols
      prj.conf: Device specific components selection and configuration
    MIMXRT1176:
      cm4:
        driver:
          CMakeLists.txt: Device core specific drivers
        Kconfig: Device core software Kconfig, mainly specify board specific component and project segment dependency
        Kconfig.chip: Device core hardware Kconfig related to device and core
        Kconfig.defconfig: Device core specific components selection and configuration for invisible Kconfig symbols
        setting.cmake: Device core specific data and settings
        variable.cmake: Device core specific variables
        prj.conf: Device core specific components selection and configuration
      cm7: # just like core cm4 
        driver:
          CMakeLists.txt:
        Kconfig:
        Kconfig.chip:
        Kconfig.defconfig:
        setting.cmake:
        variable.cmake:
        prj.conf:
      CMakeLists.txt: Device specific contents like components and settings
      driver:
        CMakeLists.txt: Device specific drivers
      Kconfig: Device 
      Kconfig.chip: Device software Kconfig, mainly specify board specific component and project segment dependency
      Kconfig.defconfig: Device specific components selection and configuration for invisible Kconfig symbols
      prj.conf: Device specific components selection and configuration
    prj.conf: Components selection and configuration by all RT series
  prj.conf: Components selection and configuration by all devices
```

#### Example Data

##### Structure

All examples are expected to be placed under `examples` folder in their category.

```yaml
examples:
  demo_apps: 
    prj.conf: Component selection and configuration for all examples under demo_apps
    hello_world: 
      Kconfig: hello_world example Kconfig, if there is no project specific configuration data, please don't add it
      CMakeLists.txt: hello world example CMakeLists.txt
      prj.conf: hello world example component selection and configuration
      example.yml: Miscellaneous description data for example including toolchain and build configuration targets support
  rtos_examples: 
    prj.conf: Component selection and configuration for all examples under rtos_examples
    freertos_hello:
      Kconfig: freertos_hello example Kconfig, if there is no project specific configuration data, please don't add it
      CMakeLists.txt: freertos_hello example CMakeLists.txt
      prj.conf: freertos hello example component selection and configuration
      example.yml: Miscellaneous description data for example including toolchain and build configuration targets support
  prj.conf: all examples shared component selection and configuration
```

Here is a typical case of example.yml:

```yaml
# yaml-language-server: $schema=../../../../../scripts/data_schema/example_description_schema.json

hello_world:
  section-type: application
  contents:
    meta_path: examples/demo_apps/hello_world
    project-root-path: boards/${board}/demo_apps/hello_world/${multicore_foldername}
    document:
      name: hello_world${core_id_suffix_name}
      category: demo_apps
      brief: The HelloWorld demo prints the "Hello World" string to the terminal using
        the SDK UART drivers and repeat what user input. The purpose of this demo
        is to show how to use the UART, and to provide a simple project for debugging
        and further development.
  boards:
    frdmk64f: []
    evk9mimx8ulp@cm33: []
    evkbimxrt1050:
    - +armgcc@flexspi_nor_sdram_debug
    - +armgcc@flexspi_nor_sdram_release
    - +armgcc@sdram_txt_debug
    - +armgcc@sdram_txt_release
    - +iar@flexspi_nor_sdram_debug
    - +iar@flexspi_nor_sdram_release
    - +iar@ram_0x1400_debug
    - +iar@ram_0x1400_release
    - +iar@sdram_txt_debug
```

##### Example Toolchain And Target

The supported toolchains and build configuration targets for an example can be got in the following way:

1. Get the designated board example.yml to get the default supported toolchains and build configuration targets.
2. Get the designated board from "boards" data attribute
    1. If the data attribute is empty, then the board level toolchains and build configuration targets are the example ones.
    2. If the data attribute exists, "+" to add extra toolchains and build configuration targets pairs from board ones. "-" to reduce extra ones from board ones.

A detailed json schema is provided in mcuxsdk/scripts/data_schema folder for the example level example.yml, please review.

#### Driver Data

Base SDK drivers are placed under `drivers` folder.

You can use `mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)` to recursively include all drivers CMakelists.txt once.

```yaml
drivers:
  clock:
    CMakeLists.txt:
    Kconfig:
  common:
    CMakeLists.txt:
    Kconfig:
  <other drivers>:
    CMakeLists.txt:
    Kconfig:
  Kconfig: load all driver Kconfig
```

#### Component Data

Base SDK components are placed under `components` folder.

You can use `mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/components)` to recursively include all components CMakelists.txt once.

```yaml
components:
  serial_manager:
    CMakeLists.txt:
    Kconfig:
  <other components>:
    CMakeLists.txt:
    Kconfig:  
  Kconfig: load all components Kconfig
```

#### Assembly Point

All the above data are pieces of building blocks. For any build process, all data shall be loaded for selection and configuration. The assembly point is the start entry from where all CMakes and Kconfigs can be loaded.

The assembly point for all cmakes is the root CMakeLists.txt. It looks like

```cmake
# Load device CMakeLists.txt
mcux_add_cmakelists(${SdkRootDirPath}/devices/${soc_portfolio}/${soc_series}/${device})

# Load board CMakeLists.txt
mcux_add_cmakelists(${SdkRootDirPath}/examples/)

# Load all drivers
mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)

# all components
mcux_add_cmakelists(${SdkRootDirPath}/components)

# middlewares
mcux_add_cmakelists(${SdkRootDirPath}/rtos/freertos/freertos-kernel OPTIONAL)
mcux_add_cmakelists(${SdkRootDirPath}/middleware/usb OPTIONAL)
mcux_add_cmakelists(${SdkRootDirPath}/middleware/fatfs OPTIONAL)
mcux_add_cmakelists(${SdkRootDirPath}/middleware/littlefs OPTIONAL)
mcux_add_cmakelists(${SdkRootDirPath}/middleware/multicore OPTIONAL)
```

The assembly point for all Kconfig is the root Kconfg.mcuxpresso which is

```bash
# board
rsource "examples/Kconfig"

# device
rsource "devices/Kconfig"

# Driver config
menu "Driver Configuration"
    rsource "drivers/Kconfig"
    osource "rtos/freertos/freertos-drivers/Kconfig"
endmenu

# Component config
rsource "components/Kconfig"

# middleware config
menu "Middleware"
    osource "middleware/wifi_nxp/Kconfig"
    osource "middleware/mbedtls/Kconfig"
    osource "middleware/usb/Kconfig"
    osource "middleware/fatfs/Kconfig"
	osource "middleware/littlefs/Kconfig"
    osource "middleware/multicore/Kconfig"
	......
endmenu

# RTOS config
menu "RTOS"
menu "FreeRTOS"
    osource "rtos/freertos/freertos-kernel/Kconfig"
    osource "rtos/freertos/backoffalgorithm/Kconfig"
	......
endmenu
endmenu

menu "External Modules"

osource "$(KCONFIG_BINARY_DIR)/Kconfig.modules"

endmenu
```

The CMake include and Kconfig rsource(load) are generally aligned which means they shall stay together corresponding each other.

For other CMake based BS which wants to integrate MCUXpresso SDK, it may needs to set up the new assembly point file for CMake and Kconfig files in this repo.