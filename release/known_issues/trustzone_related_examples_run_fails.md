# TrustZone related examples run fails

The TrustZone related examples run fails. Impacted examples are `freertos_examples/freertos_mpu` and `trustzone_examples`. Impacted toolchains are all.

Workaround:

- For `secure_faults`, modify `secure_faults_s/cm33_core0/tzm_config.c`:

  - Change `#define SAU_REGION_1_END 0x201FFFFFU` to `#define SAU_REGION_1_END 0x20207FFFU`.
  - Change `AHBSC0->SRAM_1_RULE[3] = 0;` to `AHBSC0->SRAM_1_RULE[3] = 0x33330000U;`.

- For the other examples, modify `tzm_config.c`:

  - Change `AHBSC0->SRAM_1_RULE[3] = 0;` to `AHBSC0->SRAM_1_RULE[3] = 0x33330000U;`.
