# Build a multicore example application

This section describes the steps to build and run a dual-core application. The demo applications workspace files are located in this folder:

*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_type\>/iar*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World IAR workspaces are located in this folder:

*<install\_dir\>/boards/frdmk32l3a6/multicore\_examples/hello\_world/cm0plus/iar/hello\_world\_cm0plus.eww*

*<install\_dir\>/boards/frdmk32l3a6/multicore\_examples/hello\_world/cm4/iar/hello\_world\_cm4.eww*

Build both applications separately by clicking the **Make** button. Build the application for the auxiliary core \(cm0plus\) first, because the primary core application project \(cm4\) needs to know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

