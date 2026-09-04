# RT2660 Debug Guide

This guide covers **all RT2660 debug scenarios**.

**Scope**

*Debug probes*

- **SEGGER J-Link — ✅ ready**
- **CMSIS-DAP — ✅ ready**

*Build / debug support matrix*

| Toolchain / IDE | Build | Debug | Probe |
|---|---|---|---|
| **armgcc** | ✅ | ✅ Ozone | J-Link |
| **IAR EWARM** | ✅ | ✅ C-SPY | J-Link or CMSIS-DAP |

```{toctree}
:maxdepth: 1

00_debug_mechanism.md
01_patch_install.md
02_build_targets.md
03_unified_linkage_targets.md
04_ram_only_targets.md
05_emmc_boot.md
07_blhost.md
10_setup_iar.md
12_setup_gcc.md
13_setup_ozone.md
20_flow_unified_linkage_debug.md
21_flow_ram_only_debug.md
22_flow_psram_only_debug_xspi_nor.md
23_flow_psram_only_debug_emmc.md
30_faq.md
HardwareAdaption/eMMC_HW_Rework.md
HardwareAdaption/PSRAM_Configuration.md
```

<!--
Pages commented out (files retained, not shown in navigation):
  06_spsdk.md                        - Secure Provisioning Tool (SPSDK / SPT)
  11_setup_mdk.md                    - Setup -- Keil MDK
-->

