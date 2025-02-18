# Run a demo application using IAR 
This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK.

**Note:**

IAR Embedded Workbench for Arm version 9.50.1 is used in the following example, and the IAR toolchain should correspond to the latest supported version, as described in the *MCUXpresso SDK Release Notes for MIMXRT700-EVK* \(document MCUXSDKRT798RN\).

When debug or run the `flash_debug` or `flash_release` targets, make sure that the board is configured as XSPI0 boot mode \(SW10 1 - OFF, 2 - ON\).


```{include} ../topics/iar_build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_run_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_build_and_run_a_multicore_example_application.md
:heading-offset: 1
```

