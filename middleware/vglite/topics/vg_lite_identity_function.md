# `vg_lite_identity` function

**Description:**

This function loads an identity matrix into a matrix variable.

**Syntax:**

```
vg_lite_error_t vg_lite_identity (
    vg_lite_matrix_t            *matrix,
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`*matrix`|Pointer to the [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_001.md) structure that will be loaded with an identity matrix.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Matrix control functions](../topics/matrix_control_functions.md)

