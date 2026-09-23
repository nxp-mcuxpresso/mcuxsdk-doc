## Overview

MCUXpresso SDK 26.09.00 is the September 2026 quarterly release, delivering new device and
platform enablement, significant security library upgrades, expanded wireless connectivity
support, and broad quality improvements across drivers, middleware, and examples.

This release spans **72 updated sub-repositories**, **3 newly added components**, and
**1 removed component** relative to the 26.06.00 baseline. Key themes include:

- **New silicon support:** MCXE327, MCXN556S (123-WLCSP), MCXN947T, MCXC352/353,
  MCXA556/557 (WLCSP), i.MX RT2660 (public), i.MX 93 CA55, i.MX 8M Mini CA53,
  i.MX 95 CA55, FRDM-IMXRT1152, FRDM-MCXE32B, KW43-LOC, MCXW70-LOC.
- **Security upgrades:** Mbed TLS updated to v4.2.0 (LTS) and v3.6.7; ELS_PKC v5.0.0;
  SGI_PKC v4.3.0; TF-M updated; new EdgeLock ELE S100 firmware; new `ele_hseb` component.
- **Wireless:** Wi-Fi firmware updated to IW612 18.99.8.p141, IW416 16.92.21.p166,
  RW610/IW610 p141; Bluetooth host v1.10.23; edgefast_open migration complete;
  new MSTP library added.
- **ML / AI:** ExecuTorch upgraded to v1.4.1; Neutron NPU SDK updated to v3.2.2;
  MPP updated to v4.4.0.
- **RTOS:** FreeRTOS-Plus-TCP updated to V4.4.1. 
- **Boot:** MCUboot updated to v2.4.0.
- **Toolchain:** Xtensa toolchain updated to RJ2026_6 across all DSP-capable devices.

## Release Highlights

1. **i.MX RT2660 Public Enablement** — Full device support for the i.MX RT2660 SoC
   (clock, power, eDMA, LLC, TRDC, USB) moved from pre-silicon to public availability,
   including Neutron NPU firmware for IAR and GCC toolchains.

2. **Mbed TLS 4.2.0 and 3.6.7 Upgrades** — The SDK now ships both the LTS Mbed TLS 4.2.0
   branch and the 3.6.7 maintenance update, incorporating upstream security fixes and
   NXP hardware-acceleration extensions (CASPER ECDH, HSEB opaque key operations,
   PKC transparent key export).

3. **MCUboot v2.4.0** — The open-source secure bootloader is updated to upstream v2.4.0,
   adding OTFAD encrypted XIP support for i.MX RT1152/1160/1170 and improved PSA Crypto
   integration.

4. **New MCXE327 Device Support** — Full SDK enablement for the MCXE327 MCU including
   device headers, Kconfig, startup files, QSPI driver adaptation, and errata workarounds.

5. **ExecuTorch v1.4.1 with Neutron 3.2.2** — The on-device ML inference framework is
   upgraded to ExecuTorch v1.4.1 with Neutron SDK 3.2.2, adding RT700 support and
   `softmax` operator acceleration on the Neutron NPU.

6. **USB Stack** — The version is updated to **2.13.0**.
      - Fixed memory leaks, improved host stack robustness and security, and enhanced MCX ENET adapter functionality with MII support.
    - Fixed two vulnerability issues (CVEs are pending).
      - A missing bounds check on a host-controlled field in the RNDIS device class driver of the NXP MCUXpresso SDK USB middleware up to releases **26.06.00-lts** and **26.09.00-pvw2** allowed a malicious USB host to read arbitrary memory from the connected device. All software versions starting from **26.06.01-lts** and **26.09.00** have fixed this issue.

        *Acknowledgment: NXP would like to thank dread (d7ead) for the responsible disclosure.*
      - A missing bounds check on a device-controlled field in the USB host video, audio, and CDC class drivers of the NXP MCUXpresso SDK USB middleware up to releases **26.06.00-lts** and **26.09.00-pvw2** allowed a malicious USB device to trigger a heap buffer overflow when connected to an affected host, potentially leading to memory corruption and loss of device availability. All software versions starting from **26.06.01-lts** and **26.09.00** have fixed this issue.

        *Acknowledgment: NXP would like to thank dread (d7ead) for the responsible disclosure.*

Comprehensive bounds-checking and input-validation fixes across USB host class drivers (RNDIS, CDC-ECM, Audio, Video, PHDC, MSC, MTP,
   CCID) addressing potential out-of-bounds reads from malformed USB descriptors.

7. **Wi-Fi Firmware and Driver Updates** — Wi-Fi firmware refreshed to latest patch levels
   for IW612, IW416, RW610, and IW610; Wi-Fi driver updated to v1.3.r49.p10 with
   SD8978/SD9177 compressed TX power table support, VDLL firmware download, and
   multiple stability fixes.

8. **Cortex-A Core Enablement for i.MX Devices** — CA55 (AArch64) device files added for
   i.MX 93 (MIMX9352), i.MX 95 (MIMX9596), and i.MX 8M Mini (MIMX8MM6); CA53 support
   added for i.MX 8M Mini.

9. **ELS_PKC v5.0.0 and SGI_PKC v4.3.0** — Cryptographic accelerator libraries updated
   with expanded platform support (MCXN, RT700, MCXL, MCXW Zephyr), new PQC add-on
   v4.3.0, and improved PSA driver integration.

10. **Connectivity Framework v7.4.3** — Updated wireless MCU connectivity framework with
    CERT-C/MISRA quality fixes, improved NBU fault diagnostics, KW43-LOC antenna diversity
    support, and Zephyr configuration management improvements.

