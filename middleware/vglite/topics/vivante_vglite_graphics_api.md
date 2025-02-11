# VGLite Graphics API

The Vivante VGLite Graphics API is used to control the Vivante vector graphics hardware units that provide accelerated vector and raster operations.

The Vivante VGLite API is developed for use with Vivante GCNanoLiteV, GCNanoUltraV, GCNanoV, GC355, and GC555 hardware. GC355 and GC555 support the Khronos OpenVG 1.1 feature set, while GCNanoLiteV, GCNanoUltraV and GCNanoV have a feature set smaller than that required to pass Khronos OpenVG CTS.

The VGLite API driver V4 is a new design and implementation of the driver \(from 2023Q1\) to support the new generation 2.5D GPU \(GC555\), and the previous 2.5D GPU releases \(GC255, GC265, GC355\). The new V4 driver supports the new and improved VGLite API \(version 3.0\) and can generate the most CPU-efficient, customized driver build for a specific 2.5D GPU release based on the hardware feature set.

VGLite API supported features include: Porter-Duff Blending, Gradient Controls, Fast Clear, Arbitrary Rotations, Path Filling rules, Path painting, and Pattern Path Filling.

By default, VGLite API driver V4 supports one implicit global application context in a single thread. VGLite V4 driver does not support multithreaded applications, which is not suitable for embedded IoT devices.

**Parent topic:**[Introduction](../topics/introduction.md)

