# Build and run a multicore example application 

This section describes the steps to build and run a multicore application. The demo application build scripts locate in this folder:

*<install\_dir\>/boards/mimxrt700evk/multicore\_examples/<application\_name\>/<core\_id\>/armgcc*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World GCC build scripts are located in this folder:

*<install\_dir\>/boards/ mimxrt700evk /multicore\_examples/hello\_world/cm33\_core0/armgcc/build\_debug.bat <install\_dir\>/boards/ mimxrt700evk /multicore\_examples/hello\_world/cm33/armgcc\_core1/build\_flash\_debug.bat*

Build the application for the auxiliary core \(`cm33_core1`\) first, because the primary core application project \(`cm33_core0`\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

By default, the primary core `flash_debug` target links the auxiliary core **debug** target, and the primary core `flash_release` target links the auxiliary core **release** target. During the primary core execution, the auxiliary core image is copied from flash into SRAM and executed.

**Parent topic:**[Run a demo using Arm GCC](../topics/run_a_demo_using_arm_gcc.md)

