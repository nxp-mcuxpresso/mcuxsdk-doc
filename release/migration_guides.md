# MCUXpresso SDK Migration Guide

## Introduction
Starting with version **25.12.00**, the Arm GCC SDK package will have a new format. The new format will unify the **CMake + Kconfig** support between the SDK package and the GitHub repository. When users select Arm GCC in SDK Builder, the system will deliver a ZIP package that contains similar folders/files to that found in the GitHub SDK distribution. Additionally, VS Code integration provides access to Arm GCC Archive SDK packages. Starting with 25.12.00, VS Code will import the same Arm GCC Archive SDK package users download from the SDK Builder site.

## Overview of Changes
- MCUXpresso IDE uses its own project format, while VS Code and GitHub workflows are based on CMake.
- The CMakelists.txt and folder/file structure are now consistent for any Arm GCC SDK. (Archive packages and GitHub repositories)
- Migration focuses on environment setup rather than project restructuring.
- **Upcoming Change:** Starting with version 25.12.00, Arm GCC SDK will be delivered through a ZIP package, ensuring unified **CMake + Kconfig** support across SDK builder distributions and GitHub workflows.

## Folder Structure Changes
Below are the differences in the SDK structure from older versions to the new SDK version 25.12.00 moving forward. 

## SDK Folder Structure Comparison
| **25.09.00 and Prior Releases** | **25.12.00 and Future Releases**  |
|---|---|
|📁 boards<br> 📁 CMSIS<br>📂 components<br>📁 devices<br>📁 docs<br>📁 middleware<br>📁 rtos<br>📁tools<br> |📁 .west<br> 📁 manifests<br>📂 mcuxsdk<br>├── 📁 arch<br>├── 📁 cmake<br>├── 📁 components<br>├── 📁 devices<br>├── 📁 drivers<br>├── 📁 examples<br>├── 📁 middleware<br>├── 📁 rtos<br>├── 📁 scripts<br>├── 📁 share<br>└── 📁 tool_data |
``
## Project Structure Changes
The new SDK format introduces changes to how projects are organized and configured. Looking at FRDM-MCXN947 as an example, we can see how a hello_world demo application is structured:
| **25.09.00 and Prior Releases** | **25.12.00 and Future Releases**  |
|---|---|
| 📂 boards<br>├── 📂 frdmmcxn947<br>│   ├── 📂 demo_apps<br>│  │   ├── 📂 hello_world<br>│  │  │ ├── 📂 cm33_core0<br>│  │ │  │ ├── 📂 armgcc<br>│  │ │ │  │ ├── CMakeLists.txt<br>│  │ │  │ ├── app.c<br>│  │ │  │ ├── board.c/.h<br> │  │ │  │ ├── clock_config.c/.h<br> │  │ │  │ ├── example_board_readme.md<br> │  │ │  │ ├── examples_shared_readme.md<br> │  │ │  │ ├── hardware_init.c<br> │  │ │  │ ├── hello_world.c<br>│  │ │  │ ├── mcux_config.c<br>│  │ │  │ ├── pin_mux.c/.h<br>│  │ │  │ ├── readme.md<br>  | 📂 mcuxsdk<br>├──  📁 examples<br>│   ├── 📁 demo_apps<br>│  │   ├── 📁 hello_world<br>│  │  │ ├── CMakeLists.txt<br>│  │  │ ├── example.yaml<br>│  │  │ ├── hello_world.c<br>│  │  │ ├── Kconfig<br>│  │  │ ├── readme.md<br>
``


## Cmake Changes

| **Category** | **25.09.00 and Prior Releases** | **25.12.00 and Future Releases** | **Why the Change** |
|---|---|---|---|
| **CMake version & system** | `cmake_minimum_required(3.10)`, sets `CMAKE_SYSTEM_NAME Generic`; custom build types | `cmake_minimum_required(3.22)`; relies on SDK’s CMake extensions | Align with modern CMake features and SDK automation |
| **SDK integration** | Manual includes: `devices/MCXN947/all_lib_device.cmake`; local `flags.cmake`, `config.cmake` | Centralized SDK extension: `include(${SdkRootDirPath}/cmake/extension/mcux.cmake)` and root `CMakeLists.txt` | Reduce duplication and enforce consistent SDK structure |
| **Project declaration** | `project(hello_world_cm33_core0)` + `enable_language(ASM)` | `project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH …)` | Support multi-language builds and board-specific paths |
| **Source definition** | `add_executable(...)` with explicit file list | `mcux_add_source(BASE_PATH … SOURCES …)` (SDK macro) | Simplify source management and improve portability |
| **Board/config overrides** | Includes local `flags.cmake`, `config.cmake` | Optional board-level `reconfig.cmake` | Enable flexible board-level customization without manual edits |
| **Linking** | Manual system libs `-lm -lc -lgcc -lnosys`; start/end group wrapping | Linking abstracted by SDK; no explicit system lib flags | Avoid manual link order issues and leverage SDK defaults |
| **Post-build** | `objcopy -Obinary` to produce `hello_world.bin` | `mcux_convert_binary(BINARY …)` (SDK macro) | Standardize binary conversion and reduce custom commands |
| **Build outputs** | `EXECUTABLE_OUTPUT_PATH` and `LIBRARY_OUTPUT_PATH` set manually | Uses `${APPLICATION_BINARY_DIR}` (SDK-managed) | Centralize output handling for multi-config


