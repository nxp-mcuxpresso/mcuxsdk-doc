# Run a demo using MCUXpresso IDE

**Note:** Ensure that the MCUXpresso IDE toolchain is included when generating the MCUXpresso SDK package.

This section describes the steps required to configure MCUXpresso IDE to build, run, and debug example applications. The `hello_world` demo application targeted for the `MCXW23` hardware platform is used as an example, though these steps can be applied to any example application in the MCUXpresso SDK.

LinkServer from the [nxp.com](http://nxp.com) does not have support for MCXW23. It is available only internally. You can download the installer for LinkServer distributed via the MCXW23 Early Access Sharepoint.

After the LinkServer is installed, to customize the LinkServer in MCUXpresso IDE, go to **Window** -\> **Preferences** -\> **MCUXpresso IDE** -\> **Debug Options** -\> **LinkServer Options**.

```{include} ../topics/select_the_workspace_location.md
:heading-offset: 1
```

```{include} ../topics/build_an_example_application_001.md
:heading-offset: 1
```

```{include} ../topics/run_an_example_application.md
:heading-offset: 1
```

