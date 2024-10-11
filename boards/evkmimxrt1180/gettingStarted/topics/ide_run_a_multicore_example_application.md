# Run a multicore example application {#ide_run_a_multicore_example_application}

The primary core debugger handles flashing of both the primary and the auxiliary core applications into the SoC flash memory. To download and run the multicore application, switch to the primary core application project and perform all steps as described in [Run an example application](ide_run_an_example_application.md). These steps are common for both single-core applications and the primary side of dual-core applications, ensuring both sides of the multicore application are properly loaded and started. Select the `cm7` project and start debugging the CM7 project. Then, select the `cm33` project and start debugging the CM33 project.

See [Figure 1](#FIG_DEBUGHELLOWORLD) to [Figure 3](#FIG_STOPPRIMARYCORE) for reference.

![](../images/ide_multicore_debug_hello_world_cm33_case.png "Debug hello_world_cm33 case")

![](../images/ide_multicore_attached_probes.png "Attached Probes: debug emulator selection")

![](../images/ide_multicore_stop_primary_core_application.png "Stop the primary core application at main() when running debugging")

After clicking **Resume All Debug** sessions, the `hello_world` multicore application runs and a banner is displayed on the terminal. If this is not the case, check your terminal settings and connections.

![](../images/ide_multicore_hello_world_from_primary_core_messag.png "Hello World from the primary core message")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

