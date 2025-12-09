# SDK Builder

Download customized MCUXpresso SDK packages using the online SDK Builder tool.

## Overview

The SDK Builder (https://mcuxpresso.nxp.com/) provides a web-based interface to create customized SDK packages with:
- Board-specific configurations
- Selected middleware components
- Chosen toolchain support
- Example applications
- Documentation

This method is ideal for:
- Offline development environments
- Classic IDE workflows (IAR, Keil, MCUXpresso IDE)
- Controlled SDK versions
- Environments with limited internet access

## Accessing SDK Builder

### Step 1: Navigate to SDK Builder

Visit: https://mcuxpresso.nxp.com/

### Step 2: Select Your Board

1. Click **Select Development Board**
2. Browse or search for your board (e.g., "FRDM-MCXW23")
3. Click on your board to select it

Alternatively, select by processor:
1. Click **Select a Processor**
2. Choose your MCU family and specific part number

### Step 3: Review Board Information

The SDK Builder displays:
- Board overview and features
- Supported peripherals
- Available middleware
- Documentation links

## Configuring Your SDK Package

### Toolchain Selection

Select the toolchains you plan to use:

- ☑ **MCUXpresso IDE** - NXP's Eclipse-based IDE
- ☑ **IAR Embedded Workbench** - Professional development environment
- ☑ **Keil MDK** - ARM ecosystem integration
- ☑ **ARMGCC / VSCODE** - Open-source toolchain

**Recommendation:** Select toolchain you might use, the ARMGCC / VSCODE is exclusive option comparing to others.

### Operating System Selection

Choose RTOS support:

- ☑ **Bare Metal** - No RTOS, direct hardware access
- ☑ **FreeRTOS** - Popular open-source RTOS
- ☐ **Zephyr** - (Use GitHub installation for Zephyr)

**Recommendation:** Include FreeRTOS even for bare-metal projects. Examples are valuable learning resources.

### Middleware Components

Select middleware based on your application needs:

**Connectivity:**
- ☑ USB Stack - USB device/host/OTG support
- ☑ lwIP - Lightweight TCP/IP stack
- ☑ FatFs - FAT file system
- ☐ Ethernet - If your board has Ethernet

**Wireless:**
- ☑ Bluetooth LE - For BLE-enabled MCUs
- ☑ IEEE 802.15.4 - For Thread/Zigbee applications
- ☐ Wi-Fi - If using Wi-Fi modules

**Graphics:**
- ☐ emWin - GUI library (if using displays)
- ☐ LVGL - Open-source GUI library

**Security:**
- ☑ mbedTLS - Cryptographic library
- ☐ Secure Subsystem - For secure boot/TrustZone

**Audio/Voice:**
- ☐ Voice Seeker - Voice recognition
- ☐ Audio Processing - DSP libraries

**Machine Learning:**
- ☐ eIQ - ML inference engines
- ☐ TensorFlow Lite Micro

**Tip:** Start with minimal selection. You can always download additional components later.

### Example Applications

Choose example categories:

- ☑ **demo_apps** - Full-featured demonstrations
- ☑ **driver_examples** - Peripheral driver examples
- ☑ **hello_world** - Basic getting started example
- ☐ **rtos_examples** - RTOS usage examples
- ☐ **usb_examples** - USB stack examples
- ☐ **middleware_examples** - Middleware demonstrations

**Recommendation:** Include `demo_apps` and `driver_examples` for comprehensive learning resources.

## Downloading the SDK

### Step 1: Review Configuration

Click **Review Configuration** to see your selections:
- Total package size estimate
- Included components list
- Toolchain support

### Step 2: Download

1. Click **Download SDK**
2. Accept the license agreement
3. Optionally provide email for notifications
4. Click **Download**

The SDK downloads as a ZIP archive (typically 500 MB - 2 GB depending on selections).

### Step 3: Save the Archive

Save the ZIP file to a known location:
- `C:\MCUXpresso\SDKs\` (Windows)
- `~/MCUXpresso/SDKs/` (Linux/macOS)

**Tip:** Include board name and version in filename:
- `SDK_2.15.0_FRDM-MCXW23.zip`

## Installing the Downloaded SDK

### For MCUXpresso IDE

1. Open MCUXpresso IDE
2. **Window → Preferences → MCUXpresso SDK**
3. Click **Import SDK Archive**
4. Browse to downloaded ZIP file
5. Click **OK**

The SDK is now available for project creation.

### For IAR Embedded Workbench

1. Extract the ZIP archive to a permanent location
2. Open IAR EWARM
3. Navigate to extracted SDK folder
4. Open example projects from `boards/<board>/iar_examples/`

### For Keil MDK

1. Extract the ZIP archive
2. Install CMSIS Pack from SDK:
   - Navigate to `<SDK>/CMSIS_Packs/`
   - Double-click the `.pack` file to install
3. Open Keil µVision
4. Create new project using installed pack

### For Command Line (ARM GCC)

1. Extract the ZIP archive to a permanent location
2. Navigate to the `mcuxsdk` folder, build specified example:

```bash
west build -b your_board examples/demo_apps/hello_world
```

## Package Structure

The package structure differs from IAR/MDK/MCUX/CodeWarrior toolchain and ARMGCC/VSCODE toolchain. The former one is the classic SDK package layout, which contains:

```
SDK_2.x.x_BOARD/
├── boards/                    # Board-specific files
│   └── <board_name>/
│       ├── demo_apps/         # Demo applications
│       ├── driver_examples/   # Driver examples
│       └── project_template/  # Empty project template
├── CMSIS/                     # ARM CMSIS headers
├── components/                # Reusable components
├── devices/                   # Device-specific files
│   └── <device>/
│       ├── drivers/           # Peripheral drivers
│       ├── gcc/               # GCC linker scripts
│       ├── iar/               # IAR linker scripts
│       └── arm/               # Keil linker scripts
├── docs/                      # Documentation
├── middleware/                # Selected middleware
├── rtos/                      # RTOS support
└── tools/                     # Utilities

```
The latter one is the repository-layout SDK package, which is organized as:
```
SDK_2.x.x_BOARD/
├── manifests
│   ├── boards
│   │   ├── custom.yml.template
│   │   └── <board_name>.yml
│   ├── scripts
│   │   ├── west_commands
│   │   └── west_commands.yml
│   ├── submanifests
│   │   ├── base.yml
│   │   ├── devices
│   │   └── rtos
│   └── west.yml
└── mcuxsdk
    ├── arch
    │   ├── arm
    │   └── xtensa
    ├── cmake
    │   ├── extension
    │   └── toolchain
    ├── components
    │   ├── adapter.cmake
    │   └── wifi_bt_module
    ├── COPYING-BSD-3
    ├── devices
    │   ├── prj.conf
    │   └── <device_family>
    |      ├── <device_series>
    |      │   ├── <device_part>
    ├── docs
    ├── drivers
    │   ├── acmp
    │   └── ...
    ├── examples
    │   ├── _boards
    |   │   └── <board_name>
    │   ├── _common
    │   ├── demo_apps
    │   └── driver_examples
    ├── firmware
    │   └── edgelock
    ├── middleware
    │   ├── audio_voice
    │   ├── wifi_nxp
    │   └── wireless
    ├── README.md
    ├── rtos
    │   └── freertos
    ├── scripts
    ├── tool_data
    ├── tool.yml
    └── yamllint_config.yml
```

## Updating Your SDK

SDK Builder releases new versions periodically with:
- Bug fixes
- New features
- Additional board support
- Updated middleware

### Check for Updates

1. Visit SDK Builder: https://mcuxpresso.nxp.com/
2. Select your board
3. Check version number against your current SDK

### Download New Version

1. Configure with same selections as before
2. Download new SDK archive
3. Extract to new location (keep old version until migration complete)
4. Update IDE SDK paths or environment variables

**Tip:** check [online documentation](https://docs.mcuxpresso.nxp.com/mcuxsdk/latest/html/index.html) for your specific SDK version.

## Troubleshooting

### Download Issues

**Download fails or corrupts:**
- Use download manager for large files
- Verify ZIP integrity after download
- Try different browser if issues persist
- Check available disk space (need 2x package size)

**Slow download speeds:**
- Download during off-peak hours
- Use wired connection instead of Wi-Fi
- Try different network if available

### Extraction Issues

**"Cannot extract" or "Corrupted archive":**
- Verify complete download (check file size)
- Use 7-Zip or WinRAR instead of built-in tools
- Re-download if corruption persists

**"Path too long" errors (Windows):**
- Extract to shorter path (e.g., `C:\SDK\`)
- Enable long path support in Windows 10/11
- Use 7-Zip which handles long paths better

### IDE Integration Issues

**IDE doesn't recognize SDK:**
- Verify extraction path has no spaces or special characters
- Check IDE version compatibility in SDK release notes
- Ensure all archive contents extracted completely
- Restart IDE after SDK installation

**Missing toolchain support:**
- Return to SDK Builder
- Ensure desired toolchain was selected during configuration
- Re-download with correct toolchain selection

**Example projects won't build:**
- Verify toolchain installation and version
- Check environment variables (ARMGCC_DIR, IAR_DIR, etc.)
- Review example readme for specific requirements
- Ensure SDK version matches toolchain version requirements


## Offline Development

Classic packages are ideal for offline development:

### Setup for Offline Use

1. **Download complete package** with all needed components
2. **Extract to portable location** (USB drive, network share)
3. **Install toolchain** on development machine
4. **Copy documentation** to local drive
5. **Work offline** - no internet required after setup

### Sharing with Team

1. Download SDK once
2. Extract to network share
3. Team members point IDE to shared location
4. Or distribute extracted SDK via internal file sharing

**Tip:** Include SDK version and configuration in team documentation.

## Advanced: Custom SDK Packages

For enterprise or team use, you can create custom SDK configurations:

### Save Configuration

After configuring SDK Builder:
1. Note all selections
2. Document middleware versions
3. Save configuration for reproducibility

### Scripted Downloads

SDK Builder doesn't provide API access, but you can:
1. Document exact configuration steps
2. Create team guidelines for SDK downloads
3. Maintain internal SDK repository with approved versions

## Additional Resources

- **SDK Builder:** https://mcuxpresso.nxp.com/
- **SDK Documentation:** https://docs.mcuxpresso.nxp.com/mcuxsdk/latest/html/index.html
- **NXP Community:** https://community.nxp.com/
- **Technical Support:** https://www.nxp.com/support
