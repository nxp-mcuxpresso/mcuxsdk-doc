# `vg_lite_get_mem_size`

**Description:**

This function queries whether there is any remaining allocated contiguous video memory. *\(available from June 2020\)*

**Syntax:**

```
vg_lite_error_t vg_lite_get_mem_size(
    vg_lite_uint32_t            *size
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`size`|Pointer to the remaining allocated contiguous video memory.|

**Returns:**

Returns `VG_LITE_SUCCESS` if the query is successful and memory is available. Returns `VG_LITE_NO_CONTEXT` if the driver is not initialized or there is no available memory.



**Parent topic:**[Functions for product and feature queries](../topics/functions_for_product_and_feature_queries.md)

