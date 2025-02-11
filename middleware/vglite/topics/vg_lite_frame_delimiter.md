# `vg_lite_frame_delimiter` 

**Description:**

This function sets a flag for GPU to signal the completion of current frame. A `vg_lite_finish` is called by default within this API. The enum `VG_LITE_FRAME_END_FLAG` is the only value that can be set by flag parameter.

**Syntax:**

```
vg_lite_error_t vg_lite_frame_delimiter (
    vg_lite_frame_flag_t flag
);
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

