# Workspace Structure

After you initialize your SDK workspace, it creates a specific directory structure that organizes all SDK components. This structure is identical for both GitHub Repository SDK and Repository-Layout SDK Package.

## Top-Level Organization

```
your-sdk-workspace/
├── manifests/          # West manifest repository
└── mcuxsdk/           # Main SDK content
```

The `mcuxsdk/` directory serves as your primary working directory and contains all the SDK components.

## SDK Component Layout

Based on the actual SDK structure, the main directories include:

| Directory | Contents | Purpose |
|-----------|----------|---------|
| `arch/` | Architecture-specific files | ARM CMSIS, build configurations |
| `cmake/` | Build system modules | CMake configuration and build rules |
| `components/` | Software components | Reusable software libraries and utilities |
| `devices/` | Device support packages | MCU-specific headers, startup code, linker scripts |
| `drivers/` | Peripheral drivers | Hardware abstraction layer for MCU peripherals |
| `examples/` | Sample applications | Demonstration code and reference implementations |
| `middleware/` | Optional software stacks | Networking, graphics, security, and other libraries |
| `rtos/` | Operating system support | FreeRTOS integration |
| `scripts/` | Build and utility scripts | West extensions and development tools |
| svd | Svd files for devices, this is optional because of large size. Customers run `west manifest config group.filter +optional` and `west update mcux-soc-svd` to get this folder. |

## Example Organization

Examples follow a two-tier structure separating common code from board-specific implementations:

### Common Example Files
```
examples/demo_apps/hello_world/
├── CMakeLists.txt        # Build configuration
├── example.yml           # Example metadata
├── hello_world.c         # Application source code
├── Kconfig              # Configuration options
└── readme.md            # General documentation
```

### Board-Specific Files
```
examples/_boards/your_board/demo_apps/hello_world/
├── app.h                      # Board specific application header
├── example_board_readme.md    # Board specific documentation
├── hardware_init.c            # Board specific hardware initialization
├── pin_mux.c                  # Pin multiplexing configuration
├── pin_mux.h                  # Pin multiplexing header definitions
├── hello_world.bin            # Pre-built binary for quick testing
├── hello_world.mex            # MCUXpresso Config Tools project file
├── prj.conf                   # Board specific Kconfig configuration
└── reconfig.cmake             # Board specific cmake configuration overrides
```

## Device Support Structure

Device support is organized hierarchically by MCU family:

```
devices/
└── MCX/                    # MCU portfolio
    ├── MCXW/              # MCU family
        ├── MCXW235/       # Specific device
            ├── MCXW235.h          # Device register definitions
            ├── drivers/           # Device-specific drivers
            ├── gcc/              # GNU toolchain files
            ├── iar/              # IAR toolchain files
            ├── mcuxpresso/       # MCUXpresso IDE files
            ├── startup_MCXW235.c # Startup and vector table
            └── system_MCXW235.c  # System initialization
```

## Middleware Organization

Middleware components are categorized by functionality and maintained in separate repositories. Based on the manifest files, common middleware categories include:

- **Connectivity**: USB, TCP/IP, industrial protocols
- **Security**: Cryptographic libraries, secure boot
- **Wireless**: Bluetooth, IEEE 802.15.4, Wi-Fi
- **Graphics**: Display drivers, UI frameworks
- **Audio**: Processing libraries, voice recognition
- **Machine Learning**: Inference engines, neural networks
- **Safety**: IEC60730B safety libraries
- **Motor Control**: Motor control and real-time control libraries

## Documentation Structure

SDK documentation is distributed across multiple locations:
- `docs/` - Core SDK documentation and build infrastructure
- Component repositories - API documentation and integration guides
- Board directories - Hardware-specific setup instructions

For complete documentation, refer to the [online documentation](https://mcuxpresso.nxp.com/mcuxsdk/latest/html/).

## Understanding Example Structure

Each example has **two README files**:

### 1. General README: `examples/demo_apps/hello_world/readme.md`
- What the example does
- General functionality description
- Common usage information

### 2. Board-Specific README: `examples/_boards/{board_name}/demo_apps/hello_world/example_board_readme.md`
- Board-specific setup instructions
- Hardware connections required
- Board-specific behavior notes

**Tip**: Always check both readme files - start with the general one, then read the board-specific one for detailed setup.