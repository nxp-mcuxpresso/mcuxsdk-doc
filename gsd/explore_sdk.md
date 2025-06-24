# Explore Contents
This section helps you build basic understanding of current fundamental project content and guides you how to build and run the provided example project in whole SDK delivery.

## Folder View
The whole MCUXpresso SDK project, after you have done the `west init` and `west update` operations follow the guideline at [Getting Started Guide](installation.md#get-mcuxpresso-sdk-repo), have below folder structure:

| Folder | Description |
| :--------- | :-------- |
| manifests | Manifest repo, contains the manifest file to initialize and update the west workspace. |
| mcuxsdk | The MCUXpresso SDK source code, examples, middleware integration and script files. |

All the projects record in the [Manifest repo](https://github.com/nxp-mcuxpresso/mcuxsdk-manifests) are checked out to the folder `mcuxsdk/`, the layout of mcuxsdk folder is shown as below:

| Folder | Description |
| :--------- | :-------- |
| arch | Arch related files such as ARM CMSIS core files, RISC-V files and the build files related to the architecture. |
| cmake | The cmake modules, files which organize the build system. |
| components | Software components. |
| devices | Device support package which categorized by device series. For each device, header file, feature file, startup file and linker files are provided, also device specific drivers are included. |
| docs | Documentation source and build configuration for this sphinx built online documentation. |
| drivers | Peripheral drivers. |
| examples | Various demos and examples, support files on different supported boards. For each board support, there are board configuration files. |
| middleware | Middleware components integrated into SDK. |
| rtos | Rtos components integrated into SDK. |
| scripts | Script files for the west extension command and build system support. |
| svd | Svd files for devices, this is optional because of large size. Customers run `west manifest config group.filter +optional` and `west update mcux-soc-svd` to get this folder. |


## Examples Project

The examples project is part of the whole SDK delivery, and locates in the folder `mcuxsdk/examples` of west workspace.

Examples files are placed in folder of `<example_category>`, these examples include (but are not limited to)

* demo_apps: Basic demo set to start using SDK, including hello_world and led_blinky.
* driver_examples: Simple applications that show how to use the peripheral drivers for a single use case. These applications typically only use a single peripheral but there are cases where multiple peripherals are used (for example, SPI transfer using DMA).

Board porting layers are placed in folder of `_boards/<board_name>` which aims at providing the board specific parts for examples code mentioned above.
