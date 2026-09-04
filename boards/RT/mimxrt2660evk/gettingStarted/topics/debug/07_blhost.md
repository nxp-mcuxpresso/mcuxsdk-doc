# blhost

blhost is NXP's command-line host tool for communicating with the RT2660 Boot ROM in serial download mode (SDP).

## Prerequisites

1. Install Python 3.8 or later.
2. Obtain the `blhost` tool. `blhost` is distributed as part of NXP's Secure Provisioning SDK (SPSDK) / MCUXpresso Secure Provisioning Tool, available from the [NXP website](https://www.nxp.com/spsdk). Install SPSDK (`pip install spsdk`) or download the standalone tool package from NXP, then use the following supporting files (helper scripts and test image ship with the SDK example resources for eMMC boot):
   - `blhost` / `blhost.exe` -- the blhost executable (from SPSDK / the NXP tool package).
   - `write_emmc.py`, `read_emmc.py`, `erase_emmc.py` -- Python helper scripts for eMMC read/write/erase.
   - `write_fuse_boot_cfg0.py` -- programs BOOT_CFG0 to configure eMMC boot mode.
   - `read_fuse_boot_cfg0.py` -- reads the current BOOT_CFG0 value.
   - `ahab_serial_flashloader_plain_secp521r1.bin` -- serial flashloader required by Python helper scripts.
   - `eMMC-bootable-hello_world.bin` -- pre-built test image for quick eMMC boot verification.
3. Ensure `blhost` (`blhost.exe`) is on your system PATH, or run commands from its install directory.
4. Set the MIMXRT2660-EVK boot switch to **serial download mode** (`0b10`, SDP MODE).
5. Reset the board -- the Boot ROM enters SDP and waits for a host connection.
6. Identify the COM port (USB-CDC or UART) that blhost should connect to.

Verify connectivity:

```
blhost -p COM35 -- get-property 1
```

Expected output:

```
Ping responded in 1 attempt(s)
Inject command 'get-property'
Response status = 0 (0x0) Success.
Response word 1 = 1258487809 (0x4b030001)
Current Version = K3.0.1
```

> **Note**: on Linux, use `blhost` instead of `blhost.exe` and adapt the COM port to a device path such as `/dev/ttyUSB0`.

## Configuring BOOT_CFG0 for eMMC boot

> **Warning**: fuse programming is irreversible. Do not execute if BOOT_CFG0 is already programmed to the correct value.

Two scripts are provided for BOOT_CFG0 operations:

- `read_fuse_boot_cfg0.py` -- reads BOOT_CFG0 (fuse index `0x18`). The current value is shown in `Response word 2` of the output.
- `write_fuse_boot_cfg0.py` -- programs BOOT_CFG0 to a specified value. Requires a flashloader; loads it automatically.

**Step 1.** Set boot switch to `0b10` (SDP mode) and reset the board.

**Step 2.** Read BOOT_CFG0 to check the current state before programming:

```
py read_fuse_boot_cfg0.py -p COM35
```

Options:
- `-p <COM_PORT>` -- COM port (default: `COM35`)

The script runs several blhost commands in sequence. The last step is `efuse-read-once` and its output shows the current BOOT_CFG0 value (example output with fuse not yet programmed):

```
>> blhost.exe -p COM35,115200 -- efuse-read-once 0x18
Ping responded in 1 attempt(s)
Inject command 'efuse-read-once'
Response status = 0 (0x0) Success.
Response word 1 = 4 (0x4)
Response word 2 = 0 (0x0)
```

`Response word 2` is the BOOT_CFG0 value. If it already reads `0x00000082`, BOOT_CFG0 is already configured for eMMC boot -- stop here, no further action is needed.

> **Note**: reset the board to re-enter SDP before the next step.

**Step 3.** Program BOOT_CFG0 to eMMC boot mode:

```
py write_fuse_boot_cfg0.py -p COM35 -v 0x00000082
```

Options:
- `-p <COM_PORT>` -- COM port (default: `COM35`)
- `-v <value>` -- BOOT_CFG0 value to program (`0x82` or `0x00000082` = eMMC boot mode for MIMXRT2660-EVK)

> **Note**: reset the board to re-enter SDP before the next step.

**Step 4.** Read back BOOT_CFG0 to verify:

```
py read_fuse_boot_cfg0.py -p COM35
```

`Response word 2` should now read `0x00000082`.

## eMMC operations

> **Note**: after each operation below, the Boot ROM exits SDP. Reset the board before starting the next operation to re-enter SDP.

### Writing an image to eMMC

Use `write_emmc.py` to write a bootable image to eMMC. The script handles the full sequence: loading the serial flashloader, configuring eMMC, erasing, and writing the image.

> **Note**: before writing, the script erases a region sized to the image file size rounded up to the next 256 KB boundary.

To enable eMMC POR boot, the image written to eMMC must be a bootable image containing a valid USDHC boot header.

The supporting resources include a pre-built test image `eMMC-bootable-hello_world.bin` that already contains a valid USDHC boot header and can be used to verify the full flow without building from source.

```
py write_emmc.py -p COM35 -i eMMC-bootable-hello_world.bin
```

Options:
- `-p <COM_PORT>` -- COM port (default: `COM35`)
- `-i <image.bin>` -- image file to write (default: `eMMC-bootable-hello_world.bin`)

After a successful boot, the UART will print:

```
Boot from eMMC,  Sep 20 2026 18:58:19
Shadow Fuse (BOOT CFG0) = 0x00000082
Reset Type = 0x00000200, Reset Cnt = 2
  Reset Type BIT0 = POR_VBAT    reset
  Reset Type BIT2 = POR_b pin   reset
  Reset Type BIT8 = RESET_b pin reset
  Reset Type BIT9 = Software    reset
main = 0x8800745D, SystemCoreClock = 0x88800000, 999MHz
MCUX SDK version: 2026.09.00
hello world.
```

### Reading from eMMC

```
py read_emmc.py -p COM35 -a 0 -n 0x20000 -o emmc.bin
```

Options:
- `-p <COM_PORT>` -- COM port (default: `COM35`)
- `-a <address>` -- start address
- `-n <size>` -- number of bytes to read
- `-o <output.bin>` -- output file

### Erasing eMMC

> **Note**: the script automatically rounds up the erase size to the next 256 KB boundary.

```
py erase_emmc.py -p COM35 -a 0 -n 0x20000
```

Options:
- `-p <COM_PORT>` -- COM port (default: `COM35`)
- `-a <address>` -- start address
- `-n <size>` -- number of bytes to erase
