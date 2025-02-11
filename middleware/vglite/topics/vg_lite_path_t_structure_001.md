# `vg_lite_path_t` structure

This structure describes VGLite path data.

Path data is made of op codes and coordinates. The format for op codes is always VG\_LITE\_S8. For more details on opcodes, see [Vector path opcodes for plotting paths](vector_path_opcodes_for_plotting_paths.md).

Used in init functions: `vg_lite_init_path, vg_lite_init_arc_path, vg_lite_upload_path, vg_lite_clear_path, vg_lite_append_path.`

Used in draw functions: `vg_lite_draw, vg_lite_draw_grad, vg_lite_draw_radial_grad, vg_lite_draw_pattern.`

|vg\_lite\_path\_t members|Type|Description|
|---------------------------|------|-------------|
|`bounding_box[4]`|`vg_lite_float_t`|bounding box for path \[0\] left  \[1\] top  \[2\] right  \[3\] bottom|
|`quality`|[vg\_lite\_quality\_t](vg_lite_quality_t_enumeration.md) |enum for quality hint for the path, anti-aliasing level|
|`format` |[vg\_lite\_format\_t](vg_lite_format_t_enumeration.md) |enum for coordinate format|
|`uploaded`|[vg\_lite\_hw\_memory\_t](vg_lite_hw_memory_structure.md)|struct with path data that has been uploaded into GPU addressable memory|
|`path_length`|`vg_lite_uint32_t`|number of bytes in the path|
|`path`|`vg_lite_pointer`|pointer to path data|
|`path_changed`|`vg_lite_int8_t`|0: not changed; 1: changed.|
|`pdata_internal`|`vg_lite_int8_t`|0: path data memory is allocated by application; 1: path data memory is allocated by driver.|
|`path_type`|[vg_lite_path_type_t](vg_lite_path_t_structure.md)|The draw path type as specified in enum [vg\_lite\_path\_type\_t.](vg_lite_path_t_structure.md) *\(added for stroke control, from March 2022\)*|
|`*stroke`|`vg_lite_stroke_t`|As defined by structure vg\_lite\_stroke\_t *\(added for stroke control, from March 2022\)*|
|`stroke_path`|`vg_lite_pointer`|Pointer to the physical description of the stroke path. *\(added for stroke control, from March 2022\)*|
|`stroke_size`|`vg_lite_uint32_t`|Number of bytes in the stroke path data. *\(added for stroke control, from March 2022\)*|
|`stroke_color`|[vg\_lite\_color\_t](vg_lite_color_t_parameter.md)|The stroke path fill color. *\(from Sept 2022\)*|
|`add_end`|`vg_lite_int8_t`|Flag that add end\_path in drive*r \(from March 2023\)*|

**Special notes for path objects:**

-   Endianness has no impact, as it is aligned against the boundaries
-   Multiple contiguous opcodes should be packed by the size of the specified data format. For example, by 2 bytes for VG\_LITE\_S16 or by 4 bytes for VG\_LITE\_S32.

For example, because opcodes are 8-bit \(1-byte\), 16-bit \(2-byte\), or 32-bit \(4-byte\) data types:

```
…
<opcode1_that_needs_data>
<align_to_data_size>
<data_for_opcode1>
<opcode2_that_doesnt_need_data>
<align_to_data_size>
<opcode3_that_needs_data>
<align_to_data_size>
<data_for_opcode3>
…
```

-   Path data in the array should always be 1-, 2-, or 4-byte aligned, depending on the format:

For example, for 32-bit \(4-byte\) data types:

```
…
<opcode1_that_needs_data>
<pad to 4 bytes>
<4 byte data_for_opcode1>
<opcode2_that_doesnt_need_data>
<pad to 4 bytes>
<opcode3_that_needs_data>
<pad to 4 bytes>
<4 byte data_for_opcode3>
…
```

**Parent topic:**[Vector path structures](../topics/vector_path_structures.md)

