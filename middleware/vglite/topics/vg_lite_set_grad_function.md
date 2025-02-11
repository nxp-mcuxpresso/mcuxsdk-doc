# `vg_lite_set_grad` function

**Description:**

This function is used to set values for the members of the `vg_lite_linear_gradient_t` structure.

**Note:** The `vg_lite_set_grad` API adopts the following rules to set the default gradient colors if the input parameters are incomplete or invalid:

-   If no valid stops have been specified \(for example, due to an empty input array, out-of-range or out-of-order stops\), a stop at 0 with \(R, G, B, A\) color \(0.0, 0.0, 0.0, 1.0\) \(opaque black\) and a stop at 1 with color \(1.0, 1.0, 1.0, 1.0\) \(opaque white\) are implicitly defined
-   If at least one valid stop has been specified, but none has been defined with an offset of 0, then an implicit stop is added with an offset of 0 and the same color as the first user-defined stop
-   If at least one valid stop has been specified, but none has been defined with an offset of 1, then an implicit stop is added with an offset of 1 and the same color as the last user-defined stop

**Syntax:**

```
vg_lite_error_t vg_lite_set_grad (
       vg_lite_linear_gradient_t       *grad,
       uint32_t                        count,
       uint32_t                        *colors,
       uint32_t                        *stops
      );
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*grad`|Pointer to the [vg\_lite\_linear\_gradient\_t](vg_lite_linear_gradient_t_structure.md) structure to be set|
|`count`|The number of colors in the linear gradient. The maximum color stop count is defined by `VLC_MAX_GRAD` which is 16.|
|`*colors`|Specifies the color array for the gradient stops. The color is in ARGB8888 format with alpha in the upper byte.|
|`*stops`|Pointer to the gradient stop offset|

**Returns:**

Always returns `VG_LITE_SUCCESS`.

**Parent topic:**[Linear gradient initialization and control functions](../topics/linear_gradient_initialization_and_control_functio.md)

