# vg\_lite\_set\_scissor API interface change

The VGLite API `vg_lite_set_scissor()` function name is not changed in API version 3.0, but the API parameters are defined differently in API version 3.0.

In VGLite API version 3.0, the `vg_lite_set_scissor()` function is defined as:

```
    /* Set and enable a scissor rectangle for render target. */
    vg_lite_error_t vg_lite_set_scissor(vg_lite_int32_t x, vg_lite_int32_t y,
                  vg_lite_int32_t right, vg_lite_int32_t bottom);
```

In VGLite API version 2.0, the `vg_lite_set_scissor()` function is defined as:

```
    vg_lite_error_t vg_lite_set_scissor(int32_t x, int32_t y, int32_t width, int32_t height);
```

So, the `vg_lite_set_scissor()` API parameters "width" and "height" in the VGLite API version 2.0 application must be changed to "right" x-coordinate value and "bottom" y-coordinate value.

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

