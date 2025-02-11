# `vg_lite_init`

**Description:**

This function initializes the memory and data structures needed for VGLite draw/blit functions, by allocating memory for the command buffer and a tessellation buffer of the specified size.

GC555 has a newly designed hardware tessellation module that requires less memory for the tessellation buffer than GC355 and GNanoLite-V. Specifically, the GC555 required tessellation buffer size is "buffer\_height \* 128 byte". `vg_lite_init` API can simply be called with the render buffer “width” and “height” as the input parameters for GC555. This results in the best path to tessellation performance.

GC355 and GCNanoLiteV hardware tessellation module requires a tessellation buffer with size "buffer\_height \* buffer\_width \* 8 byte". If system memory is limited, the application can define a smaller tessellation window based on the amount of memory available. GPU hardware can process the entire render buffer path tessellation in multiple passes with the tessellation window sliding across the render buffer. The multi-pass path tessellation with the smaller tessellation window has a certain performance overhead.

The minimum tessellation window that can be used is 16x16. If tess\_height or tess\_width is less than 0 in `vg_lite_init` API, then no path tessellation buffer is created and path drawing APIs do not work, only blit APIs can be used after `vg_lite_init`.

If this would be the first context that accesses the hardware, the hardware is turned on and initialized. If a new context must be initialized, `vg_lite_close` must be called to close the current context. Otherwise, `vg_lite_init` will return an error.

**Syntax:**

```
vg_lite_error_t vg_lite_init (
    vg_lite_int32_t             tess_width,
    vg_lite_int32_t             tess_height

);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`tess_width`|Width of tessellation window. Maximum cannot be greater than render buffer width. If less than or equal to 0, then no tessellation buffer is created, in which case only blit APIs can be used afterward.|
|`tess_height`|Height of tessellation window. Maximum cannot be greater than render buffer height. If less than or equal to 0, then no tessellation buffer is created, in which case blit APIs can be used afterward.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.



**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

