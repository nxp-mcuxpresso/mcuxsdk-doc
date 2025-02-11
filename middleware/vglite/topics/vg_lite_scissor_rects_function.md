# `vg_lite_scissor_rects` function 

**Description:**

This function defines scissor rectangle regions on the hardware mask layer. But the scissor function is enable/disabled by `vg_lite_enable_scissor` and `vg_lite_disable_scissor` APIs. *\(from August 2022, requires GC355 or GC555 hardware\)*.

**Syntax:**

```
vg_lite_error_t vg_lite_scissor_rects (
    vg_lite_buffer_t              *target,
    vg_lite_uint32_t              nums,
    vg_lite_rectangle_t           rect[]
);

```

**Parameters:**



|Parameter|Description|
|---------|-----------|
|`target`|Target render buffer that has the scissor mask layer.|
|`nums`|Number of scissor rectangles.|
|`rect[]`|The scissor rectangle array.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

