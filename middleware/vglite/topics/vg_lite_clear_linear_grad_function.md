# `vg_lite_clear_linear_grad` function

**Description:**

This function is used to clear the linear gradient object. This resets the grad members and free the image buffer's memory *\(from April 2022\)*.

**Syntax:**

```
vg_lite_error_t vg_lite_clear_linear_grad (
    vg_lite_ext_linear_gradient_t    *grad,
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the `vg_lite_linear_gradient_ext_t` structure that is to be cleared.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Linear gradient extended functions](../topics/extended_linear_gradient_initialization_and_contro.md)

