# Build a multicore example application

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug multicore example applications. The following steps can be applied to any multicore example application in the MCUXpresso SDK. Here, the dual-core version of `hello_world` example application targeted for the **evkmimxrt1180** hardware platform is used as an example.

1.  Multicore examples are imported into the workspace in a similar way as single core applications, explained in [Build an example application](ide_build_an_example_application.md). When the SDK zip package for **evkmimxrt1180** is installed and available in the **Installed SDKs** view, click **Import SDK example\(s\)…** on the Quickstart Panel. In the window that appears, select **evkmimxrt1180** and click **Next**.

    ![](../images/ide_multicore_select_rt1180_board.png "Select the evkmimxrt1180 board")

2.  Expand the `multicore_examples` folder and select **hello\_world\_cm33**. The `hello_world_cm7` counterpart project is automatically imported with the `cm33` project, because the multicore examples are linked together and there is no need to select it explicitly. Click **Finish**.

    ![](../images/ide_multicore_select_hello_world_core.png "Select the hello_world multicore example")

3.  Now, two projects should be imported into the workspace. To start building the multicore application, highlight the `hello_world_cm33` project \(multicore master project\) in the Project Explorer. Then choose the appropriate build target, **Debug** or **Release**, by clicking the downward facing arrow next to the hammer icon, as shown in [Figure 3](#FIG_TERMINALSSPUTTY). For this example, select **Debug**.

    ![](../images/ide_multicore_selection_of_build_target.png "Selection of the build target in MCUXpresso IDE")


Press the **Build** button to start the multi-core project build.. Because of the project reference settings in multicore projects, triggering the build of the primary core application \(`cm33`\) also makes the referenced auxiliary core application \(`cm7`\) to build.

**Note:**

When the **Release** build is requested, it is necessary to change the build configuration of both the primary and auxiliary core application projects first. To do this, select both projects in the Project Explorer view and then right click which displays the context-sensitive menu. Select **Build Configurations** -\> **Set Active** -\> **Release**. This alternate navigation using the menu item is **Project** -\> **Build Configuration** -\> **Set Active** -\> **Release**. After switching to the **Release** build configuration, the build of the multicore example can be started by triggering the primary core application \(`cm33`\) build.

![](../images/ide_multicore_switching_into_release_build.png "Switching multicore projects into the Release build configuration")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)

