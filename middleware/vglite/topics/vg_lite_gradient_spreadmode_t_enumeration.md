# `vg_lite_gradient_spreadmode_t` enumeration

`vg_lite_gradient_spreadmode_t` enum is defined to match OpenVG enum VGColorRampSpreadMode *\(from March 2023, replaces*vg\_lite\_radial\_gradient\_spreadmode*, requires GC355/GC555 hardware\)*

The application may only define stops with offsets between 0 and 1. Spread modes define how the given set of stops are repeated or extended in order to define interpolated color values for arbitrary input values outside the \[0,1\] range.

Used in structure: `vg_lite_radial_gradient_t.`

|**vg\_lite\_gradient\_spreadmode\_t String Values**|Description|
|-----------------------------------------------------|-------------|
|`VG_LITE_GRADIENT_SPREAD_FILL` |The current fill color is used for all stop values less than 0 or greater than 1 respectively.|
|`VG_LITE_GRADIENT_SPREAD_PAD`|Colors defined at 0 and 1 are used for all stop values less than 0 or greater than 1 respectively.|
|`VG_LITE_GRADIENT_SPREAD_REPEAT` |Color values defined between 0 and 1 are repeated indefinitely in both directions.|
|`VG_LITE_GRADIENT_SPREAD_REFLECT` |Color values defined between 0 and 1 are repeated indefinitely in both directions but with alternate copies of the range reversed.|

**Parent topic:**[Draw and gradient enumerations](../topics/draw_and_gradient_enumerations.md)

