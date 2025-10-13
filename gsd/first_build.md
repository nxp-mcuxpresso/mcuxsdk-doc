# Building Your First Project

This guide explains how to build and run your first SDK example project using the west build system. This applies to both GitHub Repository SDK and Repository-Layout SDK Package.

## Prerequisites

- GitHub Repository SDK workspace initialized OR Repository-Layout SDK Package extracted
- Development board connected via USB
- Build tools installed per [Installation Guide](installation.md)

## Understanding Board Support

Use the west extension to discover available examples for your board:

```bash
west list_project -p examples/demo_apps/hello_world
```

This shows all supported build configurations. You can filter by toolchain:

```bash
west list_project -p examples/demo_apps/hello_world -t armgcc
```

## Basic Build Process

### Simple Build

Build the hello_world example with default settings:

```bash
west build -b your_board examples/demo_apps/hello_world
```

The default toolchain is armgcc, and the build system will select the first debug target as default if no config is specified.

### Specifying Configuration

```bash
# Release build
west build -b your_board examples/demo_apps/hello_world --config release

# Debug build (default)
west build -b your_board examples/demo_apps/hello_world --config debug
```

### Alternative Toolchains

```bash
# IAR toolchain
west build -b your_board examples/demo_apps/hello_world --toolchain iar

# Other toolchains as supported by the example
```

## Multicore Applications

For multicore devices, specify the core ID:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug
```

For multicore projects using sysbuild:

```bash
west build -b evkbmimxrt1170 --sysbuild ./examples/multicore_examples/hello_world/primary -Dcore_id=cm7 --config flexspi_nor_debug --toolchain=armgcc -p always
```

## Flash an Application

Flash the built application to your board:

```bash
west flash -r linkserver
```

## Debug

Start a debug session:

```bash
west debug -r linkserver
```

## Common Build Options

### Clean Build

Force a complete rebuild:

```bash
west build -b your_board examples/demo_apps/hello_world -p always
```

### Dry Run

See the commands that get executed without running them:

```bash
west build -b your_board examples/demo_apps/hello_world --dry-run
```

### Device Variants

For boards supporting multiple device variants:

```bash
west build -b your_board examples/demo_apps/hello_world --device DEVICE_PART_NUMBER --config release
```

## Project Configuration

### CMake Configuration Only

Run configuration without building:

```bash
west build -b your_board examples/demo_apps/hello_world -Dcore_id=cm7 --cmake-only -p
```

### Interactive Configuration

Launch the configuration GUI:

```bash
west build -t guiconfig
```

## Troubleshooting

### Build Failures

Use pristine builds to resolve dependency issues:

```bash
west build -b your_board examples/demo_apps/hello_world -p always
```

### Getting Help

View the help information for west build:

```bash
west build -h
```

### Check Supported Configurations

To see available configuration options and board targets for an example, refer to the below command:

```bash
west list_project -p examples/demo_apps/hello_world
```

## Next Steps

- Explore other examples in the SDK
- Learn about [Command Line Development](run_project) for advanced options
- Try [VS Code Development](run_a_demo_using_mcuxvsc.md) for integrated development
- Refer [Workspace Structure](explore_sdk.md) to understand the SDK layout