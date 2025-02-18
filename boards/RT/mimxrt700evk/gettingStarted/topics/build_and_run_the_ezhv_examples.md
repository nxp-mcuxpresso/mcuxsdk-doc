# Build and run the ezhv\_examples 

This section describes the steps required to configure the environment to build, run, and debug ezhv example applications. The *<install\_dir\>/boards/<board\_name\>/ezhv\_examples/led\_blinky* is used as an example.

For each example, generally there are two folders, one for the cm33\_core0 core and the other for the EZHV core. For the `led_blinky` example, they are:

*<install\_dir\>/boards/<board\_name\>/ezhv\_examples/led\_blinky/cm33\_core0*

*<install\_dir\>/boards/<board\_name\>/ezhv\_examples/led\_blinky/ezhv*

Build the application for the auxiliary core \(ezhv\) first, because the primary core application project \(`cm33_core0`\) must know the auxiliary core application binary when running the linker. When the auxiliary core application binary is not ready, it is impossible to finish the primary core linker. This section focuses on the auxiliary core \(ezhv\). For details about building the primary core for different toolchain, see the corresponding chapter.


```{include} ../topics/ezhv_set_the_toolchain_for_ezhv.md
:heading-offset: 1
```

```{include} ../topics/ezhv_build_the_ezhv_project.md
:heading-offset: 1
```

```{include} ../topics/ezhv_run_the_project.md
:heading-offset: 1
```

