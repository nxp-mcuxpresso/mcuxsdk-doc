# `vg_lite_buffer_t` structure

This structure defines the buffer layout for a VGLite image or memory data.

Used in structures: `vg_lite_linear_gradient_t, vg_lite_radial_gradient_t.`

Used in init functions: `vg_lite_allocate, vg_lite_free, vg_lite_upload_buffer, vg_lite_map, vg_lite_unmap.`

Used in blit functions:`vg_lite_blit, vg_lite_blit_rect, vg_lite_clear, vg_lite_create_masklayer, vg_lite_fill_masklayer, vg_lite_blend_masklayer, vg_lite_set_masklayer, vg_lite_render_masklayer, vg_lite_destroy_masklayer`

Used in draw functions: `vg_lite_draw, vg_lite_draw_pattern, vg_lite_draw_grad, vg_lite_draw_radial_grad`



|vg\_lite\_buffer\_t member|Type|Description|
|----------------------------|------|-------------|
|`width`|vg\_lite\_int32\_t|Width of buffer in pixels|
|`height`|vg\_lite\_int32\_t|Height of buffer in pixels|
|`stride`|vg\_lite\_int32\_t|Stride in bytes|
|`tiled`|[vg\_lite\_buffer\_layout\_t](vg_lite_buffer_layout_t_enumeration.md)|Linear or tiled format for buffer enum|
|`format`|[vg\_lite\_buffer\_format\_t](vg_lite_buffer_format_t_enumeration.md)|color format enum|
|`handle`|vg\_lite\_pointer|memory handle|
|`memory`|vg\_lite\_pointer|pointer to the start address of the memory|
|`address`|vg\_lite\_uint32\_t|GPU address|
|`yuv`|[vg\_lite\_yuvinfo\_t](vg_lite_yuvinfo_t_structure.md)|YUV format info struct|
|`image_mode`|[vg\_lite\_image\_mode\_t](vg_lite_yuv2rgb_t_enumeration.md)|Blit image mode enum|
|`transparency_mode`|[vg\_lite\_transparency\_t](vg_lite_yuv2rgb_t_enumeration%20-%20Copy%20-%20Copy%20-%20Copy.md)|Image transparency mode enum|
|`fc_buffer[3]`|vg\_lite\_fc\_buffer\_t|Three \(3\) fast clear buffers, reserved YUV format *\(from March 2023\)*|
|`compress_mode`|vg\_lite\_compress\_mode|Compression mode *\(from March 2023\)*|
|`index_endian`|vg\_lite\_index\_endian\_t|Big/Little Endian setting for index formats *\(from March 2023\)*|
|`paintType`|[vg\_lite\_paint\_type\_t](vg_lite_yuv2rgb_t_enumeration%20-%20Copy%20-%20Copy.md)|Paint type enum *\(from May 2023\)*|
|`fc_enable`|vg\_lite\_int8\_t|Enable Image fast clear *\(moved from Aug 2023\)*|
|`scissor_layer`|vg\_lite\_int8\_t|Get paintcolor from different paint types *\(from Aug 2023\)*|
|`premulitplied`|vg\_lite\_int8\_t|The RGB pixel values are alpha-premultipled *\(from Aug 2023\)*|

**Parent topic:**[Pixel buffer structures](../topics/pixel_buffer_structures.md)

