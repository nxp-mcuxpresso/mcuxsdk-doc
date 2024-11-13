# Build an example application

To build an example application, follow these steps.

1.  Open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system **Start** menu, go to **Programs** \>**GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

    |![](../images/arm_gcc_launch_command_prompt.png "Launch command prompt")

|

2.  Change the directory to the example application project directory which has a path similar to the following:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc
    ```

    For this example, the exact path is:

    ```
    <install_dir>/boards/frdmke17z/demo_apps/hello_world/armgcc
    ```

    **Note:** To change directories, use the `cd` command.

3.  Type **build\_debug.bat** on the command line or double click on **build\_debug.bat** file in Windows Explorer to build it. The `hello_world.elf` is generated under *.\\debug* folder.


**Parent topic:**[Run a demo using Arm® GCC](../topics/run_a_demo_using_arm__gcc.md)
