# Known Issues

This section lists the known issues, limitations, and/or workarounds.

```{include} /release/known_issues/cannot_add_sdk_components.md
:heading-offset: 1
```
## Race condition during DPD1 and DPD2 modes wake-up
A race condition may occur during wake-up from DPD1 and DPD2 modes, when APB peripherals are accessed by cm0plus core.

## VDD_CORE_AON is set too low
VDD_CORE_AON voltage may be set too low in generated clock configuration used by SDK examples, and in power driver. Workaround is to use about 30 mV higher voltage.

## CM0+ core debug in Keil uVision IDE
CM0+ core debug using CMSIS-DAP is not supported in Keil uVision IDE.
