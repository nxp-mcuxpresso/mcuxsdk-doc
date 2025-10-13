# SDK Architecture Overview

The MCUXpresso SDK uses a modular architecture where software components are distributed across multiple repositories hosted on GitHub and managed through the west tool. This approach provides flexibility, maintainability, and enables selective component inclusion.

## Repository Organization

Based on the manifest structure, the SDK consists of four main repository categories:

### Manifest Repository
The manifest repo (mcuxsdk-manifests) contains the west.yml manifest file that tracks all other repositories in the SDK.

### Base Repositories
Recorded in `submanifests/base.yml` and loaded in the root west.yml manifest file. These are the foundational repositories that build the SDK:
- **Devices**: MCU-specific support packages
- **Examples**: Demonstration applications and code samples
- **Boards**: Board support packages

### Middleware Repositories
Recorded in the `submanifests/middleware` subdirectory, categorized according to functionality:
- **Connectivity**: Networking stacks, USB, and communication protocols
- **Security**: Cryptographic libraries and secure boot components
- **Wireless**: Bluetooth, IEEE 802.15.4, and other wireless protocols
- **Graphics**: Display drivers and UI frameworks
- **Audio**: Audio processing and voice recognition libraries
- **Machine Learning**: AI inference engines and neural network libraries
- **Safety**: IEC60730B safety libraries
- **Motor Control**: Motor control and real-time control libraries

### Internal Repositories
Recorded in `submanifests/internal.yml` and grouped into the "bifrost" group. These are only visible to NXP internal developers and hosted on NXP internal git servers.

## Repository Hosting

Public repositories are hosted on GitHub under these organizations:
- [nxp-mcuxpresso](https://github.com/nxp-mcuxpresso/)
- [NXP](https://github.com/NXP)
- [nxp-zephyr](https://github.com/nxp-zephyr)

Internal repositories are hosted on NXP's private Git infrastructure.

## Benefits of This Architecture

**Selective Integration**: Projects include only required components, reducing memory footprint and build complexity.

**Independent Versioning**: Each component maintains its own release cycle and version control.

**Community Collaboration**: Public repositories accept community contributions through standard Git workflows.

**Scalable Maintenance**: Component owners can update their repositories without affecting the entire SDK.

## Workspace Management

The west tool manages repository synchronization, version tracking, and workspace updates. All repositories are checked out under the `mcuxsdk/` directory with their designated paths defined in the manifest files.
