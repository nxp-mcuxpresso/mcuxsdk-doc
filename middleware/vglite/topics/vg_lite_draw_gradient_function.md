# vg\_lite\_draw\_grad function

**Description:**

This function is used to fill a path with a linear gradient according to the specified fill rules. The specified path is transformed according to the selected matrix and is filled with the specified color gradient.

**Syntax:**

```
vg_lite_error_t vg_lite_draw_grad (
    vg_lite_buffer_t            *target,
    vg_lite_path_t              *path, 
    vg_lite_fill_t              fill_rule, 
    vg_lite_matrix_t            *matrix, 
    vg_lite_linear_gradient_t   *grad, 
    vg_lite_blend_t             blend
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*target`|Pointer to the `vg_lite_buffer_t` structure containing data describing the target path.|
|`*path`|Pointer to the `vg_lite_path_t` structure containing path data that describes the path to draw and fill with the linear gradient. See opcode details in [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md).|
|`fill_rule`|Specifies the `vg_lite_fill_t` enum value for the fill rule for the path|
|`*matrix`|Pointer to the `vg_lite_matrix_t` structure that defines the 3x3 transformation matrix of the path. If the matrix is NULL, an identity matrix is assumed; however, this option is not preferable.|
|`*grad`|Pointer to the `vg_lite_linear_gradient_t` structure that contains the values to be used to fill the path.|
|`blend`|Specifies the blend mode in the `vg_lite_blend_t` enum to be applied to each drawn pixel. If no blending is required, set this value to `VG_LITE_BLEND_NONE` \(0\).|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Draw functions](../topics/draw_functions.md)

