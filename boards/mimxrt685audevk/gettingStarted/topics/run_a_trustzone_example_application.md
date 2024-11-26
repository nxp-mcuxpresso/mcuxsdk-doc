# Run a TrustZone example application

To download and run the application, perform all steps as described in *Section 3.3, "Run an example application"*. These steps are common for single core, and TrustZone applications, ensuring `evkmimxrt685_hello_world_s` is selected for debugging.

In the Quickstart Panel, click **Debug evkmimxrt685\_\_hello\_world\_s \[Debug\]** to launch the second debug session.

|![](../images/debug_mimxrt600_hello_world_s_case_trustzone.jpg "Debug evkmimxrt685_hello_world_s
									case")

|

|![](../images/trustzone_debug_sessions_mimxrt600.jpg "TrustZone debug sessions")

|

Now, the TrustZone sesions should be opened. Click **Resume**. The `hello_world` TrustZone application then starts running, and the secure application starts the non-secure application during runtime.

|![](../images/run_hello_world_trustzone_example_and_get_message_.jpg "Run Hello World
									TrustZone
									example and get the message")

|

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

