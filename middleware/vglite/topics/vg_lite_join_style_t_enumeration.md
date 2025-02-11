# `vg_lite_join_style_t` enumeration

Defines the type of styles available for line joints. *\(from March 2022\)*

Used in structure: `vg_lite_stroke_t.`

Used in function: `vg_lite_set_stroke.`

|**vg\_lite\_join\_style\_t string values**|**Description**|
|------------------------------------------|---------------|
|`VG_LITE_JOIN_MITER`|The *miter* join style appends a trapezoid with one vertex at the intersection point of the two original lines, two adjacent vertices at the outer endpoints of the two “thickened” lines and a fourth vertex at the extrapolated intersection point of the outer perimeters of the two “thickened” lines.|
|`VG_LITE_JOIN_ROUND`|The *round* join style appends a wedge-shaped portion of a circle, centered at the intersection point of the two original lines, having a radius equal to half the line width.|
|`VG_LITE_JOIN_BEVEL`|The *bevel* type join style appends a triangle with two vertices at the outer endpoints of the two "thickened” lines and a third vertex at the intersection point of the two original lines.|

**Parent topic:**[Stroke enumerations](../topics/stroke_enumerations.md)

