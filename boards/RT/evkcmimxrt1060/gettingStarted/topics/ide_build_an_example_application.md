# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install the MCUXpresso SDK. In the window that appears, click **OK** and wait until the import has finished.

    ![](../images/ide_install_an_sdk.png "Install an SDK")

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**, as shown in [Figure 2](#fig_importsdk).

    ![](../images/ide_import_sdk_example.jpeg "Import an SDK example")

3.  In the window that appears, expand the **MIMXRT1060** folder and select **MIMXRT1062xxxxB**. Then, select **evkcmimxrt1060** and click **Next**, as shown in [Figure 3](#fig_selectrt1060evkc).

    ![](../images/ide_selecting_rt1060_evkc.png "Selecting MIMXRT1060-EVKC board")

4.  Expand the `demo_apps` folder, select `hello_world`, and then click **Next**.

    ![](../images/ide_selecting_hello_world.png "Selecting hello_world")

5.  Ensure the option **Redlib: Use floating-point version of printf** is selected if the cases print floating-point numbers on the terminal \(for demo applications, such as, `dac32_adc12`, `dac_adc`, `dac_cadc`, `ecompass`, `sai`, `coremark`,`mbedtls_benchmark`, `wolfssl_benchmark`, and for `mmcau_examples`, such as, `mmcau_api`\). Otherwise, there is no need to select it. Click **Finish**.

    ![](../images/ide_selecting_user_floating_poing.png "Selecting User floating-point version of printf")

    **Note:** If you want to use `semihost` to print log, first select the **Semihost** button when importing projects, as shown in [Figure 6](#fig_selectingsemihost).

    ![](../images/ide_selecting_semihost.png "Selecting Semihost")

    ![](../images/ide_setting_sdk_debug.png "Setting SDK_DEBUGCONSOLE")

6.  On the **Quickstart Panel** tab, click **Build evkcmimxrt1060\_demo\_apps\_hello\_ world \[Debug\]**, as shown in [Figure 8](#fig_buildhelloworld).

    ![](../images/ide_building_hello_world_case.png "Building hello world case")


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

