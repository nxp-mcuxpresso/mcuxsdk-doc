# `vg_lite_clear_rad_grad` function

**Description:**

This function is used to clear the values of a radial gradient object and free the image buffer’s memory*. \(from Nov 2020, requires GC355 or GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_clear_radial_grad (
    vg_lite_radial_gradient_t   *grad, 
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_radial\_gradient\_t](vg_lite_radial_gradient_t_structure.md) structure which is to be cleared|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Radial gradient functions initialization and control functions](../topics/radial_gradient_functions_initialization_and_contr.md)

