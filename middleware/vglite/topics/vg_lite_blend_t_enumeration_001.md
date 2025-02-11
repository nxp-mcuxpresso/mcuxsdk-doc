# `vg_lite_blend_t` enumeration

This enumeration defines the blending modes supported by some VGLite API functions. S and D represent source and destination non-premultiplied RGB color channels. Sa and Da represent the source and destination alpha channels. SP and DP represent source and destination alpha-premultiplied RGB color channels \(SP = S\*Sa, DP = D\*Da\).

**Note:** `VG_LITE_BLEND_*_LVGL` modes are supported on all VG cores. On VG cores that do not support `gcFEATURE_BIT_VG_LVGL_SUPPORT`, the LVGL blend modes are supported by a combination of software and hardware operations. `OPENVG_BLEND_*` modes can only be supported on GC355 and GC555 cores.

Used in blit functions: `vg_lite_blit, vg_lite_blit2, vg_lite_blit_rect.`

Used in draw functions: `vg_lite_draw, vg_lite_draw_grad, vg_lite_draw_radial_grad, vg_lite_draw_pattern`.

|**vg\_lite\_blend\_t String Values**|Description|
|------------------------------------|-----------|
|VG\_LITE\_BLEND\_NONE| **S, no blending** Non-premultiplied|
|VG\_LITE\_BLEND\_SRC\_OVER|**S + D \* \(1 - Sa\)** Non-premultiplied|
|VG\_LITE\_BLEND\_DST\_OVER|**S \* \(1 – Da\) + D** Non-premultiplied|
|VG\_LITE\_BLEND\_SRC\_IN|**S \* Da** Non-premultiplied|
|VG\_LITE\_BLEND\_DST\_IN|**D \* Sa** Non-premultiplied|
|VG\_LITE\_BLEND\_MULTIPLY|**S \* \(1 - Da\) + D \* \(1 - Sa\) + S \* D** Non-premultiplied|
|VG\_LITE\_BLEND\_SCREEN|**S + D - S \* D** Non-premultiplied|
|VG\_LITE\_BLEND\_DARKEN|**min\(SRC\_OVER, DST\_OVER\)** Non-premultiplied|
|VG\_LITE\_BLEND\_LIGHTEN|**max\(SRC\_OVER, DST\_OVER\)** Non-premultiplied|
|VG\_LITE\_BLEND\_ADDITIVE|**S + D** Non-premultiplied|
|VG\_LITE\_BLEND\_SUBTRACT|**D \* \(1 - Sa\)** Non-premultiplied|
|VG\_LITE\_BLEND\_NORMAL\_LVGL|**S \* Sa + D \* \(1 - Sa\)** Non-premultiplied \(from March 2023\)|
|VG\_LITE\_BLEND\_ADDITIVE\_LVGL|**\(S + D\) \* Sa + D \* \(1 - Sa\)** Non-premultiplied \(from March 2023\)|
|VG\_LITE\_BLEND\_SUBTRACT\_LVGL|**\(S - D\) \* Sa + D \* \(1 - Sa\)** Non-premultiplied \(from March 2023\)|
|VG\_LITE\_BLEND\_MULTIPLY\_LVGL|**\(S \* D\) \* Sa + D \* \(1 - Sa\)** Non-premultiplied \(from March 2023\)|
|**OpenVG Porter-Duff Blend String Values**|*\(from Aug 2023\)*|
|OPENVG\_BLEND\_NONE|**SP, no blending** Premultiplied|
|OPENVG\_BLEND\_SRC\_OVER|**\(SP + DP \* \(1 - Sa\)\) / \(Sa + Da \* \(1 - Sa\)\)** Premultiplied|
|OPENVG\_BLEND\_DST\_OVER|**\(SP \* \(1 - Da\) + DP\) / \(Sa \* \(1 - Da\) + Da\)** Premultiplied|
|OPENVG\_BLEND\_SRC\_IN|**\(SP \* Da\) / \(Sa \* Da\)** Premultiplied|
|OPENVG\_BLEND\_DST\_IN|**\(DP \* Sa\) / \(Sa \* Da\)** Premultiplied|
|OPENVG\_BLEND\_MULTIPLY|**\(SP\*DP + SP\*\(1 - Da\) + DP\*\(1 - Sa\)\) / \(Sa + Da\*\(1 - Sa\)\)** Premultiplied|
|OPENVG\_BLEND\_SCREEN|**\(SP + DP - \(SP\*DP\)\) / \(Sa + Da\*\(1 - Sa\)\)** Premultiplied|
|OPENVG\_BLEND\_DARKEN|**min\(SRC\_OVER, DST\_OVER\)** Premultiplied|
|OPENVG\_BLEND\_LIGHTEN|**max\(SRC\_OVER, DST\_OVER\)** Premultiplied|
|OPENVG\_BLEND\_ADDITIVE|**\(SP + DP\) / \(Sa + Da\)** Premultiplied|



**Parent topic:**[Blit enumerations](../topics/blit_enumerations.md)

