# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install the MCUXpresso SDK. In the window that appears, click **OK** and wait until the import has finished.

    |![](../images/install_an_sdk.png "Install an SDK")

|

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**, as shown in [Figure 2](build_an_example_application.md#IMPORTANSDKEXAMPLE).

    |![](../images/import_sdk_example.png "Import an SDK example")

|

3.  In the window that appears, expand the **MIMXRT1064** folder and select **MIMXRT1064xxxxx**. Then, select **evkmimxrt1064** and click **Next**, as shown in [Figure 3](build_an_example_application.md#SELECTBOARD).

    |![](../images/select_evkb-imxrt1064_board.png "Selecting MIMXRT1064-EVK board")

|

4.  Expand the `demo_apps` folder, select `hello_world`, and then click **Next**, as shown in [Figure 4](build_an_example_application.md#SELECTHELLOWORLDCASE).

    |![](../images/select_hello_world_rt1064.png "Selecting hello_world")

|

5.  Ensure the option **Redlib: Use floating-point version of printf** is selected if the cases print floating-point numbers on the terminal \(for demo applications such as `dac32_adc12`, `dac_adc`, `dac_cadc`, `ecompass`, `sai`, `coremark`, `mbedtls_benchmark`, `wolfssl_benchmark`, and for `mmcau_examples` such as `mmcau_api`\). Otherwise, there is no need to select it. Click **Finish**.

    |![](../images/select_user_floating_print_version_of_printf_rt106.png "Selecting User
											floating-point
											version of printf")

|

    **Note:** If you want to use semihost to print log, first select the **Semihost** button when importing projects, as shown in [Figure 6](build_an_example_application.md#FLOAATING).

    |![](../images/select_semihost_rt1064.png "Selecting Semihost")

|

    |![](../images/setting_sdk_debugconsole_rt1064.png "Setting "SDK_DEBUGCONSOLE"")

|

6.  On the **Quickstart** panel, click **build `evkmimxrt1064\_demo\_apps\_hello\_world \[Debug\]`**, as shown in [Figure 8](build_an_example_application.md#FSLOATINSG).

    |![](../images/build_hello_world_case_rt1064.png "Building hello world case")

|


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)
