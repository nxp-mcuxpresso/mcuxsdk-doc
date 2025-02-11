# `vg_lite_translate` function

**Description:**

This function translates a matrix to a new location.

**Syntax:**

```
vg_lite_error_t vg_lite_translate (
    vg_lite_float_t             x,
    vg_lite_float_t             y,
    vg_lite_matrix_t            *matrix
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`x`|X location of the transformation.|
|`y`|Y location of the transformation.|
|`matrix`|Pointer to the [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_001.md) structure that will be translated.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Matrix control functions](../topics/matrix_control_functions.md)

