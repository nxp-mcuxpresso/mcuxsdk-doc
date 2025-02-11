# `vg_lite_get_grad_matrix` function

**Description:**

This function is used to get a pointer to the transformation matrix of the gradient object. It allows an application to manipulate the matrix to facilitate correct rendering of the gradient path.

**Syntax:**

```
vg_lite_error_t vg_lite_get_grad_matrix (
       vg_lite_linear_gradient_t         *grad
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_linear\_gradient\_t](vg_lite_linear_gradient_t_structure.md) structure, which contains the matrix to be retrieved|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Linear gradient initialization and control functions](../topics/linear_gradient_initialization_and_control_functio.md)

