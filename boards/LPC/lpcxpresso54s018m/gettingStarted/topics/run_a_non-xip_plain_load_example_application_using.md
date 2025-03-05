# Run a non-XIP \(plain load\) example application using J-Link/J-Trace

This section describes how to configure EWARM if using a J-link/J-Trace debug probe, or a probe which has been programmed with J-link firmware.

1.  Select “J-Link/J-Trace” and “Use macro file\(s\)”.

    ![](../images/select_j-link_j-trace_and_use_macro_files_lpc540xx.png "Select “J-Link/J-Trace” and “Use macro file(s)”")

2.  Unselect “Use flash loader\(s\)” to use SEGGER J-Link flashloaders. Then, click the "OK” button.

    ![](../images/unselect_use_flash_loaders_lpc540xx.png "Unselect “Use flash loader(s)”")

3.  In IAR, click the "Download and Debug" button to download the application to the target.

    ![](../images/download_and_debug_lpc540xx.png "Download and Debug button")

4.  The application is then downloaded to the target and automatically runs to the main\(\) function.

    ![](../images/stop_at_main_when_running_debugging_lpc540xx_001.png "Stop at main() when running debugging")

5.  Run the code by clicking the "Go" button to start the application.

    ![](../images/go_button_001.png "Go button")

6.  The hello\_world application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

    ![](../images/text_display_hello_world_001.png "Text display of the hello_world demo")


**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

