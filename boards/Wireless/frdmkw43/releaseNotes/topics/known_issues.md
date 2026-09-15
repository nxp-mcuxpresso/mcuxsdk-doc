# Known issues 

This section lists the known issues, limitations, and/or workarounds.


```{include} /release/known_issues/known_issue_only_freertos_is_tested_for_rtos_support.md
:heading-offset: 1
```

```{include} /release/known_issues/known_issue_disabled_pairing_and_bonding_for_most_sensor_appli.md
:heading-offset: 1
```

```{include} /release/known_issues/known_issue_bluetooth_le.md
:heading-offset: 1
```

```{include} /release/known_issues/known_issue_other_limitations.md
:heading-offset: 1
```
-   KW43 and MCXW70 are in early enablement. Most Bluetooth LE features are available with limited validation. Full feature robustness will be achieved in upcoming releases.
-   The wireless_ranging and localization applications have limitations in executing Channel Sounding scenarios.
-   Other Bluetooth applications available in the package (bare-metal and Arm GCC versions) have not been validated.
-   Features not supported: Trusted Firmware-M (TF-M) for Advanced Secure mode, OTA support, low power, Concurrent mode, FRO32K, limited the payload for Extended Advertising to 30 Bytes.

