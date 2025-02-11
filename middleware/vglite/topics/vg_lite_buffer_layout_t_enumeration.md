# `vg_lite_compress_mode_t` enumeration

Specifies the DECNano comprssion mode. *\(from March 2023\)*

Used in structure: `vg_lite_buffer_t`.

|**vg\_lite\_compress\_mode\_t string value**|Description|
|----------------------------------------------|-------------|
|`VG_LITE_DEC_DISABLE`|Disable compression.|
|`VG_LITE_DEC_NON_SAMPLE`|compression ratio is 1.6 for ARGB8888, 2.0 for XRGB8888|
|`VG_LITE_DEC_HSAMPLE`|compression ratio is 2.0 for ARGB8888, 2.6 for XRGB8888|
|`VG_LITE_DEC_HV_SAMPLE`|compression ratio is 2.6 for ARGB8888, 4.0 for XRGB8888|

**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)

