# Running a demo application using IAR 

This section describes the steps required to build, run, and debug example applications provided in the MCUXpresso SDK. The `hello_world` demo application targeted for the **mcxw72evk** hardware platform is used as an example, although these steps can be applied to any example application in the MCUXpresso SDK.

MCX W72 is a new product which is not natively supported by IAR toolchain at the time of this writing. The patch provides all the files to be incorporated in IAR Embedded Workbench folder structure so that MCX W72 SDK projects can be built and debugged in this IDE.

**Note:**

**IMPORTANT**

The following patch has been tested with IAR Embedded Workbench v9.60.

IAR patch is distributed via [MCX W72 Early Access Sharepoint](https://nxp1.sharepoint.com/teams/ext131/MCX_Alpha/SitePages/Home.aspx?RootFolder=%2Fteams%2Fext131%2FMCX%5FAlpha%2FDocument%2FW%20Series%2FMCX%20W72%20Advanced%20Information%2F04%2E%20Tools&FolderCTID=0x012000A56B1109B4B59044B4922AB984431F87&View=%7BF33BE67D%2D2534%2D44E7%2D98DF%2DB6B5CB8174CF%7D).

1.  Download the archive *file ewarm-mcxw72-patch.zip* from *04.Tools/IDE* and *Debbuger Patches/*.
2.  Unzip the file and copy the content in your IAR folder structure \(typically within *C:/Program Files/IAR* systems\).


```{include} ../topics/iar_building_an_example_application.md
:heading-offset: 1
```

```{include} ../topics/iar_running_an_example_application.md
:heading-offset: 1
```

