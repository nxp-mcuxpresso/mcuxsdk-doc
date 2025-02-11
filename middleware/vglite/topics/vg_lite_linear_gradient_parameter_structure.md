# `vg_lite_linear_gradient_parameter` structure 

This structure defines a radial direction for a linear gradient. *\(from April 2022\)*

Line0 connects point \(X0, Y0\) to point \(X1, Y1\) and represents the radial direction of the linear gradient.

Line1 is a line perpendicular to line0 which passes through point \(X0, Y0\).

Line2 is a line perpendicular to line0 which passes through point \(X1, Y1\)

The linear gradient paint is applied at the intersection of the path fill area and the plane starting from line 1 and ending at line 2.

Used in structure: `vg_lite_ext_linear_gradient.`

Used in functions: `vg_lite_set_linear_grad.`

|**vg\_lite\_linear\_gradient\_parameter\_t members**|**Type**|**Description**|
|----------------------------------------------------|--------|---------------|
|X0|`vg_lite_float_t`|X origin of linear gradient radial direction.|
|Y0|`vg_lite_float_t`|Y origin of linear gradient radial direction.|
|X1|`vg_lite_float_t`|X end point of linear gradient radial direction.|
|Y1|`vg_lite_float_t`|Y end point of linear gradient radial direction.|

**Parent topic:**[Draw and gradient structures](../topics/draw_and_gradient_structures.md)

