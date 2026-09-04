# Build Targets

The RT2660 SDK provides seven build targets across two categories: five **Unified Linkage** targets and two **RAM ONLY** targets.

For all debug sessions, set the MIMXRT2660-EVK boot switch to `0b00` (XSPI NOR boot mode).

## Quick reference

| Target | Type | POR boot |
|---|---|---|
| `debug` | Unified Linkage | Yes -- XSPI NOR flash |
| `xspi_nor` | Unified Linkage | Yes -- XSPI NOR flash |
| `xspi_nor_psram` | Unified Linkage | Yes -- XSPI NOR flash |
| `psram` | Unified Linkage | Yes -- XSPI NOR flash |
| `psram_txt` | Unified Linkage | Yes -- XSPI NOR flash |
| `ram_only` | RAM ONLY | Yes -- eMMC or XSPI NOR flash (requires boot header) |
| `psram_only` | RAM ONLY | Yes -- eMMC or XSPI NOR flash (requires boot header) |

> **Note**: the **default** SDK build for `ram_only` and `psram_only` does **not** include a boot header and cannot POR boot.

---

## Unified Linkage targets

Unified Linkage is the mainstream linkage approach for MIMXRT2660-EVK SDK examples.

The five Unified Linkage targets all boot from XSPI NOR flash. The image is programmed into flash, startup runs XIP from flash, then code is copied (or left in flash) according to the target before jumping to `main()`.

> **Coming from legacy RT1xxx?** Although some target names look familiar (e.g. `debug`, `psram`), the Unified Linkage mechanism on RT2660 is fundamentally different from the legacy RT1xxx RAM-download flow. Do not assume the same debug behavior -- read this guide before proceeding.

---

## RAM ONLY targets

The two RAM ONLY targets (`ram_only` and `psram_only`) do not use XSPI NOR flash as part of the debug flow.

The default build for both targets does not include a USDHC boot header.

The standard workflow is **download to RAM then run**: the debugger connects, downloads the ELF directly into ITCM or PSRAM, and starts execution -- no flash programming required, which makes the iteration cycle faster.

RAM ONLY images are volatile: cycling power clears the program.

> **Coming from legacy RT1xxx?** These two targets are the closest equivalent to the legacy RAM-download flow: `ram_only` corresponds to `debug` on RT1xxx (code in TCM), and `psram_only` corresponds to `psram_txt` on RT1xxx (code in external RAM).

> **One-time preparation required for `psram_only`**: a one-time board setup step is required before the first debug session.


