# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install an SDK. In the window that appears, click **OK** and wait until the import has finished.

    ![](../images/ide_install_an_sdk.png "Install an SDK")

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**.

    ![](../images/ide_import_sdk_example.jpg "Import an SDK example")

3.  In the window that appears, select **MIMXRT1176xxxxx**. Then, select **evkbmimxrt1170** and click **Next**.

    ![](../images/ide_select_mimxrt1170-evk_board.png "Select MIMXRT1170-EVKB board")

4.  Expand the *demo\_apps* folder and select `hello_world`. Then, click **Next**.

    ![](../images/ide_select_hello_world.png "Select hello_world")

5.  Ensure **Redlib: Use floating point version of printf** is selected if the example prints floating point numbers on the terminal for demo applications such as `adc_basic`, `adc_burst`, `adc_dma`, and `adc_interrupt`. Otherwise, it is not necessary to select this option. Then, click **Finish**.

    ![](../images/ide_select_user_floating_print_version_printf.png "Select Use floating point version of printf")


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

