# `vg_lite_feature_t` enumeration

The following feature values may be queried for availability in compatible hardware. *\(expanded March 2023 to support additional hardware for driver V4\)*

Used in information function: `vg_lite_query_feature`.

|`vg_lite_feature_t` string values |Description |
|-----------------------------------|-------------|
|gcFEATURE\_BIT\_VG\_16PIXELS\_ALIGN|Require 16 pixels aligned for the input pixel buffer|
|gcFEATURE\_BIT\_VG\_24BIT|RGB888 or RGBA5658 formats support|
|gcFEATURE\_BIT\_VG\_24BIT\_PLANAR|24-bit planar format support|
|gcFEATURE\_BIT\_VG\_AYUV\_INPUT|AYUV input format support|
|gcFEATURE\_BIT\_VG\_BORDER\_CULLING|Border culling support|
|gcFEATURE\_BIT\_VG\_COLOR\_KEY|Color key support.|
|gcFEATURE\_BIT\_VG\_COLOR\_TRANSFORMATION|Color transform support.|
|gcFEATURE\_BIT\_VG\_DEC\_COMPRESS|DEC compression format output support|
|gcFEATURE\_BIT\_VG\_DITHER|Dither support|
|gcFEATURE\_BIT\_VG\_DOUBLE\_IMAGE|Support two image source inputs|
|gcFEATURE\_BIT\_VG\_FLEXA|FLEXA interface support|
|gcFEATURE\_BIT\_VG\_GAMMA|Gamma support|
|gcFEATURE\_BIT\_VG\_GAUSSIAN\_BLUR|Gaussian blur sampling support|
|gcFEATURE\_BIT\_VG\_GLOBAL\_ALPHA|Global alpha support|
|gcFEATURE\_BIT\_VG\_HW\_PREMULTIPLY|HW supports alpha premultiply for image|
|gcFEATURE\_BIT\_VG\_IM\_DEC\_INPUT|DEC compressed format input support|
|gcFEATURE\_BIT\_VG\_IM\_FASTCLEAR|Fast Clear support|
|gcFEATURE\_BIT\_VG\_IM\_INDEX\_FORMAT|Index format support for image|
|gcFEATURE\_BIT\_VG\_IM\_INPUT|Blit and draw API support|
|gcFEATURE\_BIT\_VG\_IM\_REPEAT\_REFLECT|Image repeat reflect mode support|
|gcFEATURE\_BIT\_VG\_INDEX\_ENDIAN|Index format endian support|
|gcFEATURE\_BIT\_VG\_LINEAR\_GRADIENT\_EXT|Support for extended linear gradient capabilities|
|gcFEATURE\_BIT\_VG\_LVGL\_SUPPORT|LVGL blend mode support|
|gcFEATURE\_BIT\_VG\_MASK|Mask support|
|gcFEATURE\_BIT\_VG\_MIRROR|Mirror support|
|gcFEATURE\_BIT\_VG\_NEW\_BLEND\_MODE|New blend mode DARKEN/LIGHTEN support|
|gcFEATURE\_BIT\_VG\_NEW\_IMAGE\_INDEX|New CLUT image index support|
|gcFEATURE\_BIT\_VG\_PARALLEL\_PATHS|New parallel path HW support|
|gcFEATURE\_BIT\_VG\_PE\_CLEAR|Pixel engine clear support|
|gcFEATURE\_BIT\_VG\_PIXEL\_MATRIX|Pixel matrix support|
|gcFEATURE\_BIT\_VG\_QUALITY\_8X|8x anti-aliasing path support|
|gcFEATURE\_BIT\_VG\_RADIAL\_GRADIENT|Radial gradient support|
|gcFEATURE\_BIT\_VG\_RECTANGLE\_TILED\_OUT|Rectangle tiled output support|
|gcFEATURE\_BIT\_VG\_RGBA2\_FORMAT|RGBA2222 format support|
|gcFEATURE\_BIT\_VG\_RGBA8\_ETC2\_EAC|ETC2/EAC compressed image format support|
|gcFEATURE\_BIT\_VG\_SCISSOR|Scissor support|
|gcFEATURE\_BIT\_VG\_SRC\_PREMULTIPLIED|Source image alpha premultiplied|
|gcFEATURE\_BIT\_VG\_STENCIL|Stencil image mode support|
|gcFEATURE\_BIT\_VG\_STRIPE\_MODE|Stripe mode support|
|gcFEATURE\_BIT\_VG\_TESSELLATION\_TILED\_OUT|Tessellation tiled output support|
|gcFEATURE\_BIT\_VG\_USE\_DST|Read destination pixel support|
|gcFEATURE\_BIT\_VG\_YUV\_INPUT|YUV input format support|
|gcFEATURE\_BIT\_VG\_YUV\_OUTPUT|YUV format output support|
|gcFEATURE\_BIT\_VG\_YUV\_TILED\_INPUT|YUV tiled input format support|
|gcFEATURE\_BIT\_VG\_YUY2\_INPUT|YUY2 input format support|

**Parent topic:**[Enumerations for product and feature queries](../topics/enumerations_for_product_and_feature_queries.md)

