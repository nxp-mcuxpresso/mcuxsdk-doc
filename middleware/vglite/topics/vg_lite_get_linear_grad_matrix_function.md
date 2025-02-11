# `vg_lite_get_linear_grad_matrix` function

**Description:**

This function returns a pointer to an extended linear gradient object's matrix.*\(from March 2023\)*.

**Syntax:**

```
vg_lite_matrix_t* vg_lite_get_linear_grad_matrix (
    vg_lite_ext_linear_gradient_t   *grad,
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the `vg_lite_ext_linear_gradient_t` structure.|

**Returns:**

Returns a pointer to `vg_lite_matrix_t` for the specified extended linear gradient.

**Parent topic:**[Linear gradient extended functions](../topics/extended_linear_gradient_initialization_and_contro.md)

