# `vg_lite_buffer_layout_t` enumeration

Specifies the buffer data layout in memory.

Used in structure: `vg_lite_buffer`.

|vg\_lite\_buffer\_layout\_t String Value|Description|
|------------------------------------------|-------------|
|`VG_LITE_LINEAR`|Linear \(scanline\) layout.|
|`VG_LITE_TILED`|Data is organized in 4x4 pixel tiles. **Note:** for this layout, the buffer start address and stride must be 64-byte aligned|

**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)

