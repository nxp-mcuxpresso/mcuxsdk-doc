# `vg_lite_get_product_info`

**Description:**

This function is used to identify the VGLite-compatible product.

**Syntax:**

```
uint32_t vg_lite_get_product_info (
       char            *name,
       uint32_t        *chip_id,
       uint32_t        *chip_rev
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`name`|A character array to store the name of the chip.|
|`chip_id`|Stores an ID number for the chip.|
|`chip_rev`|Stores a revision number for the chip.|

**Parent topic:**[Functions for product and feature queries](../topics/functions_for_product_and_feature_queries.md)

