# Uninstall SDK

This guide explains how to remove MCUXpresso SDK installations from your system.

## Overview

Uninstallation steps vary depending on how you installed the SDK:
- **GitHub Repository SDK** - Remove workspace and optionally tools
- **Classic Package** - Delete extracted files and IDE references
- **IDE-Integrated** - Remove from IDE and optionally delete files

## Uninstalling GitHub Repository SDK

### Remove Workspace

The SDK workspace is simply a directory structure. To remove:

**Windows:**
```batch
cd ..
rmdir /s /q mcuxpresso-sdk
```

**Linux/macOS:**
```bash
cd ..
rm -rf mcuxpresso-sdk
```

This removes:
- All SDK repositories
- Build artifacts
- Configuration files

### Remove Development Tools (Optional)

If you want to completely remove SDK development tools:

**West Tool:**
```bash
pip uninstall west
```

**CMake, Ninja, Git:**
- These are general development tools
- Only uninstall if not needed for other projects
- Use system package manager or installer

**ARM GCC Toolchain:**
- Delete installation directory
- Remove environment variable (ARMGCC_DIR)

**Windows:**
```batch
# Remove from PATH via System Properties → Environment Variables
# Delete installation folder
rmdir /s /q "C:\Program Files (x86)\GNU Arm Embedded Toolchain"
```

**Linux:**
```bash
sudo apt remove gcc-arm-none-eabi  # If installed via apt
# Or delete manual installation directory
```

## Uninstalling Classic Package SDK

### Remove Extracted Files

Simply delete the extracted SDK directory:

**Windows:**
```batch
rmdir /s /q "C:\MCUXpresso\SDK_2.15.0_FRDM-MCXW23"
```

**Linux/macOS:**
```bash
rm -rf ~/MCUXpresso/SDK_2.15.0_FRDM-MCXW23
```

### Remove from MCUXpresso IDE

1. Open MCUXpresso IDE
2. **Window → Preferences → MCUXpresso SDK**
3. Select SDK to remove
4. Click **Remove**
5. Click **Apply and Close**

### Remove from IAR Embedded Workbench

IAR doesn't maintain SDK registry. Simply:
1. Delete extracted SDK folder
2. Remove any workspace references to SDK path

### Remove from Keil MDK

**Uninstall CMSIS Pack:**
1. Open Keil µVision
2. **Project → Manage → Pack Installer**
3. Find NXP SDK pack
4. Click **Remove**

**Delete SDK Files:**
- Delete extracted SDK folder

## Uninstalling IDE-Integrated SDK

### MCUXpresso IDE

**Remove SDK:**
1. **Window → Preferences → MCUXpresso SDK**
2. Select SDK
3. Click **Remove**

**Remove IDE (if desired):**
1. **Windows:** Control Panel → Uninstall Programs → MCUXpresso IDE
2. **Linux:** Delete installation directory
3. **macOS:** Move application to Trash

**Remove Workspace:**
- Delete workspace directory (contains projects and settings)

### VS Code with MCUXpresso Extension

**Remove SDK Workspace:**
1. Open VS Code
2. MCUXpresso extension → REPOSITORIES view
3. Right-click SDK → Remove

Or manually delete workspace directory.

**Remove Extension:**
1. **Extensions view (Ctrl+Shift+X)**
2. Find "MCUXpresso for VS Code"
3. Click **Uninstall**

**Remove VS Code (if desired):**
- Follow standard VS Code uninstallation for your OS

## Cleaning Build Artifacts

Before uninstalling, you may want to clean build artifacts to free space:

### GitHub Repository SDK

```bash
cd mcuxpresso-sdk
west build -t clean  # Clean current build
# Or delete entire build directory
rm -rf build/
```

### Classic Package

Navigate to example directories and delete build folders:

**Windows:**
```batch
cd boards\<board>\driver_examples\gpio\led_output\mdk
rmdir /s /q debug release
```

**Linux/macOS:**
```bash
cd boards/<board>/driver_examples/gpio/led_output/mdk
rm -rf debug release
```

## Removing Environment Variables

### Windows

1. **System Properties → Advanced → Environment Variables**
2. Remove SDK-related variables:
   - `ARMGCC_DIR`
   - `IAR_DIR`
   - `MDK_DIR`
   - `MCUXpresso_SDK_DIR`
3. Remove SDK paths from `PATH` variable

