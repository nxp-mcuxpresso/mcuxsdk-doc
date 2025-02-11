# `vg_lite_create_masklayer` function 

**Description:**

This function creates a mask layer with the specified width and height. The mask format defaults to A8 and the default mask value is 255. *\(from August 2022-September, requires GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_create_masklayer (
    vg_lite_buffer_t              *masklayer,
    vg_lite_uint32_t              width,
    vg_lite_uint32_t              height
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*masklayer`|Points to the address of the buffer of the mask layer to be created.|
|`width`|Mask layer width \(in pixels\).|
|`height`|Mask layer height \(in pixels\).|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

