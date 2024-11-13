# Running a demo application using IAR

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. The `hello_world` demo application targeted for the **frdmmcxw71** hardware platform is used as an example, although these steps can be applied to any example application in the MCUXpresso SDK.

MCXW71 is a new product which is not natively supported by IAR toolchain at the time of this writing.

It will be supported in IAR 9.60.3 targeted for mid-Oct 2024. So, before IAR 9.60.3, follow the steps below to apply the patch. This patch provides all the files to be incorporated in IAR Embedded Workbench folder structure so that MCXW71 SDK projects can be built and debugged in this IDE.

**Important:**

The following patch has been tested with IAR Embedded Workbench v9.60. IAR patch is distributed via [https://mcuxpresso.nxp.com/download/29461429d7fb0eb696d55ab0c47e3a6b](https://mcuxpresso.nxp.com/download/29461429d7fb0eb696d55ab0c47e3a6b).

1.  Download the archive file iar\_patch\_mcxw71.zip.
2.  Unzip the file and copy the arm directory in your IAR folder structure. For example, C:/Program Files/IAR systems.


```{include} ../topics/build_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/run_an_example_application_001.md
:heading-offset: 1
```

