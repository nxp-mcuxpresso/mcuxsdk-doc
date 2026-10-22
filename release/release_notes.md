## Overview

MCUXpresso SDK 26.12.00-pvw1 is Preview 1 of the December 2026 release. Previews give early access to new silicon and features as they are being developed. They are not at full release quality.

Compared with the 26.09.00 baseline, this preview updates **68 subrepositories**, adds **0 components**, and removes **0 components**. The main areas of change are:

- **New silicon support:** MIMX8ML8 Cortex-A53, new RT1184 parts, MCXA577VAPR / MCXA287VAPR / MCXA286VAPR (80-pin WLCSP), RW610FML, KW43 multicore, and MCXC352/353 in the public device repository.
- **Security:** ELE S100 support through the unified ELE S1xx/S4xx PSA driver, HSEB opaque AES ciphers, and EdgeLock 2GO agent v6.5.2.
- **Wireless:** Bluetooth LE Host v1.10.24, Connectivity Framework v7.5.1, Wi-Fi driver v1.3.r49.p12., and refreshed Wi-Fi/BT firmware.
- **Connectivity:** USB stack v2.13.1.
- **RTOS:** FreeRTOS-Kernel V11.3.1.

These notes are intentionally short for a preview. They cover only the repository changes and the bug fixes. For details of new features, enhancements, API changes, and other changes, see the commit history of each subrepository at the pinned revisions. The complete release notes, including New Features, Enhancements, Breaking Changes, Known Issues, and Toolchain Support, will be published with the 26.12.00 quarterly release.

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

## Bug Fixes

### Fundamental

- **Timer HAL handle overflow on 64-bit cores (security)** — On 64-bit cores such as the MIMX9596 Cortex-A55, `HAL_TIMER_HANDLE_SIZE` was too small, and the driver overwrote adjacent memory. The handle size now depends on the pointer width. Reported through NXP PSIRT.
- **Security Updates for TrustZone-M NSC Veneers**
  - TrustZone-M NSC veneer hardening** - Improper handling of non-secure-world input in NSC veneer functions of NXP MCUXpresso SDK TrustZone-M examples (trustzone_examples), affecting versions through 26.06.00-lts and 26.09.00-pvw2, may allow a non-secure caller to supply unvalidated pointers or untrusted data, causing a timing side-channel, TOCTOU condition, or format-string misuse, potentially resulting in secure-world memory disclosure or denial of service. All software versions starting from 26.06.01-lts and 26.09.00 have fixed this issue. 

    *Acknowledgment: NXP would like to thank Tijs Bellefroid, Antonis Louka, Marton Bognar, and Jo Van Bulck (DistriNet, KU Leuven) for the responsible disclosure.*

  - **RPMsg-Lite TrustZone-M NSC veneer input validation** - Improper input validation in non-secure-callable (NSC) veneer functions of the NXP MCUXpresso SDK rpmsg-lite multicore example (multicore_examples/rpmsg_lite_pingpong_tzm) up to releases 26.06.00-lts and 26.09.00 may allow a non-secure caller to supply unvalidated pointers and size values, potentially resulting in disclosure of secure-world memory to the non-secure domain, or denial of service. All software versions starting from 26.06.01-lts and 26.12.00-pvw1 have fixed this issue. 

    *Acknowledgment: NXP would like to thank Tijs Bellefroid, Antonis Louka, Marton Bognar, and Jo Van Bulck (DistriNet, KU Leuven) for the responsible disclosure.*
    
- **USB example bounds checks (security)** — The USB examples now bound descriptor, packet and payload lengths, so malicious peers cannot cause overflows or hangs. This covers:
  - Host class examples: HID, Audio, Video, Printer, MSD, PHDC.
  - Device class examples: MSC, RNDIS, DFU, MTP, CDC, UVC.
  - USB-PD examples.

- **USB Host Audio Recorder example bounds checks (security)** — Fixed a DMA out-of-bounds write vulnerability in the MCUXpresso SDK usb_host_audio_recorder example by clamping the USB descriptor-derived packet size to the stream buffer capacity; resolved in 26.06.01-lts and 26.12.00-pvw1.

  *Acknowledgment: NXP would like to thank Puda Zhao for the responsible disclosure.*

