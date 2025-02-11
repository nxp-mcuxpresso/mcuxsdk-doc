# `vg_lite_blit2` function 

**Description:**

This is the blit function for use with two sources. The blit2 operation is performed using two source buffers and one destination buffer. The source and destination buffer structures are defined using the [`vg_lite_buffer_t`](vg_lite_buffer_t_structure_001.md) structure. Source0 and Source1 are first blended according to the blend mode with a specific transformation matrix for each image. Source1 is used as the source while Source0 is used as the dest and is directly output to the render target buffer.

The specified matrices can include translation, rotation, scaling, and perspective correction. Note that [`vg_lite_buffer_t`](vg_lite_buffer_t_structure_001.md) does not support coverage sample anti-aliasing so the destination buffer edge may not be smooth, especially with a rotation matrix. VGLite path rendering can be used to achieve high-quality coverage sample anti-aliasing \(16X, 8X, 4X\) rendering effect.

Application can use VGLite API `vg_lite_query_feature(gcFEATURE_BIT_VG_DOUBLE_IMAGE)` to determine HW support for double image.

**Note:**

-   The `vg_lite_blit` function can be used for color conversion for Source0 or Source1 before merging sources with vg\_lite\_blit2.

**Syntax:**

```
vg_lite_error_t vg_lite_blit2 (
    vg_lite_buffer_t              *target,
    vg_lite_buffer_t              *source0,
    vg_lite_buffer_t              *source1,
    vg_lite_matrix_t              *matrix0,
    vg_lite_matrix_t              *matrix1,
    vg_lite_blend_t               blend,
    vg_lite_filter_t              filter
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`*target`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure, which defines the destination buffer. See [Alignment notes](alignment_notes.md) for valid destination color formats for the blit functions|
|`*source0, *source1`|Points to the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure for the source0 and source1 buffers. All color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md)` enum are valid source formats for the blit functions.|
|`*matrix0, *matrix1`|Points to a [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure.md) structure that defines the 3x3 transformation matrix0 for the source0 pixels and matrix1 for the source1 pixels. If matrix0 and matrix1 are both NULL, the identity matrix is assumed, meaning the blending result of Source0 and Source1 is copied directly on the target at location\(0,0\).|
|`blend`|Specifies one of the enum [vg\_lite\_blend\_t](vg_lite_blend_t_enumeration.md) values for hardware-supported blend modes to be applied to each image pixel. If no blending is required, set this value to `VG_LITE_BLEND_NONE (0). `Note: If the “matrix” parameter is specified with rotation or perspective, and the “blend" parameter is specified as `VG_LITE_BLEND_NONE, VG_LITE_BLEND_SRC_IN,` or `VG_LITE_BLEND_DST_IN`, the VGLite driver overwrites the application’s setting for the BLIT operation as follows: -   If `gcFEATURE_BIT_VG_BORDER_CULLING` \([vg\_lite\_feature\_t](/l)\) is supported, the transparency mode will always be set to TRANSPARENT. -   If `gcFEATURE_BIT_VG_BORDER_CULLING` \([vg\_lite\_feature\_t](/l)\) is not supported, the blend mode will always be set to `VG_LITE_BLEND_SRC_OVER`.  This is due to some limitations in the VGLite hardware.|
|`filter` |Specifies the filter type. All formats available in the [vg\_lite\_filter\_t](vg_lite_filter_t_enumeration.md) enum are valid formats for this function. A value of zero \(0\) indicates `VG_LITE_FILTER_POINT`.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

