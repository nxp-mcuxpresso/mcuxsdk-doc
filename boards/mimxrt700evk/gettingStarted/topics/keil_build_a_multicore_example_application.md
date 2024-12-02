# Build a multicore example application 

This section describes the particular steps that need to be done in order to build and run a multicore application.

The multicore Hello World MDK workspaces are located in this folder:

*<install\_dir\>/boards/mimxrt700evk/multicore\_examples/hello\_world/cm33\_core0/mdk/hello\_world\_cm33\_core0.uvmpw*

*<install\_dir\>/boards/ mimxrt700evk /multicore\_examples/hello\_world/cm33\_core1/mdk/hello\_world\_cm33\_core1.uvmpw*

To build both applications separately, click the **Rebuild** button. Build the application for the auxiliary core \(`cm33_core1`\) first, because the primary core application project \(`cm33_core0`\) must know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil_mdk_vision.md)

