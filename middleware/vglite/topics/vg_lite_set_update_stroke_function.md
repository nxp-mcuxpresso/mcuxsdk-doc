# `vg_lite_update_stroke` function

**Description:**

This function uses the path and stroke attributes as specified with the function `vg_lite_set_stroke` to update the stroke path's parameters and generate stroke path data *. \(from March 2022\)*

**Syntax:**

```
vg_lite_error_t vg_lite_update_stroke (
    vg_lite_path_t              *path,
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to the [**vg\_lite\_path\_t**](vg_lite_set_update_stroke_function.md) structure that describes the path.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Stroke functions](../topics/stroke_functions.md)

