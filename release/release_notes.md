## Overview

MCUXpresso SDK 26.12.00-pvw1 is the first preview of the December 2026 release. It adds:

- New device and platform enablement, and much wider i.MX RT2660 ecosystem support.
- A unified ELE S1xx/S4xx PSA crypto driver.
- Bluetooth LE Channel Sounding upgrades.
- FreeRTOS-Kernel V11.3.1.
- Security hardening across drivers, middleware and examples.

This release spans **68 updated sub-repositories**, **0 newly added components**, and **0 removed components** relative to the 26.09.00 baseline. Key themes include:

- **New silicon support:**
  - MIMX8ML8 Cortex-A53 core, new RT1184 parts, and MCXA577VAPR / MCXA287VAPR / MCXA286VAPR (80-pin WLCSP).
  - RW610FML (FRDM-RW610FML), KW43 multicore, and MCXC352/353 in the public device repository.
  - SVD files for RT2660, RT1184 and MCXC454.
- **Security upgrades:**
  - The unified ELE S1xx/S4xx PSA driver now covers ELE S100.
  - HSEB opaque AES ciphers.
  - EdgeLock 2GO agent v6.5.2 on TF-M 2.3.
  - EdgeLock V2X FCE AES-CBC/HMAC/SHA-2.
- **Wireless:**
  - Wi-Fi firmware: IW612 18.99.8.p150, IW416 16.92.21.p168, 88W8987 16.92.21.p156.4, IW610/RW610 p150.
  - Stacks: Wi-Fi driver v1.3.r49.p12, Bluetooth LE Host v1.10.24, Connectivity Framework v7.5.1.
  - About 37 EdgeFast Bluetooth examples plus LE Audio on MIMXRT2660-EVK.
- **ML / AI:** Ethos-U85 support for i.MX RTL375, ExecuTorch large-model PSRAM loading, and Cortex-M85 audio codec libraries.
- **RTOS:** FreeRTOS-Kernel updated to V11.3.1, with Armv8-M SMP and the new `xTaskPeriodicDelay()` API.
- **Boot:** MCUboot adds FRDM-RW610FML support (serial recovery, encrypted XIP) and moves to IPED contexts 14/15.
- **Toolchain:** New `west blobs` command, Kconfig control of hex/bin output, and a `--gdb-init` runner option.

## Release Highlights

1. **New Device Enablement** — MIMX8ML8 Cortex-A53 core with a per-core device layout, and new RT1184 parts with an internal-flash flashloader. Also added: the MCXA577VAPR/MCXA287VAPR/MCXA286VAPR WLCSP80 parts, RW610FML (including TF-M and MCUboot ports) and KW43 multicore. MCXC352/MCXC353 move to the public device repository.

2. **i.MX RT2660 Ecosystem Expansion** —
   - **Power:** a reworked power driver adds `POWER_Init`, `POWER_EnterRunMode` and `POWER_EnterLowPowerMode`, PMIC-independent regulator hooks and OTP body-bias trim. A new Power Manager port covers WFI through Deep Power Down, with a `power_manager_test` demo.
   - **Examples:** Maestro audio, USB low-power/OTG, MbedTLS 4.x PSA, and a DCIF camera-to-display demo with no frame-buffer copy.
   - **Bluetooth:** about 37 EdgeFast Bluetooth examples and a full LE Audio suite.

3. **Bluetooth LE Channel Sounding Upgrades** —
   - **Inline PCT Transfer (IPT)** on KW43 (multi-antenna) and KW47 (1x1).
   - **Antenna handling:** hardware RX phase compensation, runtime antenna configuration, and Bluetooth 6.3 CS-SYNC antenna selection.
   - **Accuracy:** a double phase correction is removed, fixing a ≈0.5 m distance error.
   - **Handover:** a GAP central using Channel Sounding can now take part in connection handover.

   Bluetooth LE Host is updated to v1.10.24.

4. **Unified ELE S1xx/S4xx PSA Crypto Driver** — One driver now supports ELE S100 and ELE S400 across `psa_crypto_driver`, `mbedtls3x` and `tf-psa-crypto`. It is enabled by default when Mbed TLS or TF-PSA-Crypto is used. HSEB adds opaque AES ciphers, key-store hardening, and re-sync of the NVM key catalog after power-on reset.

5. **FreeRTOS-Kernel V11.3.1** — SMP on all Armv8-M ports, new `xTaskPeriodicDelay()` and `uxTaskCallForEachTask()` APIs, and new Cortex-M52, Cortex-R82 and Arm China STAR-MC3 ports. Also hardens the TrustZone secure context and MPU privilege checks.

6. **Multi-Core Console over a Single UART** — The new `serial_mux` component and HAL UART `muxuart` adapter carry several logical console/data channels over one physical UART. The `console_mux` demo and PC host tools are provided for i.MX943 EVK.

7. **EdgeLock V2X FCE Crypto Services** — `v2x_fce` adds AES-CBC, HMAC generate/verify and SHA-256/384/512, with zero-copy buffers and linker-placed scratch memory. New `v2x_fce_hash`, `v2x_fce_aes_cbc` and `v2x_fce_hmac` examples ship for i.MX943 EVK.

8. **USB, lwIP and Wi-Fi Security Hardening** — These fixes protect devices from malicious USB hosts/devices, PD partners and APs:
   - **USB:** bounded parsing for USB-PD (PTN5110) extended messages and vendor VDMs, and for RNDIS, MTP, CCID, MSC and hub descriptors.
   - **lwIP:** fixes for USB-Ethernet pbuf overflow and ENET QoS TX overflow.
   - **Wi-Fi:** hardened parsing of malformed RSN IE, HE Capability IE and RX A-MSDU.

9. **Bluetooth LE and HAL Security Fixes** —
   - **Bluetooth LE:** new forced re-pairing (BLERP) mitigation.
   - **Timer HAL:** handle-size overflow on 64-bit cores fixed (reported through NXP PSIRT).
   - **Other overflows:** fixed in RPMsg-Lite name-service, 802.15.4 FSCI beacon handling and EtherCAT.

10. **Connectivity Framework v7.5.1** — New Device Manager (DEVMGR) APIs give one interface for BD/802.15.4 addresses and crystal trims. Also new: KW43/MCXW70 low-power enablement, an NCO32K clock on the NBU, a MIMXRT685S low-power platform layer, and PSA-based `SecLib_HMAC_SHA256`.

11. **Reliable Multicore Event Delivery** — MCMGR now queues forced MU events instead of overwriting unread messages, and the queue depth is configurable. This fixes silently lost RPMsg doorbells on RT1160/1170/1180, RT700, K32L3A6, KW43B43, MCXW70, MCXL20 and MCXE32B.

12. **Security Updates for TrustZone-M NSC Veneers**
  - TrustZone-M NSC veneer hardening** - Improper handling of non-secure-world input in NSC veneer functions of NXP MCUXpresso SDK TrustZone-M examples (trustzone_examples), affecting versions through 26.06.00-lts and 26.09.00-pvw2, may allow a non-secure caller to supply unvalidated pointers or untrusted data, causing a timing side-channel, TOCTOU condition, or format-string misuse, potentially resulting in secure-world memory disclosure or denial of service. All software versions starting from 26.06.01-lts and 26.09.00 have fixed this issue. 

    *Acknowledgment: NXP would like to thank Tijs Bellefroid, Antonis Louka, Marton Bognar, and Jo Van Bulck (DistriNet, KU Leuven) for the responsible disclosure.*

  - **RPMsg-Lite TrustZone-M NSC veneer input validation** - Improper input validation in non-secure-callable (NSC) veneer functions of the NXP MCUXpresso SDK rpmsg-lite multicore example (multicore_examples/rpmsg_lite_pingpong_tzm) up to releases 26.06.00-lts and 26.09.00 may allow a non-secure caller to supply unvalidated pointers and size values, potentially resulting in disclosure of secure-world memory to the non-secure domain, or denial of service. All software versions starting from 26.06.01-lts and 26.12.00-pvw1 have fixed this issue. 

    *Acknowledgment: NXP would like to thank Tijs Bellefroid, Antonis Louka, Marton Bognar, and Jo Van Bulck (DistriNet, KU Leuven) for the responsible disclosure.*

  - **TF-M Initial Attestation SHA-384 Hash Label Correction** - Corrected a logic error in the TF-M Initial Attestation component that could cause valid SHA-384 measurement hashes to be rejected during attestation verification. The fix has been backported from upstream TF-M. The affected code path is disabled by default and is not used in standard NXP TF-M example applications.

    *Acknowledgment: NXP would like to thank Siril Ganjai and Ajesh Koyatan Chathoth for the responsible disclosure.*

