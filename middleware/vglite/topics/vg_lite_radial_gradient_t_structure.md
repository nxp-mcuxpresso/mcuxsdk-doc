# `vg_lite_radial_gradient_t` structure

This structure defines the application of the radial gradient to fill a path. *\(from November 2020, requires GC355 or GC555 hardware\).*

Used in radial gradient functions: `vg_lite_draw_grad, vg_lite_set_radial_grad, vg_lite_update_radial_grad, vg_lite_get_radial_grad, vg_lite_clear_radial_grad`.

|vg\_lite\_radial\_gradient\_t member|Type|Description|
|--------------------------------------|------|-------------|
|`count`|vg\_lite\_uint32\_t|Count of colors, up to 256|
|`matrix`|[vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_002.md)|Structure that specifies the transform matrix for the gradient|
|`image`|[vg\_lite\_buffer\_t](vg_lite_buffer_t_structure.md)|Structure that specifies the image for rendering as a gradient pattern|
|`radial_grad`|[vg\_lite\_radial\_gradient\_parameter\_t](vg_lite_radial_gradient_parameter_t_structure.md)|Structure that specifies the location of the gradient’s center point \(cx, cy\), focal point\(fx, fy\) and radius\(r\)|
|`ramp_length`|vg\_lite\_uint32\_t |Color ramp parameters for gradient paints provided to the driver|
|`color_ramp[VLC_MAX_COLOR_RAMP_STOPS]`|[vg\_lite\_color\_ramp\_t](vg_lite_color_ramp_t_structure.md)|Structure that specifies the color ramp|
|`converted_length`|vg\_lite\_uint32\_t|Converted internal color ramp.|
|`converted_ramp[VLC_MAX_COLOR_RAMP_STOPS+2]`|[vg\_lite\_color\_ramp\_t](vg_lite_color_ramp_t_structure.md)|Structure that specifies the internal color ramp|
|`pre_multiplied`|vg\_lite\_uint32\_t|If this value is set to 1, the color value of `color_ramp` will be multiplied by the alpha value of `color_ramp`.|
|`spread_mode`|[vg\_lite\_radial\_gradient\_spreadmode\_t](vg_lite_radial_gradient_spreadmode_t_enumeration.md)|Enum that specifies the tiling mode, which is applied to the pixels out of the image after transformation|

**Parent topic:**[Draw and gradient structures](../topics/draw_and_gradient_structures.md)

