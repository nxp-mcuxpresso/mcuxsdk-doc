(gsd_tool_installation)=

# Development Tools Installation

This guide explains how to install the essential tools for development with the MCUXpresso SDK.

## Quick Start: Automated Installation (Recommended)

The **MCUXpresso Installer** is the fastest way to get started. It automatically installs all the basic tools you need.

1. **Download the MCUXpresso Installer** from: [Dependency-Installation](https://docs.mcuxpresso.nxp.com/mcux-vscode/latest/html/Dependency-Installation.html)

2. **Run the installer** and select **"MCUXpresso SDK Developer"** from the menu

3. **Click Install** and let it handle everything automatically

## Manual Installation

If you prefer to install tools manually or need specific versions, follow these steps:

### Essential Tools

#### Git - Version Control
**What it does**: Manages code versions and downloads SDK repositories from GitHub.

**Installation**:
- Visit [git-scm.com](https://git-scm.com/)
- Download for your operating system
- Run installer with default settings
- **Important**: Make sure "Add Git to PATH" is selected during installation

**Setup**:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

#### Python - Scripting Environment
**What it does**: Runs build scripts and SDK tools.

**Installation**:
- Install Python **3.10 or newer** from [python.org](https://www.python.org/downloads/)
- **Important**: Check "Add Python to PATH" during installation

#### West - SDK Management Tool
**What it does**: Manages SDK repositories and provides build commands. The west tool is developed by the Zephyr project for managing multiple repositories.

**Installation**:
```bash
pip install -U west
```

**Minimum version**: 1.2.0 or newer

### Build System Tools

#### CMake - Build Configuration
**What it does**: Configures how your projects are built.

**Recommended version**: 3.30.0 or newer

**Installation**:
- **Windows**: Download `.msi` installer from [cmake.org/download](https://cmake.org/download/)
- **Linux**: Use package manager or download from cmake.org
- **macOS**: Use Homebrew (`brew install cmake`) or download from cmake.org

#### Ninja - Fast Build System
**What it does**: Compiles your code quickly.

**Minimum version**: 1.12.1 or newer

**Installation**:
- **Windows**: Usually included, or download from [ninja-build.org](https://ninja-build.org/)
- **Linux**: `sudo apt install ninja-build` or download binary
- **macOS**: `brew install ninja` or download binary

#### Ruby - IDE Project Generation (Optional)
**What it does**: Generates project files for IDEs like IAR and Keil.

**When needed**: Only if you want to use traditional IDEs instead of VS Code.

**Installation**: Follow the [Ruby environment setup guide](../develop/build_system/IDE_Project.md#ruby-environment-setup)

### Compiler Toolchains

Choose and install the compiler toolchain you want to use:

| Toolchain | Best For | Download Link | Environment Variable |
|-----------|----------|---------------|---------------------|
| **ARM GCC** (Recommended) | Most users, free | [ARM GNU Toolchain](https://learn.arm.com/install-guides/gcc/arm-gnu/) | `ARMGCC_DIR` |
| **IAR EWARM** | Professional development | [IAR Systems](https://www.iar.com/) | `IAR_DIR` |
| **Keil MDK** | ARM ecosystem | [ARM Developer](https://developer.arm.com/documentation/109350/v6/Installation) | `MDK_DIR` |
| **ARM Compiler** | Advanced optimization | [ARM Developer](https://developer.arm.com/documentation/100748/0618/Getting-Started/Installing-Arm-Compiler-for-Embedded) | `ARMCLANG_DIR` |

#### Setting Up Environment Variables

After toolchain installation, set an environment variable so the build system locates it:

**Windows**:
```batch
# Example for ARM GCC installed in C:\armgcc
setx ARMGCC_DIR "C:\armgcc"
```

**Linux/macOS**:
```bash
# Add to ~/.bashrc or ~/.zshrc
export ARMGCC_DIR="/usr"  # or your installation path
```

## Verify Your Installation

After installation, verify everything works by opening a terminal/command prompt and running these commands:

```bash
# Check each tool - you should see version numbers
git --version
python --version  
west --version
cmake --version
ninja --version
arm-none-eabi-gcc --version  # (if using ARM GCC)
```

### Troubleshooting Installation Issues

**"Command not found" errors**:
- The tool isn't in your system PATH
- **Solution**: Add the installation directory to your PATH environment variable

**Python/pip issues**:
- Try using `python3` and `pip3` instead of `python` and `pip`
- On Windows, run the Command Prompt as an Administrator

**Slow downloads**:
- Add timeout option: `pip install -U west --default-timeout=1000`
- Use alternative mirror: `pip install -U west -i https://pypi.tuna.tsinghua.edu.cn/simple`