### Linux/macOS

Edit shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
# Remove or comment out SDK-related exports
# export ARMGCC_DIR=/usr/local/gcc-arm-none-eabi
# export MCUXpresso_SDK_DIR=~/MCUXpresso/SDK
```

Reload shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

## Removing Configuration Files

### West Configuration

```bash
# Remove global west configuration
rm -rf ~/.west/
```

### Git Configuration (if SDK-specific)

```bash
# Remove SDK-specific Git config
git config --global --unset-all user.name
git config --global --unset-all user.email
```

**Note:** Only do this if Git was configured solely for SDK development.

## Disk Space Recovery

After uninstallation, you can recover significant disk space:

| Component | Typical Size |
|-----------|--------------|
| GitHub Repository SDK (complete) | 7-8 GB |
| GitHub Repository SDK (board-specific) | 1-2 GB |
| SDK Archive Package | 500 MB - 2 GB |
| Build artifacts (per project) | 50-200 MB |
| ARM GCC Toolchain | 500 MB - 1 GB |
| MCUXpresso IDE | 1-2 GB |

### Verify Disk Space Recovery

**Windows:**
```batch
dir /s "C:\MCUXpresso"
```

**Linux/macOS:**
```bash
du -sh ~/MCUXpresso
```

## Reinstallation

If you need to reinstall the SDK later:

**GitHub Repository SDK:**
- Follow [GitHub Installation Guide](install/github.md)
- Previous workspace can be recreated from scratch

**Classic Package:**
- Re-download from [SDK Builder](install/sdk_builder.md)
- Extract to desired location

**IDE-Integrated:**
- Use IDE's SDK import wizard
- Follow [IDE Import Wizard Guide](install/ide_import_wizard.md)

## Troubleshooting Uninstallation

### Cannot Delete Files

**"File in use" errors:**
- Close all IDEs and terminals
- Stop any running debug sessions
- Restart computer if necessary

**Permission errors:**
- Run command prompt/terminal as administrator
- Check file permissions
- Ensure you own the files

### Leftover Registry Entries (Windows)

Some IDEs may leave registry entries:
- Generally harmless
- Can be removed with IDE's uninstaller
- Or use registry cleaner (caution advised)

### Broken IDE After SDK Removal

**MCUXpresso IDE:**
- Remove SDK references from workspace
- Clean workspace: **File → Switch Workspace → Clean**
- Restart IDE

**VS Code:**
- Remove workspace folder from recent list
- Reload window: **Ctrl+Shift+P → Reload Window**

## Partial Uninstallation

You may want to remove only parts of the SDK:

### Remove Specific Middleware

**GitHub Repository SDK:**
```bash
cd mcuxpresso-sdk
# Remove specific repository
rm -rf mcuxsdk/middleware/usb
# Update west to reflect changes
west update
```

**Classic Package:**
- Delete middleware folder
- May break examples that depend on it

### Remove Build Artifacts Only

Keep SDK but remove build outputs:

```bash
# GitHub Repository SDK
west build -t clean

# Classic Package
find . -name "debug" -type d -exec rm -rf {} +
find . -name "release" -type d -exec rm -rf {} +
```

### Remove Documentation Only

```bash
# Delete docs folder to save space
rm -rf docs/
```

**Note:** Documentation can be accessed online at [docs.mcuxpresso.nxp.com](https://docs.mcuxpresso.nxp.com/mcuxsdk)

## Complete System Cleanup

For complete removal of all SDK-related components:

1. **Remove SDK workspaces/packages**
2. **Uninstall development tools** (west, CMake, etc.)
3. **Uninstall toolchains** (ARM GCC, IAR, Keil)
4. **Uninstall IDEs** (MCUXpresso IDE, VS Code)
5. **Remove environment variables**
6. **Delete configuration files**
7. **Clean temporary files**

**Windows:**
```batch
# Clean temp files
del /s /q %TEMP%\mcux*
del /s /q %TEMP%\west*
```

**Linux/macOS:**
```bash
# Clean temp files
rm -rf /tmp/mcux*
rm -rf /tmp/west*
```

## Verification

After uninstallation, verify removal:

```bash
# Check west is removed
west --version  # Should show "command not found"

# Check SDK directory is gone
ls ~/MCUXpresso  # Should not exist or be empty

# Check environment variables
echo $ARMGCC_DIR  # Should be empty
```