## Manifest & Repository Changes

### Summary

| Category  | Count |
|-----------|------:|
| Changed   | 91    |
| Added     | 3 (customer-facing) |
| Removed   | 1 (customer-facing) |

### Added Repositories

| Repository       | Functional Area          | Description                                                  |
|------------------|--------------------------|--------------------------------------------------------------|
| `ele_hseb`       | Security                 | New EdgeLock HSEB (Hardware Security Engine B) PSA driver component, enabling opaque asymmetric key operations on supported devices. |
| `mstp-lib`       | Connectivity & Wireless  | New MSTP (Master-Slave Token Passing) library for BACnet/MS-TP connectivity support. |
| `neo_isp`        | ML / DSP / Multimedia    | New Neo ISP (Image Signal Processor) middleware component for i.MX 95 camera pipeline support. |

### Removed Repositories

| Repository         | Functional Area         | Impact                                                       |
|--------------------|-------------------------|--------------------------------------------------------------|
| `edgefast_bt_ble`  | Connectivity & Wireless | Removed legacy EtherMind-based Bluetooth stack. Applications should migrate to `edgefast_open`, which is the unified Bluetooth stack going forward. See Breaking Changes section. |

### Impact on `west update`

Running `west update` against `release/26.09.00` will fetch updated revisions for all 91
changed repositories. The three newly added repositories (`ele_hseb`, `mstp-lib`, `neo_isp`)
will be cloned for the first time. The removed `edgefast_bt_ble` repository will no longer
be checked out; any project referencing it directly must migrate to `edgefast_open`.

---

What's New
----------

### New Features

#### Fundamental

- **Phase Detector (PHD) driver** — New peripheral driver for the Phase Detector IP,
  providing initialization, deinitialization, and configurable operation modes.
- **eDMA software workaround for errata ERR052315** — The eDMA driver now applies an
  automatic software workaround for affected eDMA instances where certain TCD
  configuration errors could cause subsequent DMA requests to stall.
- **SDMA SPBA count derived from array size** — `SDMA_IsPeripheralInSPBA()` now derives
  the SPBA instance count from `SPBA_BASE_PTRS` array size rather than a fixed feature
  macro, improving portability across SoC variants.
- **ELE S100 firmware and crypto support** — EdgeLock ELE S100 firmware added to the
  `edgelock` repository; `mcu-sdk-components` extended with ELE S100 support in the
  ELE Crypto component for i.MX RT2660.
- **EdgeLock V2X FCE AES-GCM service** — New `v2x_fce` component providing EdgeLock V2X
  Fast Crypto Engine AES-GCM firmware service for i.MX 943 CM33.
- **EdgeLock V2X base service driver** — New `v2x_base` component providing the EdgeLock
  V2X base (debug) service driver and `ele_base_api` helper layer for i.MX 943 CM33.
- **CMSIS Cortex-M55 core header support** — CMSIS CMakeLists.txt and Kconfig updated to
  include Cortex-M55 (ARMv8.1-M) core headers, enabling projects targeting CM55 cores.
- **Kconfig EDMA selector project segment** — New `module.driver.edma_selector` Kconfig
  project segment allows enabling the eDMA selector driver from `prj.conf`.
- **MVE (Helium) compile flag documentation** — New documentation section covering how to
  disable MVE on Cortex-M55/M85 across IAR, Keil MDK, and ARMGCC toolchains.
- **IAR `restore_breakpoint` option** — New `restore_breakpoint` key documented under
  `debugger_setting` in IDE.yml for IAR GUI project generation.
- **Pagefind-based documentation search** — SDK documentation now includes a
  Pagefind-powered search engine with improved relevance ranking, replacing the previous
  Sphinx search that produced excessive per-board duplicate results.
- **SBOM collection documentation** — New `sbom_collect` documentation integrated into
  the SDK documentation set.

#### Security

- **Mbed TLS 4.2.0 (LTS)** — The `mbedtls` repository is updated to Mbed TLS v4.2.0,
  incorporating upstream security fixes, TLS 1.3 record boundary alignment improvements,
  and DTLS-SRTP session reset fixes.
- **Mbed TLS 3.6.7** — The `mbedtls3x` NXP fork is rebased onto upstream Mbed TLS v3.6.7,
  adding NXP hardware-acceleration extensions: CASPER ECDH PSA wrappers, HSEB opaque
  asymmetric sign/verify, and PKC transparent public-key export.
- **ELS_PKC v5.0.0** — Updated to v5.0.0 with MCXN and RT700 (MIMXRT7xx) ELS/PKC
  integration, MCXN526T device support, and improved device-header portability.
- **SGI_PKC v4.3.0 + PQC add-on v4.3.0** — SGI_PKC updated to v4.3.0 with Zephyr support
  for MCXL and MCXW platforms; new PQC (Post-Quantum Cryptography) add-on v4.3.0 included.
- **TF-PSA-Crypto updated to v1.2.0** — `tf-psa-crypto` updated from v1.1.0 to v1.2.0
  with ML-DSA builtin implementation and updated driver wrapper templates.
- **PSA crypto driver hardening** — Comprehensive CERT-C integer-overflow and pointer
  safety fixes across CAAM, DCP, ELE HSEB, ELS_PKC, SGI, and ele_s4xx PSA drivers;
  oversized key rejection on SGI import; tampered multipart AEAD CCM decrypt rejection.
- **HSEB opaque key operations** — New opaque key generation, import, export, and
  asymmetric sign/verify operations via the HSEB PSA driver.
