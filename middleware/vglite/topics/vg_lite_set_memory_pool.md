# `vg_lite_set_memory_pool` 

**Description:**

This function sets the specific memory pool from which certain type of buffers, `VG_LITE_COMMAND_BUFFER, VG_LITE_TESSELLATION_BUFFER`, or `VG_LITE_RENDER_BUFFER`, should be allocated. By default, all types of buffers are allocated from `VG_LITE_MEMORY_POOL_1`. This API must be called before `vg_lite_init()` for setting `VG_LITE_COMMAND_BUFFER` or `VG_LITE_TESSELLATION_BUFFER` memory pools. This API can be called anytime for `VG_LITE_RENDER_BUFFER` to affect the following `vg_lite_allocate() calls`.*\(from December 2023\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_memory_pool (
    vg_lite_buffer_type_t        type,
    vg_lite_memory_pool_t        pool
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`type`|The buffer type \(`VG_LITE_COMMAND_BUFFER, VG_LITE_TESSELLATION_BUFFER,` or `VG_LITE_RENDER_BUFFER`\) to be allocated from memory pool.|
|`pool`|The memory pool \(`VG_LITE_MEMORY_POOL_1, VG_LITE_MEMORY_POOL_2`\) from which the buffer type should be allocated.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the memory pool set is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

