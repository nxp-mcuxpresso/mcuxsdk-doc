# `vg_lite_flush`

**Description:**

This function explicitly submits the command buffer to the GPU without waiting for it to complete. *\(From Dec 2019, return type is vg\_lite\_error\_t, previously was void.\)*

**Syntax:**

```
vg_lite_error_t vg_lite_flush (
    void
);
```

**Returns:**

Returns `VG_LITE_SUCCESS` if the flush is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enumeration for other return codes.

**Parent topic:**[Context initialization and control functions](../topics/context_initialization_and_control_functions.md)

