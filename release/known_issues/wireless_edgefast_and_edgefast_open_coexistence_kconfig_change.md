# EdgeFast and EdgeFast Open Coexistence: Per-Example Kconfig Required

> **Note:** SDK EdgeFast v26.06.00 is classified as a Long-Term Release (LTR). The LTR status is not applied to SDK EdgeFast v26.09.00.

Starting with SDK v26.06.00, **EdgeFast Open** is introduced to coexist with EdgeFast. As a result, the global `source "middleware/edgefast_bluetooth/Kconfig"` entry has been **removed** from `Kconfig.mcuxpresso`.

All EdgeFast and EdgeFast Open examples must now include their own `Kconfig` file that explicitly selects the intended Bluetooth stack. Without this file, builds will fail or result in a missing Bluetooth stack configuration error.

Each example must add a `Kconfig` file containing the appropriate selection:

```kconfig
# Select EdgeFast (classic)
source "middleware/edgefast_bluetooth/Kconfig"
source "Kconfig.mcuxpresso"
```

or

```kconfig
# Select EdgeFast Open
source "middleware/edgefast_open/Kconfig"
source "Kconfig.mcuxpresso"
```

| Action | Description |
|---|---|
| Remove global Kconfig source | `source "middleware/edgefast_bluetooth/Kconfig"` is no longer present in `Kconfig.mcuxpresso` |
| Add per-example Kconfig | Each EdgeFast or EdgeFast Open example must include its own `Kconfig` file selecting the appropriate stack |
