# `vg_lite_quality_t` enumeration

Specifies the level of hardware assisted anti-aliasing.

Used in structure: `vg_lite_path_t`.

Used in function: `vg_lite_init_path`, `vg_lite_init_arc_path`.

|vg\_lite\_quality\_t string values|Description|
|------------------------------------|-------------|
|`VG_LITE_HIGH`|High quality: 16x coverage sample anti-aliasing|
|`VG_LITE_UPPER`|Upper quality: 8x coverage sample anti-aliasing. Use [vg\_lite\_query\_feature](vg_lite_query_feature_function.md) to determine availability of 8x CSAA \(feature enum value `gcFEATURE_BIT_VG_QUALITY_8X`.\(deprecated from June 2020, available with supported hardware from August 2022\).|
|`VG_LITE_MEDIUM`|Medium quality: 4x coverage sample anti-aliasing|
|`VG_LITE_LOW`|Low quality: No anti-aliasing|

**Parent topic:**[Vector path enumerations](../topics/vector_path_enumerations.md)

