# Build a multicore example application

This section describes the steps to build and run a dual-core application. The demo applications workspace files are located in this folder:

```
*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_type\>/mdk*
```

Begin with a simple dual-core version of the Hello World application. The multicore Hello World Keil MSDK/μVision workspaces are located in this folder:

```
*<install\_dir\>/boards/lpcxpresso54114/multicore\_examples/hello\_world/cm0plus/mdk/hello\_world\_cm0plus.uvmpw*
```

```
*<install\_dir\>/boards/lpcxpresso54114/multicore\_examples/hello\_world/cm4/mdk/hello\_world\_cm4.uvmpw*
```

Build both applications separately by clicking the **Rebuild** button. Build the application for the auxiliary core \(cm0plus\) first because the primary core application project \(cm4\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

