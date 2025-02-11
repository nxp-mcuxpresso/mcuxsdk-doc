# `vg_lite_clear_path` function

**Description:**

This function will clear and reset path member values. If the path has been uploaded, it frees the GPU memory allocated when uploading the path. *\(From Dec 2019 returns vg\_lite\_error\_t, previous was void.\)*

.

**Syntax:**

```
vg_lite_error_t vg_lite_clear_path (
    vg_lite_path_t              *path
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to the `vg_lite_path_t` path definition to be cleared.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Vector path functions](../topics/vector_path_functions.md)

