# `vg_lite_blit` function

**Description:**

This is the blit function. The blit operation is performed using a source and a destination buffer. The source and destination buffer structures are defined using the [`vg_lite_buffer_t`](vg_lite_buffer_t_structure_001.md) structure. Blit copies a source image to the destination window with a specified matrix that can include translation, rotation, scaling, and perspective correction. Note that [`vg_lite_buffer_t`](vg_lite_buffer_t_structure_001.md) does not support coverage sample anti-aliasing so the destination buffer edge may not be smooth, especially with a rotation matrix. VGLite path rendering can be used to achieve high-quality coverage sample anti-aliasing \(16X, 8X, 4X\) rendering effect.

**Note:**

-   The blit function can be used with or without the blend function \([vg\_lite\_blend\_t](/l)\)
-   The blit function can be used with or without specifying a foreground color value \([vg\_lite\_color\_t](/l)\)
-   The blit function can be used for color conversion with an identity matrix and appropriate formats specified for the source and the destination buffers. In this case, do not specify blend mode and color value.

**Syntax:**

```
vg_lite_error_t vg_lite_blit (
       vg_lite_buffer_t        *target,
       vg_lite_buffer_t        *source,
       vg_lite_matrix_t        *matrix,
       vg_lite_blend_t         blend,
       vg_lite_color_t         color,
       vg_lite_filter_t        filter
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`*target`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure, which defines the destination buffer. See [Image Source Alignment](alignment_notes.md) Requirement for valid destination color formats for the blit functions.|
|`*source`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure for the source buffer. All color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md) enum are valid source formats for the blit function.|
|`*matrix`|Points to a [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_001.md) structure that defines the transformation matrix of source pixels into the target. If the matrix is NULL, then an identity matrix is assumed, which means that the source is copied directly at 0,0 location on the target.|
|`blend`|Specifies one of the enum [vg\_lite\_blend\_t](vg_lite_blend_t_enumeration.md) values for hardware-supported blend modes to be applied to each image pixel. If no blending is required, set this value to `VG_LITE_BLEND_NONE` \(0\). **Note:** If the `matrix` parameter is specified with rotation or perspective, and the `blend` parameter is specified as `VG_LITE_BLEND_NONE`, `VG_LITE_BLEND_SRC_IN`, or `VG_LITE_BLEND_DST_IN`; then, the VGLite driver overwrites the application setting for the blit operation as follows: -   If `gcFEATURE_BIT_VG_BORDER_CULLING` \([vg\_lite\_feature\_t](/l)\) is supported, then Transparency mode is always set to `TRANSPARENT`-   If `gcFEATURE_BIT_VG_BORDER_CULLING` \([vg\_lite\_feature\_t](/l)\) is not supported, then Blend mode is always set to `VG_LITE_BLEND_SRC_OVER`. It happens due to some limitations in the VGLite hardware.|
|`color`|If non-zero, this color value is used as a mix color. The mixed color gets multiplied with each source pixel before blending happens. If you don't need a mix color, set the color parameter to 0.**Note:** this parameter has no effect if the source `vg_lite_buffer_t` structure member `image_mode` is set to `VG_LITE_ZERO` or `VG_LITE_NORMAL_IMAGE_MODE`.|
|`filter`|Specifies the filter type. All formats available in the [vg\_lite\_filter\_t](vg_lite_filter_t_enumeration.md) enum are valid formats for this function. A value of zero \(0\) indicates `VG_LITE_FILTER_POINT`.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

