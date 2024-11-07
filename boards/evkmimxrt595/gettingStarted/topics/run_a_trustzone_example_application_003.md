# Run a TrustZone example application

The secure project is configured to download both secure and non-secure output files, so debugging can be fully managed from the secure project. To download and run the TrustZone application, switch to the secure application project and perform steps 1 – 4 as described in *Section 4.2, Run an example application*. These steps are common for both single core, and TrustZone applications in IAR. After clicking **Download and Debug**, both the secure and non-secure images are loaded into the device memory, and the secure application is executed. It stops at the `Rest_Hander` function.

|![](../images/stop_at_rest_hander_when_running_debugging_lpc55xx.png "Stop at Rest_Hander when running
									debugging")

|

Run the code by clicking **Go** to start the application.

|![](../images/go_button_lpc55xx.png "Go button")

|

The TrustZone `hello_world` application is now running and a banner is displayed on the terminal. If this is not true, check your terminal settings and connections.

|![](../images/text_display_trustzone_hello_world_application.png "Text display of the trustzone hello_world
									application")

|

**Note:** If the application is running in RAM \(debug/release build target\), in **Options****\>****Debugger \> Download** tab, disable **Use flash loader\(s\)**. This can avoid the `_ns` download issue on i.MXRT500.

|![](../images/disable_use_flash_loaders_imxrt600.jpg "Disabling Use flash loader(s)")

|

**Parent topic:**[Run a demo application using IAR](../topics/run_a_demo_application_using_iar.md)

