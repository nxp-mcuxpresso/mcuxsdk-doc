# `vg_lite_upload_path` function

**Description:**

This function is used to upload a path to GPU memory.

In normal cases, the VGLite driver will copy any path data into a command buffer structure during runtime. This does take some time if there are many paths to be rendered. Also, in an embedded system the path data won’t change - so it makes sense to upload the path data into GPU memory in such a form that the GPU can directly access it. This function will signal the driver to allocate a buffer that will contain the path data and the required command buffer header and footer data for the GPU to access the data directly. Call vg\_lite\_clear\_path to free this buffer after the path is used.

**Syntax:**

```
vg_lite_error_t vg_lite_upload_path (
    vg_lite_path_t              *path
);
```

**Parameters:**

|Parameter|Description|
|---------|-----------|
|`*path`|Pointer to a [vg\_lite\_path\_t](vg_lite_path_t_structure_002.md) structure that contains the path to be uploaded.|

**Returns:**

`VG_LITE_OUT_OF_MEMORY` if not enough GPU memory is available for buffer allocation.

**Parent topic:**[Vector path functions](../topics/vector_path_functions.md)

