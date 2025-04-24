# Build an example application

The following steps guide you through opening the `hello_world` example application. These steps may change slightly for other example applications, as some of these applications may have additional layers of folders in their paths.

1.  If not already done, open the desired demo application workspace. Most example application workspace files can be located using the following path:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/iar
    ```

    Using the i.MX 93 AUTO EVK board as an example, the workspace is located in:

    ```
    <install_dir>/boards/mcimx93autoevk/demo_apps/hello_world/iar/hello_world.eww
    ```

2.  Select the desired build target from the drop-down. For this example, select **hello\_world – debug**.

3.  To build the demo application, click **Make**.

    |![](../images/demo_build_target_selection_8mm.png "Demo build target selection")

|

4.  The build completes without errors.

**Parent topic:**[Program flash.bin to SD/eMMC with UUU](../topics/run_a_flash_target_demo_by_uuu.md)

