# `vg_lite_color_key_t` structure

A “color key” have two sections, where each section contains R,G,B channels, which are noted as `high_rgb` and `low_rgb` respectively. *\(from April 2022\)*

When the enable value is true, the color key specified is effective and the alpha value is used to replace the alpha channel of the destination pixel when its RGB channels are in range \[`low_rgb, high_rgb`\]. After the color key is used in the current frame, if the color key is not needed for the next frame, it should be disabled before the next frame.

Used in structure: `vg_lite_color_key4_t`



|**vg\_lite\_color\_key\_t members**|**Type**|**Description**|
|-----------------------------------|--------|---------------|
|`enable`|vg\_lite\_uint8\_t|When set \(true\), this color key is enabled|
|`low_r`|vg\_lite\_uint8\_t|The R channel of `low_rgb`|
|`low_g`|vg\_lite\_uint8\_t|The G channel of `low_rgb`|
|`low_b`|vg\_lite\_uint8\_t|The B channel of `low_rgb`|
|`alpha`|vg\_lite\_uint8\_t|The alpha value to replace the destination pixel alpha channel value with|
|`high_r`|vg\_lite\_uint8\_t|The R channel of `high_rgb`|
|`high g`|vg\_lite\_uint8\_t|The G channel of `high_rgb`|
|`high_b`|vg\_lite\_uint8\_t|The B channel of `high_rgb`|

**Parent topic:**[Blit structures](../topics/blit_structures.md)

