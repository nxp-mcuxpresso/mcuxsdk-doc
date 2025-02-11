# `vg_lite_get_register`

**Description:**

This function can be used to read a GPU AHB register value given the AHB byte address of a register. Refer to the appropriate Vivante GPU AHB register specification documents for register descriptions. The value range of AHB accessible addresses for VGLite cores is usually `0x0` to `0x1FF` and `0xA00` to `0xA7F`.

**Syntax:**

```
vg_lite_error_t vg_lite_get_register (
       vg_lite_uint32_t      address,
       vg_lite_uint32_t      *result
);
```

**Parameters:**

|Name|Description|
|----|-----------|
|`address`|Byte Address of the register which value you want.|
|`*result`|The registers value.|

**Parent topic:**[Functions for product and feature queries](../topics/functions_for_product_and_feature_queries.md)

