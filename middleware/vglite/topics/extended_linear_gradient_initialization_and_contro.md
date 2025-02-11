# Linear gradient extended functions

The following functions are available only with IP that includes hardware support for extended linear gradient capabilities, such as GC355 and GC555. These functions are not available with GCNanoLiteV, GCNanoUltraV, or GCNanoV. Applications can use VGLite API `vg_lite_query_feature (gcFEATURE_BIT_VG_LINEAR_GRADIENT_EXT)` to determine HW support for linear gradient.


```{include} ../topics/vg_lite_set_linear_gradient_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_get_linear_grad_matrix_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_draw_linear_grad.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_update_linear_grad_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_clear_linear_grad_function.md
:heading-offset: 2
```

**Parent topic:**[Vector-dased draw operations](../topics/vector-dased_draw_operations.md)

