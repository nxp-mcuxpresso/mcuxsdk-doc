# Running a demo application using IAR

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK using IAR. The `hello_world` demo application targeted for the MIMX8ULP hardware platform is used as an example, although these steps can be applied to any example application in the MCUXpresso SDK.

**Note:**

-   Newer versions of the IAR are compatible with older versions of the project format. However, using an older version of the IAR to load the SDK project that uses the newer format generates an error. To use the SDK, it is recommended to upgrade the IAR version to 9.30.1.
-   Run an application using imx-mkimage. Generate and download flash.bin to emmc or flexspi nor flash when DBD\_EN \(Deny By Default\) is fused.


```{include} ../topics/build_an_example_application_002.md
:heading-offset: 1
```

