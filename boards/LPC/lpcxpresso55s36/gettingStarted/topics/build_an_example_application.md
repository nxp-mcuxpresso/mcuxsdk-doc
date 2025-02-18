# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install an SDK. In the window that appears, click **OK** and wait until the import has finished.

    |![](../images/install_an_sdk.png "Install an SDK")

|

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**.

    |![](../images/import_sdk_example.png "Import an SDK example")

|

3.  In the window that appears, expand the **LPC55xx** folder and select **LPCX55S36** . Then, select **lpcxpresso55s36** and click **Next**.

    |![](../images/build.png "Select LPCXpresso55S36 board")

|

4.  Expand the `demo_apps` folder and select `hello_world` . Then, click **Next** .

    |![](../images/build_hello.png "Select hello_world")

|

5.  Ensure **Redlib: Use floating point version of printf** is selected if the example prints floating point numbers on the terminalfor demo applications such as `adc_basic`, `adc_burst`, `adc_dma`, and `adc_interrupt`. Otherwise, it is not necessary to select this option. Then, click **Finish**.

    |![](../images/select_use_floating_point_version_printf_rel8.png "Select Use floating point version of printf")

|


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

