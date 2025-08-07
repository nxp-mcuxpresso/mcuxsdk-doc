# Bootable image generation

RT1180 can only boot from CM33. For CM33 application image to boot, a sophisticated boot header structure is needed. To ease the customer from complex settings, the **Secure Provisioning Tool** is provided. Among other rich features, it provides an easy way to use GUI for customer to generate bootable image from raw application image. In addition, in order for users to run the CM7 image conveniently, SDK provides the `multicore_trigger` demo for users to kick off CM7 image, combined with the SPT tool, we can run CM7 image by from POR.

In this section, two kinds of images are defined

|Terminology|Description|
|-----------|-----------|
|RAW image|Demo image without boot header|
|POR image|Demo image with boot header|

Most examples that provided in the SDK package create RAW images from project settings. Only some OOBE examples can create POR image. POR image can provide good out-of-box experience, but the cost is losing some flexibility. While RAW images, with the usage of `Secure Provisioning Tool`, have the most widely usage like image signning, multiple image combination, and so on. For demos that by default generate a POR boot image, see [RAW/POR image switch](RAW_POR_image_switch.md).


```{include} ../topics/use_SPT_tool_to_boot_cm33_image.md
:heading-offset: 1
```

```{include} ../topics/use_SPT_tool_and_multicore_trigger_image.md
:heading-offset: 1
```

```{include} ../topics/RAW_POR_image_switch.md
:heading-offset: 1
```

```{include} ../topics/use_secure_provisiong_tool_to_erase_flash.md
:heading-offset: 1
```

