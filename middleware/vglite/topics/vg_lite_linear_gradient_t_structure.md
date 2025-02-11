# `vg_lite_linear_gradient_t` structure

This structure defines the organization of a linear gradient in VGLite data. The linear gradient is applied to filling a path. It generates a 256x1 image according to the specified settings.

Used in init and draw functions: `vg_lite_init_grad, vg_lite_set_grad, vg_lite_update_grad, vg_lite_get_grad_matrix, vg_lite_clear_grad, vg_lite_draw_grad.`

|vg\_lite\_linear\_gradient\_t constants|Type|Description|
|---------------------------------------|----|-----------|
|`VLC_MAX_GRADIENT_STOPS`|`vg_lite_int32_t`|Constant. Maximum number of gradient colors = 16.|
|**vg\_lite\_linear\_gradient\_t members**| | |
|`colors [VLC_MAX_GRADIENT_STOPS]`|`vg_lite_uint32_t`|Color array for the gradient|
|`count`|`vg_lite_uint32_t`|Number of colors|
|`stops [VLC_MAX_GRADIENT_STOPS]`|`vg_lite_uint32_t`|Number of color stops, from 0 to 255|
|`matrix`|`vg_lite_matrix_t`|Struct for the matrix to transform the gradient color ramp|
|`image`|`vg_lite_buffer_t`|Image object struct to represent the color ramp|



**Parent topic:**[Draw and gradient structures](../topics/draw_and_gradient_structures.md)

