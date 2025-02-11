# `vg_lite_destroy_masklayer` function 

**Description:**

This function is used to free a mask layer. *\(from August-September 2022, requires GC555 hardware\)*

**Syntax:**

```
vg_lite_error_t vg_lite_destroy_masklayer (
    vg_lite_buffer_t              masklayer
);

```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*masklayer`|Points to the address of the buffer of the mask layer to be destroyed.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Blit/Draw extended functions](../topics/premultiply_and_scissor_functions.md)

