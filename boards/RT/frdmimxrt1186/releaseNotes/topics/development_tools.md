# Development tools

The MCUXpresso SDK was tested with following development tools. Same versions or above are recommended.

The SDK 25.12.00 release has been fully validated with IAR 9.60.4. However, since IAR 9.60.4 does not officially support the MIMXRT1186 device, you must install an additional IAR patch, enabling you to build and debug FRDMIMXRT1186 SDK projects in the IDE.

IAR 9.70.2 is not ready for MIMXRT1186 device. If you want to use IAR 9.70.2 to build your project, you need to install the IAR patch, too.

SEGGER V8.86 is not ready for MIMXRT1186 device. If you want to use SEGGER V8.86 to debug your project, you need to install the SEGGER patch, too.

IAR and SEGGER patch are distributed via [iar_segger_support_patch_rt1186](https://mcuxpresso.nxp.com/download/e8ca8e655b4a5eeff3d9265ef11fa3f2).

```{include} /release/commonrn/topics/development_tools_mcuxpresso.md
:heading-offset: 2
```

```{include} /release/commonrn/topics/development_tools_iar.md
:heading-offset: 2
```

```{include} /release/commonrn/topics/development_tools_mdk.md
:heading-offset: 2
```

```{include} /release/commonrn/topics/development_tools_armgcc.md
:heading-offset: 2
```
