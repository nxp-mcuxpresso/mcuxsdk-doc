# `vg_lite_set_command_buffer`

**Description:**

This function sets a user-defined external memory buffer \(physical, 64-byte aligned\) as the VGLite command buffer. By default, the VGLite driver allocates a static command buffer internally. Thus, it is not necessary for an application to allocate and set the command buffer. This function is only used for devices where an application needs to allocate the command buffer dynamically. *\(from December 2021\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_command_buffer (
    vg_lite_uint32_t            physical,
    vg_lite_uint32_t            size
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`physical`|The physical address of a memory buffer. The address must be 64-byte aligned.|
|`size`|The size of memory buffer. The size must be 128-byte aligned.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the command buffer set is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