## Manifest & Repository Changes

### Summary

| Category  | Count |
|-----------|------:|
| Changed   | 68    |
| Added     | 0     |
| Removed   | 0     |

### Added Repositories

No repositories were added in this release.

### Removed Repositories

No repositories were removed in this release.

### Impact on `west update`

Running `west update` against `release/26.12.00-pvw1` fetches updated revisions for all 68 changed repositories. The project list is unchanged, so no repositories are newly cloned or dropped, and existing group filters keep working. The new `west blobs` command can now manage out-of-tree prebuilt binaries; if a build reports a missing prebuilt library after updating, run `west blobs fetch`.

---

What's New
----------

### New Features

#### Fundamental

- **Multi-core serial multiplexer (`serial_mux`)** — New component that carries several logical console/data channels over one physical UART. It uses COBS framing and cache-coherent shared-memory rings, with the layout set in Kconfig.
- **HAL UART `muxuart` adapter** — New client-only adapter that routes `HAL_Uart*` calls through `serial_mux`. Cores without a physical UART can then use the standard debug console.
- **EdgeLock V2X FCE AES-CBC / HMAC / SHA-2** — `v2x_fce` adds AES-CBC encrypt/decrypt, HMAC generate/verify and SHA-256/384/512. Caller buffers are passed straight through, TCM addresses are translated automatically, and the linker places the scratch memory.
- **DualADC direct result access and DMA** — New `DUALADC_GetConversionResult32/Low/High()` read A-side and B-side results directly, and new `enableDmaA`/`enableDmaB` fields set up DMA in `DUALADC_Init()`.
- **GPIO per-pin interrupt callbacks** — New handle-based API (`GPIO_CreateHandle`, `GPIO_SetPinCallback`, `GPIO_ClearPinCallback`) with a shared IRQ dispatcher, so applications no longer need their own dispatch code.
- **PINT multi-instance support** — The driver handles several PINT/SECPINT instances with different interrupt counts. `PINT_USE_LEGACY_CALLBACK` still works.
- **I3C driver for DSC MC56F85000** — New I3C driver ported from the mainline driver. Its overflow checks avoid 64-bit types, so it builds with CodeWarrior.
- **I3C underrun reporting and extended read-terminate (RT2660)** — Under-run errors are reported as `kStatus_I3C_UnderrunError`, and read-terminate sizes go up to 2047 bytes.
- **PWM trigger stretch prescaler** — New `PWM_SetTriggerStretchPrescaler()` sets the trigger stretch count prescaler (x1/x2/x4/x8).
- **SPC single-write regulator control** — New `SPC_EnableRegulators()`/`SPC_DisableRegulators()` set the Core LDO, System LDO and DCDC in one `CNTRL` write. This is required on KW45/KW47-class devices.
- **FlexIO timer-status DMA** — New `FLEXIO_EnableTimerStatusDMA()` enables or disables timer-status DMA requests.
- **Compile-time assertion macro** — New portable `MCUX_BUILD_ASSERT(cond, msg)` in `fsl_common.h`.
- **`west blobs` command** — New West extension to fetch, check, list, update and regenerate out-of-tree prebuilt SDK binaries.
- **Hex/Bin build output control** — New Kconfig options `MCUX_BUILD_OUTPUT_HEX` (default `y`) and `MCUX_BUILD_OUTPUT_BIN` (default `n`). `.bin` conversion now works on every toolchain, and `runners.yaml` lists only the artifacts that are actually built.
- **`--gdb-init` runner option** — Adds custom GDB commands to `west debug` / `west attach` for J-Link and LinkServer. The commands run after the runner's final reset.
- **`ram_only` / `psram_only` build targets** — New build targets with matching linker files, first enabled for `hello_world` on MIMXRT2660-EVK.
- **Power Manager RT2660 port** — Power Manager supports MIMXRT2660/2661/2662/2663 in WFI, Sleep, Deep Sleep, Power Down and Deep Power Down.
- **RW610FML component support** — Wi-Fi/BT module, mflash and an MDK toolchain template for FRDM-RW610FML.
- **New V2X/FCE crypto examples** — `v2x_fce_hash`, `v2x_fce_aes_cbc` and `v2x_fce_hmac` for i.MX943 EVK (cm33_core1, cm7_core0, cm7_core1), checked against NIST/RFC known-answer vectors.
- **`console_mux` demo and host tools** — Runs the consoles of all three i.MX943 cores over a single UART. Ships with PC host tools: virtual serial ports, a Linux PTY hub, a GUI terminal and a loopback self-test.
- **TrustZone examples for RT1180 family** — `secure_faults_trdc` and TrustZone `hello_world` for FRDM-IMXRT1186 and EVK-RT1180.
- **MIMXRT2660-EVK example expansion** — New examples and board support:
  - Maestro playback, record, usb_mic and usb_speaker.
  - `power_manager_test`.
  - USB suspend/resume, LPM and OTG pin-detect examples.
  - DCIF PDI camera-to-display demo.
  - IO expander and MbedTLS 4.x PSA examples.
  - Board support for the W35T51NW octal flash, uSDHC boot headers and an optional PF9453 PMIC supply (`MCUX_BOARD_USE_PF9453`).
- **Additional board/example enablement** —
  - `freertos_hello` on the evkmimx8mp Cortex-A53 core.
  - `openvg_tiger_freertos` on FRDM-IMXRT1152.
  - Coex A2DP sink/source on EVKB-MIMXRT1170.
  - MCUXpresso IDE support for coex examples on RT1170/RT1060.
  - Wi-Fi host-sleep with WoWLAN wake on FRDM-IMXRT700.
- **SVD files for new devices** — New SVDs for RT2660, RT1184, MCXC454 and the MCXA286VAPR/MCXA287VAPR WLCSP80 parts.

#### Device Support

- **MIMX8ML8 Cortex-A53 support** — Cortex-A53 headers, system and startup files, and a DDR linker script are added. The device configuration is split per core (Cortex-M7 + Cortex-A53).
- **RT2660 power APIs** — New `POWER_Init`, `POWER_EnterRunMode` and `POWER_EnterLowPowerMode` for explicit power-mode transitions. Boards register an external-regulator hook (`power_ext_regulator_hooks_t`) for core-voltage scaling.
- **RT2660 OTP body-bias trim** — FBB N-well/P-well codes are read from fuses, with a reference fallback when the fuses are blank. This is opt-in through `PMU_DRIVER_UPDATE_TRIM_VALUE`.
- **RT1184 internal-flash flashloader** — Flashloader added for RT1184 internal flash, and the RT1183 linker flash window updated.
- **KW43 multicore** — Multicore support is enabled on KW43.
- **OSTIMER 32 kHz clock source (MCX)** — New `kCLK_32K_to_OSTIMER`; `CLOCK_GetOstimerClkFreq()` reports the frequency correctly.

