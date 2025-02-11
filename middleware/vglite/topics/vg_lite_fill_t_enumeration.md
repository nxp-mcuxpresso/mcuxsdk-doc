# `vg_lite_fill_t` enumeration

This enumeration is used to specify the fill rule to use. For drawing any path, the hardware supports both non-zero and odd-even fill rules.

To determine whether any point is contained inside an object, imagine drawing a line from that point out to infinity in any direction such that the line does not cross any vertex of the path. For each edge that is crossed by the line, add 1 to the counter if the edge is crossed from left to right, as seen by an observer walking across the line towards infinity, and subtract 1 if the edge crossed from right to left. In this way, each region of the plane will receive an integer value.

The non-zero fill rule says that a point is inside the shape if the resulting sum is not equal to zero. The even/odd rule says that a point is inside the shape if the resulting sum is odd, regardless of sign.

Used in function: `vg_lite_render_masklayer.`

Used in draw functions: `vg_lite_draw, vg_lite_draw_grad, vg_lite_draw_radial_grad, vg_lite_draw_pattern.`

|**vg\_lite\_fill\_t string values**|Description|
|-------------------------------------|-------------|
|VG\_LITE\_FILL\_NON\_ZERO|Non-zero fill rule. A pixel is drawn if it crosses at least one path pixel.|
|VG\_LITE\_FILL\_EVEN\_ODD|Even-odd fill rule. A pixel is drawn if it crosses an odd number of path pixels.|

**Parent topic:**[Draw and gradient enumerations](../topics/draw_and_gradient_enumerations.md)

