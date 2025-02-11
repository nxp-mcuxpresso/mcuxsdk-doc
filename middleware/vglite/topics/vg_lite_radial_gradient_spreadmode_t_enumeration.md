# `vg_lite_radial_gradient_spreadmode_t` enumeration 

*\(Deprecated March 2023\)* use `vg_lite_gradient_spreadmode_t.` Defines the radial gradient padding mode. *\(from Nov 2020, requires GC355 hardware\)*

Used in structure: `vg_lite_radial_gradient_t.`

|vg\_lite\_radial\_gradient\_spreadmode\_t String Values|Description|
|---------------------------------------------------------|-------------|
|`VG_LITE_RADIAL_GRADIENT_SPREAD_FILL = 0`|The current fill color is used for all stop values less than 0 or greater than 1 respectively.|
|`VG_LITE_RADIAL_GRADIENT_SPREAD_PAD`|Colors defined at 0 and 1 are used for all stop values less than 0 or greater than 1 respectively.|
|`VG_LITE_RADIAL_GRADIENT_SPREAD_REPEAT`|Color values defined between 0 and 1 are repeated indefinitely in both directions.|
|`VG_LITE_RADIAL_GRADIENT_SPREAD_REFLECT`|Color values defined between 0 and 1 are repeated indefinitely in both directions but with alternate copies of the range reversed.|

**Parent topic:**[Draw and gradient enumerations](../topics/draw_and_gradient_enumerations.md)

