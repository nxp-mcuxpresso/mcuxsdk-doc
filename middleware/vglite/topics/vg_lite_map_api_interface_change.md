# vg\_lite\_map API interface change

The VGLite API `vg_lite_map()` function name is not changed in API version 3.0, but the API parameters are defined differently in API version 3.0.

In VGLite API version 3.0, the `vg_lite_map()` function is defined as:

```
    /* Map a buffer into hardware accessible address space. */
    vg_lite_error_t vg_lite_map(vg_lite_buffer_t *buffer, vg_lite_map_flag_t flag, int32_t fd);

```

In VGLite API version 2.0, the `vg_lite_map()` function is defined as:

```
    vg_lite_error_t vg_lite_map(vg_lite_buffer_t *buffer);
```

So, `vg_lite_map()` in VGLite API version 3.0 API requires two extra parameters "flag" and "fd", which can simply be set as `vg_lite_map` \(buffer, 0, 0\) in applications.

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

