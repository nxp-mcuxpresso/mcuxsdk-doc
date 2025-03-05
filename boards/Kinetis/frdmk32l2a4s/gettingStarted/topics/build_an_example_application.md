# Build an example application

To build an example application, follow these steps.

1.  Open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system Start menu, go to **Programs** -\> **GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

    ![](../images/launch_command_prompt_20.jpg "Launch command prompt")

2.  Change the directory to the example application project directory, which has a path similar to the following:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc
    ```

    For this example, the exact path is:

    ```
    <install_dir>/examples/frdmk32l2a4s/demo_apps/hello_world/armgcc
    ```

    **Note:** To change directories, use the `cd` command.

3.  Type **build\_debug.bat** on the command line or double click on the `build_debug.bat` file in Windows Explorer to perform the build. The output is shown in this figure:

    ![](../images/hello_world_demo_build_successful_k32l2a4s.png "hello_world demo build successful")


**Parent topic:**[Run a demo using Arm® GCC](../topics/run_a_demo_using_arm__gcc.md)

