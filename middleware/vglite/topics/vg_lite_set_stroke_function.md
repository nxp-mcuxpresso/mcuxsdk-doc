# `vg_lite_set_stroke` function

**Description:**

This function uses input parameters to set stroke attributes *\(from March 2022\)*.

**Syntax:**

```
vg_lite_error_t vg_lite_set_stroke (
    vg_lite_path_t              *path,
    vg_lite_cap_style_t         cap_style,
    vg_lite_join_style_t        join_style,
    vg_lite_float_t             line_width,
    vg_lite_float_t             miter_limit,
    vg_lite_float_t             *dash_pattern,
    vg_lite_uint32_t            pattern_count,
    vg_lite_float_t             dash_phase,
    vg_lite_color_t             color
);  

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to the `vg_lite_path_t` structure that describes the path.|
|`cap_style`|The end cap style is defined by the `vg_lite_cap_style_t` enum.|
|`join_style`|The line join style defined by the `vg_lite_join_style_t` enum.|
|`line_width`|The line width of the stroke path. A line width less than or equal to 0 prevents stroking from taking place.|
|`miter_limit`|When stroking using the Miter stroke `vg_lite_join_style_t`, the miter length \(that is, the length between the intersection points of the inner and outer perimeters of the two "fattened" lines\) is compared to the product of the user-set miter limit and the line width. If the miter length exceeds this product, the Miter join is not drawn and a Bevel join is substituted. **Note**: Miter limit values less than 1 are silently clamped to 1.|
|`*dash_pattern`|Pointer to a dash pattern that consists of a sequence of lengths of alternating "on" and "off" dash segments. The first value of the dash array defines the length, in user coordinates, of the first "on" dash segment. The second value defines the length of the following "off" segment. Each subsequent pair of values defines one "on" and one "off" segment. **Note**: If the dash pattern has an odd number of elements, the final element is ignored.|
|`pattern_count`|The count of dash on/off segments.|
|`dash_phase`|Defines the starting point in the dash pattern that is associated with the start of the first segment of the path. For example, if the dash pattern is \[10 20 30 40\] and the dash phase is 35, the path is stroked with an "on" segment of length 25 \(skipping the first "on" segment of length 10, the following "off" segment of length 20, and the first 5 units of the next "on" segment\), followed by an "off" segment of length 40. The pattern is then repeated from the beginning, with an "on" segment of length 10, an "off" segment of length 20, an "on" segment of length 30.|
|`color`|The stroke color.|

**Returns:**

Returns `VG_LITE_SUCCESS` if successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Stroke functions](../topics/stroke_functions.md)

