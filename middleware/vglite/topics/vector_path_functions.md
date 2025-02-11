# Vector path functions

When using a small tessellation window and depending on a path’s size, a path might be uploaded to the hardware multiple times because the hardware scanline convert path with the provided tessellation window size, so VGLite path rendering performance might go down. That is why it is preferable to set the tessellation buffer size to the most common path size, for example if you only render 24-pt fonts, you can set the tessellation buffer to be 24x24.



All the RGBA color formats available in the [vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md) are supported as the destination buffer for the draw function.


```{include} ../topics/vg_lite_path_calc_length_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_path_append_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_init_path_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_init_arc_path_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_upload_path_function.md
:heading-offset: 2
```

```{include} ../topics/vg_lite_clear_path_function.md
:heading-offset: 2
```

**Parent topic:**[Vector path control](../topics/vector_path_control.md)

