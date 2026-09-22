# AHBSC protection not enforced on B0 silicon which version=T2.0.32

There is an errata (ERR053561) with B0 silicon which version = T2.0.32. Software relying on AHBSC protection mechanisms may observe that the intended protection behavior is not enforced. Follow the description in the errata and apply the ROM patch to fix the issue. Impacted examples are those relying on AHBSC protection mechanisms, such as trustzone_examples and freertos_examples/freertos_mpu.
