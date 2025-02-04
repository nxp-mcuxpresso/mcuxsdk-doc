# Build and run a multicore example application 

This section describes the steps to build and run a multicore application. The demo applications workspace files are available in the folder:

*<install\_dir\>/boards/<board\_name\>/multicore\_examples/<application\_name\>/<core\_id\>/iar*

Begin with a simple dual-core version of the Hello World application. The multicore Hello World IAR workspaces are available in the folder:

*<install\_dir\>/boards/mimxrt700evk/multicore\_examples/hello\_world/cm33\_core0/iar/hello\_world\_cm33\_core0.eww*

*<install\_dir\>/boards/mimxrt700evk/multicore\_examples/hello\_world/cm33\_core1/iar/hello\_world\_cm33\_core1.eww*

Build both applications separately by clicking the **Make** button. Build the application for the auxiliary core \(`cm33_core1`\) first, because the primary core application project \(`cm33_core0`\) must know the auxiliary core application binary when running the linker. When the auxiliary core application binary is not ready, it is impossible to finish the primary core linker.

By default, the primary core `flash_debug` target links the auxiliary core debug target, and the primary core `flash_release` target links the auxiliary core release target. During the primary core execution, the auxiliary core image is copied from flash into the SRAM and executed.

1.  Build the `CM33_core1` and `CM33_core0` projects respectively.
2.  Only click the **Download** and **Debug** button on the `CM33_core0` project, IAR could help start to debug a multicore project. It is user-friendly to debug multicore examples with CMSIS-DAP on IAR \(Multicore Project is set on **Debugger** → **Multicore** window\).

    ![](../images/iar_debug_multicore_project.png "Debug multicore project")

3.  Start `core0` and then start `core1` on the **CM33\_core0** project.

    ![](../images/iar_start_core0.png "Start core0")

4.  The `Hello_World` multicore demos are now running. A banner appears on the terminal and the LED blinks. If this is not true, check your terminal settings and connections.

    ![](../images/iar_banner_appears_when_multicore_demos_run_successfully.png "The banner appears when multicore demos run successfully")


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

