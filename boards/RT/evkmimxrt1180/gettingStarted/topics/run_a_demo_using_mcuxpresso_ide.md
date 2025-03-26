# Run a demo using MCUXpresso IDE 

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug example applications. The `hello_world` demo application targeted for the MIMXRT1180-EVK hardware platform is used as an example, though these steps can be applied to any example application in the MCUXpresso SDK.

Both CMSIS-DAP and J-Link debugging interface is supported for MCUX IDE. When using CMSIS-DAP debugging interface to debug CM33, the `SW5[1..4]` should be put to `0100` for SPI boot mode.
```{include} ../topics/ide_select_the_workspace_location.md
:heading-offset: 1
```

```{include} ../topics/ide_build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/ide_run_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/ide_build_a_multicore_example_application.md
:heading-offset: 1
```

```{include} ../topics/ide_run_a_multicore_example_application.md
:heading-offset: 1
```

```{include} ../topics/ide_run_applications_via_JLink_debug_interface.md
:heading-offset: 1
```

