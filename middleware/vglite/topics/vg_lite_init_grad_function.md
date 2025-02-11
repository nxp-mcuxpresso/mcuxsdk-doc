# `vg_lite_init_grad` function

**Description:**

This function initializes the internal buffer for the linear gradient object with default settings for rendering.

**Syntax:**

```
vg_lite_error_t vg_lite_init_grad (
       vg_lite_linear_gradient_t *grad
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_linear\_gradient\_t](vg_lite_linear_gradient_t_structure.md) structure, which defines the gradient to be initialized. Default values are used.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Linear gradient initialization and control functions](../topics/linear_gradient_initialization_and_control_functio.md)

