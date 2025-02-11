# `vg_lite_source_global_alpha` function 

**Description:**

This function sets the image/source global alpha and return a status error code. *\(from June 2021, requires GCNanoUltraV or GC555 hardware\)*

Application can use VGLite API [vg\_lite\_query\_feature](vg_lite_query_feature_function.md) (gcFEATURE_BIT_VG_GLOBAL_ALPHA) to determine HW support for global alpha. The global alpha BLIT-related functions require GCNanoUltraV or GC555 hardware.

**Syntax:**

```
vg_lite_error_t vg_lite_source_global_alpha (
    vg_lite_global_alpha_t        alpha_mode,
    vg_lite_uint8_t               alpha_value
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`alpha_mode`|Global alpha mode value. See enum vg\_lite\_global\_alpha\_t.|
|`alpha_value`|The image/source global alpha value to set.|

**Returns:**

`VG_LITE_SUCCESS` or `VG_LITE_NOT_SUPPORT` if global alpha is not supported.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

