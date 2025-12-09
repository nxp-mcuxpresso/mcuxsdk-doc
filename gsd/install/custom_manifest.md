# Custom Manifests

Create custom SDK configurations by modifying west manifest files to include specific repositories, versions, or private components.

## Overview

Custom manifests enable:
- **Selective component inclusion** - Include only needed middleware
- **Version pinning** - Lock specific component versions
- **Private repositories** - Integrate proprietary code
- **Custom configurations** - Tailor SDK to project requirements

## When to Use Custom Manifests

Use custom manifests when you need to:
- Include private or proprietary repositories
- Pin specific component versions for reproducibility
- Exclude unnecessary components to reduce workspace size
- Integrate third-party libraries alongside SDK components
- Maintain multiple SDK configurations for different projects

## Prerequisites

- Git installed and configured
- West tool installed (`pip install west`)
- Understanding of YAML syntax
- Familiarity with Git repository URLs and revisions

## Understanding Manifest Structure

The MCUXpresso SDK uses a hierarchical manifest structure:

```
mcuxsdk-manifests/
├── west.yml                    # Root manifest
└── submanifests/
    ├── base.yml               # Core SDK repositories
    ├── middleware/
    │   ├── connectivity.yml   # Networking components
    │   ├── wireless.yml       # Bluetooth, 802.15.4
    │   ├── security.yml       # Crypto, secure boot
    │   └── ...
    └── internal.yml           # NXP internal (optional)
```

### Manifest File Format

```yaml
manifest:
  projects:
    - name: repository-name
      url: https://github.com/org/repo.git
      revision: main
      path: mcuxsdk/components/example
      import: true  # Import nested manifests
      groups:
        - optional  # Repository group membership
```

## Creating a Custom Manifest

### Method 1: Fork and Modify

**Step 1: Fork the Manifest Repository**

```bash
# Fork on GitHub: https://github.com/nxp-mcuxpresso/mcuxsdk-manifests
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mcuxsdk-manifests.git
cd mcuxsdk-manifests
```

**Step 2: Modify west.yml**

Edit `west.yml` to customize the manifest:

```yaml
manifest:
  # Keep default remotes
  remotes:
    - name: nxp-mcuxpresso
      url-base: https://github.com/nxp-mcuxpresso

  # Add your custom remote
  remotes:
    - name: my-company
      url-base: https://github.com/my-company

  # Modify project list
  projects:
    # Keep core SDK
    - name: mcuxsdk-core
      remote: nxp-mcuxpresso
      revision: main
      path: mcuxsdk

    # Add custom repository
    - name: my-custom-middleware
      remote: my-company
      revision: v1.0.0
      path: mcuxsdk/middleware/custom

  # Import submanifests selectively
  self:
    import:
      - submanifests/base.yml
      - submanifests/middleware/connectivity.yml
      # Exclude other middleware to reduce size
```

**Step 3: Initialize Workspace with Custom Manifest**

```bash
west init -m https://github.com/YOUR_USERNAME/mcuxsdk-manifests.git my-custom-sdk
cd my-custom-sdk
west update
```

### Method 2: Local Manifest Overlay

Create a local manifest file without forking:

**Step 1: Initialize Standard Workspace**

```bash
west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
cd mcuxpresso-sdk
```

**Step 2: Create Local Manifest**

Create `.west/config` with local manifest path:

```ini
[manifest]
path = manifests
file = west.yml

[manifest "local"]
path = .
file = west-local.yml
```

**Step 3: Create west-local.yml**

```yaml
manifest:
  projects:
    # Add additional repositories
    - name: my-custom-component
      url: https://github.com/my-org/custom-component.git
      revision: main
      path: mcuxsdk/components/custom

  # Override existing project revisions
  self:
    import:
      - manifests/west.yml  # Import base manifest
```

**Step 4: Update Workspace**

```bash
west update
```

## Common Customization Scenarios

### Scenario 1: Pin Specific Versions

Lock all repositories to specific releases for reproducibility:

```yaml
manifest:
  projects:
    - name: mcuxsdk-core
      revision: MCUX_2.15.0  # Specific tag instead of 'main'
      
    - name: mcux-sdk-middleware-usb
      revision: v2.15.0
```

