# Overview

## Key Features

MCUXpresso SDK build and configuration system is based on [CMake](https://cmake.org/) and [Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html). Compared with other CMake based build system, it has the following exclusive key features:

- Introduce `Component` concept to improve software integration and portability.
- Provide comprehensive dependency resolve mechanism for software components with cmake and Kconfig.
- Fully support all mainstream embedded toolchains: iar, mdk, armgcc, codewarrior, xtensa and riscvllvm. Easily to extend to support new toolchains.
- Support IDE project generation for iar, mdk, codewarrior and xtensa to provide OOBE from build to debug.
- Support standalone project generation to export designated projects to zip and share.

## Architecture

In the overall system, [CMake](https://cmake.org/) is used to manage the whole build process. [Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html) is used to do component selection with dependency resolve, component configuration with feature enable, disable and customization. Misc yaml files are introduced to record debug settings and display data. Misc generators can be inserted into CMake configurator to extend features like standalone project generation. 

Here is the system architecture:

![](./_doc/build_system_arch.PNG)

