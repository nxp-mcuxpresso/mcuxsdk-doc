# `vg_lite_append_path` function

**Description:**

This function assembles the command buffer for the path. The command buffer is allocated by the application and assigned to the path. This function makes the final GPU command buffer for the path based on the input opcodes \(cmd\) and coordinates \(data\). The application is responsible for allocating a buffer large enough for the path*. \(from Jan 2022, returns a vg\_lite\_error\_t status code\)*

**Syntax:**

```
vg_lite_error_t vg_lite_append_path (
    vg_lite_path_t              *path
    vg_lite_uint8_t             *opcode,
    vg_lite_pointer             data,
    vg_lite_uint32_t            seg_count
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to the [vg\_lite\_path\_t](vg_lite_path_t_structure.md) structure with the path definition.|
|`*opcode`|Pointer to the opcode array to use to construct the path. *\(\*opcode from March 2023\)*|
|`data`|Pointer to the coordinate data array to use to construct the path|
|`seg_count`|The opcode count|

**Returns:**

Returns VG\_LITE\_SUCCESS if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Vector path functions](../topics/vector_path_functions.md)

