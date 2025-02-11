# `vg_lite_fc_buffer_t` structure 

This structure defines the organization of a fast clear buffer. *\(from March 2023\)*

Used in structure: `vg_lite_buffer_t.`



|vg\_lite\_fc\_buffer\_t members|Type|Description|
|-------------------------------|----|-----------|
|width|vg\_lite\_int32\_t|Width of buffer in pixels|
|height|vg\_lite\_int32\_t|Height of buffer in pixels|
|stride|vg\_lite\_int32\_t|Stride in bytes|
|handle|vg\_lite\_pointer|memory handle as allocated by the VGLite kernel|
|memory|vg\_lite\_pointer|logical pointer to the start address of the memory for the CPU|
|address|vg\_lite\_uint32\_t|address to the buffer's memory for the GPU hardware|
|color|vg\_lite\_uint32\_t|The fast clear color value|



**Parent topic:**[Pixel buffer structures](../topics/pixel_buffer_structures.md)