- **EL2GO agent: PSA key ID export API** — New
  `iot_agent_utils_psa_import_blobs_from_flash_exp_key_id()` API exports PSA key IDs of
  imported EL2GO blobs, enabling downstream key usage without re-importing.
- **EL2GO CSR application expanded** — `el2go_csr` application enabled on additional
  platforms: MCXE31B (opaque keys), KW43 (without TF-M), A20 boards, and MCXL20.
- **Secure subsystem Zephyr support** — KW45/W71 SW session tracking and Zephyr Kconfig/
  CMakeLists added to the secure subsystem component.
- **TF-M updated** — Trusted Firmware-M updated to align with TF-M 2.3, including
  adjusted binary location for signed secure images.
- **ELE FW header representation** — Centralized ELE firmware header with CMake and
  Kconfig integration, enabling dynamic and non-exclusive FW inclusion in C builds.

#### Connectivity & Wireless

- **Wi-Fi secure enterprise example with opaque keys** — New `wifi_secure_enterprise`
  example demonstrating WPA2/WPA3 Enterprise authentication using opaque (hardware-
  protected) private keys via the PSA Crypto API.
- **SDIO over SPI host driver** — New SPI host driver added to the SDMMC middleware,
  enabling SDIO connectivity over SPI interface.
- **LE Power Control via vendor HCI command** — Bluetooth host updated with a dedicated
  vendor HCI command to enable LE Power Control on KW45/KW47 platforms.
- **BLE Direct Test Mode (DTM) shell commands** — New NXP-specific DTM shell commands
  added to `edgefast_open` for RF testing on FRDM-RW612 and RD-RW612-BGA.
- **RFCOMM Remote Line Status (RLS) support** — `edgefast_open` now supports sending
  RFCOMM Remote Line Status commands to report line errors to remote devices.
- **Coex FRDM-IMXRT1152 support** — Wi-Fi + Bluetooth coexistence example
  (`coex_wifi_edgefast`) enabled on the FRDM-IMXRT1152 board.
- **Coex RT1060EVKC support** — Coexistence example support added for the
  evkcmimxrt1060 board with edgefast_open middleware.
- **Narrow-band firmware UART download** — Coex applications gain support for
  downloading narrow-band (BT/OT) firmware over UART for UART-based BT firmware
  bootstrap platforms.
- **KW43-LOC antenna diversity** — Connectivity framework updated to enable antenna
  diversity on the KW43-LOC board via `PLATFORM_InitLcl()`.
- **MSTP library** — New `mstp-lib` component added for BACnet MS-TP connectivity.
- **lwIP updated to 2.2.2** — lwIP NXP fork updated to version 2.2.2_rev2, syncing with
  upstream master (3d896ba0) and including IPv6 ND6 option parsing improvements,
  ENET_QOS flexible configuration hook, and multiple security/stability fixes.
- **USB Zephyr host controller driver support** — Zephyr USB host controller drivers
  aligned with SDK; EHCI host support extended to i.MX 952x devices.
- **SDIO SPI mode support** — SDIO middleware updated to support SPI mode operation.

#### ML / DSP / Multimedia

- **ExecuTorch v1.4.1** — On-device ML inference framework upgraded to v1.4.1 with
  Neutron SDK 3.2.2, RT700 board support, `softmax` operator acceleration on Neutron NPU,
  and simplified OSS native runtime build method.
- **Neutron NPU SDK 3.2.2** — Neutron software SDK updated to v3.2.2 across eIQ
  middleware and ExecuTorch; IAR toolchain firmware added for RT2660.
- **MPP v4.4.0** — Media Processing Pipeline updated to v4.4.0 with RTSP/RTP streaming
  support, FRDM-IMXRT1152 board support, camera gesture recognition example, and
  all NPU models rebuilt with Neutron compiler 3.2.2.
- **Ethos-U85 512 NPU support (RT700E)** — New example added for Ethos-U85 512 NPU
  with Cortex-M55 core on i.MX RT700E; IAR toolchain hang fix for Ethos-U driver in
  release mode.
- **Neo ISP component** — New `neo_isp` middleware component for i.MX 95 Image Signal
  Processor camera pipeline support.
- **Xtensa toolchain updated to RJ2026_6** — DSP codec libraries, XAF (v3.8), HiFi NN
  Library (v5.0.0 API 2.0), and NatureDSP rebuilt with the RJ2026_6 Xtensa toolchain
  across RT500, RT600, RT700, and i.MX 8ULP DSP variants.
- **FRDM-IMXRT700 DSP examples** — NatureDSP, VIT, nnlib, XAF (xaf_playback,
  xaf_record, xaf_usb_demo), and Cadence codec examples enabled on FRDM-IMXRT700.
- **MCXN947T Neutron NPU support** — MCXN947T device added to Neutron NPU DEVICE_IDS
  in the eIQ middleware.

#### RTOS

- **Boot** — Open-source secure bootloader updated to upstream v2.4.0 with
  OTFAD encrypted XIP support for i.MX RT1152/1160/1170, improved PSA Crypto
  integration, and Zephyr compatibility fixes.
- **Multicore** — 
  - RPMsg-Lite v5.5.0 updated with MCXE32B dual Cortex-M7 support, FRDM-IMXRT700 and FRDM-MCXN947T board support, new `rpmsg_lite_are_all_buffers_consumed()` API,
  CERT INT31-C/ARR38-C fixes, and Zephyr `hal_nxp` integration.
  - MCMGR v5.3.0, multicore manager updated with MCXE32B dual Cortex-M7 support, FRDM-IMXRT700 and FRDM-MCXN947T board support, KW43 ICS init-handshake fix, and MISRA compliance improvements.
  - eRPC Zephyr improvements, `CONFIG_ERPC_ENDPOINT_NAME` Kconfig option added;
  RPMsg-Lite set as default IPC service backend with multi-backend support.

