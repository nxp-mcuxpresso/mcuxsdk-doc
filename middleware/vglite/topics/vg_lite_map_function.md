# `vg_lite_map` function

**Description:**

This function is used to map the memory appropriately for a particular buffer. For some operating systems, it is used to get proper translation to the physical or logical address of the buffer needed by the GPU.

To use a frame buffer directly as a target buffer:

-   Wrap a [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure around the buffer
-   Call the kernel to map the supplied logical or physical address into hardware accessible memory

For example, if you know the logical address of the frame buffer, set the `memory` field of the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure with that address and call this function. If you know the physical address, set the `memory` field to NULL and program the `address` field with the physical address.

**Syntax:**

```
vg_lite_error_t  vg_lite_map  (
    vg_lite_buffer_t           *buffer,
    vg_lite_map_flag_t         flag,
    int32_t                    fd
    );
```

**Parameters:**

|Name|Description|
|----|-----------|
|`*buffer`|Pointer to a buffer structure that was filled in by calling the [vg\_lite\_allocate\(\)](vg_lite_allocate_function.md) function|
|`flag`|Enumerate the `vg_lite_map_flag_t` value that specifies whether the mapping is for user memory or DMA buffer. *\(from March 2023\)*|
|`fd`|File descriptor for `dma_buf` if the flag is `VG_LITE_MAP_DMABUF`. Otherwise, this parameter is ignored. *\(from March 2023\)*|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

