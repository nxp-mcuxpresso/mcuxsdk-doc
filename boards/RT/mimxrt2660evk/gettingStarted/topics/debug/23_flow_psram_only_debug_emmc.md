# Flow -- `psram_only` Debug (eMMC + PSRAM system)

Three complete end-to-end flows are provided. Each flow covers hardware rework, eMMC programming, boot mode configuration, and the debug session. Choose the flow that matches your boot mode setup.

> **Note**: "blhost" in the steps below refers to NXP's serial download host tool. SPSDK can also be used -- it communicates with the Boot ROM through the same underlying protocol. Refer to the blhost and SPSDK sections of this guide for usage details.

---

## `psram_only` Debug -- eMMC + PSRAM, shadow fuse via xspi_nor auxiliary (recommended)

> **POR boot**: the debug image is loaded into PSRAM by the debugger and is cleared on power cycle -- not POR bootable. The PSRAM auxiliary in eMMC POR boots automatically on every power-on (persistent via shadow fuse in XSPI NOR flash).

Shadow fuse is set by an xspi_nor auxiliary programmed into XSPI NOR flash. Persistent across power cycles -- no debugger intervention needed after each power-on.

The one-time setup (steps 2-a through 2-h) is required before the first debug session on each board. Skip to step 3 if already done.

```
Step 1.   Install debug patch
          (see Patch Install section)

[One-time setup -- first time only]

Step 2-a. Hardware rework
          (see HardwareAdaption/eMMC_HW_Rework)

Step 2-b. Build PSRAM auxiliary demo
          target: psram_only
          (USDHC boot header enabled by default)

Step 2-c. Set boot switch to 0b10  (SDP mode)

Step 2-d. blhost: program PSRAM auxiliary binary to eMMC
          (see blhost section)

Step 2-e. Build shadow fuse auxiliary
          target: xspi_nor_debug

Step 2-f. Set boot switch to 0b00  (XSPI NOR boot mode)

Step 2-g. Program shadow fuse auxiliary into XSPI NOR flash
          (standard Unified Linkage flash flow)

Step 2-h. Reset
          Shadow fuse auxiliary runs from flash, writes shadow fuse, warm resets
          Boot ROM reads shadow fuse, boots from eMMC
          PSRAM auxiliary runs -- PSRAM initialized on every reset from now on

[Debug session -- every time]

Step 3.   Build with psram_only target

Step 4.   Connect debugger

Step 5.   Download ELF to PSRAM and debug

--> DONE
```

> **Note**: if an IDE debug download of a Unified Linkage image fails with a verification error after the auxiliary setup, refer to the eMMC Boot section of this guide for the cause and recovery steps.

---

## `psram_only` Debug -- eMMC + PSRAM, shadow fuse via ram_only auxiliary

> **POR boot**: the debug image is loaded into PSRAM by the debugger and is cleared on power cycle -- not POR bootable. The PSRAM auxiliary in eMMC boots automatically after each shadow fuse setup, but the shadow fuse must be re-established by the debugger after each power-on.

Shadow fuse is set by a ram_only auxiliary downloaded by the debugger. Shadow fuse is volatile -- steps 4-8 must be repeated after each power-on.

The one-time setup (steps 2-a through 2-d) is required before the first debug session on each board. If the PSRAM auxiliary is already programmed to eMMC, skip steps 2-a through 2-d and proceed to the "After each power-on" section.

```
Step 1.   Install debug patch
          (see Patch Install section)

[One-time setup -- first time only]

Step 2-a. Hardware rework
          (see HardwareAdaption/eMMC_HW_Rework)

Step 2-b. Build PSRAM auxiliary demo
          target: psram_only
          (USDHC boot header enabled by default)

Step 2-c. Set boot switch to 0b10  (SDP mode)

Step 2-d. blhost: program PSRAM auxiliary binary to eMMC
          (see blhost section)

[After each power-on]

Step 3.   Build shadow fuse auxiliary
          target: ram_only_debug

Step 4.   Set boot switch to 0b00  (XSPI NOR boot mode)

Step 5.   Debugger: download and run shadow fuse auxiliary to ITCM
          Auxiliary writes shadow fuse, warm resets before reaching main()
          Boot ROM reads shadow fuse, boots from eMMC
          PSRAM auxiliary runs -- PSRAM initialized

Step 6.   Reconnect debugger

Step 7.   Build with psram_only target

Step 8.   Download ELF to PSRAM and debug

--> DONE  (repeat steps 4-8 after each power-on)
```

---

## `psram_only` Debug -- eMMC + PSRAM, fuse (production)

> **POR boot**: the debug image is loaded into PSRAM by the debugger and is cleared on power cycle -- not POR bootable. The PSRAM auxiliary in eMMC POR boots automatically on every power-on (permanent via fuse).

> **Warning**: fuse programming is irreversible.

The one-time setup (steps 2-a through 2-g) is required before the first debug session on each board. Skip to step 3 if already done.

```
Step 1.   Install debug patch
          (see Patch Install section)

[One-time setup -- first time only]

Step 2-a. Hardware rework
          (see HardwareAdaption/eMMC_HW_Rework)

Step 2-b. Build PSRAM auxiliary demo
          target: psram_only
          (USDHC boot header enabled by default)

Step 2-c. Set boot switch to 0b10  (SDP mode)

Step 2-d. blhost: program PSRAM auxiliary binary to eMMC
          (see blhost section)

Step 2-e. blhost: program BOOT_CFG0 fuse
          (see blhost section)

Step 2-f. Set boot switch to 0b00  (XSPI NOR boot mode)

Step 2-g. Reset
          Boot ROM reads fuse, boots from eMMC
          PSRAM auxiliary runs -- PSRAM initialized on every reset from now on

[Debug session -- every time]

Step 3.   Build with psram_only target

Step 4.   Connect debugger

Step 5.   Download ELF to PSRAM and debug

--> DONE
```
