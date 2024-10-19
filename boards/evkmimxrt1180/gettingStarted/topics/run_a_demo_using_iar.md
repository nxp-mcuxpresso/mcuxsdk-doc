# Run a demo using IAR {#GUID-BA1042A5-8F45-4771-B42C-476D7C55C064}

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. This document uses `hello_world` demo application targeted for the MIMXRT1180-EVK as an example. These steps can be applied to any example application in the MCUXpresso SDK.

Both CMSIS-DAP and J-Link debugging interfaces are supported for IAR IDE. It is recommended to set `SW5[1..4]` to `0001` for both debugging interfaces. It is required to reset board for each download/debug.


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
