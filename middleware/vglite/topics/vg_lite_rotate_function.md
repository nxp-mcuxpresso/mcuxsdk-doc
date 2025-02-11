# `vg_lite_rotate` function

**Description:**

This function rotates a matrix a specified number of degrees.

**Syntax:**

```
vg_lite_error_t vg_lite_rotate (
    vg_lite_float_t             degrees,
    vg_lite_matrix_t            *matrix
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`degrees`|Number of degrees to rotate the matrix. Positive numbers rotate clockwise.The coordinates for the transformation are given in the surface coordinate system \(top-to-bottom orientation\). Rotations with positive angles are in the clockwise direction.|
|`*matrix`|Pointer to the [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_001.md) structure that has to be rotated|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Matrix control functions](../topics/matrix_control_functions.md)

