# Run a demo application using IAR

**Note:**

When erasing flash on IAR, IAR will show all range that can connect to flash. Please only check address flash connect to practically. Take the evkmimxrt1160 for example:

-   M7: 0x30000000-0x3fffffff
-   M4: 0x8000000-0x17ffffff

When using IAR download/debug `flexspi_nor` related targets, make sure the boot switch is put to internal flash boot mode **SW1\[1:4\]:0010**.

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. The `hello_world` demo application targeted for the MIMXRT1160-EVK hardware platform is used as an example, although these steps can be applied to any example application in the MCUXpresso SDK.


```{include} ../topics/build_an_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/run_an_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/build_a_multicore_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/run_a_multicore_example_application_001.md
:heading-offset: 1
```

