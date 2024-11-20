# Build a TrustZone example application {#topic_tmy_pyw_lvb}

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug TrustZone example applications. The trustzone version of the `hello_world` example application targeted for the MCX-N9XX-EVK hardware platform is used as an example, though these steps can be applied to any TrustZone example application in the MCUXpresso SDK.

1.  TrustZone examples are imported into the workspace in a similar way as single core applications. When the SDK zip package for MCX-N9XX-EVK is installed and available in the **Installed SDKs** view, click Import SDK example\(s\)… on the **Quickstart** Panel. In the window that appears, expand the **MCXN9XX** folder and select **MCXN947**. Then, select **mcxn9xxevk** and click **Next**.

    ![](../images/ide_build_trustzone_example_select_board.png "Select the mcxn9xxevk board")

2.  Expand the **trustzone\_examples/** folder and select **hello\_world\_s**. Because TrustZone examples are linked together, the non-secure project is automatically imported with the secure project, and there is no need to select it explicitly. Then select **UART** as **SDK Debug Console**. Then, click **Finish**.

    ![](../images/ide_build_trustzone_example_select_hello_world.png "Select the hello_world TrustZone example")

3.  Now, two projects should be imported into the workspace. To start building the TrustZone application, highlight the **mcxn9xxevk\_hello\_world\_s** project \(TrustZone master project\) in the Project Explorer. Then, choose the appropriate build target, Debug or Release, by clicking the downward facing arrow next to the hammer icon, as shown in [Figure 3](#SELECTBULDTARGET). For this example, select the Debug target.

    ![](../images/ide_build_trustzone_example_select_build_target.png "Selection of the build target in MCUXpresso IDE")

    The project starts building after the build target is selected. It is requested to build the application for the secure project first, because the non-secure project needs to know the secure project since CMSE library when running the linker. It is not possible to finish the non-secure project linker when the secure project since CMSE library is not ready.

    **Note:**

    When the Release build is requested, it is necessary to change the build configuration of both the secure and non-secure application projects first. To do this, select both projects in the Project Explorer view by clicking to select the first project, then using shift-click or control-click to select the second project. Right click in the Project Explorer view to display the context-sensitive menu and select **Build Configurations** \> **Set Active** \> **Release**. This is also possible by using the menu item of **Project** \> **Build Configuration** \> **Set Active** \> **Release**. After switching to the Release build configuration. Build the application for the secure project first.

    ![](../images/ide_build_trustzone_example_switch_projects.png "Switching TrustZone projects into the Release build
                                configuration")


**Parent topic:**[Run a demo application using MCUXpresso IDE](../topics/ide_run_a_demo_application.md)

