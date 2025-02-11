# Destination buffer alignment requirement 

The destination \(or render target\) buffer alignment requirement depends on the specific pixel format, and some `gcFEATURE_*_ALIGNED` defines in the `vg_lite_options.h` file.

|Target format|Bits per pixel|Target tile mode|VG tile mode|Start address alignment requirement in bytes|Stride alignment requirement in bytes|Buffer height alignment requirement|
|-------------|--------------|----------------|------------|--------------------------------------------|-------------------------------------|-----------------------------------|
|VG\_LITE\_A8|8|linear|linear|4B|1B|1|
|VG\_LITE\_A8|8|linear|tile|64B|64B|4|
|VG\_LITE\_A8|8|tile|linear|64B|64B|4|
|VG\_LITE\_A8|8|tile |tile|64B|16B|4|
|VG\_LITE\_L8|8|linear|linear|4B|1B|1|
|VG\_LITE\_L8|8|linear|tile|64B|64B|4|
|VG\_LITE\_L8|8|tile|linear|64B|64B|4|
|VG\_LITE\_L8|8|tile|tile|64B|16B|4|
|VG\_LITE\_ARGB2222|8|linear|linear|4B|1B|1|
|VG\_LITE\_ARGB2222|8|linear|tile|64B|64B|4|
|VG\_LITE\_ARGB2222|8|tile|linear|64B|64B|4|
|VG\_LITE\_ARGB2222|8|tile|tile|64B|16B|4|
|VG\_LITE\_RGB565|16|linear|linear|4B|2B|1|
|VG\_LITE\_RGB565|16|linear|tile|64B|64B|4|
|VG\_LITE\_RGB565|16|tile|linear|64B|64B|4|
|VG\_LITE\_RGB565|16|tile|tile|64B|16B|4|
|VG\_LITE\_ARGB1555|16|linear|linear|4B|2B|1|
|VG\_LITE\_ARGB1555|16|linear|tile|64B|64B|4|
|VG\_LITE\_ARGB1555|16|tile|linear|64B|64B|4|
|VG\_LITE\_ARGB1555|16|tile|tile|64B|16B|4|
|VG\_LITE\_ARGB4444|16|linear|linear|4B|2B|1|
|VG\_LITE\_ARGB4444|16|linear|tile|64B|64B|4|
|VG\_LITE\_ARGB4444|16|tile|linear|64B|64B|4|
|VG\_LITE\_ARGB4444|16|tile|tile|64B|16B|4|
|VG\_LITE\_ARGB8888|32|linear|linear|4B|4B|1|
|VG\_LITE\_ARGB8888|32|linear|tile|64B|64B|4|
|VG\_LITE\_ARGB8888|32|tile|linear|64B|64B|4|
|VG\_LITE\_ARGB8888|32|tile|tile|64B|16B|4|
|VG\_LITE\_XRGB8888|32|linear|linear|4B|4B|1|
|VG\_LITE\_XRGB8888|32|linear|tile|64B|64B|4|
|VG\_LITE\_XRGB8888|32|tile|linear|64B|64B|4|
|VG\_LITE\_XRGB8888|32|tile|tile|64B|16B|4|
|VG\_LITE\_ARGB8565|24|linear|linear|64B|3B\*|1|
|VG\_LITE\_ARGB8565|24|linear|tile|64B|48B\*|4|
|VG\_LITE\_ARGB8565|24|tile|linear|64B|48B\*|4|
|VG\_LITE\_ARGB8565|24|tile|tile|64B|12B\*|4|
|VG\_LITE\_RGB888|24|linear|linear|64B|3B\*|1|
|VG\_LITE\_RGB888|24|linear|tile|64B|48B\*|4|
|VG\_LITE\_RGB888|24|tile|linear|64B|48B\*|4|
|VG\_LITE\_RGB888|24|tile|tile|64B|12B\*|4|





**Note:**

1.  The values in the table reflect the alignment requirements of pixel data in memory. The stride of ARGB8888/ARGB8565 is seen as 4 Bytes per pixel when configuring the hardware.
2.  For tile mode, the buffer stride is still the byte size of a row of pixels instead of 4 rows of pixels.
3.  For PE clear function, the clear size must align to 48 Bytes for the RGB888 or ARGB8565 format.
4.  For PE clear function with DECNano enabled, the clear size must align to 48 Bytes for RGB888, align to 64 Bytes for ARGB8888 or XRGB8888.
5.  If the DECNano function is enabled for the buffer, the target buffer start address needs to align to 64 Bytes.
6.  If the DECNano function is enabled for the buffer, the total buffer size needs to align to a 64-byte compression rate for ARGB8888 or XRGB8888 format and align to a 48 Byte\*compression rate for RGB888 format.

**Additional Alignment Requirement**

1.  Buffer starting address must be at least 4-byte aligned. Buffer stride must be at least one pixel size aligned.
2.  Buffer starting address must be 64-byte aligned for 24 bit-per-pixel format, or tile mode, or DECNano enabled.
3.  Buffer height must be 4-pixel aligned for tile mode buffer.
4.  For tile mode buffer, the buffer stride must be 16-byte aligned for non-24bit-per-pixel formats. So, 8 bits-per-pixel format buffer width must be 16-pixel aligned; 16 bits-per-pixel format buffer width must be 8-pixel aligned; 32 bit-per-pixel format buffer width must be 4 pixel aligned.
5.  For tile mode buffer, the buffer stride must be 12-byte aligned for 24 bits-per-pixel formats, that is, the buffer width must be 4-pixel aligned.
6.  For PE clear function, the clear size must align to 48 Bytes for 24-bits-per-pixel formats.
7.  For PE clear function with DECNano enabled, the clear size must align to 48 Bytes for 24 bits-per-pixel formats and align to 64 Bytes for 32 bits-per-pixel formats.
8.  If source buffer tile mode is different from destination buffer tile mode, buffer starting address must be 64 Byte aligned, buffer stride must be 64 Byte aligned for non-24 bits-per-pixel formats, buffer stride must be 48-Byte aligned for 24 bits-per-pixel formats.



VGLite hardware requires the raster image width to be a multiple of 16 pixels for linear gradient and radial gradient operations. This requirement applies to all image formats. Therefore, the user must pad an arbitrary image width to a multiple of 16 pixels for VGLite linear gradient and radial gradient APIs.



**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)

