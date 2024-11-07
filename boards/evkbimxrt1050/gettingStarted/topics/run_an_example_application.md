# Run an example application {#GUID-1B2FA3F6-A7ED-449F-87DB-081089E7B1A0}

For more information on debug probe support in the MCUXpresso IDE, visit [community.nxp.com](https://community.nxp.com/message/630901).

To download and run the application, perform these steps:

1.  On the **Quickstart Panel**, click **Debug evkbimxrt1050\_demo\_apps\_hello\_world \[Debug\]**.

    ![](../images/debug_hello_world_case_rt1050.png "Debugging hello_world case")

2.  The first time you debug a project, the **Debug Emulator Selection Dialog** is displayed, showing all supported probes that are attached to your computer. Select the probe through which you want to debug and click **OK**. \(For any future debug sessions, the stored probe selection is automatically used, unless the probe cannot be found.\)

    ![](../images/attached_probes_debug_emulator_selection_rt1050.png "Attached Probes: debug emulator selection")

3.  The application is downloaded to the target and automatically runs to `main()`.

4.  Start the application by clicking the **Resume** button.

    ![](../images/resume_button.png "Resume button")


The `hello_world` application is now running and a banner is displayed on the MCUXpresso IDE console window. If this is not the case, check your terminal settings and connections.

![](../images/text_display_hello_world_demo_rt1050.png "Text display of the hello_world demo")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

