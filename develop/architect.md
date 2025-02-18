# Architecture

## Introduction

The MCUXpresso Software Development Kit (SDK) provides comprehensive development solutions designed to help accelerate embedded system development of applications based on MCUs from NXP. The MCUXpresso SDK includes a flexible set of peripheral drivers designed to speed up and simplify development of embedded applications. Along with the peripheral drivers, the MCUXpresso SDK provides an extensive set of example applications covering everything from basic peripheral use cases to full technology demonstrations. The MCUXpresso SDK contains optional RTOS integrations such as FreeRTOS, and various other middleware to support rapid development.  

The MCUXpresso SDK architecture is built around the five key components listed below:

1.  **CMSIS** - Arm Cortex Microcontroller Software Interface Standard Core: Device headers, Math/DSP libraries

2.  **Drivers** - SoC peripheral configuration and functions

3.  **RTOS** - Real-time Operating Systems

4.  **Middleware** - Compatible Stacks and technology enablement  

5.  **Applications** - Demo and driver examples based on the MCUXpresso SDK

![](media/Kinetis_SDK_Block_Diagram.jpg)

MCUXpresso SDK provides a powerful and robust [build and configuration system](#build-and-configuration-system) which covers all aspects of the software development.

## CMSIS Support

The MCUXpresso SDK CMSIS folder provides NXP support for the [Arm CMSIS Core](http://www.keil.com/pack/doc/cmsis/Core/html/index.html) standard. Along with SoC and peripheral header files, the SDK also includes common CMSIS header files for the Arm Cortex-M cores and the math and DSP libraries. The CMSIS DSP library source code is included for reference. 

## SoC Support - Header File/Drivers/Startup/Linker\...

The MCUXpresso SDK Device folder allows support for multiple devices in the same package. For example, MIMXRT1052 is one of the devices in the RT105X family. The support files required to develop with this device are in a unique folder inside the devices folder. The following sections detail the content provided in these SoC files:

### MCU header files

Each device supported in the MCUXpresso SDK has an overall System-on-Chip (SoC) memory-mapped header file. This header file contains the
memory map and register base address for each peripheral and the IRQ
vector table with the associated vector numbers. The overall SoC header file
provides access to the peripheral registers through pointers and
predefined bit masks. 

The **MCU Header file** is located in:  
    ```
    devices/<DEVICE_PLATFORM>/<DEVICE_FAMILY\>/<DEVICE_NAME>/<DEVICE_NAME>.h
    ```

### Feature Header Files

In addition to the overall SoC memory-mapped header file, the MCUXpresso SDK includes a feature header file for each device. The feature header file allows NXP to deliver a single software driver for a given peripheral. The feature file ensures that the driver is properly compiled for the target SoC.

The peripheral drivers are designed to be reusable regardless of the
peripheral functional differences from one MCU device to another. An
overall Peripheral Feature Header File is provided for the MCUXpresso
SDK-supported MCU device to define the features or configuration
differences for each subfamily device.

### Startup codes

The startup code file provides the startup functions and assembly code required for the SoC to run from power up to the main() function. The code
usually covers the stack setup, watchdog configuration, and handles
global variables.  

The **Startup code files** are located in:  
```devices/\<DEVICE_NAME\>/system\_\<DEVICE_NAME\>.c/h ```  
```devices/\<DEVICE_NAME\>/\<TOOLCHAIN\>/startup\_\<DEVICE_NAME\>.s/S```

### Linker files

Linker files are provided to support different toolchains. The postfix of the linker file varies from toolchain to toolchain.

The **Linker Files** are located in:  
```devices/\<DEVICE_NAME\>/\<TOOLCHAIN\>/\<\>.scf```

### Peripheral Drivers

The MCUXpresso SDK peripheral drivers mainly consist of low-level
functional APIs and high-level transactional APIs to quickly enable the SoC peripherals and perform transfers.

All MCUXpresso SDK peripheral drivers only depend on the CMSIS headers,
device feature files, fsl_common.h, and fsl_clock.h files so that users
can add the drivers along with their dependencies into a project.  

Except for the clock/power-relevant peripherals, each peripheral has its own driver. Peripheral drivers handle the peripheral clock gating/ungating inside the drivers during initialization and deinitialization respectively.

Peripheral Drivers are located in:  
```devices//\<DEVICE_NAME\>/drivers```

**Low-level functional APIs** provide common peripheral functionality, abstracting the hardware peripheral register accesses into a set of stateless basic functional operations. These APIs primarily focus on the control, configuration, and function of basic peripheral operations. The APIs hide the register access details and various MCU peripheral instantiation differences so that the application can be abstracted from the low-level hardware details.  

The API prototypes are intentionally similar to help ensure easy portability across devices supported in the MCUXpresso SDK.

**Transactional APIs** provide a quick method for customers to use higher-level functionality of the peripherals. The transactional APIs use interrupts and perform asynchronous operations without user intervention. Transactional APIs operate on high-level logic that requires data storage for internal operation and context handling. However, the Peripheral Drivers don\'t allocate this memory space. Rather, the user passes in the memory to the driver for internal driver operation.

Transactional APIs ensure that the NVIC is enabled properly inside the
drivers. The transactional APIs do not meet all customer needs, but
provide a baseline for development of custom user APIs.  

**_NOTE_** The transactional drivers never disable an NVIC after use. This is due to the shared nature of interrupt vectors on devices. It is up to the user to ensure that NVIC interrupts are properly disabled after usage is complete.

#### **Interrupt Handling for Transactional APIs**

A double weak mechanism is introduced for drivers with a Transactional
API. The double weak indicates two levels of weak vector entries. See
the examples below:

```

PUBWEAK SPI0_IRQHandler

PUBWEAK SPI0_DriverIRQHandler

SPI0_IRQHandler

LDR R0, =SPI0_DriverIRQHandler

BX R0
```

The first level of the weak implementation is the functions defined in
the vector table. 

This vector table can be located in:  
```devices/\<DEVICE_NAME\>/\<TOOLCHAIN\>/startup\_\<DEVICE_NAME\>.s/.S```  

The implementation of the first layer weak function calls the
second layer weak function. The implementation of the second layer
weak function (ex. SPI0_DriverIRQHandler) jumps to itself (B.). The
MCUXpresso SDK drivers with transactional APIs provide the
reimplementation of the second layer function inside the peripheral
driver. If the MCUXpresso SDK drivers with transactional APIs are linked
into the image, the SPI0_DriverIRQHandler is replaced with the function
implemented in the MCUXpresso SDK SPI driver.

The reason for implementing the double weak functions is to provide a
better user experience when using the transactional APIs. For drivers
with a transactional function, call the transactional APIs and the
drivers complete the interrupt-driven flow. Users are not required to
redefine the vector entries out of the box. At the same time, if users
are not satisfied by the second layer weak function implemented in the
MCUXpresso SDK drivers, users can redefine the first layer weak function
and implement their own interrupt handler functions to suit their
implementation.

The limitation of the double weak mechanism is that it cannot be used
for peripherals that share the same vector entry. For this use case,
redefine the first layer weak function to enable the desired peripheral
interrupt functionality. For example, if the MCU UART0 and UART1 share
the same vector entry, redefine the UART0_UART1_IRQHandler according to
the use case requirements.

### RTOS Driver

The MCUXpresso SDK provides the bus communication driver integrated with native FreeRTOS services. These drivers are called as an RTOS driver and provide the sync transfer APIs. The user can directly call these APIs in FreeRTOS
applications.   

RTOS drivers are located in the same folder as Peripheral Drivers. They include freertos in the filename. For example:  
```devices\\MIMXRT1052\\drivers\\fsl_lpi2c_freertos.c/h```

### CMSIS Driver

The MCUXpresso SDK provides CMSIS driver support for all the variants of I2C/UART/SPI peripherals. The MCUXpresso SDK CMSIS driver implementation uses the pin mux configuration APIs generated by the NXP pinmux Config Tool in ```pinmux.c``` files.
This method is different than the way proposed by Arm to configure the PINMUX configuration by passing a set of macros in ```RTE_Device.h```.

### Project Template

Project Template is described in the Application section under Development. Compared to a board level project template, device level project templates are for use cases to create a project for a device different from the one used on a specific board.

## Components

The MCUXpresso SDK provides the `/components` folder in the root directory. The folder organizes sensor drivers, common software components, and other software components required by the MCUXpresso SDK. 

### On-Board Device driver

Sensor, PMIC, PHY, Audio Codec components that are soldered on the evaluation board are supported in the SDK. Usually, their drivers are
connected to different variants of a standard peripheral in the SoC. For example, an Audio Codec can be connected to either I2C/LPI2C peripherals.  

To ease the porting effort to work with the same driver on
different SoCs (Which usually introduces different variants of a peripheral), the device driver is not bound to a specific peripheral
like I2C or LPI2C. Instead, it requires the application to provide a function pointer which is prepared outside the device driver. The
device driver can use this API to do the data write/read and so on. The device driver does not care about how these functions pointers are implemented. An application can use different ways to implement these functions. For example, a user can choose to use the CMSIS driver or alternatively use raw read/write to registers.  

**_NOTE:_** The initialization/deinitialization of these peripherals is not done inside the device driver to avoid the race-condition.  
*Example:* Audio Codec A and Audio Codec B all use the same I2C. A doesn\'t know the status of B. If A calls the deinitialization of I2C, the B Codec stops working. 

### Common Software Component

Common software components which are not middleware/stacks are also located in this folder. For example, the NAND Flash Component which implements the common NAND flash logic operation. Another example is the
application timer. The MCUXpresso SDK now integrates several stack/middleware software and some of these solutions provide their own software components. If software components are inside a middleware/stack, these components are split out from these middleware/stacks and moved to
this folder if there are no license issues. 

## Middleware and RTOS

The Middleware folder provides support for various middleware as indicated in the name of the subfolders.

The RTOS folder is a location selected to organize MCUXpresso support for different RTOS. For FreeRTOS, the bus communication driver is also provided with native FreeRTOS support using services provided by FreeRTOS. You can find these RTOS drivers in the same location as the peripheral drivers.

### RTOS support outside SDK repository

The MCUXpresso SDK also supports other RTOS but not in the repository of the SDK.  

Zephyr/Ali-OS/MBED OS are supported in their respective online communities. Users can find support in these public repositories.  

### OSA

The MCUXpresso SDK doesn\'t provide support for the unified OSA layers. Middleware requiring OSA now includes the necessary support inside the respective middleware folder.

## Application

The MCUXpresso SDK `/examples` folder provides application examples.  

There are various subfolders that group the available examples.  

The `/demo_apps`, `/driver_examples`, and `/cmsis_driver_examples` are default for every board, other subfolders are prepared for middleware like `/usb_examples`.  
These examples include (but are not limited to):
-   `/cmsis_driver_examples`: Simple applications intended to illustrate concisely how to use CMSIS drivers

-   `/demo_apps`: Full-featured applications intended to highlight key
    functionality and use cases of the target MCU. These applications
    typically use multiple MCU peripherals and use stacks and
    middleware

-   `/driver_examples`: Simple applications intended to illustrate concisely how to use the peripheral drivers for a single-use case. These applications typically only use a single peripheral, but there are cases where multiple are used (for example, SPI conversion using DMA)

-   `/emwin_examples`: Applications that use the emWin GUI widgets

-   `/rtos_examples`: Basic FreeRTOS OS examples showcasing the use of
    various RTOS objects (semaphores, queues, and so on) and interfacing
    with the MCUXpresso SDK RTOS drivers

-   `/usb_examples`: Applications that use the USB host/device/OTG stack

-   This list continues to expand as more software components are integrated into the MCUXpresso SDK

MCUXpresso SDK board support provides example applications for NXP
development and evaluation boards.  
Board support packages are found inside the `/boards` folder.  
Each supported board has its own folder (an MCUXpresso SDK package can support multiple boards). 
Board here means the evaluation board created by the NXP available to
customer. Kits here mean a shield board without a microcontroller inside.
Kits must interface with an evaluation board by a connector like the Arduino interface. For example, inside the EVKB-IMXRT1050 packages `/boards` folder, evkbimxrt1050 is the evaluation board. evkbimxrt1050_agm01 is a shield board which can work with the EVKB-IMXRT1050 board with an Arduino connector. The AGM01 shield board gets multiple sensors on the board for a user to evaluate NXP sensor products and software.

### Project Structure

This section describes how the various types of example applications
interact with the other components in the MCUXpresso SDK.

Each \<board_name\> folder in the boards directory contains a
comprehensive set of examples that are relevant to that specific piece
of hardware.  

The following discusses the hello_world example (part of the demo_apps folder), but the same rules generally apply to the other examples.

All files in the application folder are specific to that example, so it
is easy to copy and paste an existing example to start developing a
custom application based on a project provided in the MCUXpresso SDK.

![](media/image2.png)

### Board Configuration: board.c/h

`board.c/h` Files are prepared for each board during development. 
MCUXpresso SDK release packages include board.h/c files in each project. These files provide macros and functions that provide a base configuration for a specific board. This configuration is often common among multiple examples. These files are created manually.  

For example, in the FRDM-K64F board, the UART0 is connected to OPENSDA K20
chips and the user can connect to the K20 from a PC to get the log input. The board file configures the UART0 pins connected to OPENSDA K20 as the DEBUG CONSOLE so that all cases using the debug console do not need to define the macros themselves instead using the macros directly.

### Clock configuration : clock_config.c/h

Clock configuration files are generated by the MCUXpresso Config Tools. The user can import, modify, and update these files using the Config Tools. Clock configuration files provide multiple clock configuration functions for the example application to call. MCUXpresso SDK prepares a common set of clock configurations that most of the example applications can reuse. For applications with unique requirements for code size or clock mode, they can use the Config Tools to customize the clock configuration files.

### PIN configuration: pin_mux.c/h

Pin mux configuration files are generated by the MCUXpresso Config Tools. The user can import, modify, and update these files using the Config Tools. Pin mux configuration files are always customized for each application. The pin mux files are created for a specific SoC but not for a board. If the same pin configuration was included for a board, a lot of unused functions exist that are not needed for a specific example.

### Project Template

Users are not intended to directly use the files in the project template. Instead, it provides a starting point for the MCUXpresso Config Tool or CMSIS Pack to create a project. It provides the basic template of a main file, pin mux configuration files, clock configuration files and so on. Project templates exist based on SoCs and boards. The template used depends on if the request to create a project was for an SoC or a specific board.  

The Project templates are located in:  
-  `/examples/_boards/\<board_name_or_kit_name\>/project_template/`   

- `/devices/<soc\>/\<soc_family\>/\<soc_name>/`   

**_NOTE_** The project template files must be verified to be compatible with a specific release version of the MCUXpresso Config Tool.

## Build and Configuration System

MCUXpresso SDK build and configuration system is based on [CMake](https://cmake.org/) and [Kconfig](https://www.kernel.org/doc/html/next/kbuild/kconfig-language.html). It serves every aspect of the software development:

- Toolchain setup
- Device enablement
- Board enablement
- Shield enablement
- Component configuration and integration
- Example configuration, complication, download and debug

All software data are recorded in cmake, Kconfig and misc yaml files. All functionality commands and arguments have been integrated into MCUXpresso `west` extension which can be easily used. Please refer [Build and Configuration System](build_system/index.rst) for more details.

## Documentation

Documents are located in the `/docs` folder.  

The Release Notes, Getting Started Guide, API Reference Manual and Change Log document are provided.

### Release Notes

Release notes are included with each release of the MCUXpresso SDK. It
introduces what is delivered in the SDK package and which tools were used to test the
package. It also lists any known issues for the release.  
The MCUXpresso SDK on GitHub delivers support for multiple devices and boards. The Release notes provide a Quality Level for the software support of each device/board. The quality levels are: RFP, EAR, MIN, NON.

### Getting Started Guide

The **Getting Started Guide** is a valuable resource when first evaluating the MCUXpresso SDK. It includes a clear procedure on how to use the SDK package. It outlines steps to begin working with a typical SDK project.

The user is shown how to compile, program, and debug an application for a specific board.  

### API Reference Manual and Change Log

The **API Reference Manual** details the API and data structures for a given software component. The content is generated from the doxygen tag in the source code.  

**Change Log** is a document describing the changes for software components in the package. They are generated from the doxygen information.
