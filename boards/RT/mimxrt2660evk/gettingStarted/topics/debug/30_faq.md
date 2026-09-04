# FAQ / Known Issues

## A. Install and environment

### A1. Device picker doesn't show `MIMXRT2663xxxxx_M85`

**Cause**: J-Link patch not installed, or copied to the wrong directory.

**Fix**: Re-do the J-Link patch install (see the debug patch install page). Check:

- Path is `C:\Users\<username>\AppData\Roaming\SEGGER\JLinkDevices\NXP\iMXRT2660\` (per-user AppData, **not** Program Files).
- `iMXRT2660.xml` and `iMXRT2660_M85.jlinkscript` sit directly there (no extra nesting).
- No older RT2660 patch is competing nearby — remove it if so.

### A2. jlinkscript reports "Cortex-M85 not recognized"

**Cause**: J-Link DLL older than V8.88 — doesn't define the `CORTEX_M85` script constant that the RT2660 jlinkscript references.

**Fix**: Upgrade J-Link to V8.88 or later (see the patch install section of this guide), then run `JLinkDLLUpdater.exe` to sync IDE-bundled DLLs.

### A3. How do I know which version of the J-Link patch is actually loaded?

A stale patch in some other `JLinkDevices\` tree can win the load order — device picker still shows `MIMXRT2663xxxxx_M85`, but the running jlinkscript isn't yours.

**Diagnostic**: The patch prints a banner on every connect:

```
iMXRT2660 Cortex-M85 core J-Link script - VX.Y
```

Where to find the log:

- **Ozone** — console pane at the bottom (J-Link tab).
- **IAR EWARM** — Debug Log.
- **JLinkGDBServer** — process stdout / GUI log window.

Missing banner — old / pre-banner patch loaded. Wrong version — stale patch winning.

If the banner shows the wrong version, search all `JLinkDevices` trees (per-user, system-wide, IDE-bundled), move out any competing `NXP\iMXRT2660\` folder, re-install per the patch install section of this guide, and confirm the banner again.

## B. Debug behavior and source-level issues

### B1. Ozone downloads OK but the target doesn't run correctly

This applies to Unified Linkage targets. The `.jdebug` requires a one-time manual edit to configure PC / SP correctly; skipping this step causes incorrect execution. See the Ozone setup section of this guide.

### B2. Ozone stops on the right instruction but source view is wrong (IAR ELF)

**Symptom**: `debug` / `psram` / `psram_txt` built with **IAR EWARM**, loaded in **Ozone**. PC halts at correct addresses but the source view sits on the wrong line or doesn't follow PC. Registers / disassembly / memory windows work.

**Cause**: Ozone-vs-IAR ELF DWARF compatibility issue (debugger / ELF-format level, not a bug in the SDK example or J-Link patch). This is a known issue.

### B3. Editing PSRAM (`0x80000000`–`0xAFFFFFFF`) from the IDE memory window doesn't stick

**Symptom**: In Ozone (or another J-Link-driven IDE), changing a value at a PSRAM address through the memory / watch window failed.

**Fix**: Upgrade to J-Link patch **V0.5 or later**. Confirm the loaded patch version via the banner check (see A3).

## C. Bricking and recovery

### C1. J-Link connect shows `ROM Ver = 0xFFFFFFFF` (or the debugger can't attach)

Most commonly seen with targets that write to flash (Unified Linkage targets), but can happen with any scenario where a bad image ends up in flash.

**Cause**: A previously-programmed image hung the SoC bus. All debugger reads return `0xFF`. Reset doesn't help — boot ROM keeps handing control back to the bad image in flash.

**Recovery**:

1. Flip the **boot switch** to **serial download mode** (`0b10`, SDP MODE, on MIMXRT2660-EVK) — boot ROM enters its serial loader instead of jumping into flash, bus stays clean.
2. **Reset** the board.
3. Start a normal debug / download session — flash loader runs, programs your new (good) image.
4. Flip the boot switch back to **flash NOR boot mode** (`0b00`, XSPI0-NOR, on MIMXRT2660-EVK).
5. Reset — should boot the new image cleanly.

### C2. Prevention: manual "brake" to avoid bricking during clock / power setup

Applicable to any target. Particularly useful during Unified Linkage bring-up where each bricking cycle requires the multi-step boot-switch recovery in C1.

When you're iterating on code that touches sensitive clock / power / bus rails (say `POWER_EnterHpRun()`, PLL, LDO), one bad config can hang the SoC and force the multi-step boot-switch recovery above every cycle. Add a debugger-gated brake before the risky call:

```c
volatile uint32_t gTest;   /* file-scope; BSS-init to 0 */

void BOARD_InitBootClocks(void)
{
    /* ... normal clock / mux setup ... */

    while (gTest == 0);   /* Manual brake -- set gTest=1 in the debugger to proceed */
    POWER_EnterHpRun(BOARD_BootClockHPRUN);
}
```

**Usage**:

1. Execution halts on `while (gTest == 0);`.
2. Ozone: **Watched Data** (View -> Watched Data), add `gTest`, set to `1` (any non-zero).
3. Continue — execution falls through to `POWER_EnterHpRun`.

**If `POWER_EnterHpRun` hangs the SoC**, the debugger loses connection (SoC bus hung). **Reset the board** — startup re-runs, `gTest` re-zeroes, execution stops at the brake again, and the debugger can reconnect cleanly. **No boot-switch recovery needed** — that's the whole point of the brake.

**`volatile` matters**: without it, the optimizer rewrites the loop as `while (1);` (no C-visible writer to `gTest`); the debugger's RAM write becomes dead-storage.

**Cautions**:

- Wrap in `#if DEBUG_BRICK_BRAKE` or remove before shipping — a shipped image spins forever without a debugger.
- Only protects the call site it's in front of. Other paths (ISRs, second-stage init) can still brick.
- Forgetting to set `gTest` on every power-on = image spins forever until you set it or reflash. It's a brake, not a fix.

## Getting help

For questions about the debug patch, the debug flow, or hardware / rework, contact your NXP representative or use the NXP Community.