#### Boot

- **RT1150 flashloader support** — NXP MCU bootloader updated with RT1150 flashloader
  support and SPI communication fix for RT1186.

#### Motor Control

- **FreeMASTER updated** — FreeMASTER tool updated for 26.09.00 release scope.
- **Motor control examples** — Overcurrent fault, encoder speed, and motor configuration
  fixes for HVP-MCXA346 PMSM encoder example; FRDM-MCXE32B appconfig path updated.

#### Safety

- **IEC 60730B safety library updated** — `safety_iec60730b` updated for 26.09.00
  release scope.

### New Platform / Device Support

| Device / Board          | Family      | Notes                                                        |
|-------------------------|-------------|--------------------------------------------------------------|
| MCXE327                 | MCX E-series | Full SDK enablement: device headers, Kconfig, startup, QSPI adaptation, errata ERR050705 and ERR052460 workarounds |
| MCXN556S (123-WLCSP)   | MCX N-series | New 123-ball WLCSP package variants: MCXN556TVAB, MCXN556TCAB, MCXN557TVAB, MCXN557TCAB |
| MCXN947T                | MCX N-series | New FRDM-MCXN947T board documentation, mcmgr/rpmsg-lite/eIQ support |
| MCXC352 / MCXC353       | MCX C-series | SVD files added; Keil flash loader updated with data flash and chip-erase support |
| MCXA556 / MCXA557 (WLCSP) | MCX A-series | WLCSP package SVD support added |
| i.MX RT2660             | i.MX RT     | Full public enablement: clock, power, eDMA, LLC, TRDC, USB, Neutron NPU firmware |
| i.MX RT1150 / RT1152    | i.MX RT     | RT1150 flashloader; FRDM-IMXRT1152 coex and MPP board support |
| i.MX 93 CA55 (MIMX9352) | i.MX        | AArch64 CA55 device files, startup, linker scripts, CMake/Kconfig |
| i.MX 95 CA55 (MIMX9596) | i.MX        | CA55 core definition, source code, and linker scripts        |
| i.MX 8M Mini CA53/CA55 (MIMX8MM6) | i.MX | Cortex-A53 core support files; multi-core device layer refactored |
| i.MX 943 V2X (MIMX94398) | i.MX       | ELE V2X firmware bring-up enabled; V2X FCE and base service drivers |
| KW43-LOC                | Wireless    | Flash support, documentation, antenna diversity, KW43-LOC board examples |
| MCXW70-LOC              | Wireless    | Flash support, documentation, release notes and getting-started pages |
| FRDM-MCXE32B            | MCX E-series | MDK flash programming fix for multicore; mcmgr/rpmsg-lite support |

---

## Enhancements

### Fundamental

- **Driver quality improvements (Coverity / CERT-C / MISRA)** — Systematic resolution of
  static-analysis findings across core peripheral drivers including NETC, USDHC, I3C,
  SCTimer, QSPI, RCM, LIN, LCDIC, Hiperface DSL, and eDMA. Fixes address CERT ARR30-C
  bounds violations, CERT INT30-C integer wraps, UNUSED_VALUE dead stores, and
  INCONSISTENT_UNION_ACCESS type-punning issues.
- **Include-guard macro standardization** — Leading underscores stripped from include-
  guard macros across all driver headers to comply with C reserved-identifier rules.
- **LPADC feature macro correction** — Feature macro renamed from
  `FSL_FEATURE_LPADC_ADC_TCTRL_COUNT` to `FSL_FEATURE_LPADC_TCTRL_COUNT` across RT,
  LPC, Kinetis, and Wireless device families.
- **eDMA unified driver migration** — `driver.edma4` references replaced with
  `driver.edma_unified` across i.MX 937, i.MX RT2660, and related device Kconfigs.
- **Kconfig edgefast_open centralization** — `edgefast_open` Kconfig is now sourced once
  from the top-level `Kconfig.mcuxpresso` instead of per-example, eliminating duplicate
  sourcing warnings.
- **Component quality fixes** — Coverity findings resolved in coredump, gen_hal,
  flash_nand_semc, flash_nor_spifi, UART DMA, I3C, RPMsg, and string formatter
  components.
- **Wi-Fi TX power table improvements** — Per-region compressed TX power tables added for
  AzureWave, Murata 1XK, Murata 2EL, Quectel, SD8978, and SD9177 modules; 40 MHz
  support on 2.4 GHz band edge channels for Murata 2EL.
- **CMSIS LPSPI driver improvements** — Instance configuration extracted outside
  functions; additional peripheral instances configured; build issue fixed.
- **SVD file updates** — SVD files refreshed for MCXN, MCXC, MCXA, MCXE32, RT1150,
  KW43/MCXW70 (CRR 1.41/1.42).
- **Documentation search and navigation** — Pagefind search integrated; shared topic
  deduplication across board getting-started guides; documentation URL path corrections.

### Device Support

- **i.MX RT2660 clock driver** — Clock root shutdown during reconfiguration, clock root
  and gate index validation, new `CLOCK_MeasureRootClockFreq()` and
  `CLOCK_MeasureClockSourceFreq()` APIs, USB FS clock configuration improvements.
- **i.MX RT2660 power driver** — `POWER_Init` renamed to `POWER_SetPolicy`; topology
  config renamed to handshake routing; `POWER_ApplyWakeupSources` made public.
