# `vg_lite_draw_pattern` function

**Description:**

This function fills a path with an image pattern. The path is transformed according to the specified matrix and is filled with the transformed image pattern.

**Syntax:**

```
vg_lite_error_t vg_lite_draw_pattern (
    vg_lite_buffer_t            *target,
    vg_lite_path_t              *path,
    vg_lite_fill_t              fill_rule,
    vg_lite_matrix_t            *path_matrix,
    vg_lite_buffer_t            *pattern_image,
    vg_lite_matrix_t            *pattern_matrix,
    vg_lite_blend_t             blend,
    vg_lite_pattern_mode_t      pattern_mode,
    vg_lite_color_t             pattern_color,
    vg_lite_color_t             color,
    vg_lite_filter_t            filter
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*target`|Pointer to the `vg_lite_buffer_t` structure for the destination buffer. All color formats available in the `vg_lite_buffer_format_t` enum are valid destination formats for this draw function.|
|`*path`|Pointer to the `vg_lite_path_t` structure containing path data that describes the path to draw. See opcode details in [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md)|
|`fill_rule`|Specifies the vg\_lite\_fill\_t enum value for the fill rule for the path.|
|`*path_matrix`|Pointer to the `vg_lite_matrix_t` structure that defines the 3x3 transformation matrix of the source pixels into the target. If the matrix is NULL, an identity matrix is assumed, meaning the source is copied directly onto the target at 0,0 location.|
|`*pattern_image`|Pointer to a `vg_lite_matrix_t` structure that defines the 3x3 transformation matrix of the path. If the matrix is NULL, an identity matrix is assumed.|
|`*pattern_matrix`|Pointer to the `vg_lite_buffer_t` structure that describes the source of the image pattern|
| |Pointer to a `vg_lite_matrix_t` structure that defines the 3x3 transformation matrix of the source pixels into the target. If the matrix is NULL, an identity matrix is assumed, which means that the source is copied directly at 0,0 location on the target.|
|`blend`|Specifies one of the `vg_lite_blend_t` enum values for hardware-supported blend modes to be applied to each drawn pixel in the image. If no blending is required, set this value to `VG_LITE_BLEND_NONE (0).`|
|`pattern_mode`|Specifies the `vg_lite_pattern_mode_t` value that defines how the region outside the image pattern is to be filled.|
|`pattern_color`|Specifies a 32bpp ARGB color \(`vg_lite_color_t`\) to be applied to the fill outside the image pattern area when the `pattern_mode` value is `VG_LITE_PATTERN_COLOR.` *\(from Dec 2019, type now vg\_lite\_color\_t, previously was uint32\_t\)*|
|`color`|Specifies a 32bpp ARGB color \(`vg_lite_color_t`\) to be applied as a mix color. If non-zero, the mix color value gets multiplied with each source pixel before blending happens. If a mix color is not needed, set the color parameter to 0 *\(from May 2023\)*.  **Note:** This parameter has no effect if the pattern image `vg_lite_buffer_t` structure member `image_mode` is set to `VG_LITE_ZERO` or `VG_LITE_NORMAL_IMAGE_MODE.`|
|`filter`|Specifies the filter type. All formats available in the `vg_lite_filter_t` enum are valid formats for this function. A value of zero \(0\) indicates `VG_LITE_FILTER_POINT`.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Draw functions](../topics/draw_functions.md)

