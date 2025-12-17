# Using MCUXpresso Config Tools

MCUXpresso Config tools provide a user-friendly way to configure hardware initialization of your projects. This guide explains the basic workflow with the MCUXpresso SDK west build system and the Config Tools.

## Prerequisites

- GitHub Repository SDK workspace initialized OR Repository-Layout SDK Package extracted
- MCUXpresso Config Tools standalone installed (version 25.09 or above)
- MCUXpresso SDK Project that can be successfully built

## Board Files

MCUXpresso Config Tools generate source files for the board. These files include pin_mux.c/h and clock_config.c/h. The files contain initialization code functions that reflect the hardware configuration in the Config Tools.
Within the SDK codebase, these files are specific for the board and either shared by multiple example projects or specific for one example.
Open or import the configuration from the SDK project in the Config Tools and customize the settings to match the custom board or specific project use case and regenerate the code. See *User Guide for MCUXpresso Config Tools (Desktop)*  (document [GSMCUXCTUG](https://www.nxp.com/doc/GSMCUXCTUG) ) for details.

**Note:** When opening the configuration for SDK example projects, the board files may be shared across multiple examples. To ensure a separate copy of the board configuration files exists, create a freestanding project with copied board files.

## Visual Studio Code

To open the configuration in Visual Studio Code, use the context menu for the project to access Config Tools. See [MCUXpresso Extension Documentation](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Working-with-MCUXpresso-Config-Tools.html) for details.  
Otherwise, use the manual workflow described in detail in the following section.

## Manual Workflow

Use the following steps:

1. Before using Config Tools, run the west command to get the project information for Config Tools from the SDK project files, for example:
   ```
   west cfg_project_info -b lpcxpresso55s69 ...mcuxsdk/examples/demo_apps/hello_world/ -Dcore_id=cm33_core0
   ```
   This results in the creation of the project information json file that is searched by the config tools when the configuration is created. The parameters of the command should match the build parameters that will be used for the project.

2. Launch the MCUXpresso Config Tools and in the **Start development** wizard, select **Create a new configuration based on the existing IDE/Toolchain project**. Select the created "cfg\_tools" subfolder as a project folder \(for example: ...`mcuxsdk/examples/demo_apps/hello_world/cfg_tools/`\).


### Updating the SDK West project

**Note:** Updating project is supported with Config Tools V25.12 or newer only.

Changes in the Config tools generated source code modules may require adjustments to the toolchain project to ensure a successful build. These changes may mean, for example, adding the newly generated files, adding include paths, required drivers, or other SDK components.
This section describes how to manually resolve the changes needed in the project within the toolchain projects based on the SDK project managed by the West tool.

After the configuration in the Config Tools is finished, write updated files to the disk using the 'Update Code' command. The written files include a json file with the required changes for the toolchain project. 

To resolve the changes in the project in the terminal, launch the west command that updates the project. For example:
   ```
   west cfg_resolve -b lpcxpresso55s69 ...mcuxsdk/examples/demo_apps/hello_world/ -Dcore_id=cm33_core0
   ```
   This command updates the appropriate cmake and kconfig files to address the changes. After this, the application can be built.

**Note:** The cfg_resolve command supports additional arguments. Launch the *west cfg_resolve -h* command to get the list and description.
