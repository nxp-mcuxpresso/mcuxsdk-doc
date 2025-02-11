# `vg_lite_disable_color_transform` function

**Description:**

This function is used to disable color transformation. By default, the color transform is turned off. *\(from Sept 2022, only for GC355 and GC555 hardware\)*

Applications can use the VGLite API [vg\_lite\_query\_feature](vg_lite_query_feature_function.md)(gcFEATURE_BIT_VG_COLOR_TRANSFORMATION)` to determine HW support for color transformation. Support is available with GC355 and GC555.

**Syntax:**

```
vg_lite_error_t vg_lite_disable_color_transform (
);

```

**Parameters:** None

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

