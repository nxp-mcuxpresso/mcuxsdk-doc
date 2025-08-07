# Build and run a multicore example application

This section describes the steps to build and run a dual-core application. The demo application build scripts locate in this folder:

*<install\_dir\>/boards/frdmimxrt1186/multicore\_examples/<application\_name\>/<core\_type\>/armgcc*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World GCC build scripts are located in this folder:

*<install\_dir\>/boards/frdmimxrt1186/multicore\_examples/hello\_world/cm7/armgcc/build\_debug.bat*

*<install\_dir\>/boards/frdmimxrt1186/multicore\_examples/hello\_world/cm33/armgcc/build\_flexspi\_nor\_debug.bat*

Build the application for the auxiliary core \(cm7\) first, because the primary core application project \(cm33\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

By default, the primary core **flexspi\_nor\_debug** target links the auxiliary core **debug** target, and the primary core **flexspi\_nor\_release** target links the auxiliary core **release** target. During the primary core execution, the auxiliary core image is copied from flash into CM7 RAM and executed.

**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm_gcc.md)

