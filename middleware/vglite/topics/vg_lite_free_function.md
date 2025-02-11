# `vg_lite_free` function

**Description:**

This function is used to deallocate the buffer that was previously allocated. It frees up the memory for that buffer.

**Syntax:**

```
vg_lite_error_t vg_lite_free (
       vg_lite_buffer_t       *buffer
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`buffer`|Pointer to a buffer structure that was filled in by calling the [vg\_lite\_allocate\(\)](vg_lite_allocate_function.md) function.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

