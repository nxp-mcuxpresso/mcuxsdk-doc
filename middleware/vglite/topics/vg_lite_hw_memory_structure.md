# `vg_lite_hw_memory` structure

This structure gets the memory allocation information recorded by the kernel.

Used in structure: `vg_lite_path_t`.

|vg\_lite\_hw\_memory\_t member|Type|Description|
|--------------------------------|------|-------------|
|`handle`|`vg_lite_pointer`|GPU memory object handle|
|`memory`|`vg_lite_pointer`|Logical memory address|
|`address`|`vg_lite_uint32_t`|GPU memory address|
|`bytes`|`vg_lite_uint32_t`|Size of memory|
|`property`|`vg_lite_uint32_t`|Bit 0 is used for path upload: -   0: Disable path data uploading \(always embedded into command buffer\) -   1: Enable auto path data uploading|

**Parent topic:**[Vector path structures](../topics/vector_path_structures.md)

