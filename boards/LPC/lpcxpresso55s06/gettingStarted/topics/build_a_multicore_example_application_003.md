# Build a multicore example application {#GUID-EF2033A1-63ED-4522-8BFA-4EF0A7142645}

This section describes the steps to build and run a dual-core application. The demo applications workspace files are located in this folder:

```
*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_type\>/iar*
```

Begin with a simple dual-core version of the Hello World application. The multicore Hello World IAR workspaces are located in this folder:

```
*<install\_dir\>/boards/lpcxpresso55s69/multicore\_examples/hello\_world/cm33\_core0/iar/hello\_world\_cm33\_core0.eww*
```

```
*<install\_dir\>/boards/lpcxpresso55s69/multicore\_examples/hello\_world/cm33\_core1/iar/hello\_world\_cm33\_core1.eww*
```

Build both applications separately by clicking the **Make** button. Build the application for the auxiliary core \(cm33\_core1\) first, because the primary core application project \(cm33\_core0\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