- **i.MX RT2660 LLC configuration** — Cache topology and physical-memory alias metadata
  exposed for the generic LLC driver.
- **i.MX RT DSP Xtensa core update** — Default `XTENSA_CORE` updated to `RJ26_6_newlib`
  for RT500 FusionF1, RT600 HiFi4, and RT700 HiFi1/HiFi4 variants.
- **RT700 DSP_Init reset fix** — `DSP_Init()` now asserts the HiFi1 reset before
  releasing it, preventing stale state from the always-on SENSE power domain.
- **i.MX RT FRO tuner rework** — `CLOCK_TrimUsbFroClock` replaced with
  `CLOCK_EnableFroTuner` using per-reference parameter tables for improved accuracy.
- **ARM PLL postDiv=3 fix** — Corrected ARM PLL post-divider value for `POST_DIV_SEL=0b11`
  (should be ÷1, not ÷8) on affected i.MX RT devices.
- **MCXL20 power driver** — `Power_LowPowerBoot()` updated with reset-reason check;
  `Power_ApplyDcdcMainDriveErrata053099()` added for PMU ERR053099 DCDC workaround;
  VDD CORE main trim low-power read functions added.
- **MCXW70 clock driver** — Updated per rev.1 Reference Manual with implementation
  corrections and missing features; KW43B43ZC7 clock driver similarly updated.
- **KW43 GCC AlwaysOnData section placement** — Linker script corrected to properly
  place `.AlwaysOnData.init` and related sections in GCC builds.
- **RW61x GDET disableCount fix** — PM3 entry failure no longer corrupts the GDET
  sensor context `disableCount`, preventing subsequent GDET disable/enable imbalance.
- **i.MX 8M Mini SDMA clock array** — `SDMA_CLOCKS` made 1-based to match instance
  indexing; NonCacheable region moved out of read-only MPU region.
- **i.MX 952 XSPI DDR mode** — DDR mode support added with improved DLL reference
  counter and autoupdate resolution settings.
- **MCXE32x errata ERR052460** — Startup file workaround added for MCXE31/MCXE32.
- **MCXN947T TF-M ROM API** — Bug fix for FSL driver fetch when TF-M ROM API Kconfig
  is disabled; Flash API proxy layer added for TF-M IOCTL service.

### Security

- **PSA CASPER ECDH acceleration** — CASPER hardware accelerator now supports ECDH key
  agreement; PSA entry points added in `psa_crypto_driver` and `mbedtls3x`.
- **SGI AES-192 key support** — AES-192 key size handling added to the SGI PSA driver,
  guarded by `MCUXCL_FEATURE_AES192`, for MCXW/KW platforms.
- **ELS_PKC device-header portability** — Hardcoded `MCXN947_cm33_core0.h` include
  replaced with `fsl_device_registers.h`; MCXN547 include path corrected.
- **Secure storage MDK compatibility** — `psa_status_t` typedef redefinition error with
  MDK compiler resolved; `MIN` macro redefinition guard added.
- **ELE session state tracking** — `ELE_TRACK_SESSION_STATE` made toggleable via Kconfig
  for KW45 platform.

### Connectivity & Wireless

- **Bluetooth host v1.10.23** — Updated with EATT/L2CAP storage size improvements,
  LE Power Control vendor HCI command, CS algorithm buffer alignment fix, and
  comprehensive CERT-C integer-overflow fixes in ranging service and connection manager.
- **BLE controller updates** — Link layer libraries updated with CS sniffer antenna
  switching fix, HW PCT rotation for IPT, GFSK clock enablement ordering fix, and
  HADM antenna diversity improvements.
- **XCVR NBU library updates** — Multiple NBU library refreshes with MISRA/CERT-C
  static-analysis fixes for overflow and type-casting issues.
- **IEEE 802.15.4 updates** — SW Rx address filtering for Multipurpose frames added;
  MCXW72 MAC single-instance configuration; device filtering fix for blacklist-only
  configuration.
- **Connectivity framework v7.4.3** — CERT-C/MISRA fixes across OTA, FSCI, SecLib,
  SFC, ICS, NVM, and LowPower modules; NBU fault/assert state preservation; TSTMR
  56-bit timestamp fix; RW61x RTOS heap exhaustion fix on repeated BT init.
- **lwIP TLS/HTTPS fixes** — `altcp_tls` RX window stall on large TLS records fixed;
  client TLS config auto-free on dealloc corrected; RNDIS/CDC-ECM buffer bounds hardened.
- **USB host stack security** — Descriptor length and bounds validation added across
  audio, CDC, video, PHDC, MSC, MTP, and CCID class drivers; RNDIS message builder
  buffer bounds fixed; CCID bulk-out integer overflow fixed.
- **wpa_supplicant-rtos** — Network selection based on reliability added; uAP EAP
  SIM/AKA memory leak fixed; early STA removal due to missing DEAUTH_TX_STATUS fixed;
  EAP-WSC source files guarded with preprocessor conditionals.
- **Wi-Fi driver stability** — Multiple fixes: RSN IE out-of-bounds HardFault, CMD 0x24
  response timeout hang during WPA3 SAE, uAP channel 165 start failure, roaming state
  leak, power-save mode RRM beacon handling, wowlan STA+UAP coexistence.
- **IW612 default module update** — Default Wi-Fi module updated to IW612 for RT boards;
  IW610 2LL set as default for FRDM-MCXN947, FRDM-MCXN947T, MCXNxxEVK boards.
- **edgefast_open L2CAP race condition** — BR/EDR config response race condition fixed;
  channel state transition moved to config-response-sent callback.

### ML / DSP / Multimedia

