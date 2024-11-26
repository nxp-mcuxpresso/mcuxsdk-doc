# Start Xtensa Debugger Daemon

To debug DSP applications on RT600, ensure that the xt-ocd daemon is running. This application runs a gdb server that the Xtensa core debugger connects to.

Go to the command-line window and change directory \(cd\) to xt-ocd daemon installation path. The default path on Windows is `C:\Program Files (x86)\Tensilica\Xtensa OCD Daemon 14.08`.

Execute the daemon with the custom topology.

```
**xt-ocd.exe -c topology.xml**
XOCD <VERSION_INFO>
(c) 1999-2021 Cadence Design Systems Inc. All rights reserved.
[Debug Log 2021-06-17 08:12:29]
Loading module "gdbstub" <VERSION_INFO>
Loading module "jlink" <VERSION_INFO>
Using JLINK lib <VERSION_INFO>
Jlink USB Serial Number: XXXXXXXXX
Connected to Jlink Device:
  Name:'J-Link LPCXpresso V2 compiled Apr  4 2019 16:54:03'
  S/N:XXXXXXXX
  Firmware: J-Link LPCXpresso V2 compiled Apr  4 2019 16:54:03
  Requested/Set TCK: 2000kHz/65534kHz
Jlink: Select SWD
SWD-DP with ID 0x6BA02477
Loading module "jtag" <VERSION_INFO>
Loading module "xtensa" <VERSION_INFO>
Starting thread 'GDBStub'
Opened GDB socket at port 20000
Initialize XDM driver
Warning: Warning: DAP Reset request failed! Ignoring...
```

**Note:** Some warning messages are expected and can be ignored. If you receive an error initializing the XDM driver, initialize and start the DSP core before debugging. For details on initializing and debugging, see [Initialize DSP Core](initialize_dsp_core.md) and [Link DSP Profiles](link_dsp_profiles.md). For details on xt-ocd runtime options and configuration, see Chapter 7 of the Xtensa Debug Guide, available in **Help \> PDF Documentation**.

**Parent topic:**[Run and Debug DSP Demo using Xplorer IDE](../topics/run_and_debug_dsp_demo_using_xplorer_ide.md)

