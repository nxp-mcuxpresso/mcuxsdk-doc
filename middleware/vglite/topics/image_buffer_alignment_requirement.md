# Image buffer alignment requirement 

The image \(or source\) buffer alignment requirement depends on the specific pixel format, and some `gcFEATURE_*_ALIGNED` defines in the `vg_lite_options.h` file.

|Image format|Bits per pixel|Source tile mode|Start address alignment requirement in bytes|Stride alignment requirement in bytes|Buffer height alignment requirement|Supported for destination|
|------------|--------------|----------------|--------------------------------------------|-------------------------------------|-----------------------------------|-------------------------|
|VG\_LITE\_INDEX1|1|linear|8B|2B|1|　|
|VG\_LITE\_INDEX1|1|tile|8B|1B|4|　|
|VG\_LITE\_INDEX2|2|linear|8B|4B|1|　|
|VG\_LITE\_INDEX2|2|tile|8B|1B|4|　|
|VG\_LITE\_INDEX4|4|linear|8B|8B|1|　|
|VG\_LITE\_INDEX4|4|tile|8B|2B|4|　|
|VG\_LITE\_INDEX8|8|linear|16B|16B|1|　|
|VG\_LITE\_INDEX8|8|tile|16B|4B|4|　|
|VG\_LITE\_A4|4|linear|8B|8B|1|　|
|VG\_LITE\_A4|4|tile|8B|2B|4|　|
|VG\_LITE\_A8|8|linear|16B|16B|1|Yes|
|VG\_LITE\_A8|8|tile|16B|4B|4|Yes|
|VG\_LITE\_L8|8|linear|16B|16B|1|Yes|
|VG\_LITE\_L8|8|tile|16B|4B|4|Yes|
|VG\_LITE\_ARGB2222|8|linear|16B|16B|1|Yes|
|VG\_LITE\_ARGB2222|8|tile|16B|4B|4|Yes|
|VG\_LITE\_RGB565|16|linear|32B|32B|1|Yes|
|VG\_LITE\_RGB565|16|tile|32B|8B|4|Yes|
|VG\_LITE\_ARGB1555|16|linear|32B|32B|1|Yes|
|VG\_LITE\_ARGB1555|16|tile|32B|8B|4|Yes|
|VG\_LITE\_ARGB4444|16|linear|32B|32B|1|Yes|
|VG\_LITE\_ARGB4444|16|tile|32B|8B|4|Yes|
|VG\_LITE\_ARGB8888|32|linear|64B|64B|1|Yes|
|VG\_LITE\_ARGB8888|32|tile|64B|16B|4|Yes|
|VG\_LITE\_XRGB8888|32|linear|64B|64B|1|Yes|
|VG\_LITE\_XRGB8888|32|tile|64B|16B|4|Yes|
|VG\_LITE\_ARGB8565|24|linear|64B|48B\*|1|Yes|
|VG\_LITE\_ARGB8565|24|tile|64B|12B\*|4|Yes|
|VG\_LITE\_RGB888|24|linear|64B|48B\*|1|Yes|
|VG\_LITE\_RGB888|24|tile|64B|12B\*|4|Yes|
|VG\_LITE\_YUY2/UYVY|16|linear|32B|32B|1|　|
|VG\_LITE\_YUY2/UYVY|16|tile|32B|8B|4|　|
|VG\_LITE\_NV12|12|linear|Y: 32B UV: 32B|Y: 32B UV: 32B|1|　|
|VG\_LITE\_YV12|12|linear|Y: 32B U: 16B V: 16B |Y: 32B U: 16B V: 16B|1|　|
|VG\_LITE\_NV16|16|linear|Y: 32B UV: 32B |Y: 32B UV: 32B |1|　|
|VG\_LITE\_YV16|16|linear|Y: 32B U: 16B V: 16B |Y: 32B U: 16B V: 16B|1|　|
|VG\_LITE\_YV24|24|linear|Y: 32B U: 32B V: 32B |Y: 32B U: 32B V: 32B|1|　|
|VG\_LITE\_ETC2|8|tile|16B|4B|4|　|  


**Note:**

1.  The values in the table reflect the alignment requirements of the data in memory. The stride of ARGB8888 / ARGB8565 is seen as 4Byte per pixel when configuring the hardware.
2.  For tile mode, the stride is still the byte size of a row of pixels in the buffer instead of 4 rows.
3.  When DECNano function is enabled for the buffer, the total buffer size need align to 64Byte\*compression rate for ARGB8888 or XRGB8888 format, align to 48Byte\*compress rate for RGB888 format.

**Additional Alignment Requirement**

1.  Buffer starting address must be 16 pixel-byte-size aligned, that is 8 bit-per-pixel format buffer must be 16 bytes aligned; 16 bit-per-pixel format buffer must be 32 bytes aligned; 24 and 32 bit-per-pixel format buffer must be 64 bytes aligned.
2.  For linear mode buffer, the buffer stride must be 16 pixel-byte-size aligned.
3.  For tile mode buffer, buffer width and height must be 4 pixel aligned so buffer width and height end at tile boundary.



**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)

