# Install from GitHub

Install MCUXpresso SDK directly from GitHub repositories for the most flexible and up-to-date development experience.

## Overview

The GitHub installation method provides:
- Latest SDK updates and features
- Modular component selection
- Version control integration
- Community contributions and fixes

## Recommended: MCUXpresso Installer

**The fastest way to set up GitHub-based SDK development is using the MCUXpresso Installer.**

### Quick Start with Installer

1. **Download MCUXpresso Installer**
   - Visit: [Dependency-Installation](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Dependency-Installation)
   - Download for your operating system

2. **Run Installer**
   - Launch the installer
   - Select **"MCUXpresso SDK Developer"**
   - Click **Install**

3. **Automatic Setup**
   The installer automatically configures:
   - Git version control
   - Python environment
   - West tool for repository management
   - CMake and Ninja build tools
   - ARM GCC toolchain (optional)

4. **Initialize Workspace**
   After installation completes, open a terminal and run:
   ```bash
   west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
   cd mcuxpresso-sdk
   west update
   ```

### Why Use the Installer?

- **One-click setup** - All tools configured automatically
- **Correct versions** - Ensures compatible tool versions
- **Path configuration** - Environment variables set correctly
- **Time savings** - Avoid manual installation steps

## Advanced: Manual Installation

For users who need specific tool versions or custom configurations, manual installation provides full control.

### Prerequisites

Verify these tools are installed:

```bash
git --version      # 2.25 or later
python --version   # 3.8 or later
west --version     # 1.2.0 or later
cmake --version    # 3.20 or later
ninja --version    # 1.12.1 or later
```

### Detailed Manual Setup

For complete manual installation instructions, see:
- [Development Tools Installation](../installation.md)
- [GitHub Repository Setup](../repo_setup.md)

### Quick Manual Steps

1. **Install Prerequisites**
   ```bash
   pip install -U west
   ```

2. **Initialize Workspace**
   ```bash
   west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
   cd mcuxpresso-sdk
   ```

3. **Update Repositories**
   
   **Option A: Complete SDK (7-8 GB)**
   ```bash
   west update
   ```

   **Option B: Board-Specific (1-2 GB, Recommended)**
   ```bash
   west update_board --set board frdmmcxw23
   ```

## Custom Manifests

For advanced users who need custom repository combinations or private forks, see [Custom Manifests](custom_manifests.md).