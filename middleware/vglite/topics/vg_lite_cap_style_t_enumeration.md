# `vg_lite_cap_style_t` enumeration

Defines the style of cap at the end of a stroke *\(from March 2022\)*.

Used in structure: `vg_lite_stroke_t.`

Used in function: `vg_lite_set_stroke.`

|**vg\_lite\_cap\_style\_t values**|**Description**|
|----------------------------------|---------------|
|`VG_LITE_CAP_BUTT`|The *butt* end cap style terminates each segment with a line perpendicular to the tangent at each endpoint.|
|`VG_LITE_CAP_ROUND`|The *round* end cap style appends a semicircle with a diameter equal to the line width centered around each endpoint.|
|`VG_LITE_CAP_SQUARE`|The *square* end cap style appends a rectangle with two sides of length equal to the line width perpendicular to the tangent, and two sides of length equal to half the line width parallel to the tangent, at each endpoint.|

**Parent topic:**[Stroke enumerations](../topics/stroke_enumerations.md)