### Using SDK Release 25.12.00
This guide will focus on those who use the repository ZIP package with ARMGCC toolchain in VS Code or command-line environments.

####  Installing the SDK Repository

 There are two ways to obtain the SDK repository:
 ##### Option 1: Download from SDK Builder
 1. Navigate to [NXP's SDK Builder](https://mcuxpresso.nxp.com/en/builder)
 ![alt text](image.png)
 2. Select your board  
 ![alt text](image-1.png)
 3. Choose **ARM GCC / VS Code** package format  
 ![alt text](image-2.png)
 4. Select Build SDK  
 ![alt text](image-3.png)
 5. Download the ZIP file and extract it to your desired location  
 ![alt text](image-4.png)
To import into VS Code skip to section [Importing the Repository](#importing-the-repository).

 ##### Option 2: Clone from GitHub through VS Code
 1. Open VS Code and click on the MCUXpresso icon in the Activity Bar to open the MCUXpresso panel.  
 ![alt text](image-5.png)
 2. Click **Import Repository** and select the **Remote Archive** tab.  
![alt text](image-6.png)
 3. Select the repository ZIP package you wish to clone and follow the prompts to complete the import process.  
 ![alt text](image-7.png)

#### Importing the Repository

If you have obtained the package from the SDK Builder, follow these steps to import it into VS Code:
1. Open VS Code and click on the MCUXpresso icon in the Activity Bar to open the MCUXpresso panel.  
 ![alt text](image-5.png)
2. Click  **Import Repository** and select the **Local Arcive** tab.  
![alt text](image-6.png) 
3. Navigate to the extracted SDK repository folder and select it to complete the import process.  
![alt text](image-8.png)

#### Importing an example
When your workspace is completely empty you will see that under 'Projects' there will be two options to import an example. If your workspace is not empty, then use the QuickStart panel to import an example.
This guide will focus on importing an example from the repository retrieved previously.

1. Click on **Import Example from Repository** in the **Quickstart Panel** view.  
![alt text](image-9.png)
2. Select the repository you previously imported from the dropdown list.  
![alt text](image-10.png)
3. Select the board   
4. Choose the example application you wish to import.  
5. You will need to select the APP type, i.e. freestanding, standalone or repository application, the name and location of the project.  
6. Next select the toolchain of choice, i.e. as ARM GNU Toolchain.  
7. Click **Import** to complete the import process.  

#### Run an example application

**Note:** for full details on MCUXpresso for VS Code debug probe support, see [MCUXpresso for VS Code Wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/DebugK).

1. Open the **Serial Monitor** from the VS Code's integrated terminal. Select the VCom Port for your device and set the baud rate to 115200 and press **Start Monitoring**.  
![alt text](image-11.png)
2. Navigate to the **PROJECTS** view and click the play button to initiate a debug session.  
    The debug session will begin. The debug controls are initially at the top.  
![alt text](image-12.png)
3. Click **Continue** on the debug controls to resume execution of the code. Observe the output on the **Serial Monitor**.  
![alt text](image-13.png)

#### Exploring the Project Structure
Once you have successfully imported an example, you can explore the project structure in the **File Explorer** view. The project follows a standard CMake-based layout that is consistent across all MCUXpresso SDK releases. The structure of the workspace follows a standardized layout. To get started, refer to [SDK Project Layout](../gsd/explore_sdk.md) for a detailed breakdown of the project hierarchy.


## Additional Resources
- [MCUXpresso for VS Code Wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)
- [Official GitHub Repositories](https://github.com/nxp-mcuxpresso)



