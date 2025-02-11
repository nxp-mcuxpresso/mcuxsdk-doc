# `vg_lite_set_color_transform` function 

**Description:**

This function is used to set pixel scale and bias values for color transformation for each pixel channel. *\(from August 2022, only for GC355 and GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_color_transform (
    vg_lite_color_transform_t     *values
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*values`|Pointer to the color transformation values to set. See enum [`vg_lite_color_transform_t.`](vg_lite_color_t_parameter_001%20-%20Copy.md)|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

