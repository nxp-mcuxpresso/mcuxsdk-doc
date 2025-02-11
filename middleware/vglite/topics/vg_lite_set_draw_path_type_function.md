# `vg_lite_set_path_type` function

**Description:**

This function sets the path type*. \(from March 2022\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_path_type (
    vg_lite_path_t              *path,
    vg_lite_path_type_t         path_type
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to the [**vg\_lite\_path\_t**](vg_lite_set_draw_path_type_function.md) structure that describes the vector path.|
|`path_type`|Pointer to a `vg_lite_path_type_t` structure that describes the path type.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Stroke functions](../topics/stroke_functions.md)