#### Security

- **ELE S100 support through the reworked S1xx/S4xx driver** — One PSA driver covers ELE S100 and S400 and is enabled by default with Mbed TLS or TF-PSA-Crypto. The Mbed TLS 4 wrappers follow the updated PSA driver API.
- **HSEB opaque AES ciphers** — Opaque-key AES cipher support, using the same handle model as the asymmetric driver. Matching cipher wrappers are added in `mbedtls3x` and an opaque cipher context in `tf-psa-crypto`.
- **HSEB NVM key sync after power-on reset** — The runtime key catalog is rebuilt from the internal NVM key store after a power-on reset.
- **SGI/PKC session helpers** — New `mcux_psa_sgi_session_helper.h` macros make sure the mutex is released and the session destroyed on every error path.
- **EdgeLock 2GO agent v6.5.2** — The agent is upgraded to v6.5.2, and EL2GO applications now build and run on TF-M 2.3.
- **Opaque keys in `el2go_csr` on L20 / A2TS** — The CSR application can use hardware-protected opaque keys.
- **TF-M FRDM-RW610FML platform** — New TF-M platform port based on FRDM-RW612, with a flash driver shared by RW610 and RW612.
- **ELE HSEB firmware for MCXE327** — EdgeLock HSEB firmware binaries added for MCXE327.

#### Connectivity & Wireless

- **Channel Sounding connection handover** — New `Gap_HandoverSetCsLlContextByConnHandle` lets a GAP central that uses Channel Sounding take part in connection handover.
- **Forced re-pairing (BLERP) mitigation** — The connection manager rejects pairing that would weaken an existing bond and reports a forced re-pairing security event.
- **Inline PCT Transfer (IPT)** — Enabled on KW43 (including multi-antenna) and on KW47 1x1 configurations.
- **Hardware RX phase compensation for CS** — Channel Sounding now uses hardware RX phase compensation.
- **Runtime CS antenna configuration** — `BLE_HADM_SetAntennaType()` also takes the antenna-path count and switch time (`t_sw`), and reported capabilities update at runtime.
- **Non-CS antenna switching APIs** — New controller APIs switch antennas outside Channel Sounding.
- **Localization data export and Anchor Monitor** — CDE distance results are added to the localization export, and the Anchor Monitor displays RSSI.
- **EdgeFast Bluetooth on MIMXRT2660-EVK** — About 37 BLE and Bluetooth Classic examples, including `wifi_cli_over_ble_wu`, with GCC/IAR targets and LittleFS settings storage.
- **LE Audio on MIMXRT2660-EVK** —
  - Broadcast and unicast media sender/receiver, including 4-BIS/4-CIS variants.
  - Call gateway and call terminal.
  - `ums_microphone`.
  - The `umr2bms` and `a2dp_bridge` bridges.
- **EdgeFast Bluetooth on FRDM-RW610 and EVK-MIMXRT685** — RW610 is enabled, and RT685 gets low-power HT examples with the Murata 2EL module.
- **Device Manager (DEVMGR) APIs** — One API for BD/802.15.4 addresses and 32 MHz/32 kHz trims across HwParameter, FFR and NMPA. It can also derive an address from the UID or generate a random one, and a CFPA backend is provided on KW43/MCXW70.
- **KW43/MCXW70 low-power enablement** — Connectivity Framework support for KW43/MCXW70:
  - Build support.
  - LPTMR wake-up sources.
  - SRAM retention map.
  - SPC trims.
  - NCO32K clock source on the NBU.
- **MIMXRT685S low-power platform layer** — New Connectivity Framework platform module with an OSTIMER timestamp and Power Manager integration.
- **`SecLib_HMAC_SHA256` on PSA** — HMAC-SHA256 through the PSA API, hardware-accelerated where available.
- **Pluggable fault-report output** — New `FWK_FaultHandlerSetOutput()` sends fault dumps to a coredump port or any other output.
- **Wi-Fi gateway probe on same-SSID roaming** — After a same-SSID roam, the driver ARP-probes the gateway and re-runs DHCP if needed, so IP connectivity is kept.
- **Wi-Fi external antenna gain in 0.25 dB steps** — `wlan-set-ant-gain` accepts [-127, 127], which is -31.75 to +31.75 dBi.
- **Wi-Fi worldwide Tx power default and country CLI** — The worldwide table is used when no region matches. `wlan-set-country` is now available on SD9177 (IW611/IW612) and SD8978.
- **MII support in MCX ENET USB adapter** — New `EXAMPLE_PHY_INTERFACE_MII` option, and the adapter MAC address can be overridden.

#### ML / DSP / Multimedia

- **Cortex-M85 audio codec libraries** — AAC, FLAC, MP3, WAV and SSRC prebuilt libraries for Cortex-M85 (armgcc, IAR), selectable in Maestro on Cortex-M85 cores.
- **Ethos-U85 support for i.MX RTL375** — Ethos-U85 NPU components support IMXRTL3759MCA.
- **ExecuTorch large-model support** — The model runner copies large models from PSRAM into SRAM and loads bytecode and weights with eDMA.

#### RTOS

- **FreeRTOS-Kernel V11.3.1** — The NXP kernel moves to upstream V11.3.1.
- **`xTaskPeriodicDelay()` and `uxTaskCallForEachTask()`** — `xTaskPeriodicDelay()` replaces `xTaskDelayUntil()`: it catches up on skipped periods and returns how many were skipped. `uxTaskCallForEachTask()` runs a callback for every task.
- **SMP on Armv8-M** — Symmetric multiprocessing on all Armv8-M ports (GCC, ArmClang, IAR), with IDLE-task core affinity.
- **New FreeRTOS ports** — Cortex-M52 (secure and NTZ), Arm China STAR-MC3, and Cortex-R82 (AArch64, MPU and non-MPU). The RISC-V port now saves FPU and vector context.

#### Boot

- **MCUboot FRDM-RW610FML support** — RW610 is treated like RW612, which enables serial recovery, encrypted XIP and the remap boot modes.

#### Safety

- **IEC 60730B Zephyr HAL analog I/O test** — New Zephyr AIO test with LPADC and DTS bandgap configuration for FRDM-MCXA153, A156, A266 and A344.
- **"Skip and Continue" error action** — New `APP_SAFETY_ERROR_ACTION_CONTINUE` option.

### New Platform / Device Support

| Device / Board | Family | Notes |
|----------------|--------|-------|
| MIMX8ML8 Cortex-A53 (evkmimx8mp) | i.MX | Cortex-A53 headers, startup, DDR linker script, per-core device layout; `freertos_hello` example |
| RT1184 (new parts) | i.MX RT | New part headers, internal-flash flashloader, NETC part support, SVD files |
| RT1183 / RT118D / RT118E | i.MX RT | NETC driver part support; RT1183 internal-flash linker window updated |
| MCXA577VAPR | MCX A-series | New 80-pin WLCSP part: CPU macro guard, part list, Kconfig/MDK identifiers |
| MCXA287VAPR / MCXA286VAPR | MCX A-series | New 80-pin WLCSP parts with SVD and SMARTDMA interrupt |
| MCXC352 / MCXC353 | MCX C-series | Device support moved to the public device repository; FRDM-MCXC353 examples enabled |
| MCXC454 | MCX C-series | SVD files added |
| RW610FML (FRDM-RW610FML) | Wireless | Part headers, Wi-Fi/BT module, mflash, MDK template, TF-M and MCUboot ports |
| KW43 (multicore) | Wireless | Multicore support, low-power enablement, DEVMGR CFPA backend |
| i.MX RT2660 (MIMXRT2660-EVK) | i.MX RT | Power driver rework, Power Manager port, SVD files, broad example and Bluetooth expansion |
| MIMXRT685S | i.MX RT | Connectivity Framework low-power platform; EdgeFast BLE low power |
| i.MX RTL375 (IMXRTL3759MCA) | i.MX RT | Ethos-U85 eIQ support; LPADC driver and port file |
| MC56F85000 | DSC | New I3C driver; DAC driver update |

