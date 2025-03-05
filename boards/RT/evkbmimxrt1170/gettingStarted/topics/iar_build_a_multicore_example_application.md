# Build a multicore example application

This section describes the steps to build and run a dual-core application. The demo applications workspace files are located in this folder:

*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_type\>/iar*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World IAR workspaces are located in this folder:

*<install\_dir\>/boards/evkbmimxrt1170/multicore\_examples/hello\_world/cm4/iar/hello\_world\_cm4.eww*

*<install\_dir\>/boards//evkbmimxrt1170/multicore\_examples/hello\_world/cm7/iar/hello\_world\_cm7.eww*

Build both applications separately by clicking the **Make** button. Build the application for the auxiliary core \(cm4\) first, because the primary core application project \(cm7\) needs to know the auxiliary core application binary when running the linker. It is not possible to finish the primary core linker when the auxiliary core application binary is not ready.

Because the auxiliary core runs always from RAM, only debug and release RAM targets are present in the project. When building the primary core project, it is possible to select either *debug/release* RAM targets or `flexspi_nor_debug`/`flexspi_nor_release` Flash targets. When choosing Flash targets \(preferred\) the auxiliary core binary is linked with the primary core image and stored in the external SPI Flash memory. During the primary core execution the auxiliary core image is copied from flash into the CM4 RAM and executed.

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

