# Run a TrustZone example application

To download and run the application perform all steps as described in *Section 3.3, "Run an example application"*. These steps are common for single core, dual-core, and TrustZone applications, ensuring both sides of the TrustZone application are properly loaded and started secure application. However, there is one additional dialogue that is specific to TrustZone examples. See the following figures as reference.

![](../images/load_lpcxpresso55s16_hello_world_ns_case.png "Load lpcxpresso55s16_hello_world_ns case")

![](../images/attached_probes_debug_emulator_selection_trustzone.png "Attached Probes: debug emulator selection")

After loading the non-secure application, press **RESET** on board to release the device connect. Then, highlight the `lpcxpresso55s16_trustzone_examples_hello_world_s` project \(TrustZone master project\) in the Project Explorer. In the Quickstart Panel, click **lpcxpresso55s16\_trustzone\_examples\_hello\_world\_s \[Debug\]** to launch the second debug session.

![](../images/debug_lpcxpresso55s16_hello_world_s_case_trustzone.png "Debug lpcxpresso55s16_hello_world_s case")

![](../images/debug_the_hello_world_s_project_lpcxpress55s16.png "Debug the hello_world_s project")

Start the application by clicking **Resume**. The `hello_world` TrustZone application then starts running, and the secure application starts the non-secure application during run time.

![](../images/run_hello_world_trustzone_example_and_get_message_.png "Run Hello World trustzone example and get the message")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