---

## Enhancements

### Fundamental

- **ENET init sequence and SMII delay** — The init sequence is corrected in `mcx_enet`, `lpc_enet` and `enet_qos`. The SMII delay can now be set through Kconfig.
- **LLC maintenance timeout** — The poll budget now scales with cache size and can be overridden with `LLC_MAINTENANCE_TIMEOUT`. A `kStatus_Timeout` result now means the cache actually stalled.
- **SINC doze-mode guard** — Doze-mode handling is guarded by `FSL_FEATURE_SINC_MCR_HAS_DOZEN`, so SINC works on devices that have no DOZEN bit.
- **DCIF and BiSS improvements** — DCIF gamma configuration now uses the real register macros, and the PDI defaults are updated. BiSS bit reversal is now branchless and faster.
- **Static-analysis hardening** — MISRA/CERT-C/Coverity fixes are applied to these drivers: SAI, PDM, SPDIF, EASRC, eDMA, FlexCAN, MSCAN, NETC, I2C, SPI, FlexIO, LPADC, SFA, TSI, flash_ftmr, DPU/MIPI-DSI and the motor-encoder drivers. Audio IRQ paths also get runtime NULL guards.
- **mflash for the new RT2660 QSPI flash** — mflash supports the new QSPI flash on the board and still works with W25Q512. The SFP setting must now be passed explicitly in the FRAD config.
- **Wi-Fi TX power tables** — AzureWave tables are updated with 2.4 GHz BW40 limits. Murata 2EL band-edge channels now allow 40 MHz. RW612 worldwide tables are refreshed.
- **I3C driver auto-selection** — Kconfig now picks the `i3c` or `dsc_i3c` driver from the SoC IP type, so per-board `prj.conf` overrides are no longer needed.
- **Default Wi-Fi modules in examples** — The default modules are now:
  - IW61x (Murata 2EL) on RT1050/1060/1160/595/685/1180.
  - 88W8987 (1ZM) on RT1064.
  - IW610 (Murata 2LL) on the MCXN boards and mimxrt685audevk.
- **SLIM `wifi_cli` profile** — A low-memory profile is added for MCXN5xx-EVK and MCXN9xx-EVK.
- **Wireless MCU app defaults (KW43/MCXW70)** — Async flash and Deep Sleep are on by default. Fault output goes through the debug log engine. Host coredump is enabled in debug builds and disabled in release builds.
- **eIQ model runners** — The model runners now use eDMA-based copy/wait hooks. The TFLM and HiFi4 runners share code, and the runners print the SDK version.
- **Board files** — Updates in this release:
  - The RT2660 pin mux is exported from Config Tools.
  - The MCXA `board.h` has `extern "C"` guards.
  - RT700 LVGL examples run at 325 MHz.
  - MPU regions are adjusted for FreeRTOS 11.3.1.
- **PSA driver auto-selection in examples** — The ELE S400/S100 PSA driver is chosen by device, so it no longer needs to be listed in `prj.conf`.
- **MCXA SVD re-sync** — SVD files are re-synchronized for MCXA456/457/536/537/556/557/566/567/577.
- **Build documentation** — `CMAKE_OBJECT_PATH_MAX` and how to override it for sysbuild are now documented. Documentation links point to `https://docs.mcuxpresso.nxp.com/mcuxsdk/<version>/`.

### Device Support

- **RT2660 memory sleep-mode rework** — Memory blocks are identified by enum values. New functions `POWER_SetMemBlockSleepMode()` and `POWER_ForceAllDomainsToHwTrigger()` are added. Memory slices are reset to Active when entering Sleep.
- **RT2660 platform additions** — Adds a GPIO interrupt handler and the feature macros `FSL_FEATURE_ISI_SUPPORT_DEST` and `FSL_FEATURE_SINC_MCR_HAS_DOZEN`.
- **PINT per-instance feature macros** — New macros `FSL_FEATURE_PINT_NUMBER_OF_INSTANCE` and `FSL_FEATURE_PINT_NUMBER_OF_CONNECTED_OUTPUTSn(x)` are added for LPC, MCX, RT and Wireless devices. PINT clocks are added for LPC800, LPC55S06/S16/S36/S69 and RW610/RW612.
- **CMSIS `RTE_Device.h` templates** — Templates are added for 30 MCXA/MCXC/MCXE/MCXW devices and 19 KW43/KW47 devices, so `device.RTE` and CMSIS-Driver builds succeed.
- **MCXA577 clock attach IDs** — New attach enumerators for FlexCAN, ADC and eSPI. The old names are kept for compatibility.
- **Glitch detection disabled at boot** — `SystemInit()` now disables glitch detection on MCXW70 and KW43, as on KW47/MCXW72.
- **RT700 USB LPM macros and RT1180 headers** — RT700 gets `USBHS_`-prefixed LPM macros. RT1180 headers now match the latest reference manual.
- **MCXE32B EMAC errata macro** — `FSL_FEATURE_EMAC_HAS_ERRATA_050595` is added on both Cortex-M7 cores.

### Security

- **SGI key-locations sub-component** — `mcux_psa_sgi_opaque_key_locations.h` is now part of SGI common as its own component, so TF-M non-secure applications can select it without the full opaque driver.
- **Unified secure-subsystem session ID** — SSSAPI session init uses `CONFIG_MCUX_SECURE_SUBSYSTEM_SESSION_ID` everywhere. `ELEMU_loadFw()` moved into SSSAPI to match Zephyr upstream.
- **ELE S100 entropy in Mbed TLS 3.x** — The ELE S400 entropy entry points also work with ELE S100.
- **EL2GO key-store recovery (MCXE31B)** — EL2GO now recovers when PSA ITS and the HSEB key store are out of sync.
- **SGI/PKC RAM execute permission** — XEN is set for every RAM bank in both `SRAM_XEN` and its Glikey-protected duplicate.
- **Prefixed Kconfig helper symbols** — The device-family helper symbols in `els_pkc`, `sgi_pkc` and `sgi_pkc_pqc` now carry a prefix to avoid name collisions.
- **Secure storage API cleanup** — The non-standard offset APIs are removed. LittleFS globals are now `static`.

### Connectivity & Wireless

- **Bluetooth LE Host v1.10.24** — Changes in this version:
  - Connection Subrating uses less flash.
  - Anchor monitoring draws less current.
  - BD address and crystal trim are handled through DEVMGR.
  - Host task stacks are sized per application.
  - IPT no longer requires experimental features.
- **BLE controller DCOC calibration** — DCOC calibration state is now tracked per PHY, so an HCI Reset skips calibrations that are already complete. Up to 4 retries are allowed.
- **BLE controller HADM init** — `BLE_HADM_Init()` now distinguishes a cold boot from an HCI Reset. Controller headers have `extern "C"` guards.
- **EdgeFast Bluetooth crypto migration** — RT2660 and FRDM-MIMXRT1152 examples move to Mbed TLS 4.x / TF-PSA-Crypto. Bluetooth crypto now goes through PSA.
- **EdgeFast Bluetooth Matter integration** — `CONFIG_ARM=1` is now provided, and macro conflicts with `wifi_config.h` are resolved.
- **Connectivity Framework v7.5.1** — Changes in this version:
  - Mutex-free RemoteActive APIs for use in low-power callbacks.
  - The power-down handshake can be compiled out per platform.
  - NVS/Settings is aligned with Zephyr v4.4.1 and can coexist with EdgeFast in the same image.
  - KW43 RTT trim values are forwarded to the NBU.
  - The SPC wake-up delay is tuned.
