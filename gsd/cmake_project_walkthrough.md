# MCUXpresso SDK Projects with NXP CMake Format
## User Guide / Walkthrough

### 1. Introduction
This section explains how to use MCUXpress Cmake extensions. How to add/remove and customize projects with NXP cmake format. This guide uses the `hello_world` demo application to demonstrate how use the cmake project format.

### 2. Prerequisites
- MCUXpresso SDK 25.09 or newer installed
- MCUXpresso SDK developer (Installed with MCUXpresso Installer)
- Basic understanding of CMake syntax

> FIXME:

### 3. Understanding NXP CMake Format
The NXP build system uses macros to simplify project configuration:
- include(mcux_config) → Loads board and SDK settings
- mcux_add_source(<file>) → Adds source files
- mcux_add_include(<path>) → Adds include directories
- mcux_add_component(<component>) → Adds SDK components (drivers, middleware)


Directory Structure Example:
boards/
  └── <board_name>/
       ├── demo_app/
       │    ├── source/
       │    │    └── main.c
       │    └── CMakeLists.txt
       └── CMakeLists.txt
> END FIXME

### 4. Import a project and examine the CMakeLists.txt file 
> Note: See [Run a demo using MCUXpresso for VS Code](run_a_demo_using_mcuxvsc.md) for project import walkthrough.
- Steps:
  - Import Hello_World for your device as a freestanding project
  - Expand the project from the **PROJECTS** view
  - Expand the **Project Files** directory
  - Open the **CMakeLists.txt** file
  ![project cmakelists](images/mcuxvsc_cmakelists_location_in_src_pane.png)

- This CMakeLists.txt file is what we will use to configure the project
![CMakelists.txt file](images/mcuxvsc_cmakelists_file.png)


### 5. Adding Source files to the project
In this step, we will turn our Hello_World project into Hello_Blinky. We can do this by adding source files explicitly using the NXP CMake extension **mcux_add_source()**. For the completeness, we will create an include directory for header files and add those into the project.

- Steps:
    - Create a new source file. Name it blink.c
        - Insert the following code snippet into blink.c
        ```C
        #include "fsl_gpio.h"
        void blink_led(void) {
        GPIO_PortToggle(GPIO, 1u << 5); // Example pin toggle
        }
        ```
    - Create a header file blink in an include directory
        - Insert


### 6. Adding required drivers

### 7. Adding sompiler flags

### 7. Build and Verify

### 8. References
