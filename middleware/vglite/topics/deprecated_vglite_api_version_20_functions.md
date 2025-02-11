# Deprecated VGLite API version 2.0 functions

The VGLite API `vg_lite_perspective(), vg_lite_enable_premultiply(), vg_lite_disable_premultiply()` functions are removed from API version 3.0. These API functions must be deleted from a VGLite API version 2.0 application to work with the VGLite API version 3.0 driver.

In VGLite API version 3.0, the color premultiply setting is defined by the `vg_lite_blend_t` enumeration to replace the original `vg_lite_enable_premultiply()` and `vg_lite_disable_premultiply()` APIs.

-   VG\_LITE\_BLEND\_\* enumeration values in `vg_lite_blend_t` define non-premultiplied blending modes.
-   OPEVG\_BLEND\_\* enumeration values in `vg_lite_blend_t` define premultiplied Porter-Duff blending modes.

So, the VGLite API version 3.0 application can set different blending modes to get the desired premultiplied/non-premultiplied blending result.

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

