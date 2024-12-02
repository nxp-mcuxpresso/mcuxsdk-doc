# Install Xtensa Software Tools without IDE

The Xtensa Software Tools optionally be installed without the use of the IDE, which may be desired for use in a command-line only Linux environment, or for better compatibility with an unsupported Linux environment.

The command-line tools package is available as a redistributable zip file that is extracted with an Xplorer IDE install. The IDE must be installed one time in your organization to gain access to the tools package, which is then available at:

```
~/xtensa/XtDevTools/downloads/RI-2023.11/tools/ XtensaTools_RI_2023_11_linux.tgzz
```

With the tools package and the DSP Build Configuration package available from, the Tensilica Tools download site \(see [Xtensa Software Tools Platform Support](xtensa_software_tools_platform_support.md), the toolchain can be set up as follows.

```
# Create Xtensa install root
mkdir -p ~/xtensa/tools
mkdir -p ~/xtensa/builds
# Set up the configuration-independent Xtensa Tool:
tar zxvf XtensaTools_RI_2023_11_linux.tgz -C ~/xtensa/tools
# Set up the configuration-specific core files:
tar zxvf nxp_RT500_RI23_11_newlib_linux_redist.tgz -C ~/xtensa/builds
# Install the Xtensa development toolchain:
cd ~/xtensa./builds/RI-2023.11-linux/nxp_RT500_RI23_11_newlib/install
\--xtensa-tools./tools/RI-2023.11-linux/XtensaTools \
--registry ./tools/RI-2023.11-linux/XtensaTools/config
```

**Parent topic:**[Install Xplorer Toolchains](../topics/install_xplorer_toolchains.md)

