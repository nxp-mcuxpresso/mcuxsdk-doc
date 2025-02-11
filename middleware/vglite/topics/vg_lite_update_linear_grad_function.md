# `vg_lite_update_linear_grad` function

**Description:**

This function is used to update or generate the corresponding image object to render *\(from April 2022\)*.

The `vg_lite_ext_linear_gradient_t` object has an image buffer that is used to render the linear gradient paint. The image buffer is created/updated according to the specified grad parameters.

**Syntax:**

```
vg_lite_error_t vg_lite_update_linear_grad (
    vg_lite_ext_linear_gradient_t   *grad,
);  
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the `vg_lite_linear_gradient_ext_t` structure that is to be updated or created.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Linear gradient extended functions](../topics/extended_linear_gradient_initialization_and_contro.md)

