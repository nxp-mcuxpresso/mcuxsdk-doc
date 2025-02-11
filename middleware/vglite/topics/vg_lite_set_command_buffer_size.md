# `vg_lite_set_command_buffer_size` 

**Description:**

This function is optional. If used, call it before `vg_lite_init` if you want to change the command buffer size. *\(available from March 2020\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_command_buffer_size (
    vg_lite_uint32_t            size
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`size`|Size of the VGLite Command buffer. Default is 64K.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the flush is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

