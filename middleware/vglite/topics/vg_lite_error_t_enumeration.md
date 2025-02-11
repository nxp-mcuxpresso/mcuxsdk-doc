# `vg_lite_error_t` enumeration

Most functions in the API include an error status via the `vg_lite_error_t`enumeration. API functions return the status of the command and will report `VG_LITE_SUCCESS` if successful with no errors. Possible error values include the values in the table below. `vg_lite_error_t`enumeration is used in many functions, including initialization, flush, blit, draw, gradient, and pattern functions.

|`vg_lite_error_t` string values|Description|
|-------------------------------|-----------|
|`VG_LITE_GENERIC_IO`|Cannot communicate with the kernel driver|
|`VG_LITE_INVALID_ARGUMENT`|An invalid argument was specified|
|`VG_LITE_MULTI_THREAD_FAIL`|Multi-thread/tasks fail *\(available from June 2020\)*|
|`VG_LITE_NO_CONTEXT`|No context specified|
|`VG_LITE_NOT_SUPPORT`|Function call is not supported. Hardware support is not available.|
|`VG_LITE_OUT_OF_MEMORY`|Out of memory \(driver heap\)|
|`VG_LITE_OUT_OF_RESOURCES`|Out of resources \(OS heap\)|
|`VG_LITE_SUCCESS`|Successful with no errors|
|`VG_LITE_TIMEOUT`|Timeout|
|`VG_LITE_ALREADY_EXISTS`|Object exists *\(available from August 2021\)*|
|`VG_LITE_NOT_ALIGNED`|Data alignment error *\(available from August 2021\)*|

**Parent topic:**[Enumerations for error reporting](../topics/enumerations_for_error_reporting.md)

