# Install Xtensa On Chip Debugger Daemon

The Xtensa On Chip Debugger Daemon \(xt-ocd\), is a gdb-based debugging tool but is not installed by default with the Xplorer IDE. For installation, a self-extracting executable installer is included with the IDE, which can be found at the following location:

**Windows:**

`C:\usr\xtensa\XtDevTools\downloads\RI-2023.11\tools\xt-ocd-14.11-windows64-installer.exe`

**Linux:**

`~/xtensa/XtDevTools/downloads/RI-2023.11/tools/xt-ocd-14.11-linux64-installer`

Currently, xt-ocd supports J-Link and Arm RVI/DSTREAM probes over Serial Wire Debug \(SWD\) for RT600. xt-ocd installs support for J-Link probes but does not install the required J-Link drivers which must be installed separately. Make sure that the latest version of J-Link software is installed.

**Note:** **For Linux:** When installing xt-ocd on Linux, ensure that the symlink is manually added to the installed J-Link driver: `ln -s <jlink-install-dir>libjlinkarm.so.6 <xocd-install-dir>/modules/libjlinkarm.so.6`.

xt-ocd is configured with an XML input file ‘topology.xml’ that modifies to fit the debugger hardware. Using J-link as an example, use the content below to replace the original template.

**Note:** It is mandatory to replace the ‘usbser’ section with the 9-digits number J-Link serial number on the back of the J-Link hardware in use.

```
<configuration>
  <controller id='Controller0' module='jlink' usbser='600100000' type='swd' speed='1000000' locking='1'/>
  <driver id='XtensaDriver0' dap='1' xdm-id='12' module='xtensa' step-intr='mask,stepover,setps' />
  <chain controller='Controller0'>
    <tap id='TAP0' irwidth='4' />
  </chain>
  <system module='jtag'>
    <component id='Component0' tap='TAP0' config='trax' />
  </system>
  <device id='Xtensa0' component='Component0' driver='XtensaDriver0' ap-sel='3' />
  <application id='GDBStub' module='gdbstub' port='20000' sys-reset='0'>
    <target device='Xtensa0' />
  </application>
</configuration>
```

Below is another topology.xml example if Arm RealView ICE \(RVI\) and DSTREAM debug probes is used.

```
<configuration>
  <controller id='Controller0' module='rvi' />
  <driver id='XtensaDriver0' debug='' inst-verify='mem' module='xtensa' step-intr='mask,stepover,setps'/>
  <driver id='TraxDriver0'   module='trax' />
  <chain controller='Controller0'>
    <tap id='TAP0' irwidth='4' />
  </chain>
  <system module='jtag'>
    <component id='Component0' tap='TAP0' config='trax' />
  </system>
  <device id='Xtensa0' component='Component0' driver='XtensaDriver0' xdm-id='12' />
  <device id='Trax0'   component='Component0' driver='TraxDriver0' xdm-id='12' />
  <application id='GDBStub' module='gdbstub' port='20000' >
    <target device='Xtensa0' />
  </application>
  <application id='TraxApp' module='traxapp' port='11444'>
    <target device='Trax0' />
  </application>
</configuration>
```

Congratulations! All Xplorer toolchains are installed.

For more details on Xtensa software tools, build configurations, or xt-ocd daemon, see the full set of documents in Xplorer menu **Help \> PDF Documentation**.

**Parent topic:**[Install Xplorer Toolchains](../topics/install_xplorer_toolchains.md)

