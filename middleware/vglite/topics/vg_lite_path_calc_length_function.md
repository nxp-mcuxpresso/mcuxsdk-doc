# `vg_lite_get_path_length` function

**Description:**

This function calculates the path command buffer length \(in bytes\).

The application is responsible for allocating a buffer according to the buffer length calculated with this function. Then, the buffer is used by the path as a command buffer. The VGLite driver does not allocate the path command buffer.

**Syntax:**

```
vg_lite_uint32_t vg_lite_get_path_length (
    vg_lite_uint8_t             *opcode,
    vg_lite_uint32_t            count,
    vg_lite_format_t            format
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*opcode`|Pointer to the opcode array to use to construct the path. *\(\*opcode from March 2023\)*|
|`count`|The opcode count|
|`format`|The coordinate data format. All formats available in the [vg\_lite\_format\_t](vg_lite_format_t_enumeration.md) enum are valid formats for this function.|

**Returns:**

Returns the command buffer length in bytes.

**Parent topic:**[Vector path functions](../topics/vector_path_functions.md)