- **SAI eDMA multichannel RX** — RX previously used the TX enum by mistake, which silently selected write-combine mode. It now uses `kSAI_RXFifoCombineModeEnabledOnRead`.
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
- **MIPI-DSI command corruption** — Video mode is now turned off during APB command-mode transfers and restored afterward.
- **PMU body-bias trim** — `PMU_ConfigBodyBias()` now does a read-modify-write and keeps the ROM-owned NWELL/PWELL trim.
- **RPMsg HAL handshake** — Fixes init/deinit hangs and lost-READY races. Compatibility with remote cores running 26.06.00 is restored.
- **USART DMA adapter RX loss** — Fixes occasional data loss when bytes arrive between reading the count and aborting DMA.
- **mflash RT700 / ARB_WIN** — The read LUTs now follow XSPI errata ERR052528, and the `ERRSTAT.ARB_WIN` init hang is fixed.
- **Component fixes** — Fixes in several components:
  - `HASH_CTX_SIZE_SHA256` is restored to 112.
  - SerialManager deletes the timer task before its mutex.
  - The codec adapters, WM8524 and WM8962, now check for NULL at runtime.
- **SDMA / PDM / CAAM** — The SDMA SPBA range check is fixed. The PDM build on i.MX95V is fixed. CAAM entropy descriptors are placed in noncacheable memory.
- **LinkServer RAM image loading** — LinkServer now resets the target before loading and turns off the gdb memory-map check, so images that run from RAM load completely.
- **West tooling** — Fixes three issues:
  - A `west build` crash in device-only builds with `-p auto`.
  - Relative-path handling in `west list_project`.
  - A crash in `west blobs regen --init`.
- **Project generation** — Fixes three issues:
  - RISC-V LLVM projects can be generated without `RISCVLLVM_DIR` set.
  - Standalone `-include` paths are corrected.
  - CodeWarrior projects generate when the install path contains spaces.
- **RT2660 example fixes** — Fixes in the RT2660 examples:
  - XBAR pad direction (eqdc/evtg/qtmr).
  - ASRC reference clock.
  - Codec I2C baud rate.
  - LLC PSRAM bring-up.
  - A GCC 14.2 checksum miscompiles in lwIP.
  - ENET PHY init.
  - SD power-rail settling time.
  - MCUboot XIP pin re-init.
- **Clock-enable ordering** — On MCXW70-LOC, FRDM-KW43, and FRDM-MCXW70, the FRO HF divider is now enabled before the clock source is selected. This fixes the TPM image mismatch and the silent Lin responder output.
- **Wireless low-power resets** — The 2.4 GHz radio low-power request is now always released on KW43/MCXW70/KW47, so waking up no longer causes unexpected resets.
- **Wireless app stability** — Stack overflows are fixed, LPUART is reinitialized after Deep Sleep, and the `m_shared_data` section is NOLOAD so `.bin` images stay small.
- **Other example fixes** — Fixes in several examples:
  - Overcurrent routing in `pmsm_enc` on HVP-MCXA346.
  - EtherCAT shared-lock corruption.
  - An MDK hardfault in LVGL.
  - Model-runner hangs on scalar tensors.
  - Several IAR/MDK build errors.
- **RT2660 repository package** — The repo-zip packaging failure for RT2660 is fixed.
- **USB with FreeRTOS** — The USB stack now starts after `vTaskStartScheduler()`, so an early interrupt can no longer touch kernel objects before they exist.
- **USB Stack** — The version is updated to 2.13.1.
  - Fixed memory leaks, improved host stack robustness and security.
  - Fixed two vulnerability issues:
    - CVE-2026-89311: A missing bounds check on a host-controlled field in the RNDIS device class driver of the NXP MCUXpresso SDK USB middleware up to releases 26.06.00-lts and 26.09.00-pvw2 allowed a malicious USB host to read arbitrary memory from the connected device. All software versions starting from 26.06.01-lts and 26.09.00 have fixed this issue.

      *Acknowledgment: NXP would like to thank dread (d7ead) for the responsible disclosure.*

    - CVE-2026-93503: A missing bounds check on a device-controlled field in the USB host video, audio, and CDC class drivers of the NXP MCUXpresso SDK USB middleware up to releases 26.06.00-lts and 26.09.00-pvw2 allowed a malicious USB device to trigger a heap buffer overflow when connected to an affected host, potentially leading to memory corruption and loss of device availability. All software versions starting from 26.06.01-lts and 26.09.00 have fixed this issue.

      *Acknowledgment: NXP would like to thank dread (d7ead) for the responsible disclosure.*
      