- **OpenVG stability** — Multiple Coverity fixes: null pointer dereference guards,
  signed-to-unsigned cast guards, overflow guards; mutex pointer cleared after delete;
  vertical flip revert; EGL display free on OS_DestroyDisplay.
- **OpenH264 type consistency** — Fixed-width `uint32_t` used in public headers instead
  of `unsigned int` for cross-platform compatibility.
- **VGLite RT1150/RT1152 buffer address** — Starting address offset corrected for
  `tiled_freertos` example on RT1150 and RT1152.

### Filesystem

- **FatFS integer overflow fixes** — Sector+count bounds checks added in USB disk
  read/write; GET_SECTOR_SIZE ioctl signed-shift fixed; RAM disk pointer arithmetic
  cast to `size_t`.
- **LittleFS CERT INT30-C fix** — Unsigned wrap guards added in `lfs_mflash.c`.
- **SDMMC SD voltage switch** — Voltage switch workflow updated: DAT line low is
  retried multiple times after CMD11 for improved reliability.
- **SDMMC SDIO over SPI** — Added SDIO over SPI support.
- **SDMMC FreeRTOS** — Converted to use Kconfig generated FreeRTOSConfig_Gen.h.
   
### Multicore

- **RPMsg-Lite virtqueue NUL-termination** — `virtqueue_create[_static]` now
  NUL-terminates `vq_name` after `env_strncpy` to prevent potential overread.
- **MCMGR initialization guard** — All public MCMGR API functions now return
  `kStatus_MCMGR_NotReady` before `MCMGR_Init()` completes, preventing race conditions.

---

## Bug Fixes

### Fundamental

- **NETC EP_Down crash on errata path** — Fixed crash in `EP_Down()` when
  `FSL_FEATURE_NETC_HAS_ERRATA_050543` is active for pseudo Endpoint ports.
- **LPADC feature macro name** — Corrected `FSL_FEATURE_LPADC_ADC_TCTRL_COUNT` to
  `FSL_FEATURE_LPADC_TCTRL_COUNT` (affected LPADC trigger control count queries).
- **SCTimer Coverity ARR30-C** — Match-register indices decoded from event CTRL
  registers are now bounds-checked before use as `MATCH[]` subscripts.
- **QSPI MCXE327 RXBRD handling** — QSPI driver updated to read Rx data from ARDB on
  MCXE327 which lacks the RXBRD bitfield in the RBCT register.
- **DSC EVTG FORCE_BYPASS macro** — Mismatched parentheses in `EVTG_Init` fixed;
  flags cast to `uint16_t` to resolve CodeWarrior compiler errors.
- **RT2K PMU `PMU_ConfigLfro1M` removal** — Removed deleted API and associated struct
  that referenced a non-existent CCUPMHI FREERUN bitfield.
- **I3C driver Coverity unused value** — Dead assignment of `instance` variable in
  `I3C_MasterSetTxDMA` DDR branch removed.
- **i.MX 8M Mini QSPI read** — Fixed QSPI read issue on i.MX 8MQ: Rx buffer set to
  RBDR instead of default ARDB for IP read operations.
- **RT1180 NVIC_SystemReset include-order hazard** — Include-order dependency in
  `system_MIMXRT*_cmXX.h` headers that could silently override `NVIC_SystemReset()`
  resolved.
- **MCXE32x MDK flash programming** — Keil uVision CMSIS-DAP multicore flash
  programming fixed; MDK CPU identifier corrected.
- **MCXW70 EMVSIM TX_CNT mask** — `EMVSIM_TX_STATUS_TX_CNT_MASK` corrected from 4-bit
  to 5-bit width per design confirmation.
- **MCXN947/MCXN236 clock Coverity** — Dead `mMult` initializer removed from
  `findPllMMult()` and related functions across MCX, LPC, and RT device families.
- **RT2660 TRDC MEDIA master mapping** — MEDIA-domain master table corrected to match
  the RT2660 reference-manual master-assignment table (was missing entries).
- **RT2660 InputMux/clock connections** — Wrong `main_freq` and `comm_freq` connections
  corrected; USB taps and FREQEAS TAR 21 added for `comm_freq`.
- **RT2660 linker file typo** — Typo in GCC linker file corrected; `__heap_noncacheable__`
  symbol now works correctly.
- **RT2660 USBPHY DCD** — Disabled `FSL_FEATURE_USBPHY_HAS_DCD_ANALOG` macro re-enabled
  to fix DCD analog module recognition on mimxrt2660evk.
- **KW43 IAR startup vector table** — `m_image_length` restored in IAR vector table
  at offset 0x20 after incorrect removal.
- **KW43 AHB timeout** — CPU1 AHB timeout counter increased from 2 to 3 cycles to fix
  HardFault observed on NBU when accessing TSTMR.
- **KW43 CTCM1 ECC initialization** — Removed incorrect ECC RAM initialization of
  CTCM1 (which does not support ECC) in KW47/MCXW72 startup.
- **TrustZone NSC veneer hardening** — NSC veneer functions hardened against
  TrustZone-M confused-deputy attacks (Arm PSIRT ARMSEC-559, NXP PSIRT).
- **MCXC data flash Keil flashloader** — Data flash range (0x1c000–0x1ffff, 16 KB)
  added to Keil flashloader for MCXC devices.
- **MCXN556S ROM API context** — Undersized reserved field in `api_core_context_t`
  fixed to match the 512-byte `flexspi_nor_config_t`-sized slot expected by ROM API_Init.

### Security

- **SGI CCM tampered multipart AEAD** — Tampered multipart AEAD CCM decrypt now
  correctly rejected; CCM context initialized in `sgi_aead_set_nonce()` instead of
  deferred to `sgi_aead_update_ad()`.
