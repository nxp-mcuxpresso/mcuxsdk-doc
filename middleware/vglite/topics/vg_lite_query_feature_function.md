# `vg_lite_query_feature`

**Description:**

This function is used to query if a specific feature is available.

**Syntax:**

```
vg_lite_uint32_t vg_lite_query_feature (
    vg_lite_feature_t          feature
);

```

**Parameters:**

|Name|Description|
|----|-----------|
|`feature`|Feature to be queried, as detailed in enum [vg\_lite\_feature\_t](vg_lite_feature_t_enumeration.md)|

**Returns:**

The feature is either not supported \(0\) or supported \(1\).

**Parent topic:**[Functions for product and feature queries](../topics/functions_for_product_and_feature_queries.md)