- **Wi-Fi driver v1.3.r49.p12** — SDIO CMD53 reads now retry with IO_ABORT recovery. uAP link-local IPv6 addresses now reach the Preferred state. The lwIP ND6 queue size is bounded.
- **Wi-Fi/BT firmware** — Updated firmware versions:
  - IW612 18.99.8.p150
  - IW416 16.92.21.p168
  - 88W8987 16.92.21.p156.4
  - IW610/RW610 p150
- **Coex RPMSG shared memory** — `RPMSG_SHMEM_SIZE` can be overridden on EVKB-MIMXRT1170. The A2DP sink example uses 128 KB.
- **IEEE 802.15.4 SMAC** — SMAC updates from the Zephyr enablement work are included, and the NBU libraries are refreshed.
- **SOEM NETC handles** — NETC interface handles are now pointer types. Prebuilt WinPcap libraries are no longer shipped.
- **wpa_supplicant NAN USD** — NAN USD is aligned with upstream hostap.

### ML / DSP / Multimedia

- **TensorFlow Lite Micro overridable hooks** — The copy/wait functions are now weak symbols, so applications can supply eDMA-based versions.
- **OpenVG SDK build integration** — Adds Kconfig and `mcux.cmake` support for OpenVG, with a declared dependency on VGLite.

### RTOS

- **FreeRTOS secure-context and privilege hardening** — Changes in this version:
  - Armv8-M `SecureContext_AllocateContext` rejects secure stacks that are too small.
  - The start-scheduler and free-secure-context SVCs can only be called from privileged code.
  - MPU wrappers v2 refuse unprivileged critical sections.
- **FreeRTOS API input validation** — Stricter checks are added for timer command IDs, queue sets, recursive-mutex counters and task stack sizes.

### Boot

- **MCUboot IPED region change** — MCUboot now uses IPED contexts 14 and 15 for execution areas. This avoids clashes with regions 0–3, which applications or ROM may configure.

### Multicore

- **MCMGR forced-event queue** — Forced MU events now go into an ordered per-MU queue that is drained from the TX-empty interrupt, instead of overwriting unread messages. Queue sizes are set with `MCMGR_MU_RPMSG_DOORBELL_SLOTS` and `MCMGR_MU_FORCED_QUEUE_SIZE`.
- **MCMGR blocking send** — The blocking send now writes with interrupts disabled. It returns `kStatus_MCMGR_Error` when `MCMGR_BUSY_POLL_COUNT` runs out.
- **RPMsg-Lite Zephyr module conventions** — Adds an SPDX header and requires CMake ≥ 3.20.0.

### Filesystem

- **SDMMC cache control** — A new Kconfig option forces cache maintenance on platforms with an external cache controller. The uSDHC host now uses `SDMMCHOST_ENABLE_CACHE_CONTROL`.

### Motor Control

- **FreeMASTER automatic platform selection** — FreeMASTER now selects the target platform automatically, with no manual configuration.
- **Motor control speed loop and MCAT** — The speed loop now takes a frequency parameter instead of `SpeedLoopTs`. Also adds MCAT support for MCXC162, an updated sensorless state machine, and updated MCXC162 appconfigs.

### Safety

- **Simpler IEC 60730B AIO API** — `iec60730b_test_aio()` now runs the whole test sequence. Channel tables can be `const` and stay in flash.

---

## Bug Fixes

### Fundamental

- **Timer HAL handle overflow on 64-bit cores (security)** — On 64-bit cores such as the MIMX9596 Cortex-A55, `HAL_TIMER_HANDLE_SIZE` was too small and the driver overwrote adjacent memory. The handle size now depends on pointer width. Reported through NXP PSIRT.
- **TrustZone NSC veneer hardening (security)** — Cortex-M33 example veneers now validate non-secure buffers, copy them into secure memory, and format strings with `"%s"`. This fixes confused-deputy, timing side-channel, TOCTOU and format-string issues reported through Arm and NXP PSIRT.
- **TrustZone NSC veneer hardening** - NSC veneer functions hardened against TrustZone-M confused-deputy attacks (Arm PSIRT ARMSEC-559, NXP PSIRT).
- **USB example bounds checks (security)** — The USB examples now bound descriptor, packet and payload lengths, so malicious peers cannot cause overflows or hangs. This covers:
  - Host class examples: HID, Audio, Video, Printer, MSD, PHDC.
  - Device class examples: MSC, RNDIS, DFU, MTP, CDC, UVC.
  - USB-PD examples.
- **SAI eDMA multi-channel RX** — RX previously used the TX enum by mistake, which silently selected write-combine mode. It now uses `kSAI_RXFifoCombineModeEnabledOnRead`.
- **DualADC calibration** — `GAIN_CAL` is now sign-extended correctly; the old handling could double conversion results. The driver also supports the 17-bit `GAIN_CAL` field and waits the required delay after `CAL_RDY`.
- **ENET_QoS MCXE32B errata** — Adds workarounds for:
  - ERR050707: the DMA bus error is now reported as `kENET_QOS_DmaBusErrEvent`.
  - ERR050597.
  - ERR051222.
  - ERR050595.
- **FlexCAN bus-off workaround** — The ERR009595 workaround no longer leaves Freeze mode early, and IMASK2 is always preserved.
- **PWM ERR051989 workaround** — The workaround now follows the latest errata guidance and sets only `SMxPHASEDLY=1`.
- **SCTimer 0 % duty glitch** — A one-tick output glitch on edge-aligned PWM at 0 % duty is removed.
- **LLC maintenance serialization** — The driver now waits for `MNTOPACTV` to go idle around each maintenance operation. This fixes false timeouts during a full flush on MIMXRT2660-EVK.
- **MIPI-DSI command corruption** — Video mode is now turned off during APB command-mode transfers and restored afterwards.
- **PMU body-bias trim** — `PMU_ConfigBodyBias()` now does a read-modify-write and keeps the ROM-owned NWELL/PWELL trim.
- **RPMsg HAL handshake** — Fixes init/deinit hangs and lost-READY races. Compatibility with remote cores running 26.06.00 is restored.
- **USART DMA adapter RX loss** — Fixes occasional data loss when bytes arrive between reading the count and aborting DMA.
- **mflash RT700 / ARB_WIN** — The read LUTs now follow XSPI errata ERR052528, and the `ERRSTAT.ARB_WIN` init hang is fixed.
- **Component fixes** — Fixes in several components:
  - `HASH_CTX_SIZE_SHA256` is restored to 112.
  - SerialManager deletes the timer task before its mutex.
  - The codec adapters, WM8524 and WM8962 now check for NULL at runtime.
- **SDMA / PDM / CAAM** — The SDMA SPBA range check is fixed. The PDM build on i.MX95V is fixed. CAAM entropy descriptors are placed in non-cacheable memory.
- **LinkServer RAM image loading** — LinkServer now resets the target before loading and turns off the GDB memory-map check, so images that run from RAM load completely.
- **West tooling** — Fixes three issues:
  - A `west build` crash in device-only builds with `-p auto`.
  - Relative-path handling in `west list_project`.
  - A crash in `west blobs regen --init`.
- **Project generation** — Fixes three issues:
  - RISC-V LLVM projects can be generated without `RISCVLLVM_DIR` set.
  - Standalone `-include` paths are corrected.
  - CodeWarrior projects generate when the install path contains spaces.
- **USB with FreeRTOS** — The USB stack now starts after `vTaskStartScheduler()`, so an early interrupt can no longer touch kernel objects before they exist.
- **RT2660 example fixes** — Fixes in the RT2660 examples:
  - XBAR pad direction (eqdc/evtg/qtmr).
  - ASRC master clock.
  - Codec I2C baud rate.
  - LLC PSRAM bring-up.
  - A GCC 14.2 checksum miscompile in lwIP.
  - ENET PHY init.
  - SD power-rail settling time.
  - MCUboot XIP pin re-init.
