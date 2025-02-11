# `vg_lite_enable_scissor` function

**Description:**

This function enables scissor rectangle operation for the rectangle regions defined by `vg_lite_scissor_rects` API. *\(from March 2020, modified August 2020, requires GC355 or GC555 hardware\)*

Applications can use VGLite API [vg\_lite\_query\_feature](vg_lite_query_feature_function.md) \(gcFEATURE\_BIT\_VG\_SCISSOR\) to determine HW support for scissoring. Support is available with GC355 and GC555.

**Syntax:**

```
vg_lite_error_t vg_lite_enable_scissor (
    void
);
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

