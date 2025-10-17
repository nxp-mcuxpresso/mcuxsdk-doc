# Build an example application

The following steps guide you through opening the `hello_world` example application. These steps may change slightly for other example applications, as some of these applications may have additional layers of folders in their paths.

1.  If not already done, open the desired demo application workspace. Most example application workspace files can be located using the following path:

    ```
    <install_dir>/boards/<board_name>/<example_type>/<application_name>/iar
    ```

    Using the i.MX 943 EVK board as an example, the workspace is located in:

    ```
    <install_dir>/boards/imx943_orangebox/demo_apps/hello_world/iar/hello_world.eww
    ```

2.  Select the desired build target from the drop-down. For this example, select **hello\_world - debug**.


3.  To build the demo application, click **Make**.

4.  The build completes without errors.
5.  Rename the generated `hello_world.bin` to `m70_image.bin/m71_image.bin/m33s_image.bin`, then copy it to the uuu tool directory.

**Parent topic:**[Generate flash.bin](../topics/generate_flash_bin.md)

