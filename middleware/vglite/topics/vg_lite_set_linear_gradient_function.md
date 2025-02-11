# `vg_lite_set_linear_grad` function

**Description:**

This function is used to set the values that define the linear gradient. *\(from April 2022\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_linear_grad (
    vg_lite_ext_linear_gradient_t          *grad,
    vg_lite_uint32_t                       count,
    vg_lite_color_ramp_t                   *color_ramp,
    vg_lite_linear_gradient_parameter_t    grad_param,
    vg_lite_radial_gradient_spreadmode_t   spread_mode,
    vg_lite_uint8_t                        pre_mult
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the `vg_lite_ext_linear_gradient_t` structure that is to be set.|
|`count`|Count of the colors in the gradient. The maximum color stop count is defined by `MAX_COLOR_RAMP_STOPS`, which is set to 256.|
|`*color_ramp`|It is the array of stops for the linear gradient. The number of parameters for each stop is 5, and gives the offset and color of the stop. Each stop is defined by a floating-point *offset* value and four floating-point values containing the sRGBA color and alpha value associated with each stop, in the form of a non-premultiplied \(R, G, B, alpha\) quad. The range of all parameters is \[0,1\].|
|`grad_param`|Gradient parameters as specified in the structure `vg_lite_linear_gradient_parameter_t`.|
|`spread_mode`|The fill mode is applied to the pixels out of the paint after transformation. Uses the same spread mode enumeration types as radial gradient. For details, see `vg_lite_radial_gradient_spreadmode_t` enum.|
|`pre_mult`|This parameter controls whether color and alpha values are interpolated in premultiplied or non-premultiplied form.|



**Returns:**

Returns `VG_LITE_INVALID_ARGUMENTS` to indicate the parameters are wrong.

**Parent topic:**[Linear gradient extended functions](../topics/extended_linear_gradient_initialization_and_contro.md)

