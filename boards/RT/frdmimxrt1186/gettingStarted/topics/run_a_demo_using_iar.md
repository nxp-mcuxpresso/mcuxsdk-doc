# Run a demo using IAR

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. This document uses `hello_world` demo application targeted for the FRDM-IMXRT1186 as an example. These steps can be applied to any example application in the MCUXpresso SDK.

Both CMSIS-DAP and J-Link debugging interfaces are supported for IAR IDE. Though not mandatory, it is recommended to reset board for each download/debug. **Since IAR and Segger are not ready for FRDMIMXRT1186 currently, 3rd party patch is provided: [iar_segger_support_patch_rt1186](https://mcuxpresso.nxp.com/download/e8ca8e655b4a5eeff3d9265ef11fa3f2)**

```{include} ../topics/iar_build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_run_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_build_and_run_a_multicore_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_run_applications_via_JLink_debug_interface.md
:heading-offset: 1
```

