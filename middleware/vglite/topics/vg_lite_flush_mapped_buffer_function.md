# `vg_lite_flush_mapped_buffer` function 

**Description:**

This function flushes the CPU cache for the mapped buffer to make sure the buffer contents are written to GPU memory.

**Syntax:**

```
vg_lite_error_t vg_lite_flush_mapped_buffer (
    vg_lite_buffer_t           *buffer
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`*buffer`|Pointer to a buffer structure that was filled in by calling the [vg\_lite\_map\(\)](vg_lite_map_function.md) function|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

