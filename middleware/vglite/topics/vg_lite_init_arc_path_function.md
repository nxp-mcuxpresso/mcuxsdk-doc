# `vg_lite_init_arc_path` function

**Description:**

This function initializes an arc path definition with specified values. *\(from February 2021\)*

**Syntax:**

```
vg_lite_error_t vg_lite_init_arc_path (
    vg_lite_path_t              *path,
    vg_lite_format_t            format,
    vg_lite_quality_t           quality,
    vg_lite_uint32_t            length,
    vg_lite_pointer             *data,
    vg_lite_float_t             min_x, 
    vg_lite_float_t             min_y,
    vg_lite_float_t             max_x, 
    vg_lite_float_t             max_y
);
```

**Parameters:**

|Parameter|Function|
|---------|--------|
|`*path`|Pointer to the [vg\_lite\_path\_t](vg_lite_path_t_structure_001.md) structure for the path object to be initialized with the member values specified.|
|`format`|The coordinate data format. The vg\_lite\_format\_t enum value should be FP32.|
|`quality`|The quality for the path object. All formats available in the [vg\_lite\_quality\_t](vg_lite_quality_t_enumeration.md) enum are valid formats for this function.|
|`length`|The length of the path data \(in bytes\).|
|`*data`|Pointer to path data.|
|`min_x` `min_y` `max_x` `max_y`|Minimum and maximum x and y values specifying the bounding box of the path.|

**Returns:**

Returns VG\_LITE\_SUCCESS if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Vector path functions](../topics/vector_path_functions.md)

