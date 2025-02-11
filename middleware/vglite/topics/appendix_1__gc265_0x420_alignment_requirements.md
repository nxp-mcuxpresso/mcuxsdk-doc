# Appendix 1. GC265 0x420 alignment requirements {#appendix_1_gc265_0x420_alignment_requirements}

|Image format|Bits per pixel|Source tile mode|Start Address alignment requirement in bytes|Stride alignment requirement in bytes|Buffer Height alignment requirement|Supported for destination|
|------------|--------------|----------------|------------------------------------------------|-------------------------------------|---------------------------------------|-----------------------------|
|VG\_LITE\_INDEX1|1|linear|8B|1B|1| |
|VG_LITE_INDEX1|1|tile|8B|1B|4| |
|VG\_LITE\_INDEX2|2|linear|8B|1B|1| |
|VG\_LITE\_INDEX2|2|tile|8B|1B|4| |
|VG\_LITE\_INDEX4|4|linear|8B|1B|1| |
|VG\_LITE\_INDEX4|4|tile|8B|2B|4| |
|VG\_LITE\_INDEX8|8|linear|8B|1B|1| |
|VG\_LITE\_INDEX8|8|tile|8B|4B|4| |
|VG\_LITE\_A4|4|linear|8B|1B|1| |
|VG\_LITE\_A4|4|tile|8B|2B|4| |
|VG\_LITE\_A8|8|linear|8B|1B|1|Yes|
|VG\_LITE\_A8|8|tile|8B|4B|4|Yes|
|VG\_LITE\_L8|8|linear|8B|1B|1|Yes|
|VG\_LITE\_L8|8|tile|8B|4B|4|Yes|
|VG\_LITE\_ARGB2222|8|linear|8B|1B|1|Yes|
|VG\_LITE\_ARGB2222|8|tile|8B|4B|4|Yes|
|VG\_LITE\_RGB565|16|linear|8B|2B|1|Yes|
|VG\_LITE\_RGB565|16|tile|8B|8B|4|Yes|
|VG\_LITE\_ARGB1555|16|linear|8B|2B|1|Yes|
|VG\_LITE\_ARGB1555|16|tile|8B|8B|4|Yes|
|VG\_LITE\_ARGB4444|16|linear|8B|2B|1|Yes|
|VG\_LITE\_ARGB4444|16|tile|8B|8B|4|Yes|
|VG\_LITE\_ARGB8888|32|linear|16B|4B|1|Yes|
|VG\_LITE\_ARGB8888|32|tile|16B|16B|4|Yes|
|VG\_LITE\_XRGB8888|32|linear|16B|4B|1|Yes|
|VG\_LITE\_XRGB8888|32|tile|16B|16B|4|Yes|
|VG\_LITE\_ARGB8565|24|linear|8B|3B\*|1|Yes|
|VG\_LITE\_ARGB8565|24|tile|8B|12B\*|4|Yes|
|VG\_LITE\_RGB888|24|linear|8B|3B\*|1|Yes|
|VG\_LITE\_RGB888|24|tile|8B|12B\*|4|Yes|
|VG\_LITE\_ARGB8565\_PLANAR|24|linear|A: 8B RGB: 8B|A: 1B  RGB: 2B|1|Yes|
VG_LITE_ARGB8565_PLANAR||24|tile|A: 8B RGB: 8B|A: 4B RGB: 8B|4|Yes|
|VG\_LITE\_YUY2/UYVY|16|linear|8B|4B|1| |
VG_LITE_YUY2/UYVY||16|tile|8B|8B|4| 
|VG\_LITE\_NV12|12|linear|Y: 8B UV: 8B|Y: 2B UV: 2B|1| |
VG_LITE_NV12||12|tile|Y: 8B UV: 8B|Y: 8B UV: 8B|4| |
|VG\_LITE\_YV12|12|linear|Y: 8B U: 8B V: 8B|Y: 2B U: 1B V: 1B|1| |
VG_LITE_YV12||12|tile|Y: 8B U: 8B V: 8B|Y: 8B U: 4B V: 4B|4| |
|VG\_LITE\_NV16|16|linear|Y: 8B UV: 8B|Y: 2B UV: 2B|1| |
|VG\_LITE\_YV16|16|linear|Y: 8B U: 8B V: 8B|Y: 2B U: 1B V: 1B|1| |
|VG\_LITE\_YV24|24|linear|Y: 8B U: 8B V: 8B|Y: 1B U: 1B V: 1B|1| |
VG_LITE_YV24||24|tile|Y: 8B U: 8B V: 8B|Y: 4B U: 4B V: 4B|4| |
|VG\_LITE\_ETC2|8|tile|8B|4B|4| |



