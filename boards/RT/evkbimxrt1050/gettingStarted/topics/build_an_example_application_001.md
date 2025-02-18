# Build an example application

To build an example application, follow these steps.

1.  Drag and drop the SDK zip file into the **Installed SDKs** view to install the MCUXpresso SDK. In the window that appears, click **OK** and wait until the import has finished.

    ![](../images/install_an_sdk.png "Install an SDK")

2.  On the **Quickstart Panel**, click **Import SDK example\(s\)…**, as shwon in [Figure 2](build_an_example_application_001.md#IMPORTANSDKEXAMPLE).

    ![](../images/import_sdk_example.png "Import an SDK example")

3.  In the window that appears, expand the **MIMXRT1050** folder and select **MIMXRT1052xxxxx**. Then, select **evkbimxrt1050** and click **Next**, as shown in [Figure 3](build_an_example_application_001.md#SELECTBOARD).

    ![](../images/select_evkb-imxrt1050_board.png "Selecting EVKB-IMXRT1050 board")

4.  Expand the `demo_apps` folder, select `hello_world`, and then click **Next**, as shown in [Figure 4](build_an_example_application_001.md#SELECTHELLOWORLDCASE).

    ![](../images/select_hello_world_rt1050.png "Selecting hello_world")

5.  Ensure the option **Redlib: Use floating point version of printf** is selected if the cases print floating point numbers on the terminal \(for demo applications such as `dac32_adc12`, `dac_adc`, `dac_cadc`, `ecompass`, `sai`, `coremark`, `mbedtls_benchmark`, `wolfssl_benchmark`, and for `mmcau_examples` such as `mmcau_api`\). Otherwise, there is no need to select it. Click **Finish**.

    ![](../images/use_floating_print_version_printf_rt1050.png "Selecting User floating point version of printf")

    **Note:** If you want to use semihost to print log, first select the **Semihost** button when importing projects, as shown in [\#FLOAATING](#FLOAATING).

6.  On the **Quickstart** panel, click **build ``**, as shown in [\#FSLOATINSG](#FSLOATINSG).


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

