# `vg_lite_pattern_mode_t` enumeration

Defines how the region outside the image pattern is filled for the path.

Used in function: `vg_lite_draw_gradient`, `vg_lite_draw_pattern`.

|**vg\_lite\_pattern\_mode\_t string values**|Description|
|----------------------------------------------|-------------|
|`VG_LITE_PATTERN_COLOR`|Pixels outside the bounds of the source image should be taken as the color.|
|`VG_LITE_PATTERN_PAD`|Pixels outside the bounds of the source image should be taken as having the same color as the closest edge pixel. The color of the pattern border is expanded to fill the region outside the pattern.|
|`VG_LITE_PATTERN_REPEAT`|Pixels outside the bounds of the source image should be repeated indefinitely in all directions. *\(from March 2023\)*|
|`VG_LITE_PATTERN_REFLECT`|Pixels outside the bounds of the source image should be reflected indefinitely in all directions. *\(from March 2023\)*|

**Parent topic:**[Draw and gradient enumerations](../topics/draw_and_gradient_enumerations.md)

