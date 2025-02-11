# `vg_lite_set_mirror` function 

**Description:**

This function is used to control mirror functionality. By default, the mirror is turned off and the default output orientation is from top to bottom. *\(from August 2022, only for GC555 hardware\)*

Application can use VGLite API `[vg\_lite\_query\_feature](vg_lite_query_feature_function.md) (gcFEATURE_BIT_VG_MIRROR)` to determine HW support for mirror. Mirror functions require GC555 hardware.



**Syntax:**

```
vg_lite_error_t vg_lite_set_mirror (
    vg_lite_orientation_t         orientation
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`orientation`|The orientation mode as defined by the enum [vg\_lite\_orientation\_t](vg_lite_filter_t_enumeration_001_Copy_Copy_Copy.md).`|

**Returns:**

`VG_LITE_SUCCESS` or `VG_LITE_NOT_SUPPORT` if not supported.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

