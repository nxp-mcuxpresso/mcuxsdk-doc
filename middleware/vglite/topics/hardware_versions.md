# Hardware versions 

The Vivante VGLite API is compatible with a range of Vivante Vector Graphics IPs including: GCNanoLiteV, GCNanoUltraV, GCNanoV, GC355, and GC555.

**Note:** A specific hardware version has customized feature set that may limit hardware support for some VGLite API options. The VGLite application can use the `vg_lite_query_feature` API to query specific VGLite feature availability.

Users can also check the `VGLite/VGLite/vg_lite_options.h` file which includes CHIPID, REVISION, CID to identify specific HW releases, and the `gcFEATURE_VG_*` macros to define the feature set for the HW release.

The gcFEATURE\_VG\_\* macro values \(except a few SW features\) should NOT be changed. Otherwise, the VGLite driver does not function correctly on the specific HW release. Users can change the “SW Features” macro values to disable some software features, unnecessary error checks, or enable VGLite API trace for debug purposes.

.



**Parent topic:**[Introduction](../topics/introduction.md)

