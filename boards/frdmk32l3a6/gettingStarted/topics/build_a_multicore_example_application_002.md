# Build a multicore example application

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug multicore example applications. The following steps can be applied to any multicore example application in the MCUXpresso SDK. Here, the dual-core version of hello\_world example application targeted for the FRDM-K32L3A6 hardware platform is used as an example.

1.  Multicore examples are imported into the workspace in a similar way as single core applications, explained in [Build an example application](build_an_example_application.md#). When the SDK zip package for FRDM-K32L3A6 is installed and available in the **Installed SDKs** view, click **Import SDK example\(s\)…** on the Quickstart Panel. In the window that appears, expand the **K32L3A60** folder and select **K32L3A60xxx**. Then, select **frdmk32l3a6** and click **Next**.

2.  Expand the `multicore_examples/hello\_world` folder and select **cm4**. The `cm0plus` counterpart project is automatically imported with the `cm4` project, because the multicore examples are linked together and there is no need to select it explicitly. Click **Finish**.

    ![](../images/select_hello_world_multicore_example_rel8.png "Select the hello_world multicore example")

3.  Now, two projects should be imported into the workspace. To start building the multicore application, highlight the `frdmk32l3a6_multicore_examples_hello_world_cm4` project \(multicore master project\) in the Project Explorer. Then choose the appropriate build target, **Debug** or **Release**, by clicking the downward facing arrow next to the hammer icon, as shown in [Figure 2](build_a_multicore_example_application_002.md#TERMINALSSPUTTY). For this example, select **Debug**.

    ![](../images/7_4_selection_of_build_target_mcuxpresso_ide_k32.png "Selection of the build target in MCUXpresso IDE")


The project starts building after the build target is selected. Because of the project reference settings in multicore projects, triggering the build of the primary core application \(`cm4`\) also causes the referenced auxiliary core application \(`cm0plus`\) to build.

**Note:** When the **Release** build is requested, it is necessary to change the build configuration of both the primary and auxiliary core application projects first. To do this, select both projects in the Project Explorer view and then right click which displays the context-sensitive menu. Select **Build Configurations** -\> **Set Active** -\> **Release**. This alternate navigation using the menu item is **Project** -\> **Build Configuration** -\> **Set Active** -\> **Release**. After switching to the **Release** build configuration, the build of the multicore example can be started by triggering the primary core application \(`cm4`\)build.

![](../images/switching_multicore_projects_into_release_build_co.png "Switching multicore projects into the Release build configuration")

**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_mcuxpresso_ide.md)
