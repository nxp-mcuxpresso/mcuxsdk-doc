# `vg_lite_set_scissor` function

**Description:**

This is a legacy scissor API function that can be used to set a single scissor rectangle for the render target. This scissor API is supported by a different hardware mechanism other than the mask layer and it has better performance than the mask layer scissor function.

This API is not enabled/disabled by `vg_lite_enable_scissor` and `vg_lite_disable_scissor` APIs. Instead, the `vg_lite_set_scissor` API calls with a valid scissor rectangle input \(x, y, right, bottom\) enables the scissor function by default. The `vg_lite_set_scissor` API call with input parameter \(-1, -1, -1, -1\) disables the scissor function. *\(requires GC355 or GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_scissor (
    vg_lite_int32_t               x,
    vg_lite_int32_t               y,
    vg_lite_int32_t               right,
    vg_lite_int32_t               bottom
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`x`|X Origin of rectangle, left coordinate in pixels|
|`Y`|Y Origin of rectangle, top coordinate in pixels|
|`right`|X rightmost pixel of the rectangle|
|`bottom`|Y bottom pixel of the rectangle|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

