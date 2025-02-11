# `vg_lite_color_ramp_t` structure

This structure defines the stops for the radial gradient. The five parameters provide the offset and color for the stop. Each stop is defined by a set of floating point values which specify the offset and the sRGBA color and alpha values. Color channel values are in the form of a non-premultiplied \(R, G, B, alpha\) quad. All parameters are in the range of \[0,1\]. The red, green, blue, alpha value of \[0, 1\] is mapped to an 8-bit pixel value \[0, 255\].*\(from November 2020, requires GC355 hardware\)*

The define for the max number of radial gradient stops is `#define MAX_COLOR_RAMP_STOPS`256.

Used in radial gradient structure: `vg_lite_radial_gradient_t.`

|vg\_lite\_color\_ramp\_t members|Type|Description|
|----------------------------------|------|-------------|
|`stop`|`vg_lite_float_t`|Offset value for the color stop|
|`red`|`vg_lite_float_t`|Red color channel value for the color stop|
|`green`|`vg_lite_float_t`|Green color channel value for the color stop|
|`blue`|`vg_lite_float_t`|Blue color channel value for the color stop|
|`alpha`|`vg_lite_float_t`|Alpha color channel value for the color stop|

**Parent topic:**[Draw and gradient structures](../topics/draw_and_gradient_structures.md)