- **Clock-enable ordering** — On MCXW70-LOC, FRDM-KW43 and FRDM-MCXW70, the FRO HF divider is now enabled before the clock source is selected. This fixes the TPM image mismatch and the silent LIN slave output.
- **Wireless low-power resets** — The 2.4 GHz radio low-power request is now always released on KW43/MCXW70/KW47, so waking up no longer causes unexpected resets.
- **Wireless app stability** — Stack overflows are fixed, LPUART is re-initialized after Deep Sleep, and the `m_shared_data` section is NOLOAD so `.bin` images stay small.
- **Other example fixes** — Fixes in several examples:
  - Overcurrent routing in `pmsm_enc` on HVP-MCXA346.
  - EtherCAT shared-lock corruption.
  - An MDK hardfault in LVGL.
  - Model-runner hangs on scalar tensors.
  - Several IAR/MDK build errors.
- **RT2660 repository package** — The repo-zip packaging failure for RT2660 is fixed.

### Device Support

- **MCXN556S / MCXN947T ROM API overflow** — `api_core_context_t` now reserves the full 512-byte slot. Previously, `API_Init()` overwrote application globals and broke `printf`.
- **MCXE31 FXOSC bypass mode** — Bypass now sets `OSC_BYP` only and configures the oscillator while it is disabled. `CLOCK_GetFxoscFreq()` now returns the configured frequency.
- **MCXE31B LPSPI clock array** — The clock array was selected by the wrong instance-count guard, so Lpspi4/Lpspi5 were missing. All six LPSPI instances are now included.
- **MCXA536 / MCXA537 build** — References to `USBHS1_PHY` in the shared clock driver are now guarded, so builds for these parts succeed.
- **MCXC353 RAM size** — The linker files now use a RAM size of 0x4000.
- **KW43 / MCXW70 LPTMR clock option** — The unsupported FRO6M prescaler clock option is removed.
- **i.MX937 part-number builds** — Driver paths for MIMX9371/9373 are fixed, and EIM/ERM driver types are removed because these parts don't have those IPs.
- **i.MX943 logical machine** — An earlier change is reverted, so the Cortex-A55 LMM remains the default.
- **RT118x USBPHY2 / RT2660 AVPLL** — USBPHY2 support is excluded on the new parts that lack it. RT2660 AVPLL bitfields are cleared before configuration, and an unnecessary XSPI LLC address translation is removed.

### Security

- **HSEB orphaned persistent keys** — The driver now checks PSA ITS for an existing persistent key ID before generating or importing a key, so the original key is no longer orphaned.
- **HSEB cipher bounds and key-size checks** — `cipher_update` now has a bounds check, and cipher keys with an invalid bit size are rejected.
- **EdgeLock 2GO agent vulnerability fixes** — Vulnerabilities and bugs found in the agent code, including through AI-assisted code scanning, are fixed. Updating is recommended.
- **ELE S100 ECDH** — ECDH acceleration on ELE S100 is temporarily disabled; ECDH uses the software implementation for now.
- **ELS/PKC device header and HMAC-DRBG** — MCXN947/MCXN547 CPU1 builds now pick the correct core header. The HMAC-DRBG source is now compiled, which fixes deterministic ECDSA linking on RT700.
- **PSA driver build fixes** — Fixes three build issues:
  - The unreachable-loop error in AEAD builds that have neither GCM nor CCM.
  - The missing SGI key-locations include path.
  - A header missing after TF-PSA-Crypto 1.2.0.
- **PSA ITS (FatFS)** — The FatFS backend is fixed after the ELE driver header was renamed.
- **TF-M packaging and L20/A2TS** — The TF-M secure libraries are now packaged for FRDM-MCXN947T, so `_s`/`_ns` examples link. The L20/A2TS non-secure RAM size and the PKC + eDMA anti-pole configuration are corrected.
- **SGI/PKC MCXW70 and MCXA5xx builds** — Glikey is no longer enabled in TF-M on MCXW70. The missing MCXA5xx platform header is added.
- **Secure storage** — Building alongside EdgeFast Bluetooth is fixed. CERT EXP33-C, INT30-C, ERR33-C and POS54-C findings are resolved.

### Connectivity & Wireless

- **CS distance accuracy** — The controller's per-antenna-path phase correction was applied twice, causing about 0.5 m of distance error. The double correction is removed, and a remaining ~3.5 cm offset is tuned out.
- **BTCS segmentation corruption** — L2CAP corruption when CS subevent data crossed a segment boundary is fixed. This includes a `uint16_t` underflow that produced a wild pointer.
- **CS-SYNC antenna selection** — The antenna lookup-table index for ACI 7 is fixed, and the Bluetooth 6.3 value `0xFD` for `CS_SYNC_Antenna_Selection` is now accepted.
- **NBU HardFault without antenna configuration** — If the Host does not configure the supported antenna count, it now defaults to 1 instead of causing a HardFault.
- **KW43-LOC RF switch and handover timeout** — The antenna switch pins PTA20/PTA21 are corrected. The anchor-search-start event is now handled correctly on supervision timeout.
- **GAP default connection parameters macro** — The missing comma and the missing `usePeerIdentityAddress` field are added, so the macro works as a brace initializer.
- **EdgeFast SMP entropy (security)** — RT2660 SMP pairing used an unseeded `rand()`, so every board generated the same P-256 keys. Entropy now comes from the ELE hardware TRNG.
- **EdgeFast L2CAP BR/EDR configuration race** — The channel now stays in the `CONFIG` state until the configuration response has been sent, so peer data arriving in that window is no longer dropped.
- **EdgeFast RT2660 audio and build** — Audio fixes for SAI MCLK, eDMA handle alignment, PLL clocking and ring-tone pitch. Also fixes GCC ITCM overflow, the IAR section selectors, liblc3 at -O3, and the M.2 SDIO port and reset timing.
- **IEEE 802.15.4 FSCI beacon overflow (security)** — The FSCI beacon-notify buffer now accounts for the pending address list, which closes a heap overflow of up to 70 bytes.
- **IEEE 802.15.4 dual-PAN rx-after-poll** — Transmit requests that arrived during rx-after-poll with dual-PAN enabled (a Matter use case) are no longer lost.
- **IEEE 802.15.4 ED scan and ASP CW** — Energy detect no longer reports `0xFF`, and the hard fault after an ASP continuous-wave test is fixed.
- **USB stack security** — Bounds and length checks are added across the USB stack:
  - USB-PD (PTN5110) extended messages and vendor VDMs.
  - RNDIS device commands and host message builders.
  - MTP parameter and event counts.
  - CCID bulk-out length.
  - MSC LBA range.
  - Hub descriptors.
  - Runt-frame dropping in the Ethernet adapter.
- **USB MCX ENET Rx buffer table** — The Rx buffer table moved off the stack, because `ENET_Init()` keeps the pointer after the call returns.
- **lwIP security** — Fixes in the lwIP network interfaces:
  - USB CDC-ECM/RNDIS pbuf overflow, fixed by copying with `pbuf_take()`.
  - ENET QoS TX overflow with chained pbufs.
  - Hosts no longer adopt a stale or incomplete MAC address.
  - Device-reported MTU and segment size are clamped.
- **Wi-Fi security** — An AP sending a malformed RSN/RSNO IE can no longer cause a HardFault, and the HE Capability IE copy and RX A-MSDU handling are now bounds-checked.
- **Wi-Fi stability** — Fixes in the Wi-Fi driver:
  - A WPA3-SAE reset hang.
  - Corrupt BSSID/SSID after a roaming scan.
  - The uAP secondary channel offset and channel-165 bandwidth.
  - Honoring a requested passive scan.
  - Memory leaks of enterprise certificates and RX net_buf.
