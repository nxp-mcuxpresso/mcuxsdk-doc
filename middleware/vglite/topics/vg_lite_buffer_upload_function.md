# `vg_lite_upload_buffer` function

**Description:**

The function uploads the pixel data to a GPU memory buffer object. The format of the data \(pixel\) to be uploaded must match the format defined for the buffer object. The input data memory buffer should contain enough data to be uploaded to the GPU buffer pointed by the input parameter `buffer`.

**Note:** Vivante Vector Graphics IP only uses data\[0\] and stride\[0\] as it does not support planar YUV formats..

**Syntax:**

```
vg_lite_error_t vg_lite_upload_buffer (
    vg_lite_buffer_t           *buffer,
    vg_lite_uint8_t            *data[3],
    vg_lite_uint32_t           stride[3]
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`buffer`|Pointer to a buffer structure that was filled in by calling the [vg\_lite\_allocate\(\)](vg_lite_allocate_function.md) function|
|`data[3]`|Pointer to pixel data. For the YUV format, there may be up to 3 pointers.|
|`stride[3]`|Stride for the pixel data|

**Returns:**

Returns `VG_LITE_SUCCESS` if the function is successful. See [vg\_lite\_error\_t](vg_lite_error_t_enumeration.md) enum for other return codes.

**Parent topic:**[Pixel buffer functions](../topics/pixel_buffer_functions.md)

