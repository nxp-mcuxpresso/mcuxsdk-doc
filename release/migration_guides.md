# MCUXpresso SDK Migration Guide

## Introduction
Starting with version **25.12.00**, the Arm GCC SDK package will have a new format. The new format will unify the **CMake + Kconfig** support between the SDK package and the GitHub repository. When users select Arm GCC in SDK Builder, the system will deliver a ZIP package that contains similar folders/files to that found in the GitHub SDK distribution. Additionally, VS Code integration provides access to Arm GCC Archive SDK packages. Starting with 25.12.00, VS Code will import the same Arm GCC Archive SDK package users download from the SDK Builder site.

## Overview of Changes
- VS Code and GitHub workflows are based on CMake.
- The CMakelists.txt and folder/file structure are now consistent for any Arm GCC SDK. (Archive packages and GitHub repositories)
- **Upcoming Change:** Starting with version 25.12.00, Arm GCC SDK will be delivered through a ZIP package, ensuring unified **CMake + Kconfig** support across SDK builder distributions and GitHub workflows.

## Folder Structure Changes
Below are the differences in the SDK structure from older versions to the new SDK version 25.12.00 moving forward. 

## SDK Folder Structure Comparison  
Starting with SDK version 25.12.00, the overall organization of the SDK has been streamlined to improve modularity and maintainability for the Arm GCC SDK.  
In previous releases, most source files and configuration files were grouped under the boards directory. In the new structure, the SDK introduces a centralized mcuxsdk folder that contains shared components, drivers, middleware, and examples. This change makes it easier to reuse code across multiple boards and projects. While some folders will translate directly to what was seen previously, there will also be new folders introduced to support the new CMake and Kconfig build system. 
  
| **25.09.00 and Prior Releases** | **25.12.00 and Future Releases**  |
|---|---|
|📁 ***boards***<br> 📁 CMSIS<br>📂 components<br>📁 devices<br>📁 docs<br>📁 middleware<br>📁 rtos<br>📁tools<br> |📁 .west<br> 📁 manifests<br>📂 mcuxsdk<br>├── 📁 arch<br>├── 📁 cmake<br>├── 📁 components<br>├── 📁 devices<br>├── 📁 drivers<br>├── 📁 ***examples***<br>├── 📁 middleware<br>├── 📁 rtos<br>├── 📁 scripts<br>├── 📁 share<br>└── 📁 tool_data |  
For more details on how to use the new SDK structure, refer to [Workspace Structure](../gsd/explore_sdk.md)  
  
