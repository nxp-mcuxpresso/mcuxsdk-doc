# `vg_lite_update_grad` function

**Description:**

This function is used to update or generate values for an image object that is going to be rendered. The `vg_lite_linear_gradient_t` object has an image buffer, which is used to render the gradient pattern. The image buffer is created or updated with the corresponding gradient parameters.

**Syntax:**

```
vg_lite_error_t vg_lite_update_grad (
       vg_lite_linear_gradient_t     *grad
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_linear\_gradient\_t](vg_lite_linear_gradient_t_structure.md) structure, which contains the update values to be used for the object to be rendered|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Linear gradient initialization and control functions](../topics/linear_gradient_initialization_and_control_functio.md)

