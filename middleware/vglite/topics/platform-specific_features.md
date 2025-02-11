# Platform-specific features

The table below describes VGLite features that are supported by some but not all NXP VGLite-compatible i.MX RT platforms. The features that are not mentioned here are supported by all NXP VGLite-compatible i.MX RT platforms.



|VGLite feature|Supported? \(Yes/No\)|
|i.MX RT500|i.MX RT1160|i.MX RT1170|
|--------------|:-------------------:|
|----------|:---------:|:---------:|
|2 bits per channel image formats \(ARGB2222, BGRA2222, ABGR2222, RGBA2222\)|Yes|No|No|
|Indexed image formats \(1, 2, 4, and 8 bits per pixel\)|Yes|No|No|
|8x coverage sample anti-aliasing for vector paths \(`VG_LITE_UPPER`\)|Yes|No|No|
|Border culling|Yes|No|No|
|Alpha channel premultiplication during `vg_lite_blit`|No|Yes|Yes|
|Dithering|No|Yes|Yes|
|Color Keying|No|Yes|Yes|
|Radial gradients|No|Yes|Yes|
|Linear gradients extensions|No|Yes|Yes|

