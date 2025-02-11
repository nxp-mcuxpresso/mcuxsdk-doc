# `vg_lite_get_transform_matrix` function

**Description:**

This function generates a 3x3 homogenous transform matrix from 4 float point source coordinates and 4 float point target coordinates. *\(from March 2021\)*

**Syntax:**

```
vg_lite_error_t vg_lite_get_transform_matrix (
    vg_lite_float_point4_t       src,
    vg_lite_float_point4_t       dst,
    vg_lite_matrix_t             *mat
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`src`|Pointer to the four 2D points that form a source polygon|
|`dst`|Pointer to the four 2D points that form a destination polygon|
|`mat`|Output parameter, pointer to a 3x3 homogenous matrix that transforms the source polygon to a destination polygon.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

