# Building an example application 

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install an SDK. In the window that appears, click **OK** and wait until the import has finished.

    ![](../images/ide_installing_an_sdk.jpg "Install an SDK")

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**.

    ![](../images/ide_importing_an_sdk_example.jpg "Import an SDK example")

3.  In the window that appears, expand the **mcx** folder and select **MCXW72**. Then, select **mcxw72evk** and click **Next**.

    ![](../images/ide_selecting_kw4x_board.png "Select KW4x board")

4.  Expand the `demo_apps` folder and select `hello_world`. Then, click **Next**.

    ![](../images/ide_selecting_hello_world.png "Select hello_world")

5.  Ensure **Redlib: Use floating point version of printf** is selected if the example prints floating point numbers on the terminal for demo applications such as `adc_basic`, `adc_burst`, `adc_dma`, and `adc_interrupt`. Otherwise, it is not necessary to select this option. Then, click **Finish**.

    ![](../images/ide_selecting_user_floating_print_version_of_printf.png "Select Use floating point version of printf")


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/running_a_demo_using_mcuxpresso_ide.md)

