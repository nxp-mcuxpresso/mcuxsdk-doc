# `vg_lite_render_masklayer` function 

**Description:**

This function draws the mask layer according to the specified path, color, and matrix information. *\(from August-September 2022, requires GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_render_masklayer (
    vg_lite_buffer_t              *masklayer,
    vg_lite_mask_operation        operation,
    vg_lite_path_t                *path,
    vg_lite_fill_t                fill_rule,
    vg_lite_color_t               color,
    vg_lite_matrix_t              *matrix
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*masklayer`|Points to the address of the buffer of the destination mask layer.|
|`operation`|Blending mode to be applied to each image pixel, as defined by the enum `vg_lite_mask_operation_t`|
|`*path`|Pointer to the [vg\_lite\_path\_t](vg_lite_path_t_structure.md) structure containing path data that describes the path to draw. Refer to [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md) in this document for opcode detail.|
|`fill_rule`|Specifies the [vg\_lite\_fill\_t](vg_lite_fill_t_enumeration.md) enum value for the fill rule for the path.|
|`color`|Specifies the color [vg\_lite\_color\_t](vg_lite_color_t_parameter.md) RGBA value to be applied to each pixel drawn by the path.|
|`*matrix`|Points to a [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure.md) structure that defines the 3x3 transformation matrix of the path. If the matrix is NULL, an identity matrix is assumed, meaning the source is copied directly on the target at 0,0 location. which is usually a bad idea since the path can be anything.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

