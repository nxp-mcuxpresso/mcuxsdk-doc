# Build a multicore example application

This section describes the particular steps that need to be done in order to build and run a dual-core application. The demo applications workspace files are located in this folder:

*<install\_dir\>/boards/evkmimxrt1160/multicore\_examples/<application\_name\>/<core\_type\>/mdk*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World MDK workspaces are located in this folder:

*<install\_dir\>/boards/evkmimxrt1160/multicore\_examples/hello\_world/cm4/mdk/hello\_world\_cm4.uvmpw*

*<install\_dir\>/boards//evkmimxrt1160/multicore\_examples/hello\_world/cm7/mdk/hello\_world\_cm7.uvmpw*

Build both applications separately by clicking the **Rebuild** button. Build the application for the auxiliary core \(cm4\) first, because the primary core application project \(cm7\) needs to know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

Because the auxiliary core runs always from RAM, debug and release RAM targets are present in the project only. When building the primary core project, it is possible to select `flexspi_nor_debug`/`flexspi_nor_release` Flash targets. When choosing Flash targets the auxiliary core binary is linked with the primary core image and stored in the external SPI Flash memory. During the primary core execution the auxiliary core image is copied from flash into the CM4 RAM and executed.

**Parent topic:**[Run a demo using Keil® MDK/μVision](../topics/run_a_demo_using_keil_mdk_vision.md)

