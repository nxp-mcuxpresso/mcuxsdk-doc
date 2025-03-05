# Build an example application

To build an example application, follow these steps.

1.  Open a GCC Arm Embedded tool chain command window. To launch the window, from the Windows operating system Start menu, go to **Programs** -\> **GNU Tools Arm Embedded <version\>** and select **GCC Command Prompt**.

    |![](../images/launch_command_prompt_20.jpg "Launch command prompt")

|

2.  Change the directory to the example application project directory, which has a path similar to the following:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/armgcc
    ```

    For this example, the exact path is:

    ```
    <install_dir>/boards/mcimx93qsb/demo_apps/hello_world/armgcc
    ```

3.  Type **build\_debug.bat** on the command line or double click on the `build_debug.bat` file in Windows Explorer to perform the build.

**Parent topic:**[Windows OS host](../topics/windows_os_host.md)

