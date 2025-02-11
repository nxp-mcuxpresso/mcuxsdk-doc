# `vg_lite_allocate` function

**Description:**

This function is used to allocate a buffer before it is used in either blit or draw functions.

To allow the hardware to access some memory, such as a source image or target buffer, you must first allocate the memory. The supplied [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure must be initialized with the size \(width and height\) and format of the requested buffer. If the stride is set to zero, then this function fills it in. The only input parameter to this function is the pointer to the buffer structure. If the structure has all the information needed, then appropriate memory is allocated for the buffer.

This function calls the kernel to allocate the memory. The kernel fills in the memory handle, logical address, and hardware addresses in the [vg\_lite\_buffer\_t](vg_lite_buffer_t_structure_001.md) structure.

**Alignment note:**

Vivante GPUs have an alignment requirement of 64 bytes. However, to meet the alignment requirements of the Vivante display controller, the VGLite driver sets the render target buffer alignment to 128 bytes. For source image buffer alignment requirements, see the alignment notes available in [Table 1](alignment_notes.md#IMAGE_SOURCE_ALIGNMENT_SUMMARY).

The vg\_lite\_buffer\_format\_t value descriptions:

**Syntax:**

```
vg_lite_error_t vg_lite_allocate (
       vg_lite_buffer_t       *buffer
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`buffer`|Pointer to the buffer that holds the size and format of the buffer being allocated. Either the memory or address field must be set to a non-zero value to map either a logical or physical address into hardware  accessible memory.|

**Returns:**

-   `VG_LITE_SUCCESS` if the contiguous buffer was allocated successfully.
-   `VG_LITE_OUT_OF_RESOURCES` if there is insufficient memory in the host OS heap for the buffer.
-   `VG_LITE_OUT_OF_MEMORY` if allocation of a contiguous buffer failed.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