- **Wi-Fi CSI HT40 distance** — `libcsi.a` is rebuilt for all toolchains and cores, which fixes a 2× distance error on HT40.
- **Connectivity Framework** — Fixes in the Connectivity Framework:
  - Valid HCI packets longer than 255 bytes are accepted again.
  - KW43/MCXW70 low-power register fixes (RF_CMC RAM power, MU wake-up, PMPROT).
  - OTA reads see pending async-flash operations.
  - WorkQ stack overflow.
  - `US_TO_TICK` now saturates instead of truncating.
- **wpa_supplicant** — The `mbedtls_ms_time` ALT implementation is now guarded by `MBEDTLS_PLATFORM_MS_TIME_ALT`.

### ML / DSP / Multimedia

- **OPUS decoder NULL handling** — `OggOPUSInit`, `OggOPUSDecode` and `OggOPUSSeek` validate their pointers and return an error instead of dereferencing NULL.
- **Maestro AAC start delay** — The delay before AAC playback started in `maestro_playback` is fixed.
- **ExecuTorch cross-compilation** — A stale host `libflatccrt.a` is removed before the target rebuild, which fixes cross-builds including HiFi4 profiling builds.
- **XAF USB speaker distortion** — `flash_debug` builds on FRDM-IMXRT700 and RT685-AUD-EVK are now built at `-O2`, so the Cortex-M33 USB real-time path meets its deadline.
- **VGLite MDK hardfault** — VGLite MDK projects now link with microlib. Previously, semihosting initialization caused a hardfault at reset when no debugger was attached.

### RTOS

- **FreeRTOS `vTaskListTasks()` TOCTOU (security)** — A race that could under-size the allocation and overflow the buffer in `uxTaskGetSystemState()` is fixed.
- **FreeRTOS kernel object fixes** — Fixes in kernel objects:
  - Batching stream buffers now trigger at the correct level.
  - heap_5 no longer asserts falsely on out-of-memory.
  - Priority disinheritance after a timeout is correct.
  - `xTimerDelete` no longer leaks an MPU wrappers v2 object-pool entry.
- **FreeRTOS RISC-V context** — Context restore now uses the saved `mstatus` to decide the FPU/VPU state, and the FPU register offsets are corrected.

### Boot

- **MCU bootloader ecosystem paths** — The `system_MIMXRT*.h` paths in the ecosystem metadata are corrected, so generated packages are complete.

### Multicore

- **RPMsg-Lite name-service overflow (security)** — `rpmsg_ns_announce` now copies at most `RL_NS_NAME_SIZE - 1` bytes and always NUL-terminates the endpoint name.
- **RPMsg-Lite TrustZone NSC veneer hardening** - Improved validation of non-secure pointers and size values in the rpmsg_lite_pingpong_tzm example to prevent secure-world memory disclosure or denial of service.
- **RPMsg-Lite MISRA C-2012** — Rules 10.3, 14.4, 8.4 and 5.8 are fixed with no API change.
- **MCMGR KW43 release build** — The failing KW43 release targets are fixed.

### Filesystem

- **FatFs sector-size truncation** — `GET_SECTOR_SIZE` now returns `RES_PARERR` when `blockSize` exceeds 0xFFFF, instead of silently truncating it.

### Motor Control

- **Sensorless speed catch-up** — Merging speed catch-up no longer runs twice in the sensorless start-up sequence.

---

## Breaking Changes

| # | Description | Impact | Required Action |
|---|-------------|--------|-----------------|
| 1 | **RT2660 power driver API rework** | `POWER_SetPolicy` is split into `POWER_Init` + `POWER_SetPolicy`. `POWER_LoadBodyBiasFuse` is renamed to `POWER_InitBodyBiasConfig` and `POWER_ApplyZbb` to `POWER_ApplyZeroBodyBias`. The `POWER_SetMemSlicesSleepMode()` parameter order is now (mems, count, mode). `MCUX_POWER_PF9453_SUPPLY` is removed. | Call `POWER_Init()`, update the renamed APIs and the parameter order, and register `power_ext_regulator_hooks_t` callbacks (or enable `MCUX_BOARD_USE_PF9453`) on PF9453-based boards. |
| 2 | **PINT feature macro replaced by a per-instance macro** | Code that uses `FSL_FEATURE_PINT_NUMBER_OF_CONNECTED_OUTPUTS` fails to build on LPC, MCX, RT and Wireless devices. | Use `FSL_FEATURE_PINT_NUMBER_OF_CONNECTED_OUTPUTSn(x)` and `FSL_FEATURE_PINT_NUMBER_OF_INSTANCE`. |
| 3 | **SAI eDMA multi-channel RX requires the RX combine enum** | Passing `kSAI_FifoCombineModeEnabledOnRead` to `SAI_TransferRxSetConfigEDMA` asserts in debug builds. | Use `kSAI_RXFifoCombineModeEnabledOnRead`. |
| 4 | **DualADC API and config changes** | The `DUALADC_CalculateGainResult()` parameter is now `uint32_t`, and `dadc_config_t` has new `enableDmaA`/`enableDmaB` fields. | Update call sites, and start from the default config or initialize the new fields. |
| 5 | **PMU body-bias trim not written by default** | `PMU_ConfigBodyBias()` no longer writes NWELL/PWELL trim. | Enable `PMU_DRIVER_UPDATE_TRIM_VALUE` if your software supplies the trim. |
| 6 | **`.bin` output disabled by default** | Flows that expect `.bin` artifacts fail, because `MCUX_BUILD_OUTPUT_BIN` defaults to `n`. | Set `MCUX_BUILD_OUTPUT_BIN=y` in `prj.conf`. |
| 7 | **V2X FCE scratch configuration** | `V2X_FCE_DDR_SCRATCH_BASE` is removed, and the scratch area is now placed by the linker. | Use `V2X_FCE_SCRATCH_PAYLOAD_SIZE` and place the scratch section in the application linker script. |
| 8 | **HAL UART adapter selection with `muxuart`** | When `muxuart` is enabled, the LPUART adapter is no longer selected automatically, and only one UART adapter can be linked per image. | Choose the adapter explicitly for each core. |
| 9 | **`DbgConsole_Printf_NSE()` signature** | TrustZone non-secure callers fail to build, because the function now takes a `size_t length` argument. | Pass the buffer length. |
| 10 | **MCXE31 FXOSC bypass value** | `kFXOSC_ModeBypass` changed from 0x81000000 to 0x80000000, and bypass mode no longer waits on `OSC_STAT`. | Review code that stores or compares the raw value or relies on the wait. |
| 11 | **MIMX8ML8 per-core layout** | Device and board files moved to per-core folders, and the board ID is now `evkmimx8mp@cm7`. | Update custom build scripts and the board qualifier. |
| 12 | **BLE controller HADM API changes** | `BLE_HADM_Init()` takes a new `bReset` argument. `BLE_HADM_SetAntennaType()` takes `num_ap` and `t_sw`. | Update custom integration call sites. |
| 13 | **BLE hardware-parameter access via DEVMGR** | The HWParameter / `PLATFORM_GetBdAddr` path is replaced. `gGapDefaultConnectionRequestParameters_d` gains the `usePeerIdentityAddress` field. | Migrate to the `DEVMGR_*` APIs and update positional initializers. |
| 14 | **Connectivity Framework KW43 IFR and fault output** | The KW43 default IFR layout is now CFPA 0x170. The DEVMGR types header is merged into `fwk_platform_devmgr.h`. Fault reports are dropped if no output is registered. | Define `KW43_A0_0` for A.0.0 silicon, update includes, and call `FWK_FaultHandlerSetOutput()`. |
| 15 | **Wi-Fi external antenna gain units** | Values are now interpreted in 0.25 dB steps, so existing settings apply a quarter of the intended gain. | Multiply existing values by 4. |
| 16 | **EdgeFast Bluetooth Mbed TLS 4.x migration (RT2660/RT1152)** | `mbedtls3x` is replaced by TF-PSA-Crypto. The user config file is renamed, and `mbedtls_hardware_poll()` is replaced by `mbedtls_platform_get_entropy()`. | Rename to `tf_psa_crypto_user_config.h` / `TF_PSA_CRYPTO_USER_CONFIG_FILE` and implement `mbedtls_platform_get_entropy()`. |
| 17 | **ELE S400 driver reworked as S1xx/S4xx** | The header is renamed, and the driver is now enabled by default with Mbed TLS / TF-PSA-Crypto. | Update includes and review the driver selection in `prj.conf`. |
| 18 | **Secure storage offset APIs removed** | Callers of `its_get_from_offset()` / `its_set_at_offset()` fail to link. | Use the standard PSA ITS APIs. |
| 19 | **Crypto library Kconfig helper symbols renamed** | Custom Kconfig/CMake that references the old unprefixed symbols in `els_pkc`, `sgi_pkc` or `sgi_pkc_pqc` breaks. | Update to the prefixed symbol names. |
| 20 | **MCMGR forced-event queue** | `MCMGR_TriggerEventForce()` can return `kStatus_MCMGR_Error` when the queue is full. | Check the return value or increase `MCMGR_MU_FORCED_QUEUE_SIZE`. |
| 21 | **MCUboot IPED contexts moved to 14/15** | Applications that use IPED contexts 14/15 conflict with MCUboot. | Move application IPED regions to other contexts. |
| 22 | **IEC 60730B AIO API** | `iec60730b_aio_test_init()` is removed, and the layout of `struct iec60730b_adc_channel` changed. | Call `iec60730b_test_aio()` only and update the channel tables. |
| 23 | **Motor control speed-loop parameter** | `SpeedLoopTs` is replaced by a frequency parameter. | Convert existing sample-time settings to frequency. |
| 24 | **FreeRTOS V11.3.1 MPU/RISC-V changes** | `configALLOW_UNPRIVILEGED_CRITICAL_SECTIONS=1` is a compile error under MPU wrappers v2. The RISC-V context layout changed. | Remove unprivileged critical sections and update custom context-switch assembly or debugger scripts. |
| 25 | **SOEM NETC handles and WinPcap** | NETC `if_port` handle members are now pointers, and the WinPcap libraries are no longer shipped. | Update application code and install the WinPcap/Npcap SDK for Windows host builds. |
| 26 | **Removed examples / toolchains** | These are removed: XAF examples on EVK-MIMXRT595/685, i.MX93 I3C component examples, RW612 NCP socket commands, and MDK for OpenVG on FRDM-IMXRT1152. | Use the 26.09.00 release, or a supported board/toolchain. |

