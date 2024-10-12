# Misra/Coverity issues {#coverity_misra_problems}

There are several Misra/Coverity issues in the following source code, to be fixed in future releases.

|Source code location|Possible violation rule|Number of issues|
|--------------------|-----------------------|----------------|
|`devices/MIMXRT1189/drivers/fsl_tstmr.h`|Rule 10.4|1|
|`components/flash/nor/flexspi/fsl_flexspi_nor_flash.c`|Rule 9.3|1|
|`components/edgefast_wifi/source/wpl_nxp.c`|Rule 10.3, 17.7, 21.6|10|

|Source code location|Possible violation rule|Number of issues|
|--------------------|-----------------------|----------------|
|`middleware/mbedtls3x/port/ele_s4xx/src/opaque/mcux_psa_s4xx_opaque_asymmetric_signature.c`|Uninitialized Variables|2|
|`middleware/mbedtls/port/ele_s400/ecc_opaque/ecdsa_alt.c`|Uninitialized Variables|2|
|`middleware/wifi_nxp/wifidriver/mlan_glue.c`|Memory - corruptions|1|

**Note:** Related tickets are: MCUX-66358, MCUX-66527, MCUX-66528, MCUX-66529.

**Parent topic:**[Known issues](../topics/known_issues.md)

