# `vg_lite_ext_linear_gradient` structure

This structure defines the organization of the extended parameters possible for a linear gradient *\(from April 2022\)*.

Used in functions: `vg_lite_draw_linear_grad.`

|vg\_lite\_ext\_linear\_gradient\_t members|Type|Description|
|------------------------------------------|----|-----------|
|`count`|`vg_lite_uint32_t`|Count of colors, up to 256.|
|`matrix`|`vg_lite_matrix_t`|The matrix to transform the gradient.|
|`image`|`vg_lite_buffer_t`|The image for rendering as gradient pattern.|
|`linear_grad`|`vg_lite_linear_gradient_parameter_t`|Linear gradient parameters. Includes center point, focal point and radius.|
|`ramp_length`|`vg_lite_uint32_t`|Color ramp length for gradient paints provided to the driver.|
|`color_ramp[VLC_MAX_COLOR_RAMP_STOPS]`|`vg_lite_color_ramp_t`|Color ramp parameter for gradient paints provided to the driver.|
|`converted_length`|`vg_lite_uint32_t`|Converted internal color ramp length.|
|`converted_ramp[VLC_MAX_COLOR_RAMP_STOPS+2]`|`vg_lite_color_ramp_t`|Converted internal color ramp.|
|`pre-multiplied`|`vg_lite_uint8_t`|If this value is set to 1, the color value of `color_ramp` will be multiplied by the alpha value of `color_ramp`.|
|`spread_mode`|`vg_lite_radial_gradient_spreadmode_t`|The spread mode that is applied to the pixels out of the image after transformed.

|

**Parent topic:**[Draw and gradient structures](../topics/draw_and_gradient_structures.md)

