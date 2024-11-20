# Build a multicore example application {#GUID-3DF2B1FC-DBD9-498A-BDA3-A654B7201B48}

This section describes the steps to build and run a dual-core application. The demo applications workspace files are located in this folder:

```
*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_type\>/mdk*
```

Begin with a simple dual-core version of the Hello World application. The multicore Hello World Keil MSDK/μVision workspaces are located in this folder:

```
*<install\_dir\>/boards/lpcxpresso55s69/multicore\_examples/hello\_world/cm33\_core0/mdk/hello\_world\_cm33\_core0.uvmpw*
```

```
*<install\_dir\>/boards/lpcxpresso55s69/multicore\_examples/hello\_world/cm33\_core1/mdk/hello\_world\_cm33\_core1.uvmpw*
```

Build both applications separately by clicking the **Rebuild** button. Build the application for the auxiliary core \(cm33\_core1\) first because the primary core application project \(cm33\_core0\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

