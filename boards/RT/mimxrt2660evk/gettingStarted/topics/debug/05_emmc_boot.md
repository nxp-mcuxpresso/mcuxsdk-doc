# eMMC Boot

This page covers the steps required to get a MIMXRT2660-EVK booting an image from eMMC.

> **Applies to**: primarily `ram_only` and `psram_only` targets, where eMMC is one of the typical production boot media for these RAM ONLY images. Unified Linkage targets use XSPI NOR flash as their standard boot medium.

## Hardware adaptation

The MIMXRT2660-EVK requires hardware rework before eMMC is usable. Refer to the [eMMC hardware rework document](HardwareAdaption/eMMC_HW_Rework.md) in the **HardwareAdaption** directory for the details.

## Boot mode setting

Unlike XSPI NOR boot, eMMC boot mode cannot be selected via the boot switch on the MIMXRT2660-EVK. To boot from eMMC, the SoC's boot mode must be configured through one of the following approaches:

- **Fuse programming (production)** -- the standard path.
- **Auxiliary image workaround (development)** -- avoids blowing permanent fuses.

### Fuse programming (production)

> **Warning**: fuse programming is irreversible. Use the auxiliary image workaround during development and only blow the fuse when the configuration is confirmed.

Booting from eMMC requires the BOOT_CFG0 fuse to be programmed with the correct eMMC boot mode (USDHC instance, bus width). Program it once via blhost or SPSDK; the setting is permanent and survives power cycles.

For the fuse programming commands, refer to the blhost page and the SPSDK page in this guide.

### Auxiliary image workaround (development)

The SDK auxiliary demo (xspi_nor and ram_only targets) sets the eMMC boot mode via a volatile shadow fuse at runtime, then performs a warm reset so Boot ROM boots from eMMC.

Ensure the boot switch is set to `0b00` (XSPI NOR boot mode) before running the auxiliary image. After the warm reset, Boot ROM uses the shadow fuse to boot from eMMC. If the boot switch is set to `0b10` (SDP mode), SDP takes priority over the shadow fuse and eMMC boot will not proceed.

> **Note**: the auxiliary image performs the warm reset before reaching `main()`. When running under a debugger, execution will not halt at `main()` and the debugger may lose connection after the reset -- both are expected behavior, not failures.

Two auxiliary targets are available:

#### `xspi_nor` target (recommended for MIMXRT2660-EVK)

Requires XSPI NOR flash. Program the auxiliary image into XSPI NOR flash using the standard Unified Linkage flash flow. On every power-on, the auxiliary image within XSPI NOR flash runs automatically, enabling eMMC POR boot without any permanent fuse.

Build with target `xspi_nor_debug` (or `xspi_nor_release`).

> **Note -- IDE download after auxiliary setup**: once the `xspi_nor` auxiliary is in flash, it runs on every reset and sets the eMMC shadow fuse before warm-resetting. If an IDE debug download of a Unified Linkage image is attempted after this, the IDE triggers a reset after programming; Boot ROM follows the shadow fuse and boots from eMMC, leaving XSPI NOR flash uninitialized. The IDE then fails to verify the programmed image and reports an error. This is expected on the first download. To recover, press the reset button manually -- Boot ROM boots from XSPI NOR flash normally and the image runs. Subsequent IDE downloads will succeed without this error.

#### `ram_only` target

Works regardless of whether XSPI NOR flash is present. Download the auxiliary image to ITCM via the debugger. eMMC POR boot is not supported with this variant -- a new debugger download-and-run cycle is required after each power-on.

Build with target `ram_only_debug` (or `ram_only_release`).

## Downloading an image to eMMC

- **blhost**: to enable eMMC POR boot, the image written to eMMC must be a bootable image containing a valid USDHC boot header. For the download command, refer to the blhost page in this guide.
- **SPSDK**: requires the raw binary without a boot header; SPSDK attaches the header during the programming process. For the steps, refer to the SPSDK page in this guide.
