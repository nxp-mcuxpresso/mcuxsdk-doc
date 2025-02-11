# `vg_lite_mask_operation_t` enumeration 

Specifies the mask operation mode in VGLite blit APIs.

Used in functions: `vg_lite_blend_masklayer, vg_lite_render_masklayer.`

|vg\_lite\_mask\_operation\_t string values|Description|
|------------------------------------------|-------------|
|`VG_LITE_CLEAR_MASK`|This operation sets all mask values in the region of interest to 0, ignoring the new mask layer.|
|`VG_LITE_FILL_MASK`|This operation sets all mask values in the region of interest to 1, ignoring the new mask layer.|
|`VG_LITE_SET_MASK`|This operation copies values in the region of interest from the new mask layer, overwriting the previous mask values.|
|`VG_LITE_UNION_MASK`|This operation replaces the previous mask in the region of interest by its union with the new mask layer. The resulting values are always greater than or equal to their previous value.|
|`VG_LITE_INTERSECT_MASK`|This operation replaces the previous mask in the region of interest by its intersection with the new mask layer. The resulting mask values are always less than or equal to their previous value.|
|`VG_LITE_SUBTRACT_MASK`|This operation subtracts the new mask from the previous mask and replaces the previous mask in the region of interest by the resulting mask. The resulting values are always less than or equal to their previous value.|

**Parent topic:**[Blit enumerations](../topics/blit_enumerations.md)

