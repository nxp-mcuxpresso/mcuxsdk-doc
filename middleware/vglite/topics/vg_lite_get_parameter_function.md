# `vg_lite_get_parameter` function

**Description:**

This function returns the selected VGLite / GPU states to the application.

*\(from Aug 2023\)*

**Syntax:**

```
vg_lite_error_t vg_lite_get_parameter (
    vg_lite_param_type_t          type,
    vg_lite_int32_t               count,
    vg_lite_pointer               params
);

```

**Parameters:**



|Parameter|Description|
|---------|-----------|
|`type`|The parameter type to be queried \(`VG_LITE_GPU_IDLE_STATE, VG_LITE_SCISSOR_RECT`\)|
|`count`|The number of returned parameters|
|`params`|The pointer to the array of returned parameters|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

