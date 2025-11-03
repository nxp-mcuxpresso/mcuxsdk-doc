# Bootable image generation

RT1180 can only boot from CM33. For CM33 application image to boot, a sophisticated boot header structure is needed. To ease the customer from complex settings, the **Secure Provisioning Tool** is provided. Among other rich features, it provides an easy way to use GUI for customer to generate bootable image from raw application image. In addition, in order for users to run the CM7 image conveniently, SDK provides the `multicore_trigger` demo for users to kick off CM7 image, combined with the SPT tool, we can run CM7 image by from POR.

In this section, two kinds of images are defined

|Terminology|Description|
|-----------|-----------|
|RAW image|Demo image without boot header|
|POR image|Demo image with boot header|

Most CM33 examples provided in the SDK package generate POR images based on project settings. Only a few examples create RAW images by default. POR images offer a good out-of-the-box experience but reduce flexibility. In contrast, RAW images, when used with the Secure Provisioning Tool, support broader functionality such as image signing, combining multiple images, and more. For demos that generate a POR boot image by default, see [RAW/POR image switch](RAW_POR_image_switch.md).


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

