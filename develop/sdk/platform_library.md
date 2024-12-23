# Platform Library

## Overview

Device platform library examples are device specific example which share the general build system mechanism for example creation and configuration. They are all located in examples_int repo folder.

Take MIMXRT1176 as an example, the cmd to run is like:

```bash
west build --device MIMXRT1176 examples_int/platformlib -Dcore_id=cm7 --enable-all-drivers -p
west build --device MIMXRT1176 examples_int/platformlib -Dcore_id=cm7 --enable-all-drivers -p --toolchain=iar
west build --device MIMXRT1176 examples_int/platformlib -Dcore_id=cm7 --enable-all-drivers -p --toochain=mdk
```

## CMakeLists.txt

The platform library example CMakeLists.txt is located in `examples_int/platformlib`.

Here is its contents:

```cmake
cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

# PROJECT_DEVICE_PORT_PATH instead of PROJECT_BOARD_PORT_PATH
# PROJECT_TYPE must be LIBRARY
project(mcux_platformlib LANGUAGES C CXX ASM PROJECT_DEVICE_PORT_PATH examples_int/_devices/${device}/platformlib PROJECT_TYPE LIBRARY)

# Unlike common board examples, it doesn't add the root CMakeLists.txt as entry point. Instead, it only uses device cmakes and driver cmakes.
# device cmakes
mcux_add_cmakelists(${SdkRootDirPath}/${device_root}/${soc_portfolio}/${soc_series}/${device})
# driver cmakes
mcux_load_all_cmakelists_in_directory(${SdkRootDirPath}/drivers)

# example port/reconfiguration for device
include(${SdkRootDirPath}/examples_int/_devices/${device}/platformlib/${multicore_foldername}/reconfig.cmake OPTIONAL)
```

## Kconfig

### Overview

Platform library example has its own Kconfig only "source" `drivers` and `device`.

```
mainmenu "Mcux platform library"

source "${SdkRootDirPath}/drivers/Kconfig"

source "${SdkRootDirPath}/devices/Kconfig"
```

### Driver selection

`--enable-all-drivers` feature is provided to automatically selected all depended drivers for designated device based on the Kconfig.chip IP information. It will add `default y` for all Kconfig symbols starting with MCUX_COMPONENT_driver prefix if there is `default` provided so that if the driver dependency is satisfied for the device, then it will be added into build tree.

The common prj.conf for platform library example sets CMSIS, system and startup components to y:

```
CONFIG_MCUX_COMPONENT_device.CMSIS=y
CONFIG_MCUX_COMPONENT_device.system=y
CONFIG_MCUX_COMPONENT_device.startup=y
```

If you want to disable or enable some drivers additionally, you can still use the device port prj.conf to do it.

## GUI Project Generation

Platform library example support GUI project generation. The cmd is like

```bash
west build --device MIMXRT1176 examples_int/platformlib -Dcore_id=cm7 --enable-all-drivers -p --toochain=iar -t guiproject
```

The common IDE.yml only sets the project template:

```yaml
mdk:
  project_language: cpp
  project-templates:
    - scripts/guigenerator/templates/mdk/lib_generic_arm/libgeneric_armclang.uvprojx
  config:
    __common__:
      cp-define:
        ${CONFIG_MCUX_TOOLCHAIN_MDK_CPU_IDENTIFIER}: NXP

iar:
  project_language: auto
  project-templates:
    - scripts/guigenerator/templates/iar/lib_generic_arm/libgeneric.ewp
    - scripts/guigenerator/templates/iar/lib_generic_arm/libgeneric.eww
  config:
    __common__:
      cp-define:
        ${CONFIG_MCUX_TOOLCHAIN_IAR_CPU_IDENTIFIER}: NXP ${CONFIG_MCUX_TOOLCHAIN_IAR_CPU_IDENTIFIER}
      cx-flags:
        - -e # enable IAR extension, if no cpp file included, gui project cant get this flag from ninja
```

If customization is needed for certain device, then additional IDE.yml could be provided in the device port folders just like common board example.

## Example.yml

The device example.yml content is a little different from board example:

```yaml
# yaml-language-server: $schema=../../scripts/data_schema/example_description_schema.json
mcux_platformlib:
  section-type: library
  contents:
    meta_path: examples_int/platformlib
    project-root-path: ""
    document:
      name: mcux_platformlib${core_id_suffix_name}
      device_example: true
      category: platformlib
      brief: platformlib containing all base SDK drivers
      extra_build_args:
        - "--enable-all-drivers"
    toolchains: # specify the basic toolchains and targets
    - +armgcc@debug
    - +armgcc@release
    - +iar@debug
    - +iar@release
    - +mdk@debug
    - +mdk@release
  devices:
    MIMXRT1176@cm7: []
```

It uses the `mcux_platformlib/contents/toolchains` to specify the basic toolchains and build configurations it supports. Extra device specific toolchains and build configurations are specified in `devices` hash data just like `boards` for board examples.
