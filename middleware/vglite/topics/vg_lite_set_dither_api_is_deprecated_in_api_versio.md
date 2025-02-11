# vg\_lite\_set\_dither API is deprecated in API version 3.0

The original API version 2.0 function `vg_lite_set_dither(int enable)` API is removed from API version 3.0, it is replaced with two new APIs for dither enable/disable:

```

    /* Enable dither function. Dither is OFF by default. */
    vg_lite_error_t vg_lite_enable_dither();
    /* Disable dither function. Dither is OFF by default. */
    vg_lite_error_t vg_lite_disable_dither();
```

Therefore, the `vg_lite_set_dither(enable)` function in the VGLite API version 2.0 application must be replaced with `vg_lite_enable_dither()` or `vg_lite_disable_dither()` to work with the VGLite API version 3.0 driver.

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

