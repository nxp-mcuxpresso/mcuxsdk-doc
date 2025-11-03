# FRO6M Clock Stability Issue

According to ERRATA ERR052742, the FRO6M clock is not stable on some parts. FRO6M outputs lower frequency signal instead of 6MHz when
device is reset or wakes up from low power. It can impact peripherals using it as a clock source.

## Impact on TSTMR Module

The TSTMR (Time Stamp Timer) module exclusively uses the FRO6M clock source. Due to the aforementioned stability issues, **avoid using TSTMR-related APIs if your application requires high-precision timing**.

## Recommendation

For applications requiring precise timing, consider using alternative timer modules that support more stable clock sources.