- **SGI oversized key rejection** — Raw HMAC keys exceeding `PSA_MAX_KEY_BITS` now
  rejected on SGI import (previously accepted up to 65536 bits).
- **Secure storage MDK `psa_status_t` redefinition** — Typedef conflict between
  `mbedtls3x` PSA Crypto and `secure_storage` headers resolved.
- **ELS_PKC MCXN547 include path** — Missing MCXN947 drivers include path for MCXN547
  added to `McuxElsPkc` CMake target.

### Connectivity & Wireless

- **Wi-Fi RSN IE OOB HardFault** — Out-of-bounds memory access in `process_rsn_ie()`
  triggered by malformed RSN IE after wlan-reset fixed.
- **Wi-Fi CMD 0x24 hang** — Host hang on CMD 0x24 DEAUTHENTICATE response timeout
  during WPA3 SAE handshake when `wlan_reset()` is called shortly after connect fixed.
- **Wi-Fi uAP channel 165** — uAP start failure on channel 165 with WPA supplicant
  fixed by correcting secondary channel offset in embedded supplicant path.
- **Wi-Fi power save RRM** — Wi-Fi ceasing to function during power save mode when
  receiving 802.11k RRM Beacon Request targeting 5 GHz channel fixed.
- **Wi-Fi wowlan STA+UAP** — WoWLAN failed to wake host when STA and UAP coexist fixed.
- **Wi-Fi enterprise cert memory leak** — Memory leak of enterprise certificate on
  `wlan-reset` with opaque keys fixed.
- **Wi-Fi roaming state leak** — Roaming state not reset when neighbor list report
  arrives in IDLE state fixed.
- **wpa_supplicant early STA removal** — STA removed too early due to missing
  `DEAUTH_TX_STATUS` flag fixed.
- **Coex PM3 hang** — UART entering PM3 causing coex hang fixed; LPUART DMA cache
  coherency issue on evkbmimxrt1170 resolved.
- **edgefast_open audio frame length** — Incorrect audio frame length for 88W8987
  modules on evkmimxrt595 corrected.
- **LIN slave no output** — LIN stack slave example produced no serial output on
  FRDM-KW43 and FRDM-MCXW70 due to FRO HF div not enabled before clock source
  selection; fixed.
- **Connectivity framework HCI packet length** — HCI RX/TX length checks incorrectly
  clamped to 255 bytes (UINT8_MAX) by MCSE-1743, rejecting valid HCI/ACL packets;
  corrected.
- **RW61x RTOS heap exhaustion** — Heap space exhaustion when performing repeated
  `bt init → bt disable` cycles on RW61x fixed.

### Filesystem

- **FatFS USB disk sector wrap** — Sector+index wrap in USB disk read/write guarded
  against integer overflow.
- **SDMMC CMD53 multiblock read** — Stop command no longer sent for CMD53 multiblock
  read (fixed block count); SPI zippack build error fixed.

### Boot

- **MCUboot PSA Crypto init** — PSA Crypto initialization issue in MCUboot fixed.
- **MCUboot `boot_copy_region_pre_hook`** — Prototype reworked to use bootloader state
  only; implementation adjusted in `bootutil_hooks.c`.
- **RT1186 SPI flashloader** — Communication failure with RT1186 flashloader via SPI
  fixed.
- **RT117x fuse write on macOS** — Fuses not correctly written on macOS fixed.

### Multicore

- **MCMGR KW43 ICS init-handshake hang** — `MCMGR_CHECK_INIT()` returning
  `kStatus_MCMGR_NotReady` during `MCMGR_Init()` caused KW43 ICS init-handshake to
  hang; fixed with correct initialization ordering.
- **MCMGR CERT EXP33-C** — Uninitialized `target_core` variable in all mcmgr platform
  files fixed.
- **RPMsg-Lite IMU_Deinit guard** — `IMU_Deinit` in `platform_deinit` now guarded with
  `RL_USE_MCMGR_IPC_ISR_HANDLER` to prevent double-deinit when MCMGR owns the IMU link.

### ML / DSP / Multimedia

- **Ethos-U IAR release mode hang** — Ethos-U driver hang in IAR release mode on
  i.MX RT700E (imxrtl375) fixed.
- **XAF FRDM-IMXRT700 codec I2C routing** — Codec I2C routing fix propagated to
  `xaf_playback`, `xaf_record`, and `xaf_usb_demo` CM33 core0 ports.

---

## Breaking Changes

