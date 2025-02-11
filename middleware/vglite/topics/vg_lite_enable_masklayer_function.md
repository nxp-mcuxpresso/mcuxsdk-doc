# `vg_lite_enable_masklayer` function 

**Description:**

This function controls the availability of mask functionality. The mask is turned off by default. *\(from August - Sept mber 2022, requires GC555 hardware\)*

Applications can use VGLite API [vg\_lite\_query\_feature](vg_lite_query_feature_function.md) \(gcFEATURE\_BIT\_VG\_MASK\) to determine HW support for mask. The blit and draw mask functions below require GC555 hardware support. These functions were introduced in August 2022 and the syntax or name was further refined in September 2022.

**Syntax:**

```
vg_lite_error_t vg_lite_enable_masklayer (
    void
  );
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

