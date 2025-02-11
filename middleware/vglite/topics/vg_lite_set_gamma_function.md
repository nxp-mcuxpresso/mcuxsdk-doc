# `vg_lite_set_gamma` function 

**Description:**

This function sets a gamma value.

Application can use the VGLite API `vg_lite_query_feature`\(gcFEATURE\_BIT\_VG\_GAMMA\) to determine HW support for gamma.

**Syntax:**

```
vg_lite_error_t vg_lite_set_gamma (
    vg_lite_gamma_conversion_t    gamma_value
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`gamma_value`|Sets a gamma value. See enum [vg\_lite\_gamma\_conversion\_t](vg_lite_buffer_transparency_mode_t_enumeration.md).|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

