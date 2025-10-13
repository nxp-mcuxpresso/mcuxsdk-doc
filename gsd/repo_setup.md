# GitHub Repository Setup

This guide explains how to initialize your MCUXpresso SDK workspace from GitHub repositories using the west tool. The GitHub Repository SDK uses multiple repositories hosted on GitHub to provide modular, flexible development.

## Prerequisites

Verify the requirements:

**System Requirements:**
- Python 3.8 or later
- Git 2.25 or later
- CMake 3.20 or later
- Build tools for your target platform

**Verification Commands:**
```bash
python --version    # Should show 3.8+
git --version      # Should show 2.25+
cmake --version    # Should show 3.20+
west --version     # Should show west tool installation
```

## Workspace Initialization

The GitHub Repository SDK uses the Zephyr west tool to manage multiple repositories containing different SDK components.

### Step 1: Initialize Workspace

Create and initialize your SDK workspace from GitHub:

**Get the latest SDK from main branch:**
```bash
west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
```

**Get SDK at specific revision:**
```bash
west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk --mr {revision}
```
*Note: Replace `{revision}` with the desired release tag, such as `v25.09.00`*

### Step 2: Choose Your Repository Update Strategy

Navigate to the SDK workspace:
```bash
cd mcuxpresso-sdk
```

The west tool manages multiple GitHub repositories containing different SDK components. You have two options for downloading:

#### Option A: Download All Repositories (Complete SDK)

Download all SDK repositories for comprehensive development:

```bash
west update
```

This command downloads all the repositories defined in the manifest from GitHub. Initial download takes several minutes and requires ~7 GB of disk space.

**Best for:**
- Exploring the complete SDK
- Multi-board development projects
- Comprehensive middleware evaluation

#### Option B: Targeted Repository Download (Recommended)

Download only repositories needed for your specific board or device to save time and disk space:

```bash
# For specific board development
west update_board --set board your_board_name

# For specific device family development  
west update_board --set device your_device_name

# List available repositories before downloading
west update_board --set board your_board_name --list-repo
```

**Best for:**
- Single board development
- Faster setup and reduced disk usage
- Focused development workflows

**Examples:**
```bash
# Update only repositories for FRDM-MCXW23 board
west update_board --set board frdmmcxw23

# Update only repositories for MCXW23 device family
west update_board --set device mcxw23
```

### Step 3: Verify Installation

Confirm successful setup:

```bash
# Verify workspace structure
ls -la
# Should show: manifests/ and mcuxsdk/ directories

# Test build system
west list_project -p examples/demo_apps/hello_world
# Should display available build configurations
```

## Advanced Repository Management

The west extension command `update_board` provides advanced repository management capabilities for optimized workspace setup with GitHub repositories.

### Board-Specific Setup

Update only repositories required for a specific board:

```bash
# Update only repositories for specific board, e.g., frdmmcxw23
west update_board --set board frdmmcxw23

# List available repositories for the board before updating
west update_board --set board frdmmcxw23 --list-repo
```

### Device-Specific Setup

Update only repositories required for a specific device family:

```bash
# Update only repositories for specific device, e.g., MCXW235
west update_board --set device mcxw23

# List available repositories for the device family
west update_board --set device mcxw23 --list-repo
```

### Custom Configuration

For advanced users who want to create custom repository combinations:

```bash
# Use custom configuration file
west update_board --set custom path/to/custom-config.yml

# Generate custom configuration template
cp manifests/boards/custom.yml.template my-custom-config.yml
```

### Benefits of Targeted Setup

**Reduced Download Size**
- Download only components needed for your target board or device
- Significantly faster initial setup for focused development
- Typical reduction from 7 GB to 2GB

**Optimized Workspace**
- Cleaner workspace with relevant components only
- Reduced disk space usage
- Faster repository operations

**Flexible Development**
- Switch between different board configurations easily
- Maintain separate workspaces for different projects
- Include optional components as needed

### Repository Information

Before setting up your workspace, you can explore what repositories are available:

```bash
# Display repository information in console
west update_board --set board frdmmcxw23 --list-repo

# Export repository information to YAML file for reference
west update_board --set board frdmmcxw23 --list-repo -o board-repos.yml
```

This command lists all the available repositories with descriptions and outlines the included components in the workspace.

### Package Generation (Optional)

The `update_board` command can also generate ZIP packages for offline distribution:

```bash
# Generate board-specific SDK package
west update_board --set board frdmmcxw23 -o frdmmcxw23-sdk.zip
```

**Note**: Package generation is primarily intended for creating custom SDK distributions. For regular development, use the workspace update commands without the `-o` option.

## Workspace Management

### Updating Your Workspace

Keep your SDK current with latest updates from GitHub:

**For Complete SDK Workspace:**
```bash
# Update manifest repository
cd manifests
git pull

# Update all component repositories
cd ..
west update
```

**For Targeted Workspace:**
```bash
# Update manifest repository
cd manifests
git pull

# Update board-specific repositories
cd ..
west update_board --set board your_board_name
```

### Workspace Status

Check workspace synchronization status:

```bash
# Show status of all repositories
west status

# Show detailed information about repositories
west list
```

## Troubleshooting

**Network Issues:**
- Use `west update --keep-descendants` for partial failures
- Configure Git credentials for private repositories
- Check firewall settings for Git protocol access

**Permission Issues:**
- Ensure write permissions in workspace directory
- Run commands without sudo/administrator privileges
- Verify Git SSH key configuration for authenticated access

**Disk Space:**
- Full SDK workspace requires approximately 7-8 GB
- Targeted workspace typically requires 1-2 GB
- Use board-specific setup to reduce workspace size

**Repository Management Issues:**
- Verify board/device names match available configurations
- Check that custom YAML files follow the correct template format
- Use `--list-repo` to verify available repositories before setup

## Next Steps

With your workspace initialized:
1. Review [Workspace Structure](explore_sdk.md) to understand the layout
2. Build your first project with [First Build Guide](first_build.md)
3. Explore [Development Workflows MCUXPresso VSCode](run_a_demo_using_mcuxvsc.md) or [Development Workflows Command Line](run_project.md) for the details on project setup and execution

For advanced repository management, see the [west tool documentation](https://docs.zephyrproject.org/latest/develop/west/index.html).