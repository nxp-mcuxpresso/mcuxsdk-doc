# vg\_lite\_set\_radial\_grad function

**Description:**

This function is used to set the values for the radial linear gradient definition. *\(from November 2020, requires GC355 or GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_radial_grad (
    vg_lite_radial_gradient_t              *grad,
    vg_lite_uint32_t                       count,
    vg_lite_color_ramp_t                   *color_ramp,
    vg_lite_radial_gradient_parameter_t    grad_param,
    vg_lite_radial_gradient_spreadmode_t   spread_mode,
    vg_lite_uint8_t                        pre_mult
); 

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_radial\_gradient\_t](vg_lite_radial_gradient_t_structure.md) structure for the radial gradient that has to be set|
|`count`|The number of color stops in the gradient. The maximum color stop count is defined by `MAX_COLOR_RAMP_STOPS`, which is currently 256.|
|`*color_ramp`|Pointer to the [vg\_lite\_color\_ramp\_t](vg_lite_color_ramp_t_structure.md) structure that defines the stops for the radial gradient. The five parameters provide the offset and color for each stop. Each stop is defined by a set of floating point values that specify the offset and the sRGBA color and alpha values. Color channel values are in the form of a non-premultiplied \(R, G, B, alpha\) quad. All parameters are in the range of \[0,1\]. The red, green, blue, alpha value of \[0, 1\] is mapped to an 8-bit pixel value \[0, 255\].|
|`grad_param`|The radial gradient parameters are supplied as a vector of 5 floats. Parameters \(cx, cy\) specify the center point, parameters \(fx, fy\) specify the focal point, and r specifies the radius. See structure [vg\_lite\_radial\_gradient\_parameter\_t](vg_lite_radial_gradient_parameter_t_structure.md).|
|`spread_mode`|The tiling mode that is applied to pixels out of the paint after transformation. See enum [vg\_lite\_radial\_gradient\_spreadmode\_t](vg_lite_radial_gradient_spreadmode_t_enumeration.md).|
|`pre_mult`|Controls whether color and alpha values are interpolated in premultiplied or non-premultiplied form. If this value is set to 1, the color value of `vgColorRamp` is multipled by the alpha value of `vgColorRamp`.|

**Returns:**

Returns `VG_LITE_INVALID_ARGUMENTS` to indicate that the parameters are wrong.

**Parent topic:**[Radial gradient functions initialization and control functions](../topics/radial_gradient_functions_initialization_and_contr.md)

