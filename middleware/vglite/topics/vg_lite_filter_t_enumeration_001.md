# `vg_lite_filter_t` enumeration

Specifies the sample-filtering mode in VGLite blit and draw APIs.

Used in blit functions: `vg_lite_blit`, `vg_lite_blit_rect`.

Used in draw functions: `vg_lite_draw_radial_gradient`, `vg_lite_draw_pattern`.

|vg\_lite\_filter\_t string values|Description|
|---------------------------------|-------------|
|`VG_LITE_FILTER_POINT` |Fetch only the nearest image pixel|
|`VG_LITE_FILTER_LINEAR`|Use linear interpolation along a horizontal line|
|`VG_LITE_FILTER_BI_LINEAR`|Use a 2x2 box around the image pixel and perform an interpolation|
|`VG_LITE_FILTER_GAUSSIAN`|Perform 3x3 gaussian blur with the convolution for image pixel. *\(from March 2023\)*|

**Parent topic:**[Blit enumerations](../topics/blit_enumerations.md)

