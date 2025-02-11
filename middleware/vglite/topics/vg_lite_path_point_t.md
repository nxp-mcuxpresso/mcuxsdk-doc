# `vg_lite_path_point_t` structure 

The structure `vg_lite_path_point_ptr` points to the `vg_lite_path_point` structure which provides path detail *\(from March 2022\)*

Used \(`vg_lite_path_point_ptr`\) in structures: `vg_lite_path_point_t, vg_lite_stroke_conversion. vg_lite_sub_path_t.`



|**vg\_lite\_path\_point\_t members**|**Type**|**Description**|
|------------------------------------|--------|---------------|
|`x`|`vg_lite_float_t`|X coordinate|
|`y`|`vg_lite_float_t`|Y coordinate|
|`flatten_flag`|`vg_lite_uint8_t`|Flatten flag for flattened path|
|`curve_type`|`vg_lite_uint8_t`|Curve type for the stroke path|
|`tangentX`|`vg_lite_float_t`|X tangent \(Note: \#define centerX tangent\)|
|`tangentY`|`vg_lite_float_t`|Y tangent \(Note: \#define centerX tangent\)|
|`length`|`vg_lite_float_t`|Line length|
|`prev`|`vg_lite_path_point_ptr`|Pointer to the previous point node|

**Parent topic:**[Stroke structures](../topics/stroke_structures.md)

