# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install the MCUXpresso SDK. In the window that appears, click **OK** and wait until the import has finished.

    ![](../images/install_an_sdk.png "Install an SDK")

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**, as shwon in [Figure 2](build_an_example_application.md#IMPORTANSDKEXAMPLE).

    ![](../images/import_sdk_example.png "Import an SDK example")

3.  In the window that appears, expand the **MIMXRT1011** folder and select **MIMXRT1011xxxxx**. Then, select **evkmimxrt1010** and click **Next**, as shown in [Figure 3](build_an_example_application.md#SELECTBOARD).

    ![](../images/select_evk-imxrt1015_board.png "Selecting MIMXRT1010-EVK board")

4.  Expand the `demo_apps` folder, select `hello_world`, and then click **Next**, as shown in [\#SELECTHELLOWORLDCASE](#SELECTHELLOWORLDCASE).

    ![](../images/figure_29_rt1010.png "Selecting hello_world")

5.  Ensure the option **Redlib: Use floating point version of printf** is selected if the cases print floating point numbers on the terminal \(for demo applications such as `dac32_adc12`, `dac_adc`, `dac_cadc`, `ecompass`, `sai`, `coremark`, `mbedtls_benchmark`, `wolfssl_benchmark`, and for `mmcau_examples` such as `mmcau_api`\). Otherwise, there is no need to select it. Click **Finish**.

    ![](../images/use_floating_print_version_printf_rt1015.png "Selecting User floating point version of printf")

    **Note:** If you want to use semihost to print log, first select the **Semihost** button when importing projects, as shown in [Figure 6](build_an_example_application.md#FLOAATING).

    ![](../images/select_semihost_rt1015.png "Selecting Semihost")

    ![](../images/sdk_debugconsole_rt1015.png "Setting SDK_DEBUGCONSOLE")

6.  On the **Quickstart** panel, click **build `evkmimxrt1010\_demo\_apps\_hello\_world \[Debug\]`**, as shown in [Figure 8](build_an_example_application.md#FSLOATINSG).

    ![](../images/build_hello_world_case_rt1015.png "Building hello world case")


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

