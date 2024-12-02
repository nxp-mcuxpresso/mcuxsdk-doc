# Install Xtensa On Chip Debugger Daemon

The Xtensa On Chip Debugger Daemon \(xt-ocd\), is a powerful gdb-based debugging tool. It is not installed by default with the Xplorer IDE. A self-extracting executable installer is included with the IDE, which can be found at the following location:

**Windows**

```
C:\usr\xt-ocd-14.11-windows64-installer.exe
```

**Linux**

```
~/xtensa/XtDevTools/downloads/RI-2023.11/tools/xt-ocd-14.11-linux64-installerr
```

At this moment xt-ocd supports J-Link and ARM RVI/DSTREAM probes over Serial Wire Debug \(SWD\) for RT500. xt-ocd installs support for J-Link probes but does not install the required J-Link drivers which must be installed separately. The RT500 requires J-Link software version 6.46 or newer.

**Note:** When installing xt-ocd on Linux, you must manually add a symlink to the installed J-Link driver:

```
ln -s <jlink-install-dir>libjlinkarm.so.6 <xocd-install-dir>/modules/libjlinkarm.so.6
```

xt-ocd is configured with an XML input file ‘topology.xml’ that you will need to modify to fit your debugger hardware. Using J-link as example, use below content to replace the original template.

**Note:** You must replace ‘usbser’ section to your own JINK serial number \(9 digits number on the back of the J-Link hardware\).

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

Below showing another topology.xml example for ARM RealView ICE \(RVI\) and DSTREAM debug probes.

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

Congratulations! Now you have all Xplorer toolchains installed.

For more details, about Xtensa software tools, build configurations, or xt-ocd daemon, see the full set of documents in Xplorer menu **Help \> PDF Documentation**.

**Parent topic:**[Install Xplorer Toolchains](../topics/install_xplorer_toolchains.md)