### Scenario 2: Add Private Repository

Include proprietary middleware:

```yaml
manifest:
  remotes:
    - name: company-private
      url-base: https://git.company.com

  projects:
    - name: proprietary-stack
      remote: company-private
      revision: release-1.0
      path: mcuxsdk/middleware/proprietary
```

### Scenario 3: Exclude Optional Components

Reduce workspace size by excluding unused middleware:

```yaml
manifest:
  # Import only required submanifests
  self:
    import:
      - submanifests/base.yml
      - submanifests/middleware/connectivity.yml
      # Exclude graphics, audio, ML, etc.
```

### Scenario 4: Multi-Project Configuration

Maintain separate configurations for different products:

```bash
# Product A - Full featured
west init -m https://github.com/company/sdk-manifests.git --mr product-a sdk-product-a

# Product B - Minimal
west init -m https://github.com/company/sdk-manifests.git --mr product-b sdk-product-b
```

## Advanced Manifest Features

### Conditional Imports

Use groups to conditionally include repositories:

```yaml
manifest:
  projects:
    - name: optional-component
      groups:
        - optional

  # Enable optional group
  group-filter: [+optional]
```

Enable in workspace:

```bash
west config manifest.group-filter -- +optional
west update
```

### Nested Manifests

Import manifests from included repositories:

```yaml
manifest:
  projects:
    - name: middleware-collection
      import: true  # Import manifest from this repo
```

### Path Remapping

Change where repositories are checked out:

```yaml
manifest:
  projects:
    - name: mcuxsdk-core
      path: custom/location/core  # Non-default path
```

## Validating Custom Manifests

### Check Manifest Syntax

```bash
west manifest --validate
```

### List Resolved Projects

```bash
west list
```

### Show Manifest Resolution

```bash
west manifest --freeze > resolved-manifest.yml
```

This creates a fully-resolved manifest with all imports expanded.

## Best Practices

1. **Version Control Your Manifest**
   - Keep custom manifests in Git
   - Tag releases for reproducibility
   - Document customization rationale

2. **Test Before Deployment**
   - Validate manifest syntax
   - Test in clean workspace
   - Verify all repositories clone successfully

3. **Minimize Divergence**
   - Extend rather than replace base manifests
   - Use imports to leverage official manifests
   - Document all customizations

4. **Security Considerations**
   - Use HTTPS for public repositories
   - Configure SSH keys for private repos
   - Review third-party repository contents

5. **Maintenance**
   - Regularly sync with upstream manifests
   - Update pinned versions periodically
   - Test compatibility after updates

## Troubleshooting

**Manifest validation errors:**
```bash
west manifest --validate
# Fix YAML syntax errors reported
```

**Repository clone failures:**
- Verify repository URLs are accessible
- Check authentication for private repos
- Ensure revision/tag exists

**Import resolution errors:**
- Check imported manifest paths are correct
- Verify nested manifests are valid
- Use `west manifest --freeze` to debug

**Workspace update conflicts:**
```bash
# Reset to clean state
west forall -c "git reset --hard HEAD"
west update --rebase
```

## Example: Complete Custom Manifest

```yaml
# custom-sdk-manifest.yml
manifest:
  version: "0.13"

  remotes:
    - name: nxp-mcuxpresso
      url-base: https://github.com/nxp-mcuxpresso
    - name: company
      url-base: https://github.com/my-company

  defaults:
    remote: nxp-mcuxpresso
    revision: MCUX_2.15.0

  projects:
    # Core SDK - pinned version
    - name: mcuxsdk-core
      path: mcuxsdk

    # Selected middleware - pinned versions
    - name: mcux-sdk-middleware-usb
      revision: v2.15.0
      path: mcuxsdk/middleware/usb

    - name: mcux-sdk-middleware-lwip
      revision: v2.15.0
      path: mcuxsdk/middleware/lwip

    # Custom proprietary component
    - name: company-protocol-stack
      remote: company
      revision: v1.2.0
      path: mcuxsdk/middleware/company_stack

  # Import only base SDK, exclude optional components
  self:
    import:
      - submanifests/base.yml
```

Initialize workspace:

```bash
west init -m https://github.com/my-company/custom-sdk-manifest.git my-sdk
cd my-sdk
west update
```