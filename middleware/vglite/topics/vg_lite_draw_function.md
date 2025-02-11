# `vg_lite_draw` function

**Description:**

This function performs a hardware accelerated 2D vector draw operation.

The size of the tessellation buffer can be specified at initialization and it is aligned with the minimum hardware alignment requirements of the kernel. Specifying a smaller size for tessellation buffer allocates less memory but reduces performance. Because the hardware walks the target with the provided tessellation window size, a path may be sent to the hardware multiple times. It is a good practice to set the tessellation buffer size to the most common path size. For example, if all you do is render up to 24-point fonts, you can set the tessellation buffer to 24x24.

**Note:**

-   All the color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md) enum are supported as the destination buffer for the draw function
-   The hardware does not support strokes; they must be converted to paths before you use them in the draw API

**Syntax:**

```
vg_lite_error_t vg_lite_draw (
       vg_lite_buffer_t         *target,
       vg_lite_path_t           *path,
       vg_lite_fill_t           fill_rule,
       vg_lite_matrix_t         *matrix,
       vg_lite_blend_t          blend,
       vg_lite_color_t          color
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*target`|Pointer to the `vg_lite_buffer_t` structure for the destination buffer. All color formats available in the `vg_lite_buffer_format_t` enum are valid destination formats for the draw function.|
|`*path`|Pointer to the `vg_lite_path_t` structure containing path data that describes the path to draw. See opcode details in [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md).|
|`fill_rule`|Specifies the `vg_lite_fill_t` enum value for the fill rule for the path|
|`*matrix`|Pointer to a `vg_lite_matrix_t` structure that defines the *affine* transformation matrix of the path. If the matrix is NULL, an identity matrix is assumed. **Note:** Non-affine transformations are not supported by `vg_lite_draw`; therefore, a perspective transformation matrix might have unexpected effects on path rendering.|
|`blend`|Select one of the hardware-supported blend modes in the `vg_lite_blend_t` enum to be applied to each drawn pixel. If no blending is required, set this value to `VG_LITE_BLEND_NONE` \(0\).|
|`color`|The color applied to each pixel drawn by the path.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Draw functions](../topics/draw_functions.md)

