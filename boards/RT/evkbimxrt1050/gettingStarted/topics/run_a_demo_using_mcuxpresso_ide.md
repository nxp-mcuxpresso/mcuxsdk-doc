# Run a demo using MCUXpresso IDE

**Note:**

Ensure that the MCUXpresso IDE toolchain is included when generating the MCUXpresso SDK Package.

MCUXPresso IDE is not supported in this release.

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug example applications. The `hello_world` demo application targeted for the IMXRT1050-EVKB platform is used as an example, though these steps can be applied to any example application in the MCUXpresso SDK.

**Note:** By default, three macros, `XIP_EXTERNAL_FLASH=1`, `XIP_BOOT_HEADER_ENABLE=1`, and `XIP_BOOT_HEADER_DCD_ENABLE=1`, are set in the project. If you do not use `Board_Flash` in the project, these macros should be removed or set value to **0** in project settings.


```{include} ../topics/select_the_workspace_location.md
:heading-offset: 1
```

```{include} ../topics/build_an_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/run_an_example_application.md
:heading-offset: 1
```

