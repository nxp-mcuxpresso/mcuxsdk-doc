# Development tools

The MCUXpresso SDK was tested with following development tools. Same versions or above are recommended.

**The SDK 25.12.00 release has been fully validated with IAR 9.60.4. However, since IAR 9.60.4 does not officially support the MCXW23 device, you must install an additional IAR patch, enabling you to build and debug MCX W23 SDK projects in the IDE.
IAR patch is distributed via [https://mcuxpresso.nxp.com](https://mcuxpresso.nxp.com/download/dceae9212840ef0af4cc0bc6c84f6f9b). Download the archive file iar_support_patch_mcxw23x_25_09_00.zip. Then, unzip the file and copy the content into your IAR folder structure \(typically within *C:/Program Files/IAR* systems\).
IAR 9.70.2 now officially supports the MCXW23 device. If you want to use IAR 9.70.2 to build your project, you do not need to install any additional IAR patch.
The SDK will be fully validated with IAR 9.70.2 in the next 26.03.00 release cycle.**

```{include} /release/commonrn/topics/development_tools_iar.md
:heading-offset: 2
```

```{include} /release/commonrn/topics/development_tools_mdk.md
:heading-offset: 2
```

```{include} /release/commonrn/topics/development_tools_armgcc.md
:heading-offset: 2
```
