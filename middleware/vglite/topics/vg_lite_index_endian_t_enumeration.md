# `vg_lite_index_endian_t` enumeration

Specifies the endian order parsing mode for index formats *\(from March 2023\)*.

Used in structure: `vg_lite_buffer_t`.

|vg\_lite\_index\_endian\_t string value|Description|
|-----------------------------------------|-------------|
|`VG_LITE_INDEX_ENDIAN_LITTLE_ENDIAN`|Parse the index pixel from low to high, when using index1, the parsing order is bit0~bit7. when using index2, the parsing order is bit0:1,bit2:3,bit4:5.bit6:7. when using index4, the parsing order is bit0:3,bit4:7.|
|`VG_LITE_INDEX_ENDIAN_BIG_ENDIAN`|Parse the index pixel from low to high, when using index1, the parsing order is bit7~bit0. when using index2, the parsing order is bit7:6,bit5:4,bit3:2.bit1:0. when using index4, the parsing order is bit4:7,bit0:3.|

**Parent topic:**[Pixel buffer enumerations](../topics/pixel_buffer_enumerations.md)
