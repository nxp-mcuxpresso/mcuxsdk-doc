# `vg_lite_copy_image` function 
**Description:**

This API copied a pixel rectangle with dimension \(width, height\) from source buffer to destination buffer. The source image pixel \(sx *+ i,*sy *+ j*\) is copied to the destination image pixel \(dx *+ i,*dy *+ j*\), for *0 ≤ i <*width and *0 ≤ j <*height. Pixels whose source or destination lie outside the bounds of the respective image are ignored. Pixel format conversion is applied as needed.

No pre-multiply, transformation, blending, filtering operations are applied to the pixel copy.

**Syntax:**

```
vg_lite_error_t vg_lite_copy_image (
    vg_lite_buffer_t              *target,
    vg_lite_buffer_t              *source,
    vg_lite_int32_t               sx,
    vg_lite_int32_t               sy,
    vg_lite_int32_t               dx,
    vg_lite_int32_t               dy,
    vg_lite_int32_t               width,
    vg_lite_int32_t               height
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`*target`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure that defines the destination buffer.|
|`*source`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure for the source buffer. All color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md) enum are valid source formats for the blit function.|
|`sx, sy`|Pixel coordinates of the lower-left corner of a pixel rectangle within the source buffer.|
|`dx, dy`|Pixel coordinates of the lower-left corner of a pixel rectangle within the target buffer.|
|`width`|Width of the copied pixel rectangle.|
|`height`|Height of the copied pixel rectangle.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

