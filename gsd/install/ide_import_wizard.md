# IDE Import Wizard

The IDE Import Wizard provides the fastest way to get started with MCUXpresso SDK in supported IDEs.

## Overview

The IDE Import Wizard automatically:
- Downloads required SDK components
- Configures toolchain settings
- Sets up project structure
- Imports example applications

This method is recommended for users who prefer integrated development environments and want minimal setup complexity.

## Supported IDEs

The Import Wizard is available in:
- **MCUXpresso IDE** - Full integration with NXP tooling
- **VS Code with MCUXpresso Extension** - Modern, extensible editor

## Prerequisites

### For MCUXpresso IDE
- MCUXpresso IDE 11.8.0 or later installed
- Internet connection for SDK download
- USB connection to target board (for debugging)

### For VS Code
- Visual Studio Code installed
- MCUXpresso for VS Code extension installed
- Internet connection for SDK download

## Using the Import Wizard in MCUXpresso IDE

### Step 1: Launch the Wizard

1. Open MCUXpresso IDE
2. Navigate to **File → New → Project**
3. Select **MCUXpresso SDK Project**
4. Click **Next**

### Step 2: Select SDK Source

Choose one of the following options:

**Option A: Download from NXP**
1. Select **Download SDK from NXP**
2. Choose your target board from the list
3. Click **Download** to fetch the latest SDK

**Option B: Use Local SDK**
1. Select **Use local SDK**
2. Browse to your SDK installation directory
3. Click **Next**

### Step 3: Configure Project

1. Select your target board
2. Choose an example application (e.g., `hello_world`)
3. Configure project name and location
4. Click **Finish**

The IDE will automatically:
- Import all required files
- Configure build settings
- Set up debug configurations

### Step 4: Build and Run

1. Right-click the project in Project Explorer
2. Select **Build Project**
3. Once built, click **Debug** to flash and run

## Using the Import Wizard in VS Code

For detailed VS Code workflow, see [VS Code First Project](../run_a_demo_using_mcuxvsc.md).

Quick steps:
1. Open MCUXpresso for VS Code extension
2. Click **Import Repository** or **Import Example**
3. Follow the guided workflow
4. Build and debug from the integrated interface
