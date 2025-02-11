# Alignment notes

**Source image alignment requirement**

The buffer start address and stride byte-alignment requirement for a pixel depends on the specific pixel format and the `gcFEATURE_VG_16PIXELS_ALIGNED` value \(0/1\) in the `vg_lite_options.h` file.

|Image format|Bits per pixel|Start address alignment requirement in bytes|Stride alignment requirement in bytes

|Supported for source image|Supported for destination|
|------------|--------------|--------------------------------------------|---------------------------------------|--------------------------|-------------------------|
|VG\_LITE\_INDEX1|1|8B|8B|Yes| |
|VG\_LITE\_INDEX2|2|8B|8B|Yes||
|VG\_LITE\_INDEX4|4|8B|8B|Yes||
|VG\_LITE\_INDEX8|8|16B|16B|Yes||
|VG\_LITE\_A4|4|4B|8B|Yes||
|VG\_LITE\_A8|8|4B|16B|Yes|Yes|
|VG\_LITE\_L8|8|4B|16B|Yes|Yes|
|VG\_LITE\_ARGB2222 group|8|4B|16B|Yes|Yes|
|VG\_LITE\_RGB565 group|16|4B|32B|Yes|Yes|
|VG\_LITE\_ARGB1555 group|16|4B|32B|Yes|Yes|
|VG\_LITE\_ARGB4444 group|16|4B|32B|Yes|Yes|
|VG\_LITE\_YUY2/UYVY|16|4B|32B|Yes||
|VG\_LITE\_ARGB8888/XRGB8888 group|32|4B|64B|Yes|Yes|
|VG\_LITE\_ARGB8565/RGB888 group|32|4B|64B|Yes|Yes|
|VG\_LITE\_NV12\_TILED|Tile 4x4|Y: 16B

 UV: 8B

|Y: 16B

 UV: 8B

|Yes||
|VG\_LITE\_ANV12\_TILED|Tile 4x4|Y: 16B

 UV: 8B

|Y: 16B

 UV: 8B

|Yes||
|VG\_LITE\_AYUY2\_TILED|Tile 4x4|32B|32B|Yes||

VGLite hardware requires the raster image width to be a multiple of 16 pixels for linear gradient and radial gradient operations. This requirement applies to all image formats. Therefore, the user must pad an arbitrary image width to a multiple of 16 pixels for the VGLite linear gradient and radial gradient APIs.

**Destination alignment requirement:**

-   For Pixel Engine \(PE\) destination, the alignment should be 64B for all tiled \(4x4\) formats.
-   Alignment may also be limited by the alignment requirements of backend modules such as DC \(Display Controller\).

**Parent topic:**[vg\_lite\_buffer\_format\_t enumeration](../topics/vg_lite_buffer_format_t_enumeration.md)

