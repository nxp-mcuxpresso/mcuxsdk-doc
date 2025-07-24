# Brief Driver-Only Configuration Guide

## In-depth guide
**For more comprehensive and up-to-date information on driver-only builds,**
**please refer to the `/middleware/mbedtls3x/docs/driver-only-builds.md`**
**document.**

## Mbed TLS 3.x
Default config file at : `mbedtls3x/include/mbedtls/mbedtls_config.h`

### To use, keep these steps in mind
* This config is always enabled and should not be bypassed.
* Define `MBEDTLS_CONFIG_FILE` with your config filename to use your own
  configuration file instead of the default one.
* Disable all `MBEDTLS_xxx_C` algorithm macros that you do not want the software
  implementations of. Disabling them makes the build system skip the
  Mbed TLS 3.x built-in implementations (**NOTE: READ IMPORTANT CAVEAT BELOW**).

### Caveat for `MBEDTLS_xxx_C`
These macros **may get re-enabled automatically by**
**the `config_adjust_legacy_*.h` reconfig files** if the disabled feature macro
is a dependency for another.

This mainly relates to PSA-based configurations (see the **[PSA](#psa)** section
below). If you `PSA_WANT` some algorithm and not all prerequisites for that
algorithm are `MBEDTLS_PSA_ACCEL`erated, then the appropriate `MBEDTLS_xxx_C`
macros **will get enabled automatically by**
**the `config_adjust_legacy_from_psa.h` reconfig file**.

In short, `PSA_WANT` has higher priority over `MBEDTLS_xxx_C`.

## PSA
Default config file at : `mbedtls3x/include/psa/crypto_config.h`

### To use, keep these steps in mind
* `MBEDTLS_PSA_CRYPTO_CONFIG` must be enabled to use the `PSA_WANT` macros
  (see below). This option needs to be enabled in the Mbed TLS 3.x config file
  (disabled by default; you can find it commented out in `mbedtls_config.h`).
* Define `MBEDTLS_PSA_CRYPTO_CONFIG_FILE` with your config filename to use your
  own configuration file instead of the default one.
* Enable all the `PSA_WANT` macros in this config file that are required for
  your project. Granularity is fairly fine-grained, but not atomic (e.g. no
  distinguishing between one-go and multipart operations). This macro just
  enables the functionality that you `PSA_WANT`. This means that functionality
  may be provided either by calling the accelerated wrappers of the `PSA_WANT`ed
  algorithms, or, if acceleration is not supported, by calling the Mbed TLS 3.x
  software implementation. For enabling only accelerated functionality, see
  the next list item.
* Enable all the `MBEDTLS_PSA_ACCEL` macros in this config file that are
  accelerated and are required for your project. The names for these generally
  mirror the `PSA_WANT` macros. They let the build system know whether or not to
  include the software implementation. So, generally, the more
  `MBEDTLS_PSA_ACCEL` macros are enabled, the smaller the binary size,
  as less software is compiled in.
* Please refer to the `driver-only-builds.md` documentation file for enablement
  of specific algorithms.

#### Example
For example, if you `PSA_WANT` AES CMAC, you must `PSA_WANT` the AES key type,
as well as CMAC. This means that `PSA_WANT_KEY_TYPE_AES` and `PSA_WANT_ALG_CMAC`
need to be enabled.

If there is CMAC acceleration via PSA implemented on your device, you can enable
`MBEDTLS_PSA_ACCEL_ALG_CMAC` to prevent the inclusion of Mbed TLS 3.x software
implementation of CMAC in the build.
