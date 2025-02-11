# `vg_lite_enable_dither` function 

**Description:**

This function is used to enable the dither function. Dither is turned off by default. The application can use the VGLite API `vg_lite_query_feature` \(gcFEATURE\_BIT\_VG\_DITHER\) to determine HW support for dither.

**Syntax:**

```
vg_lite_error_t vg_lite_enable_dither (
);
```

**Parameters:** None

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

