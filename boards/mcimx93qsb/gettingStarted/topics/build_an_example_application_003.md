# Build an example application

Perform the following steps to build the `hello_world` example application.

1.  Open the desired demo application workspace. Most example application workspace files can be located using the following path:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/iar
    ```

    Using the i.MX 93 QSB hardware platform as an example, the `hello_world` workspace is located in:

    ```
    <install_dir>/boards/mcimx93qsb/demo_apps/hello_world/iar/hello_world.eww
    ```

    Other example applications may have additional folders in their path.

2.  Select the desired build target from the drop-down menu.

    For this example, select **hello\_world** – **debug**.

    |![](../images/demo_build_target_selection_imx8mq.png "Demo build target selection")

|

3.  To build the demo application, click **Make**, highlighted in red in [Figure 2](build_an_example_application_003.md#BUILDINGDEMOAPP).

    |![](../images/build_demo_application_imx8mq.png "Build the demo application")

|

4.  The build completes without errors.

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

