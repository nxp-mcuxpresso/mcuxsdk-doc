# `vg_lite_scale` function

**Description:**

This function scales a matrix in both horizontal and vertical directions.

**Syntax:**

```
vg_lite_error_t vg_lite_scale (
    vg_lite_float_t             scale_x,
    vg_lite_float_t             scale_y,
    vg_lite_matrix_t            *matrix
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`scale_x`|Horizontal scale|
|`scale_y`|Vertical scale|
|`matrix`|Pointer to the [vg\_lite\_matrix\_t](vg_lite_matrix_t_structure_001.md) structure that will be scaled.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Matrix control functions](../topics/matrix_control_functions.md)

