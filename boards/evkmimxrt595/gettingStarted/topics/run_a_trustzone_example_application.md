# Run a TrustZone example application

To download and run the application, perform all steps as described in [Run an example application](run_an_example_application.md). These steps are common for single core, and TrustZone applications, ensuring `evkmimxrt595_hello_world_s` is selected for debugging.

In the Quickstart Panel, click **Debug** to launch the second debug session.

|![](../images/trustzone_debug_sessions_mimxrt500.jpg "TrustZone debug sessions")

|

Now, the TrustZone sessions should be opened. Click **Resume**. The `hello_world` TrustZone application then starts running, and the secure application starts the non-secure application during runtime.

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)
