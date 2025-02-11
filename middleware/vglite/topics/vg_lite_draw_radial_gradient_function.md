# vg\_lite\_draw\_radial\_grad function

**Description:**

This function is used to fill a path with a radial gradient according to the specified fill rules. The specified path is transformed according to the selected matrix and is filled with the radial color gradient. The application can use `VGLite API vg_lite_query_feature` \(`gcFEATURE_BIT_VG_RADIAL_GRADIENT`\) to determine HW support for radial gradient.

**Syntax:**

```
vg_lite_error_t vg_lite_draw_radial_grad (
    vg_lite_buffer_t            *target,
    vg_lite_path_t              *path, 
    vg_lite_fill_t              fill_rule, 
    vg_lite_matrix_t            *path_matrix, 
    vg_lite_radial_gradient_t   *grad,
    vg_lite_color_t             paint_color,
    vg_lite_blend_t             blend,
    vg_lite_filter_t            filter
);  
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*target`|Pointer to the `vg_lite_buffer_t` structure containing data describing the target path.|
|`*path`|Pointer to the `vg_lite_path_t` structure containing path data that describes the path to draw for and fill with the radial gradient. See opcode details in [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md).|
|`fill_rule`|Specifies the `vg_lite_fill_t` enum value for the fill rule for the path|
|`*path_matrix`|Pointer to a `vg_lite_matrix_t` structure that defines the 3x3 transformation matrix of the path. If the matrix is NULL, an identity matrix is assumed; however, his option is not preferable.|
|`*grad`|Pointer to the `vg_lite_radial_gradient_t` structure that contains the values to be used to fill the path. **Note:** grad-\>image.image\_mode does not support `VG_LITE_MULTIPLY_IMAGE_MODE` .|
|`paint_color`|Specifies the paint color `vg_lite_color_t` RGBA value to be applied by `VG_LITE_RADIAL_GRADIENT_SPREAD_FILL` set by the function `vg_lite_set_radial_grad`. When pixels are out of the image after transformation, `paint_color` is applied to them. For details, see `vg_lite_radial_gradient_spreadmode_t`.|
|`blend`|Specifies the blend mode in the `vg_lite_blend_t` enum to be applied to each drawn pixel. If no blending is required, set this value to `VG_LITE_BLEND_NONE` \(0\).|
|`filter`|Specified the filter mode `vg_lite_filter_t` enum value to be applied to each drawn pixel. If no filtering is required, set this value to `VG_LITE_BLEND_POINT` \(0\).|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Draw functions](../topics/draw_functions.md)

