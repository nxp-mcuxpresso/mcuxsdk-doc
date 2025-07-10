# ROM API otp_fuse_read return value is not 0 on B0 Silicon
 
The return value of the APIs in romapi/otp driver is changed on the B0 silicon. The next release will include a fix to this issue.
 
**Workaround**: Take it as a success operation when the API's return value is 0x5AC3C35A.

**Examples**: romapi_otp, pmc_temperature_sensor

**Affected platforms**: mimxrt700evk