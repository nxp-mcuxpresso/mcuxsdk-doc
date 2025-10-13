# MCUXpresso SDK

The **MCUXpresso SDK** is NXP's comprehensive software platform for embedded development on NXP microcontrollers. It includes peripheral drivers, RTOS support, middleware, and example applications to accelerate development from prototype to production.

## Distribution Formats

MCUXpresso SDK is available in two main formats:

### GitHub Repository SDK
Git-based distribution hosted on GitHub for modular development, continuous updates, and collaborative workflows. The SDK uses multiple repositories managed by the Zephyr west tool to provide flexible, component-based development.

### SDK Package
Downloadable packages from [SDK Builder](https://mcuxpresso.nxp.com/) for offline development. Starting with release 25.09.00, MCUXpresso SDK introduced two package versions for offline development:
- **Classic SDK Package**: Traditional board-specific packages with pre-configured IDE projects for MCUXpresso IDE, IAR, Keil, and other toolchains.
- **Repository-Layout SDK Package**: Board-specific packages that maintain the same structure and build system as the GitHub Repository SDK, providing offline access to the repository-based development experience. Available when selecting the ARMGCC toolchain.

From version 25.12.00 onward:
- When you select ARMGCC, the SDK download will use the Repository-Layout version.
- For all other toolchains, the SDK download will remain in the Classic version.

```{note}
The Repository-Layout SDK package was first introduced in version 25.09.00, but initially only for MCXW23x platforms.
```

## Key Features

**Comprehensive Driver Library**
- Flexible peripheral drivers for rapid development
- Optimized for performance and code size

**Extensive Examples**
- Basic peripheral use cases to full technology demonstrations
- Board-specific reference implementations
- Out-of-box Demo Applications
- Middleware component examples and integrations

**RTOS Integration**
- FreeRTOS support with optimized configurations
- Real-time application frameworks
- Task management and scheduling examples

**Middleware Components**
- Connectivity stacks (USB, Ethernet, wireless, communication protocols)
- AI inference engines and neural network libraries
- Audio processing and voice recognition libraries
- Security frameworks and cryptographic libraries
- Graphics and user interface components
- Motor control and real-time control libraries
- File systems and storage solutions

## GitHub Repository Setup

```{note}
Skip this section if using Classic SDK Package
```

For users working with **GitHub Repository SDK** or **Repository-Layout SDK Package**, follow the instructions below:

### Prerequisites

Ensure you have the required tools installed. Follow the [Installation Guide](../gsd/installation.md) for detailed setup instructions.

### Workspace Initialization

```{note}
Skip this subsection if using Repository-Layout SDK Package
```

The GitHub Repository SDK uses multiple repositories managed by the Zephyr west tool for modular organization and flexible component selection.

**Initialize with latest SDK:**
```bash
west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
```

**Initialize with specific version:**
```bash
west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk --mr {revision}
```
*Replace `{revision}` with the desired release tag, such as `v25.09.00`*

**Navigate to workspace:**
```bash
cd mcuxpresso-sdk
```

### Repository Checkout

```{note}
Skip this subsection if using Repository-Layout SDK Package
```

The west tool manages multiple repositories containing different SDK components:

**Checkout all repositories:**
```bash
west update
```

**Selective checkout for specific hardware:**
```bash
# Checkout only repositories for a specific board
west update_board --set board your_board_name

# Checkout only repositories for a specific MCU part
west update_board --set device your_mcu_part
```

```{tip}
Selective checkout reduces download time and disk space by including only repositories required for your target hardware.
```

### Environment Configuration

```bash
export ARMGCC_DIR=/path/to/gcc-arm-none-eabi
west --version
cmake --version
```

### Quick Start Example

```bash
west build -b your_board examples/demo_apps/hello_world
west flash
```

## Repository Architecture

The SDK uses a multi-repository structure hosted on GitHub and managed by the [Zephyr West Tool](https://docs.zephyrproject.org/latest/guides/west/index.html), enabling:

- **Modular Organization**: Drivers, RTOS, middleware, and examples in separate GitHub repositories
- **Customizable Manifests**: Targeted setups for specific requirements
- **Selective Downloads**: Include only needed components from relevant repositories
- **Independent Updates**: Component-level version control and updates
- **Scalable Integration**: Easy addition of new repository components

## Development Workflows

**Recommended Approach**  
[MCUXpresso for VS Code](../gsd/run_a_demo_using_mcuxvsc.md) - Modern IDE experience with integrated debugging and project management

**Command Line Development**  
[ARM GCC/IAR/MDK Command Line](../gsd/run_project.md) - Terminal-based development with full toolchain support

**Traditional IDE Integration**  
Export projects to IAR, Keil, and other development environments

## Support and Resources

**Community Support**  
Open GitHub issues and discussions for questions and contributions

**Documentation**  
Comprehensive guides and API documentation available [online](https://mcuxpresso.nxp.com/mcuxsdk/latest/html/index.html)

**Technical Support**  
Contact NXP technical support for commercial development assistance