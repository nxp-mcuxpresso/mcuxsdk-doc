# `vg_lite_close`

**Description:**

This function deallocates all the resources and free up all the memory that was initialized earlier by the `vg_lite_init` function. It will also turn OFF the hardware automatically if this was the only active context.

**Syntax:**

```
vg_lite_error_t vg_lite_close (
    void
);
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

