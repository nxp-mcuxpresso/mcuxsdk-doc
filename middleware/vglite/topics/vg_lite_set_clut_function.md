# `vg_lite_set_CLUT` function

**Description:**

This function sets the Color Lookup Table \(CLUT\) in the context state for index color image. Once the CLUT is set \(Not NULL\), the image pixel color for index format image rendering is obtained from the Color Lookup Table \(CLUT\) according to the pixel’s color index value.

**Note:** Available only for IP with Indexed color support..

**Syntax:**

```
vg_lite_error_t vg_lite_set_CLUT (
  vg_lite_uint32_t                    count,
  vg_lite_uint32_t                    *colors
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`count`|This is the count of the colors in the color look-up table:  -   For INDEX\_1, there can be up to 2 colors in the table -   For INDEX\_2, there can be up to 4 colors in the table -   For INDEX\_4, there can be up to 16 colors in the table -   For INDEX\_8, there can be up to 256 colors in the table|
|`*colors`|The Color Lookup Table \(CLUT\) pointed by “colors” will be stored in the context and programmed to the command buffer when needed. The CLUT will not take effect until the command buffer is submitted to HW. The color is in ARGB format with A located in the upper bits.  **Note:** The VGLite driver does not validate the CLUT contents from the application.|

**Returns:**

`VG_LITE_SUCCESS` as no checking is done.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

