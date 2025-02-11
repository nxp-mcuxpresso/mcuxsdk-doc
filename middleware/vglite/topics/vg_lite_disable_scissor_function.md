# `vg_lite_disable_scissor` function

**Description:**

This function disables scissor operation for the rectangle regions defined by the `vg_lite_scissor_rects` API. *\(from March 2020, modified August 2020, requires GC355 or GC555 hardware\)*.

**Syntax:**

```
vg_lite_error_t vg_lite_disable_scissor (
    void
);
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

