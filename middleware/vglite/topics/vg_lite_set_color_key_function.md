# `vg_lite_set_color_key` function

**Description:**

This function sets a color key. Color key can be used for blit or for draw pattern operations. *\(from April 2022\)*

A “color key” have two sections, where each section contains R,G,B channels which are noted as `high_rgb` and `low_rgb` respectively.

When the `vg_lite_color_key_t` structure value enable is true, the color key specified is effective and the alpha value is used to replace the alpha channel of the destination pixel when its RGB channels are within range \[low\_rgb, high\_rgb\]. After the color key is used in the current frame, if the color key is not needed for the next frame, it should be disabled before the next frame.



Hardware support for color key is not available for GCNanoLiteV. Application can use VGLite API `vg_lite_query_feature(gcFEATURE_BIT_VG_COLOR_KEY)` to determine HW support for color key.

**Syntax:**

```
vg_lite_error_t vg_lite_set_color_key (
    vg_lite_color_key4_t          colorkey
);
```

**Parameters:**



|Parameter|Description|
|---------|-----------|
|`colorkey`|Color keying parameters as defined by [vg\_lite\_color\_key4\_t.](vg_lite_color_key4_t_structure.md)

 Here are 4 groups of color key states:

 -   color\_key\_0, high\_rgb\_0, low\_rgb\_0, alpha\_0, enable\_0
-   color\_key\_1, high\_rgb\_1, low\_rgb\_1, alpha\_1, enable\_1
-   color\_key\_2, high\_rgb\_2, low\_rgb\_2, alpha\_2, enable\_2
-   color\_key\_3, high\_rgb\_3, low\_rgb\_3, alpha\_3, enable\_3

 The priority order of these states is:

 color\_key\_0 \> color\_key\_1 \> color\_key\_2 \> color\_key\_3.



**Returns:**

`VG_LITE_SUCCESS` if successful. `VG_LITE_NOT_SUPPORT` if color key is not supported in hardware.

**Parent topic:**[Blit functions](../topics/blit_functions.md)

