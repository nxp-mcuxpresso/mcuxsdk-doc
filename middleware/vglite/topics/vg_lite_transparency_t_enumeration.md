# `vg_lite_transparency_t` enumeration 

Specifies the transparency mode for a buffer *\(prior to Sept 2022 name was vg\_lite\_buffer\_transparency\_mode\_t\)*.

Used in structure:`vg_lite_buffer.`

|vg\_lite\_transparency\_t string value|Description|
|----------------------------------------|-------------|
|`VG_LITE_IMAGE_OPAQUE`|Opaque image: all image pixels are copied to the VG PE for rasterization|
|`VG_LITE_IMAGE_TRANSPARENT`|Transparent image: only the non-transparent image pixels are copied to the VG PE. **Note:** This mode is only valid when `IMAGE_MODE` \(`vg_lite_image_mode_t`\) is either `VG_LITE_NORMAL_IMAGE_MODE` or `VG_LITE_MULTIPLY_IMAGE_MODE`.|

**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)

