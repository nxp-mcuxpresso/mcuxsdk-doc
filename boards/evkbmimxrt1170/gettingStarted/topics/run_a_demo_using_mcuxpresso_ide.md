# Run a demo using MCUXpresso IDE

**Note:**

Most MCUXpresso projects provide two targets \(debug and release\). For CM7 projects, they are actually flash target. For CM4 projects, they are linked to RAM. To debug and run the CM7 examples, set **SW1\[1:4\]** to **0010** as internal flash boot mode. Currently, MCUXpresso IDE does not support CM4 download/debug.

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug example applications. The `hello_world` demo application targeted for the MIMXRT1170-EVKB hardware platform is used as an example, though these steps can be applied to any example application in the MCUXpresso SDK.


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

