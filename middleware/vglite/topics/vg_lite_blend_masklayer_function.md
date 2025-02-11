# `vg_lite_blend_masklayer` function 

**Description:**

This function blends the specified area of the source mask layer with the destination mask layer according to an vg\_lite\_mask\_operation\_t enumeration value, to create a blended destination mask layer. *\(from August-September 2022, requires GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_blend_masklayer (
    vg_lite_buffer_t              *dst_masklayer,
    vg_lite_buffer_t              *src_masklayer,
    vg_lite_mask_operation        operation,
    vg_lite_rectangle_t           *rect,
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*dst_masklayer`|Points to the address of the buffer of the destination mask layer.|
|`*src_masklayer`|Points to the address of the buffer of the source mask layer.|
|`operation`|Blending mode to be applied to each image pixel, as defined by the enum [vg\_lite\_mask\_operation\_t](vg_lite_filter_t_enumeration_001%20-%20Copy%20-%20Copy.md).|
|`*rect`|The rectangle area \(x, y, width, height\) of the blend operation.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

