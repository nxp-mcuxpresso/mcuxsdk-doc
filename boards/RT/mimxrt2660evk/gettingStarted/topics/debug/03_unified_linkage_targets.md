# Unified Linkage Targets

This page explains the Unified Linkage boot and debug mechanism in detail. All five Unified Linkage targets share the same linker template, startup code, and debug entry sequence.

> **Scope**: everything on this page describes the **Unified Linkage** flow. When legacy RT1xxx RAM-target behavior is discussed for comparison, it is explicitly labeled as "legacy RT1xxx".

## What is Unified Linkage?

Every Unified Linkage SDK example is **linked, packaged, and flashed the same way**, regardless of which of the five target variants is being built:

- **Storage is always XSPI NOR flash** -- every section's **LMA** (Load Memory Address) is in flash.
- **Startup always runs XIP from flash.** The Boot ROM jumps to the reset vector, which lives in flash, and startup begins executing from there.
- **Non-startup code placement varies per target.** After startup, `main()` and the rest of the application code either stay XIP in flash, or are copied to ITCM / PSRAM before `main()` is called.
- **Working data placement also varies per target** -- DTCM or PSRAM, depending on the target.

"Startup" here means the **user-image code between Reset_Handler and `main()`** -- not the Boot ROM itself.

The "unified" part is that all five targets share a consistent linker template (region names, section handling), the same startup source, and the same debug entry sequence. Only the memory addresses differ between targets.

## Comparison with the legacy RT1xxx RAM-target flow

In the legacy RT1xxx model, a typical RAM-target debug session works like this:

1. Debugger connects.
2. Debugger downloads the image directly into RAM (TCM, SRAM, or PSRAM).
3. Debugger sets PC to the reset vector and hits Go.
4. Code runs from RAM. Flash is never touched.

Unified Linkage is fundamentally different.

### Side-by-side comparison

| | RAM target (legacy RT1xxx) | Unified Linkage |
|---|---|---|
| Where the image lives | Downloaded to RAM at debug time | Programmed into XSPI NOR flash |
| Survives power cycle | No -- RAM is volatile | Yes -- flash is non-volatile |
| Boot without debugger | No -- needs debugger to load | Yes -- POR-boots on its own |
| Debug iteration speed | Fast -- RAM download | Slower -- flash program each cycle |
| Debugger role | Just a loader | Flash programmer |
| Recovery from a bad image | Just reset -- RAM is empty | Boot-switch recovery required |
| Code size limit | RAM size | XSPI NOR size (large) |
| Production realism | Different from production boot | Same boot path as production |

### The key mental shift

"RAM target" and "non-XIP" mean different things in the two flows, even though the observable behavior looks the same (code ends up running from RAM).

- In the **legacy RT1xxx model**: code is linked to RAM addresses, the debugger downloads it directly to RAM, and it executes from there. Flash is never involved.
- In **Unified Linkage**: a non-XIP target (`debug`, `psram`, `psram_txt`) still programs the image into flash. Startup runs XIP from flash and copies the application code to its RAM VMA before calling `main()`.

**In Unified Linkage, "code runs from RAM" does NOT mean flash is not involved.** Every Unified Linkage target programs XSPI NOR flash and boots XIP from there.

## Trade-offs

**Why Unified Linkage wins for SDK examples:**

- **Images match production.** The boot path, section layout, and startup code are identical to what a real product image would use. Bugs that only appear during real boot (uninitialized data, wrong section attributes, boot-header errors) are caught during development instead of at deployment.
- **Standalone POR boot.** Pull the debugger, cycle power, and the image comes up on its own. Enables hands-off testing, POR-timing measurements, and demos without a debugger cable.
- **Debugger support is hardware-independent.** The debugger programs flash and steps back -- it never needs to initialize external memory. Swapping the XSPI NOR flash chip or the PSRAM chip doesn't require any changes to the debug script; external memory initialization is handled by Boot ROM reading the boot header, not by the debugger.

**What you pay for it:**

- **Slower iteration.** Every code change triggers a flash program cycle, which is noticeably slower than a RAM download.
- **Worse failure modes.** A bad image in flash keeps booting on every reset until the boot switch is used to break the cycle. Legacy RT1xxx RAM-target failures disappear on their own after a reset.

## Common misconceptions

- **"`debug` means it runs from ITCM without flash."** No. In Unified Linkage, the `debug` target still programs the image into flash and boots XIP from flash. Startup copies the non-startup code to ITCM and jumps there, but the image, boot flow, and startup code are always in flash.

- **"Power cycle clears the image."** No. Flash is non-volatile. If a bad image bricked the board before power-off, the same bad image runs again after power-on. Use the boot switch to break out of the loop.

- **"I can download the image directly to RAM and skip the flash step."** This won't work. The reset vector points into flash, startup lives in flash, and even the "code in RAM" targets rely on flash-resident startup to perform the copy. Bypassing flash bypasses the entire boot flow.

- **"It's a debug target, so it won't POR-boot without a debugger."** Every Unified Linkage target POR-boots because the image is in flash. If yours doesn't, that's a bug in the image (or a bricked SoC), not a limitation of the target type.
