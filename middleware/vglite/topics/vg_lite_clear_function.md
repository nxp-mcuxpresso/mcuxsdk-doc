# `vg_lite_clear` function 

**Description:**

This function performs the clear operation, clearing/filling the specified buffer \(entire buffer or partial rectangle in a buffer\) with an explicit color.

**Syntax:**

```
vg_lite_error_t vg_lite_clear (
    vg_lite_buffer_t              *target,
    vg_lite_rectangle_t           *rect,
    vg_lite_color_t               color
);


```

**Parameters:**

|Name|Description|
|----|-----------|
|`*target`|Pointer to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure for the destination buffer. All color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md) enum are valid destination formats for the clear function.|
|`*rect`|Pointer to the [vg\_lite\_rectangle\_t](vg_lite_rectangle_t_structure.md)structure that specifies the area to be filled. If the rectangle is NULL, the entire target buffer is filled with the specified color.|
|`color`|Clear color, as specified in the [vg\_lite\_color\_t](vg_lite_color_t_parameter.md) enum that is the color value to use for filling the buffer. If the buffer is in L8 format, the RGBA color is converted into a luminance value.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

