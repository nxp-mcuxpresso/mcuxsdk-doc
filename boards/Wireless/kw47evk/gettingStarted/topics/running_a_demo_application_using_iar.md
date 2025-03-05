# Running a demo application using IAR 

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. The `hello_world` demo application targeted for the **kw47evk** hardware platform is used as an example, although these steps can be applied to any example application in the MCUXpresso SDK.

KW47 is a new product which is not natively supported by IAR toolchain at the time of this writing. The patch provides all the files to be incorporated in IAR Embedded Workbench folder structure so that KW47 SDK projects can be built and debugged in this IDE.

**Note:**

**IMPORTANT**

The following patch has been tested with IAR Embedded Workbench v9.60.

IAR patch is distributed via [KW47 Early Access Sharepoint](https://nxp1.sharepoint.com/:f:/r/teams/ext131/kw47/Documents/04. Tools?csf=1&web=1&e=xHnOm9).

1.  Download the archive file *ewarm-kw47-patch.zip* from *04.Tools/IDE* and *Debbuger Patches/*.
2.  Unzip the file and copy the content in your IAR folder structure \(typically within *C:/Program Files/IAR* systems\).


```{include} ../topics/iar_building_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_running_an_example_application.md
:heading-offset: 1
```

