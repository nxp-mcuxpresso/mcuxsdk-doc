# RAW/POR image switch 

In current delivered SDK package, most demos generate RAW images. To enhance customer OOBE experience, the following RT1186 SDK CM33 project/targets generate POR image, which means that they can POR run after you debug/download it in IDE.

-   IAR/GCC/MDK, *hello\_world\_demo\_cm33 flexspi\_nor\_debug/release*, *flexspi\_nor\_hyperram\_debug/release*
-   IAR/GCC/MDK, *multicore\_hello\_world\_cm33 flexspi\_nor\_debug/release*, *flexspi\_nor\_hyperram\_debug/release*
-   MCUX CM33 image are all POR images except the `multicore_trigger` demo.

**Note:**

-   These POR images are not signed, just for develop convenience, not recommended for product usage.
-   It is highly recommended to use SPT for image download.

For the SDK CM33 IAR/MDK/ARMGCC project, `flexspi_nor` targets, as well as for MCUX project, debug/release targets. It is easy to switch RAW/POR image, via the project macro `XIP_BOOT_HEADER_ENABLE` setting. [Table 1](#table_rules)describes the rules.

|XIP\_BOOT\_HEADER\_ENABLE setting|Image type|
|---------------------------------|----------|
|1|POR|
|0|RAW|

-   For IAR/ARMGCC, change the macro `XIP_BOOT_HEADER_ENABLE` in the compiler setting.
-   For MDK, change the macro `XIP_BOOT_HEADER_ENABLE` in compiler and link setting simultaneously.

For detailed settings, see the following sections.


```{include} ../topics/IAR_settings_for_image_type_switch.md
:heading-offset: 2
```

```{include} ../topics/armgcc_settings_for_image_type_switch.md
:heading-offset: 2
```

```{include} ../topics/MDK_setting_for_image_type_switch.md
:heading-offset: 2
```

```{include} ../topics/mcuxpresso_setting_for_image_type_switch.md
:heading-offset: 2
```

**Parent topic:**[Bootable image generation](../topics/bootable_image_generation.md)