### Device Support

- **MCXN556S / MCXN947T ROM API overflow** — `api_core_context_t` now reserves the full 512-byte slot. Previously, `API_Init()` overwrote application globals and broke `printf`.
- **MCXE31 FXOSC bypass mode** — Bypass now sets `OSC_BYP` only and configures the oscillator while it is disabled. `CLOCK_GetFxoscFreq()` now returns the configured frequency.
- **MCXE31B LPSPI clock array** — The clock array was selected by the wrong instance-count guard, so Lpspi4/Lpspi5 were missing. All six LPSPI instances are now included.
- **MCXA536 / MCXA537 build** — References to `USBHS1_PHY` in the shared clock driver are now guarded, so builds for these parts succeed.
- **MCXC353 RAM size** — The linker files now use a RAM size of 0x4000.
- **KW43 / MCXW70 LPTMR clock option** — The unsupported FRO6M prescaler clock option is removed.
- **i.MX937 part-number builds** — Driver paths for MIMX9371/9373 are fixed, and EIM/ERM driver types are removed because these parts do not have those IPs.
- **i.MX943 logical machine** — An earlier change is reverted, so the Cortex-A55 LMM remains the default.
- **RT118x USBPHY2 / RT2660 AVPLL** — USBPHY2 support is excluded on the new parts that lack it. RT2660 AVPLL bit fields are cleared before configuration, and an unnecessary XSPI LLC address translation is removed.

### Security

- **HSEB orphaned persistent keys** — The driver now checks PSA ITS for an existing persistent key ID before generating or importing a key, so the original key is no longer orphaned.
- **HSEB cipher bounds and key-size checks** — `cipher_update` now has a bounds check, and cipher keys with an invalid bit size are rejected.
- **EdgeLock 2GO agent vulnerability fixes (security)** — Vulnerabilities and bugs found in the agent code, including through AI-assisted code scanning, are fixed. Updating is recommended.
- **ELE S100 ECDH** — ECDH acceleration on ELE S100 is temporarily disabled; ECDH uses the software implementation for now.
- **ELS/PKC device header and HMAC-DRBG** — MCXN947/MCXN547 CPU1 builds now pick the correct core header. The HMAC-DRBG source is now compiled, which fixes deterministic ECDSA linking on RT700.
- **PSA driver build fixes** — Fixes three build issues:
  - The unreachable-loop error in AEAD builds that do not have GCM or CCM.
  - The missing SGI key-locations include path.
  - A header missing after TF-PSA-Crypto 1.2.0.
- **PSA ITS (FatFS)** — The FatFs backend is fixed after the ELE driver header was renamed.
- **TF-M packaging and L20/A2TS** — The TF-M secure libraries are now packaged for FRDM-MCXN947T, so `_s`/`_ns` examples link. The L20/A2TS non-secure RAM size and the PKC + eDMA antipole configuration are corrected.
- **SGI/PKC MCXW70 and MCXA5xx builds** — Glikey is no longer enabled in TF-M on MCXW70. The missing MCXA5xx platform header is added.
- **Secure storage** — Building alongside EdgeFast Bluetooth is fixed. CERT EXP33-C, INT30-C, ERR33-C, and POS54-C findings are resolved.

### Connectivity & Wireless

