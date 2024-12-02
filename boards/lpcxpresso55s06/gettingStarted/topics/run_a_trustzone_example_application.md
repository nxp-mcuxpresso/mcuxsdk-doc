# Run a TrustZone example application {#GUID-453D0DE4-C140-4E1C-8721-CCBF2AD2CB17}

To download and run the application perform all steps as described in *Section 3.3, "Run an example application"*. These steps are common for single core, dual-core, and TrustZone applications, ensuring both sides of the TrustZone application are properly loaded and started secure application. However, there is one additional dialogue that is specific to TrustZone examples. See the following figures as reference.

|![](../images/load_lpcxpresso55s69_hello_world_ns_case.png "Load lpcxpresso55s69_hello_world_ns
									case")

|

|![](../images/attached_probes_debug_emulator_selection_trustzone.png "Attached Probes: debug emulator selection")

|

|![](../images/target_core_selection_dialog_trustzone_lpc55xx.png "Target core selection dialog")

|

|![](../images/load_lpcxpresso55s69_hello_world_ns_axf.png "Load
									lpcxpresso55s69_hello_world_ns.axf")

|

After loading the non-secure application, press **RESET** on board to release the device connect. Then, highlight the `lpcxpresso55s69_trustzone_examples_hello_world_s` project \(TrustZone master project\) in the Project Explorer. In the Quickstart Panel, click **lpcxpresso55s69\_trustzone\_examples\_hello\_world\_s \[Debug\]** to launch the second debug session.

|![](../images/debug_lpcxpresso55s69_hello_world_s_case_trustzone.png "Debug lpcxpresso55s69_hello_world_s
									case")

|

|![](../images/debug_the_hello_world_s_project_lpcxpress55s69.png "Debug the hello_world_s project")

|

Start the application by clicking **Resume**. The `hello_world` TrustZone application then starts running, and the secure application starts the non-secure application during runtime.

|![](../images/run_hello_world_trustzone_example_and_get_message_.png "Run Hello World
									TrustZone
									example and get the message")

|

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

