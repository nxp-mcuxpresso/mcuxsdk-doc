# Start Xtensa Debugger Daemon

To debug DSP applications on RT700, ensure that the xt-ocd daemon is running. This application runs a gdb server that the Xtensa core debugger connects to.

Go to the command-line window and change directory \(cd\) to xt-ocd daemon installation path. The default path on Windows is `C:\Program Files (x86)\Tensilica\Xtensa OCD Daemon 14.11`.

Execute the daemon with the custom topology.

```
**xt-ocd.exe -c topology.xml**
XOCD 14.11 2023-04-06 14:27:20
(c) 1999-2024 Cadence Design Systems Inc. All rights reserved.
[Debug Log 2024-02-19 22:41:53]
Loading module "gdbstub" v2.0.0.12
Loading module "jlink" v2.0.2.0
Using JLINK lib v.79410
Jlink USB Serial Number: 851006054
Connected to Jlink Device:
  Name:'SEGGER J-Link'
  S/N:851006054
  Firmware: J-Link V11 compiled Dec  4 2023 10:22:45
  Requested/Set TCK: 1000kHz/1000kHz
Jlink: Select pipelined SWD
SWD-DP with ID 0x6BA02477
Loading module "jtag" v2.0.0.20
Loading module "xtensa" v2.0.0.48
Starting thread 'GDBStub'
Opened GDB socket at port 20000
Initialize XDM driver
Warning: Warning: DAP Reset request failed! Ignoring...
```

**Note:** Some warning messages are expected and can be ignored. If you receive an error initializing the XDM driver, initialize and start the DSP core before debugging. For details on initializing and debugging, see [Initialize DSP Core](initialize_dsp_core.md) and [Link DSP Profiles](link_dsp_profiles.md).

**Parent topic:**[Run and Debug DSP Demo using Xplorer IDE](../topics/run_and_debug_dsp_demo_using_xplorer_ide.md)

