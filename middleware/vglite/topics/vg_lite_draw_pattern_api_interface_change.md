# vg\_lite\_draw\_pattern API interface change

The VGLite API `vg_lite_draw_pattern()` function name is not changed in API version 3.0, but the API parameters are defined differently in API version 3.0.

In VGLite API version 3.0, the `vg_lite_draw_pattern()` function is defined as:

```
    /* Draw a path that is filled by a transformed image pattern. */
    vg_lite_error_t vg_lite_draw_pattern(vg_lite_buffer_t *target,
                                    vg_lite_path_t *path,
                                    vg_lite_fill_t fill_rule,
                                    vg_lite_matrix_t *path_matrix,
                                    vg_lite_buffer_t *pattern_image,
                                    vg_lite_matrix_t *pattern_matrix,
                                    vg_lite_blend_t blend,
                                    vg_lite_pattern_mode_t pattern_mode,
                                    vg_lite_color_t  pattern_color,
                                    vg_lite_color_t  color,
                                    vg_lite_filter_t filter);

```

Compared to the VGLite API version 2.0 `vg_lite_draw_pattern()` function, “color” is a new additional parameter. It specifies a 32bpp ARGB color \(`vg_lite_color_t`\) to be applied as a mix color. If nonzero, the mix color value gets multiplied with each source pixel before blending happens. If a mix color is not needed, set the color parameter to 0.

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