| # | Description | Impact | Required Action |
|---|-------------|--------|-----------------|
| 1 | **`edgefast_bt_ble` (EtherMind Bluetooth stack) removed** | Applications using the legacy `edgefast_bt_ble` middleware component will fail to build after updating to 26.09.00. | Migrate to `edgefast_open`. The `edgefast_open` repository provides a unified Bluetooth stack with equivalent functionality. Update CMakeLists.txt, Kconfig, and include paths accordingly. Refer to the EdgeFast Open migration guide in the SDK documentation. |
| 2 | **`POWER_Init` renamed to `POWER_SetPolicy` on i.MX RT2660** | Code calling `POWER_Init()` or `POWER_GetDefaultInitConfig()` on RT2660 will not compile. | Replace `POWER_Init()` with `POWER_SetPolicy()` and `POWER_GetDefaultInitConfig()` with `POWER_GetDefaultPolicyConfig()`. |
| 3 | **`PMU_ConfigLfro1M` API removed on RT2K** | Code calling `PMU_ConfigLfro1M()` or referencing `pmu_lfro1m_config_t` will not compile. | Remove calls to `PMU_ConfigLfro1M()`. The LFRO 1M configuration is no longer supported via this API. |
| 4 | **`edma4` Kconfig replaced by `edma_unified` on i.MX 937 and RT2660** | Projects selecting `MCUX_COMPONENT_driver.edma4` on i.MX 937 or RT2660 will not resolve the eDMA driver. | Replace `MCUX_COMPONENT_driver.edma4` with `MCUX_COMPONENT_driver.edma_unified` in project Kconfig or CMakeLists.txt. |
| 5 | **TF-PSA-Crypto updated to v1.2.0 (removes `ecp_curves_new.c`)** | Projects with explicit CMake references to `drivers/builtin/src/ecp_curves_new.c` will fail to build. | Remove the explicit reference; the file was removed upstream in v1.2.0. The `psa_crypto_driver` CMake has been updated accordingly. |
| 6 | **MCXW70AA part number removed** | Any project or configuration referencing the `MCXW70AA` part number will not find a matching device definition. | Use the remaining MCXW70 part numbers. `MCXW70AA` is no longer a productized part number. |

---

## Known Issues

- **IAR Embedded Workbench 9.70.4 on FRDM-IMXRT700** — When using IAR Embedded
  Workbench for Arm 9.70.4 with the FRDM-IMXRT700 board, users must install a patch
  from IAR. Refer to the FRDM-IMXRT700 release notes known issues section in the SDK
  documentation for the download link.
- **`cube_freertos` IAR build disabled on FRDM-IMXRT700** — The IAR debug/release
  configurations for `cube_freertos` on `frdmimxrt700@cm33_core0` are disabled in this
  release as the example did not reach quality targets. GCC and MDK builds are unaffected.
- **FRDM-MCXA287 / FRDM-MCXA577 `hello_world_qspi_xip` ISP programming** — Programming
  via blhost ISP may fail or leave the device in an unresponsive state if CMPA/ISP
  configuration is not cleared first. A debug-mailbox mass-erase step is required before
  ISP programming. Refer to the example documentation for the updated programming sequence.
- **FRDM-MCXN947T `mcxn_encrypted_xip`** — The encrypted XIP build project for
  FRDM-MCXN947T depends on the SEC tool and is disabled in this release. It will be
  re-enabled in a future release.
- **edgefast_open K32W061 transceiver** — K32W061 transceiver support has been removed
  from `evkmimxrt595`, `evkmimxrt685`, and `evkbimxrt1050` EdgeFast Open examples.
  Applications requiring K32W061 on these boards should use the previous release or
  contact NXP support.
- **MCUXpresso IDE toolchain** — MCUXpresso IDE toolchain support has been removed from
  wireless board examples. Use IAR, Keil MDK, or ARMGCC for wireless examples.

---

## Toolchain & Environment Support

The following toolchain versions are documented for this release. Version information is
transcribed from the `release/26.09.00` branch of `mcu-sdk-doc`; label as
**"Documented for this release"**.

| Toolchain                          | Version        | Notes                                                        |
|------------------------------------|----------------|--------------------------------------------------------------|
| MCUXpresso for VS Code       | v26.09 | Default toolchain for all device families. Refer to SDK Getting Started guide for the recommended version. |
| Arm GNU Toolchain (armgcc)         | 14.2.x |  |
| IAR Embedded Workbench for Arm     | 9.70.4         | Patch required for FRDM-IMXRT700. See Known Issues.          |
| Keil MDK (µVision)                 | 5.43a | Supported for MCX, Kinetis, LPC, and i.MX RT families.      |
| Xtensa C/C++ Compiler (XCC)        | RJ2026_6       | Required for DSP examples on RT500, RT600, RT700, i.MX 8ULP. Updated in this release. |
| MCUXpresso IDE                     |25.06.xx | Removed from wireless board examples in this release. |

> **Note:** Firm toolchain version numbers for armgcc and Keil MDK could not be verified
> from the available commit log. Refer to the SDK documentation
> (`mcuxsdk/docs/release/commonrn/topics/development_tools_*.md`) on the
> `release/26.09.00` branch for the authoritative toolchain matrix.

---

## Final Release Summary

MCUXpresso SDK 26.09.00 (September 2026, implied) represents a significant quarterly
advancement across the full breadth of the NXP MCUXpresso SDK ecosystem. This release
delivers production-ready support for the i.MX RT2660 SoC, full enablement of the MCXE327
MCU, and expanded Cortex-A core support for i.MX 93, i.MX 95, and i.MX 8M Mini devices.
The security posture of the SDK is substantially strengthened through the upgrade to
Mbed TLS 4.2.0 (LTS) and 3.6.7, ELS_PKC v5.0.0, SGI_PKC v4.3.0 with PQC add-on, and
comprehensive hardening of USB host class drivers and PSA crypto drivers against
malformed-input attacks. The wireless ecosystem benefits from refreshed Wi-Fi firmware
across all supported modules, Bluetooth host v1.10.23, the completed migration to the
unified `edgefast_open` Bluetooth stack, and the addition of the MSTP library for BACnet
connectivity. On the ML/AI front, ExecuTorch v1.4.1 with Neutron SDK 3.2.2 and MPP v4.4.0
bring expanded model support and new board enablement. MCUboot v2.4.0 adds OTFAD encrypted
XIP for i.MX RT1152/1160/1170. Across all functional areas, this release incorporates
extensive CERT-C, MISRA, and Coverity quality improvements, making 26.09.00 a high-quality
foundation for production embedded software development on NXP MCU and MPU platforms.