- **CS distance accuracy** — The controller's per-antenna-path phase correction was applied twice, causing about 0.5 m of distance error. The double correction is removed, and a remaining ~3.5 cm offset is tuned out.
- **BTCS segmentation corruption** — L2CAP corruption when CS subevent data crossed a segment boundary is fixed. This includes a `uint16_t` underflow that produced a wild pointer.
- **CS-SYNC antenna selection** — The antenna lookup-table index for ACI 7 is fixed, and the Bluetooth 6.3 value `0xFD` for `CS_SYNC_Antenna_Selection` is now accepted.
- **NBU HardFault without antenna configuration** — If the Host does not configure the supported antenna count, it now defaults to 1 instead of causing a HardFault.
- **KW43-LOC RF switch and handover timeout** — The antenna switch pins PTA20/PTA21 are corrected. The anchor-search-start event is now handled correctly on a supervision timeout.
- **GAP default connection parameters macro** — The missing comma and the missing `usePeerIdentityAddress` field are added, so the macro works as a brace initializer.
- **EdgeFast SMP entropy (security)** — RT2660 SMP pairing used an unseeded `rand()`, so every board generated the same P-256 keys. Entropy now comes from the ELE hardware TRNG.
- **EdgeFast L2CAP BR/EDR configuration race** — The channel now stays in the `CONFIG` state until the configuration response has been sent, so peer data arriving in that window is no longer dropped.
- **EdgeFast RT2660 audio and build** — Audio fixes for SAI MCLK, eDMA handle alignment, PLL clocking, and ring-tone pitch. Also fixes GCC ITCM overflow, the IAR section selectors, liblc3 at -O3, and the M.2 SDIO port and reset timing.
- **IEEE 802.15.4 FSCI beacon overflow (security)** — The FSCI beacon-notify buffer now accounts for the pending address list, which closes a heap overflow of up to 70 bytes.
- **IEEE 802.15.4 dual-PAN rx-after-poll** — Transmit requests that arrived during rx-after-poll with dual-PAN enabled (a Matter use case) are no longer lost.
- **IEEE 802.15.4 ED scan and ASP CW** — Energy detect no longer reports `0xFF`, and the hard fault after an ASP continuous-wave test is fixed.
- **USB stack input validation (security)** — USB stack v2.13.1 adds bounds and length checks so that malformed host, device, or PD peer traffic can no longer cause buffer overruns:
  - USB-PD (PTN5110) extended messages and vendor VDMs.
  - RNDIS device commands and host message builders.
  - MTP parameter and event counts.
  - CCID bulk-out length.
  - MSC LBA range.
  - Device ch9 control-OUT requests.
  - Host hub descriptor and hub status responses.
  - Frame length and ENET status in the ENET and MCX ENET Ethernet adapters; runt frames are dropped.
- **USB MCX ENET RX buffer table** — The RX buffer table moved off the stack, because `ENET_Init()` keeps the pointer after the call returns.
- **lwIP network interface hardening (security)** — Fixes in the lwIP network interfaces:
  - USB CDC-ECM/RNDIS pbuf overflow, fixed by copying with `pbuf_take()`.
  - ENET QoS TX overflow with chained pbufs.
  - Hosts no longer adopt a stale or incomplete MAC address.
  - Device-reported MTU and segment size are clamped.
- **Wi-Fi IE parsing hardening (security)** — An AP sending a malformed RSN/RSNO IE can no longer cause a HardFault, and the HE Capability IE copy and RX A-MSDU handling are now bounds-checked.
- **Wi-Fi stability** — Fixes in the Wi-Fi driver:
  - A WPA3-SAE reset hangs.
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
- **VGLite MDK hard fault** — VGLite MDK projects now link with microlib. Previously, semihosting initialization caused a hard fault at reset when no debugger was attached.

### RTOS

- **FreeRTOS `vTaskListTasks()` TOCTOU (security)** — A race that could undersize the allocation and overflow the buffer in `uxTaskGetSystemState()` is fixed.
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
- **RPMsg-Lite MISRA C-2012** — Rules 10.3, 14.4, 8.4 and 5.8 are fixed with no API change.
- **MCMGR KW43 release build** — The failing KW43 release targets are fixed.

### File system

- **FatFs sector-size truncation** — `GET_SECTOR_SIZE` now returns `RES_PARERR` when `blockSize` exceeds 0xFFFF, instead of silently truncating it.

### Motor Control

- **Sensorless speed catch-up** — Merging speed catch-up no longer runs twice in the sensorless startup sequence.