## Project Structure Changes  
The new SDK format introduces changes to how projects are organized and configured.
In the new project structure:  
- Your application source files (e.g., hello_world.c) remain within the example folder, so you still have everything you need to build and modify your demo.  
- Board-specific files (like pin_mux.c, clock_config.c, and hardware initialization code) are no longer inside the same project folder. These are now located in shared directories under mcuxsdk further details in [board specific files](../gsd/explore_sdk.md#board-specific-files).  
- Build configuration files (CMakeLists.txt, Kconfig, example.yaml) are included in the example folder for easier project setup.

Looking at FRDM-MCXN947 as an example, we can see how a hello_world demo application is structured:  

| **25.09.00 and Prior Releases** | **25.12.00 and Future Releases** |
---|---|
|📁 boards<br>└─ 📁 frdmmcxn947<br>└─ 📁 demo_apps<br>└─ 📁 hello_world<br>└─ 📁 cm33_core0<br>├─ 📁 armgcc<br>│ └─ 📄 ***CMakeLists.txt***<br>├─ 📄 app.c<br>├─ 📄 board.c<br>├─ 📄 board.h<br>├─ 📄 clock_config.c<br>├─ 📄 clock_config.h<br>├─ 📄 example_board_readme.md<br>├─ 📄 examples_shared_readme.md<br>├─ 📄 hardware_init.c<br>├─ 📄 ***hello_world.c***<br>├─ 📄 mcux_config.c<br>├─ 📄 pin_mux.c<br>├─ 📄 pin_mux.h<br>└─ 📄 readme.md |📁 mcuxsdk<br>└─ 📁 examples<br>└─ 📁 demo_apps<br>└─ 📁 hello_world<br>├─ 📄 ***CMakeLists.txt***<br>├─ 📄 example.yaml<br>├─ 📄 ***hello_world.c***<br>├─ 📄 Kconfig<br>└─ 📄 readme.md |  
For more details on how to build and run a project, refer to [First Build](../gsd/first_build.md)  


## What’s New in Projects

### **MCUXpresso SDK CMake extensions and configuration**    
The CMake extensions can be reviewed in the `mcuxsdk/cmake` folder. These extensions introduce an abstraction layer that significantly reduces the complexity of individual `CMakeLists.txt` files, making them more minimal and easier to maintain.

Instead of requiring developers to manually declare toolchains, link flags, source lists, and post-build steps, the SDK provides macros and functions (such as `mcux_add_source`, `mcux_convert_binary`, etc.) that encapsulate these repetitive tasks. This approach improves portability and enforces consistency across projects.

However, the abstraction does not hide the underlying logic entirely. The extension scripts expose the **atomic CMake commands** they rely on—such as `add_executable`, `target_link_libraries`, and `add_custom_command`—within modular files. This transparency allows developers to:
- Understand how the build system is structured.
- Inspect or override specific behaviors when needed.
- Learn the mapping between high-level SDK macros and standard CMake primitives.

In short, the extensions strike a balance between **simplicity for day-to-day use** and **visibility for advanced customization**, making the build system both developer-friendly and flexible.

  
| **Category** | **25.09.00 and Prior Releases** | **25.12.00 and Future Releases** | **Why the Change** |
|---|---|---|---|
| **CMake version & system** | `cmake_minimum_required(3.10)`, sets `CMAKE_SYSTEM_NAME Generic`; custom build types | `cmake_minimum_required(3.22)`; relies on MCUXpresso SDK CMake extensions | Align with modern CMake features and SDK automation |
| **SDK integration** | Manual includes: `devices/MCXN947/all_lib_device.cmake`; local `flags.cmake`, `config.cmake` | Centralized SDK extension: `include(${SdkRootDirPath}/cmake/extension/mcux.cmake)` and root `CMakeLists.txt` | Reduce duplication and enforce consistent SDK structure |
| **Project declaration** | `project(hello_world_cm33_core0)` + `enable_language(ASM)` | `project(hello_world LANGUAGES C CXX ASM PROJECT_BOARD_PORT_PATH …)` | Support multi-language builds and board-specific paths |
| **Source definition** | `add_executable(...)` with explicit file list | `mcux_add_source(BASE_PATH … SOURCES …)` (SDK macro) | Simplify source management and improve portability |
| **Board/config overrides** | Includes local `flags.cmake`, `config.cmake` | Optional board-level `reconfig.cmake` | Enable flexible board-level customization without manual edits |
| **Linking** | Manual system libs `-lm -lc -lgcc -lnosys`; start/end group wrapping | Linking abstracted by SDK; no explicit system lib flags | Avoid manual link order issues and leverage SDK defaults |
| **Post-build** | `objcopy -Obinary` to produce `hello_world.bin` | `mcux_convert_binary(BINARY …)` (SDK macro) | Standardize binary conversion and reduce custom commands |
| **Build outputs** | `EXECUTABLE_OUTPUT_PATH` and `LIBRARY_OUTPUT_PATH` set manually | Uses `${APPLICATION_BINARY_DIR}` (SDK-managed) | Centralize output handling for multi-config


### **Kconfig Support**
The new project format introduces **Kconfig**, which enables advanced configuration management.

- Kconfig provides **GUIConfig**, a visual interface for setting key software configuration symbols and values.
- This makes it easier to customize features without manually editing configuration files.

### For more details:
- [**Kconfig User Guide**](../gsd/using_kconfig.md)
- [**GuiConfig Overview**](../gsd/using_kconfig.md#2-guiconfig-tool-to-explore-kconfig-symbols)
- [**Using CMake Extensions**](../gsd/cmake_project_walkthrough.md)


## Getting Started with 25.12.00 SDK
While the content noted above has changed, the process for importing the SDK and projects remains the same:

- [**Use SDK Builder**](../gsd/install/sdk_builder.md) to download your Arm GCC SDK as a ZIP/archive file
- [**Import SDK**](../gsd/install/github.md) to download your Arm  GCC SDK from GitHub directly to your VS Code workspace
- [**Import projects**]() and checkout the new project structure
- [**Build and run**]() a project using the updated CMake configuration


## Additional Resources
- [MCUXpresso for VS Code Docs](https://docs.mcuxpresso.nxp.com/mcux-vscode/latest/html/index.html)
- [MCUXpresso GitHub SDK Distribution](https://github.com/nxp-mcuxpresso/mcuxsdk-manifests)
- [MCUxpresso Archive SDK Builder](https://mcuxpresso.nxp.com/)



