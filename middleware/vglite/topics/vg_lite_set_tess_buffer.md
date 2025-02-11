# `vg_lite_set_tess_buffer`

**Description:**

This function specifies a memory buffer from an application as the VGLite driver’s tessellation buffer. By default, the VGLite driver allocates a static tessellation buffer internally. Thus, it is not necessary for an application to allocate and set the tessellation buffer. This function is only used for devices where the application needs to allocate the tessellation buffer dynamically. *\(from December 2021\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_tess_buffer (
    vg_lite_uint32_t            physical,
    vg_lite_uint32_t            size
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`physical`|The physical address of a tessellation buffer. The address must be 64-byte aligned.|
|`size`|The size of tessellation buffer. tessellation buffer size = target buffer's height \* 128B.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the tessellation buffer set is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

