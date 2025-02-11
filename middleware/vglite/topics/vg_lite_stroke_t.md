# `vg_lite_stroke_t` structure 

The structure provides stroke parameters and pointers to temp storage for a stroke sub path. Refer to the function `vg_lite_set_stroke` parameter descriptions for additional description for some members. *\(from March 2022\)*

Used in structure: `vg_lite_path_t.`



|**vg\_lite\_stroke\_t members**|**Type**|**Description**|
|-------------------------------|--------|---------------|
|`cap_style`|`vg_lite_cap_style_t`|Stroke cap style|
|`join_style`|`vg_lite_join_style_t`|Stroke joint style|
|`line_width`|`vg_lite_float_t`|Stroke line width|
|`miter_limit`|`vg_lite_float_t`|Stroke miter limit|
|`*dash_pattern`|`vg_lite_float_t`|Pointer to stroke dash pattern|
|`pattern_count`|`vg_lite_uint32_t`|Number of dash pattern repetitions|
|`dash_phase`|`vg_lite_float_t`|Stroke dash phrase|
|`dash_length`|`vg_lite_float_t`|Stroke dash initial length|
|`dash_index`|`vg_lite_uint32_t`|Stroke dash initial index|
|`half_width`|`vg_lite_float_t`|Half line width|
|`pattern_length`|`vg_lite_float_t`|Total length of stroke dash patterns.|
|`miter_square`|`vg_lite_float_t`|For fast checking|
|`path_points`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`path_end`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`point_count`|`unint32_t`|Temp storage for stroke sub path|
|`left_point`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`right_pont`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`stroke_points`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`stroke_end`|`vg_lite_path_point_ptr`|Temp storage for stroke sub path|
|`stroke_count`|`vg_lite_uint32_t`|Temp storage for stroke sub path|
|`path_list_divide`|`vg_lite_path_list_ptr`|Divide stroke path according to move or move\_rel for avoiding implicit closure. *\(from Aug 2023\)*|
|`cur_list`|`vg_lite_path_list_ptr`|Pointer to current divided path data. *\(from Aug 2023\)*|
|`add_end`|`vg_lite_uint8_t`|Flag that adds end\_path in driver *\(from Aug 2023\)*|
|`dash_reset`|`vg_lite_uint8_t`|*\(from Aug 2023\)*|
|`stroke_paths`|`vg_lite_sub_path_ptr`||
|`last_stroke`|`vg_lite_sub_path_ptr`||
|`swing_handling`|`vg_lite_uint32_t`||
|`swing_deltax`|`vg_lite_float_t`||
|`swing_deltay`|`vg_lite_float_t`||
|`swing_start`|`vg_lite_path_point_ptr`||
|`swing_stroke`|`vg_lite_path_point_ptr`| |
|`swing_length`|`vg_lite_float_t`||
|`swing_centlen`|`vg_lite_float_t`||
|`swing_count`|`vg_lite_uint32_t`||
|`need_swing`|`vg_lite_uint8_t`||
|`swing_ccw`|`vg_lite_uint8_t`||
|`stroke_length`|`vg_lite_float_t`||
|`stroke_size`|`vg_lite_uint32_t`||
|`fattened`|`vg_lite_uint8_t`|The stroke line is a fat line.|
|`closed`|`vg_lite_uint8_t`||

**Parent topic:**[Stroke structures](../topics/stroke_structures.md)

