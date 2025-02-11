# Radial gradient functions initialization and control functions

The following functions are available only with IP that supports radial gradients, such as GC355 and GC555. These functions are not available with GCNanoLiteV, or GCNanoUltraV or GCNanoV.

**Note:** There is no init function required for radial gradients. Buffer initialization is done through the `vg_lite_update_radial_grad` function. *\(from Nov 2020, requires GC355 or GC555 hardware\)*


```{include} ../topics/vg_lite_set_rad_grad_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_update_rad_grad_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_get_rad_grad_matrix_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_clear_rad_grad_function.md
:heading-offset: 2
```

**Parent topic:**[Vector-dased draw operations](../topics/vector-dased_draw_operations.md)

