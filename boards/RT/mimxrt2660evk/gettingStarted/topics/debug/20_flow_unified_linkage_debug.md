# Flow -- Unified Linkage Debug

Applies to all five Unified Linkage targets: `debug`, `xspi_nor`, `xspi_nor_psram`, `psram`, `psram_txt`.

All Unified Linkage targets program the image into XSPI NOR flash as part of the debug flow. The image supports POR boot directly -- pull the debugger, cycle power, and the board boots the image on its own without any additional steps.

---

## Unified Linkage Debug

```
Step 1.  Install debug patch
         (see Patch Install section)

Step 2.  Set boot switch to 0b00  (XSPI NOR boot mode)

Step 3.  Build with the chosen Unified Linkage target

Step 4.  IDE setup
         [Ozone]
           - Create Ozone project, set PC/SP in the New Project Wizard
           - Save project, then hand-edit .jdebug  (one-time per project)
           - (see Ozone Setup section)
         [IAR C-SPY]
           - Open the SDK .eww file, select the target configuration
           - (see IAR Setup section)

Step 5.  Download and debug
         [Ozone]  Click Debug -- Ozone programs XSPI NOR flash then starts execution
         [IAR]    Download and debug -- IAR programs XSPI NOR flash then starts execution

--> DONE
```
