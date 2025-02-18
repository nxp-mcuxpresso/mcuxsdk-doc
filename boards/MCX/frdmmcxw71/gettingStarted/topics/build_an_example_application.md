# Build an example application

Do the following steps to build the `hello_world` example application..

1.  Open the desired demo application workspace. Most example application workspace files can be located using the following path:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/iar
    ```

    Using the `frdmmcxw71` hardware platform as an example, the `hello_world` workspace is located in:

    ```
    <install_dir>/boards/frdmmcxw71/demo_apps/hello_world/iar/hello_world.eww
    ```

    Other example applications may have additional folders in their path.

2.  Select the desired build target from the drop-down menu.

    For this example, select **hello\_world** – **debug**.

    ![](../images/iar_demo_build_target_selection.jpg "Demo build target selection")

3.  To build the demo application, click **Make**, highlighted in red in [Figure 2](build_an_example_application.md#FIG_BUILDDEMO).

    ![](../images/iar_build_the_demo_application.jpg "Build the demo application")

4.  The build completes without errors.

**Parent topic:**[Running a demo application using IAR](../topics/running_a_demo_application_using_iar.md)

