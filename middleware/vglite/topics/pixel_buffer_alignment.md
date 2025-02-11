# Pixel buffer alignment

The VGLite hardware requires the pixel buffer start address and stride to be properly byte-aligned to work correctly. The start address and stride alignment requirement for a pixel buffer depends on the specific pixel format, and `gcFEATURE_VG_16PIXELS_ALIGNED` value \(0/1\) in `vg_lite_options.h` file. 

**Parent topic:**[Pixel buffers](../topics/pixel_buffers.md)