---

## Known Issues

- **ELE S100 ECDH acceleration** — ECDH hardware acceleration is temporarily disabled on ELE S100, and ECDH falls back to the software implementation.
- **MIMXRT2660-EVK Bluetooth module support** —
  - LE Audio works only with the Murata 2EL / W9177 modules, and the 4-BIS/4-CIS examples support only the 2EL M.2 module.
  - Bluetooth Classic examples do not support the 2LL module.
- **MIMXRT2660-EVK board rework** —
  - The Bluetooth UART needs board rework (remove R553/R554).
  - Depending on the example, codec, sync and handsfree signals also need rework. See the example readme files.
- **KW47 Inline PCT Transfer** — IPT is disabled by default and is enabled only when one antenna and one antenna path are configured.
- **FRDM-MCXA577 (A0 silicon) USB Ethernet** — Because of ENET RMII receive erratum ERR053383, the CDC-VNIC/ECM examples use MII. The debug console moves to LPUART2, and board rework is required.
- **KW43 OTA write verification** — OTA write verification is disabled because it is not compatible with async flash operations.
- **KW43/MCXW70 DEVMGR platform backend** — The DEVMGR platform backend is not enabled by default in this preview.
- **Murata 1XK (IW416) HT40** — HT40 on 2.4 GHz is not supported, so uAP is forced to 20 MHz.
- **Temporarily disabled builds** —
  - `lpspi_loopback` on FRDM-MCXC353.
  - `mcxn_encrypted_xip` on FRDM-MCXN947T.
  - Coex EdgeFast FlexSPI builds on FRDM-IMXRT1152.
  - MCUXpresso IDE builds of coex A2DP on EVKB-MIMXRT1170.
  - The `tfm_regression_s` MDK debug build.
  - Selected MCXL SLCD/USB targets.
- **Wi-Fi/BT firmware validation** — Full regression testing of the updated firmware binaries is still in progress for this preview.

---

## Toolchain & Environment Support

The following toolchain versions are documented for this release. Version information is transcribed from the `mcu-sdk-doc` release documentation of the `release/26.12.00-pvw1` revision; label as **"Documented for this release"**.

| Toolchain | Version | Notes |
|-----------|---------|-------|
| MCUXpresso for VS Code | v26.06 | Default IDE experience for all device families |
| Arm GNU Toolchain (armgcc) | 14.2.x | Command line / `west build` |
| IAR Embedded Workbench for Arm | 9.70.4 | |
| Keil MDK (µVision) | 5.43a | |
| MCUXpresso IDE | 25.06.xx | |
| CodeWarrior Development Studio | v11.2 with CodeWarrior for DSC v11.2 SP1 | DSC devices |
| RISC-V LLVM | 19.1.7 | RISC-V cores |
| Xtensa Xplorer | 12.0.6 | DSP examples |
| Xtensa C/C++ Compiler (XCC) | RJ-2026.6 | DSP examples |

> **Note:** At this revision, the documented MCUXpresso for VS Code (v26.06) and MCUXpresso IDE (25.06.xx) versions have not yet been refreshed for the December 2026 release. Refer to the final release documentation for the authoritative toolchain matrix.

---

## Final Release Summary

MCUXpresso SDK 26.12.00-pvw1 (December 2026, implied) is the first preview of the December quarterly release.

- **New devices:** the MIMX8ML8 Cortex-A53 core, new RT1184 parts, MCXA WLCSP80 parts, RW610FML and KW43 multicore. MCXC352/MCXC353 are now in the public SDK.
- **i.MX RT2660:** much wider support, covering power management, audio, USB, display, Bluetooth and LE Audio.
- **Security:** a single ELE S1xx/S4xx PSA driver that supports ELE S100, HSEB opaque AES ciphers, EdgeLock 2GO agent v6.5.2, and new EdgeLock V2X FCE crypto services.
- **Wireless:**
  - Bluetooth LE Channel Sounding gains Inline PCT Transfer and better distance accuracy.
  - Updated stacks: Bluetooth LE Host v1.10.24, Connectivity Framework v7.5.1 and Wi-Fi driver v1.3.r49.p12.
  - Refreshed Wi-Fi firmware for IW612, IW416, 88W8987 and IW610/RW610.
- **RTOS and multicore:** FreeRTOS-Kernel V11.3.1 adds Armv8-M SMP, the new `serial_mux` component shares one UART console across cores, and MCMGR event delivery is more reliable.
- **Hardening:** USB, lwIP, Wi-Fi, TrustZone examples, RPMsg-Lite and the HAL layer.

Before migrating, review the Breaking Changes section, in particular:

- the RT2660 power API;
- the PINT feature macros;
- the build-output defaults;
- the Mbed TLS 4.x / TF-PSA-Crypto migration;
- the Bluetooth controller API updates.

Then run `west update` to sync the workspace.