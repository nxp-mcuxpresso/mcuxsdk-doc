# Run a TrustZone example application

The secure project is configured to download both secure and non-secure output files so debugging can be fully managed from the secure project.

To download and run the TrustZone application, switch to the secure application project and perform steps as described in [Run a TrustZone example application](run_a_trustzone_example_application_001.md#). These steps are common for single core, dual-core, and TrustZone applications in μVision. After clicking **Download and Debug**, both the secure and non-secure images are loaded into the device flash memory, and the secure application is executed. It stops at the `main()` function.

|![](../images/49_rt500.png "Stop at main() when running
									debugging")

|

Run the code by clicking **Run** to start the application.

|![](../images/figure53_rt600.png "Run button")

|

The `hello_world` application is now running and a banner is displayed on the terminal. If not, check your terminal settings and connections.

|![](../images/text_display_trustzone_hello_world_app.png "Text display of the TrustZone
									hello_world application")

|

**Parent topic:**[Run a demo using Keil MDK/μVision](../topics/run_a_demo_using_keil__mdk_vision.md)

