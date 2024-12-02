# Build a multicore example application {

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug multicore example applications. The following steps can be applied to any multicore example application in the MCUXpresso SDK. Here, the dual-core version of hello\_world example application targeted for the **mimxrt700evk** hardware platform is used as an example.

1.  Multicore examples are imported into the workspace in a similar way as single core applications, explained in [Build an example application](ide_build_an_example_application.md). When the SDK zip package is installed and available in the **Installed SDKs** view, click **Import SDK example\(s\)…** on the Quickstart Panel. In the window that appears, select **mimxrt700evk** and click **Next**.
2.  Expand the *multicore\_examples* folder and select **hello\_world\_cm33\_core0**. The `hello_world_cm33_core1` counterpart project is automatically imported with the `cm33_core0` project, because the multicore examples are linked together and there is no need to select it explicitly. Click **Finish**.

    ![](../images/ide_select_the_hello_world_multicore_example.png "Select the hello_world multicore example")

3.  Now, two projects should be imported into the workspace. To start building the multicore application, highlight the `hello_world_cm33_core0` project \(multicore master project\) in the Project Explorer. Then choose the appropriate build target, Debug or Release, by clicking the downward facing arrow next to the hammer icon, as shown in [Figure 2](#fig_selectbuildtarget). For this example, select **Debug**.

    ![](../images/ide_selection_of_the_build_target_in_MCUXpresso_IDE.png "Selection of the build target in MCUXpresso IDE")

    Press the **Build** button to start the multi-core project build.. Because of the project reference settings in multicore projects, triggering the build of the primary core application \(`cm33_core0`\) also makes the referenced auxiliary core application \(`cm33_core1`\) to build.

    **Note:**

    When the **Release** build is requested, it is necessary to change the build configuration of both the primary and auxiliary core application projects first. To do this, select both projects in the Project Explorer view and then right click which displays the context-sensitive menu. Select **Build Configurations** -\> **Set Active** -\> **Release**. This alternate navigation using the menu item is **Project** -\> **Build Configuration** -\> **Set Active** -\> **Release**. After switching to the **Release** build configuration, the build of the multicore example can be started by triggering the primary core application \(cm33\_core0\) build.

    ![](../images/ide_switching_multicore_projects_into_the_release_build_configuration.png "Switching multicore projects into the Release build configuration")


**Parent topic:**[Run a demo using MCUXpresso IDE](../topics/run_a_demo_using_ide.md)

