# Bluetooth Synopsys Controller

-   Stability Observation During extended Testing
    During extended sequences of link layer tests, typically after 1.5 hours of continuous execution without a hardware reset,
    an unexpected behavior has been observed in the llhwc_set_adv_param function.
    -   This behavior is rare and has only been seen under specific test conditions.
    -   It appears to be related to the extended advertising feature.
    -   Regular usage scenarios are not expected to be impacted.

- Faulty Passive Channel Assessment Behavior
    -   In rare cases where only one channel is deemed suitable during channel assessment, connection establishment may not succeed.
    -   Channel assessment might not work on connections with slave latency > 0
    -   A fix has been identified and will be included in the next release.