# Explore MCUXpresso SDK
This section helps you build basic understanding of current fundamental project content and guide you how to build and run the provided example project in whole SDK delivery.

## Folder View
The fundamental project, alias the core project in west workspace which places in the folder `core`. The core project focus on the delivery of device support, board support, shared peripheral drivers and components.

| Folder | Description |
| :--------- | :-------- |
| examples | Board support package. For each board, there are board configuration files. |
| arch | Arch related files such as ARM CMSIS core files. |
| components | Software components. |
| devices | Device support package. For each device, header file, feature file, startup file and linker files are provided, also device specific drivers are included. |
| docs | Documentation. |
| drivers | Peripheral drivers. |
| middleware | Middleware components used in software examples. |
| tools | Software tools. |
| utilities | Software utilities. |

## Examples Project

The examples project part of the whole SDK delivery, and locates in the folder `core/examples` of west workspace.

Examples files are placed in folder of `<example_category>`, these examples include (but are not limited to)

* demo_apps: Basic demo set to start using SDK, including hello_world and led_blinky.
* driver_examples: Simple applications that show how to use the peripheral drivers for a single use case. These applications typically only use a single peripheral but there are cases where multiple peripherals are used (for example, SPI transfer using DMA).

Board porting layers are placed in folder of `_boards/<board_name>` which aims at providing the board specific parts for examples code mentioned above.
