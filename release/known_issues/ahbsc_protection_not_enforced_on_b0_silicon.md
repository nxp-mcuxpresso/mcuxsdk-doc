# AHBSC protection not enforced on B0 silicon which version=T2.0.32

An erratum (ERR053561) affects B0 silicon (version T2.0.32). Due to this issue, software that depends on AHBSC protection mechanisms may experience unintended behavior because the configured protection settings are not properly enforced.

To resolve the issue, follow the guidance provided in the errata document and apply the corresponding ROM patch.

Examples impacted by this erratum include applications and examples that rely on AHBSC protection features, such as:

trustzone_examples
freertos_examples/freertos_mpu

These examples should be updated with the recommended workaround to ensure correct protection behavior on affected devices.
