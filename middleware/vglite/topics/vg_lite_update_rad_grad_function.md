# `vg_lite_update_radial_grad` function

**Description:**

This function is used to update or generate values for an image object that is going to be rendered. The vg\_lite\_radial\_gradient\_t object has an image buffer that is used to render the gradient pattern. The image buffer will be created or updated with the corresponding gradient parameters. *\(from November 2020, requires GC355 or GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_update_radial_grad (
    vg_lite_radial_gradient_t   *grad, 
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_radial\_gradient\_t](vg_lite_radial_gradient_t_structure.md) structure, which contains the updated values to be used for the object to be rendered|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Radial gradient functions initialization and control functions](../topics/radial_gradient_functions_initialization_and_contr.md)

