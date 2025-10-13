# Command Line Development

This guide covers developing with the MCUXpresso SDK using command line tools and the west build system. This workflow applies to both GitHub Repository SDK and Repository-Layout SDK Package distributions.

## Prerequisites

- GitHub Repository SDK workspace initialized OR Repository-Layout SDK Package extracted
- Development tools installed per [Installation Guide](installation.md)
- Target board connected via USB

## Understanding Board Support

Use the west extension to discover available examples for your board:

```bash
west list_project -p examples/demo_apps/hello_world
```

This shows all supported build configurations. You can filter by toolchain:

```bash
west list_project -p examples/demo_apps/hello_world -t armgcc
```

## Basic Build Commands

### Standard Build Process

Build with default settings (armgcc toolchain, first debug config):

```bash
west build -b your_board examples/demo_apps/hello_world
```

### Specifying Build Configuration

```bash
# Release build
west build -b your_board examples/demo_apps/hello_world --config release

# Debug build with specific toolchain
west build -b your_board examples/demo_apps/hello_world --toolchain iar --config debug
```

### Multicore Applications

For multicore devices, specify the core ID:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug
```

For multicore projects using sysbuild:

```bash
west build -b evkbmimxrt1170 --sysbuild ./examples/multicore_examples/hello_world/primary -Dcore_id=cm7 --config flexspi_nor_debug --toolchain=armgcc -p always
```

### Shield Support

For boards with shields:

```bash
west build -b mimxrt700evk --shield a8974 examples/issdk_examples/sensors/fxls8974cf/fxls8974cf_poll -Dcore_id=cm33_core0
```

## Advanced Build Options

### Clean Builds

Force a complete rebuild:

```bash
west build -b your_board examples/demo_apps/hello_world -p always
```

### Dry Run

See what commands would be executed:

```bash
west build -b your_board examples/demo_apps/hello_world --dry-run
```

### Device Variants

For boards supporting multiple device variants:

```bash
west build -b your_board examples/demo_apps/hello_world --device MK22F12810 --config release
```

## Project Configuration

### CMake Configuration Only

Run configuration without building:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world -Dcore_id=cm7 --cmake-only -p
```

### Interactive Configuration

Launch the configuration GUI:

```bash
west build -t guiconfig
```

## Flashing and Debugging

### Flash Application

Flash the built application to your board:

```bash
west flash -r linkserver
```

### Debug Session

Start a debugging session:

```bash
west debug -r linkserver
```

## IDE Project Generation

Generate IDE project files for traditional IDEs:

```bash
# Generate IAR project
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug -p always -t guiproject
```

IDE project files are generated in `mcuxsdk/build/<toolchain>` folder.

**Note**: Ruby installation is required for IDE project generation. See [Installation Guide](installation.md#ruby---ide-project-generation-optional) for setup instructions.

## Troubleshooting

### Build Failures

Use pristine builds to resolve dependency issues:

```bash
west build -b your_board examples/demo_apps/hello_world -p always
```

### Toolchain Issues

Verify environment variables are set correctly:

```bash
# Check ARM GCC
echo $ARMGCC_DIR
arm-none-eabi-gcc --version

# Check IAR (if using)
echo $IAR_DIR
```

### Getting Help

Display help information:

```bash
west build -h
west flash -h
west debug -h
```

### Check Supported Configurations

If unsure about supported options for an example:

```bash
west list_project -p examples/demo_apps/hello_world
```

## Best Practices

### Project Organization

- Keep custom projects outside the SDK tree
- Use version control for your application code
- Document any SDK modifications

### Build Efficiency

- Use `-p always` for clean builds when troubleshooting
- Leverage `--dry-run` to understand build processes
- Use specific configs and toolchains to reduce build time

### Development Workflow

1. Start with existing examples closest to your requirements
2. Copy and modify rather than building from scratch
3. Test with hello_world before moving to complex examples
4. Use configuration tools for pin muxing and clock setup

## Next Steps

- Explore [VS Code Development](run_a_demo_using_mcuxvsc.md) for integrated development experience
- Review [Workspace Structure](explore_sdk.md) to understand SDK organization
- Refer build system documentation for advanced configurations