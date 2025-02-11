# `vg_lite_set_masklayer` function 

**Description:**

This function sets the given mask layer to the hardware. *\(from August-September 2022, requires GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_set_masklayer (
    vg_lite_buffer_t             *masklayer
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*masklayer`|Points to the address of the buffer of the mask layer to be set.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

