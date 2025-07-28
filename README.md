# MCUXpresso SDK : mcuxsdk-doc

This repository contains the documentation source files and build infrastructure for MCUXpresso SDK. The repository also includes examples guidelines, middleware documentation, and so on. The documentation is built using [Sphinx](https://www.sphinx-doc.org/) with the [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/) theme and leverages the Zephyr project's documentation framework. The content is authored in the reStructuredText (.rst) and Markdown (.md) formats. The authored content is then processed by Sphinx to generate a standalone website and is deployed at https://mcuxpresso.nxp.com/mcuxsdk/latest/html/.

## Architecture Overview

MCUXpresso SDK follows a multi-repository architecture where individual components are organized as separate repositories and managed through the [west tool](https://docs.zephyrproject.org/latest/develop/west/index.html). This documentation repository serves as one of several sub-repositories that collectively form the complete SDK ecosystem.

**Important:** The complete MCUXpresso SDK documentation is distributed across multiple repositories. While this repository contains the core documentation infrastructure and primary content, additional documentation sources are embedded within their respective component repositories, including:
- Example application guidelines and documentation (see [mcuxsdk-examples](https://github.com/nxp-mcuxpresso/mcuxsdk-examples))
- Middleware-specific documentation and API references (see [mcuxsdk-middleware-connectivity-framework](https://github.com/nxp-mcuxpresso/mcuxsdk-middleware-connectivity-framework))
- Component-specific user guides and implementation notes

To build the complete documentation with all sources, you must download the entire SDK ecosystem through the manifest repository.

The primary entry point for the entire project is the manifest repository [mcuxsdk-manifests](https://github.com/nxp-mcuxpresso/mcuxsdk-manifests), which orchestrates the multi-repository structure and provides unified access to all SDK components and their associated documentation.

## Getting Started

### Prerequisites

Before building documentation locally, ensure you have the following software installed:

**Required Software:**
- Python 3.8 or later
- pip package manager  
- Doxygen 1.9.1 or later
- Graphviz 2.40 or later
- LaTeX distribution (required for PDF generation)

### Initial Setup

MCUXpresso SDK uses a west-based multi-repository structure managed through manifest files. To access the complete documentation sources and build the full documentation set, you must initialize from the manifest repository.

> **Important:** Do not clone this repository directly for complete documentation builds. This repository alone contains only a subset of the total documentation sources. Follow the complete setup process outlined in the [Getting Started with SDK - Detailed Installation Instructions](https://mcuxpresso.nxp.com/mcuxsdk/latest/html/gsd/installation.html#installation).

The setup process includes:
1. Installing the west tool and its dependencies
2. Initializing the workspace from the manifest repository using west
3. Cloning and updating all sub-repositories via west (this includes all documentation sources)
4. Configuring the build environment for SDK components and documentation

### Installing Dependencies

#### Python Dependencies
Navigate to the docs folder located at `${west_workspace}/mcuxsdk/docs`, then run the following command:
```bash
pip install -r requirements.txt
```

#### System Dependencies

**Windows (using Chocolatey):**
```bash
choco install doxygen.install graphviz strawberryperl miktex rsvg-convert imagemagick
```

**macOS (using Homebrew):**
```bash
brew install doxygen graphviz mactex librsvg imagemagick
```

**Ubuntu/Debian:**
```bash
sudo apt-get install --no-install-recommends doxygen graphviz librsvg2-bin \
  texlive-latex-base texlive-latex-extra latexmk texlive-fonts-recommended imagemagick
```

## Building Documentation

### Using West Extension Commands

The SDK provides a west extension command `west doc` for building documentation. Use `west doc <target>` to build documentation for different output formats.

> **Note:** The following commands will build documentation using all available sources when run from a complete SDK workspace initialized via the manifest repository. If run from this repository alone, only the core documentation will be built.

#### HTML Documentation
```bash
west doc html
```
Generates complete HTML documentation in the `docs/_build/html/` directory.

#### PDF Documentation
```bash
west doc pdf
```
Generates complete PDF documentation as `docs/_build/latex/mcuxsdk.pdf`.

#### View Documentation
```bash
west doc view
```
Builds HTML documentation, starts a local HTTP server, and opens the documentation in your default web browser.

### Performance Considerations

> **Important:** Full documentation generation is not recommended for routine development due to performance constraints. Complete builds can take approximately 4 hours. For development and validation purposes, use selective documentation generation as described below.

### Selective Documentation Generation

The documentation system is organized into modules, with each module maintaining its component-specific documentation. This modular architecture enables efficient development workflows and faster validation cycles.

#### Module-Level Generation

Generate documentation for a specific module:
```bash
west doc html -t <module_name>
```

Available module names and their included sources are defined in the [configuration file](docs/_cfg/user_config.yml). This approach includes only the specified module's documentation sources in the build process.

#### Board-Level Generation

Generate documentation for a specific board:
```bash
west doc html --board <board_name>
```

This command identifies all modules relevant to the specified board and includes only those modules in the build process. Available board names can be found in the `docs/boards/` directory.

> **Note:** Replace `html` with `pdf` in the above commands to generate PDF output instead of HTML.

## Project Structure

```
mcuxsdk-doc/
├── docs/                   # Main documentation directory
│   ├── _cfg/              # Configuration files
│   │   └── user_config.yml # Module and build configuration
│   ├── _doxygen/          # Doxyfiles for API reference generation
│   ├── _extensions/       # Custom Sphinx extensions
│   ├── _static/           # Static assets (images, CSS, JavaScript)
│   ├── _templates/        # Jinja2 templates for documentation processing
│   ├── boards/            # Board-specific documentation by device series
│   ├── develop/           # Development guidelines and SDK usage patterns
│   ├── drivers/           # Device driver documentation and examples
│   ├── gsd/               # Getting Started Guide documentation
│   ├── introduction/      # SDK overview and architectural introduction
│   ├── middleware/        # Middleware components documentation index
│   ├── release/           # Release notes, quality documentation, known issues
│   ├── rtos/              # Real-time operating system documentation
│   ├── scripts/           # Build automation and generation scripts
│   ├── _build/            # Generated documentation output (created during build)
│   │   ├── html/          # HTML documentation output
│   │   └── latex/         # LaTeX and PDF output
│   └── requirements.txt   # Python package dependencies
└── README.md              # Project documentation (this file)

# Additional documentation sources (available only in complete SDK workspace):
# ├── examples/             # Example applications with embedded documentation
# ├── middleware/           # Middleware components with integrated documentation  
# ├── components/           # Component libraries with API documentation
# └── boards/               # Board support packages with hardware documentation
```

## Troubleshooting

### Common Build Issues

**Incomplete Documentation Sources:**
- Ensure you have initialized the complete SDK workspace via the manifest repository
- Verify all sub-repositories are properly cloned and updated using `west update`
- Missing documentation may indicate incomplete workspace setup

**Missing Dependencies:**
- Ensure all system dependencies are installed according to your platform
- Verify Python version compatibility (3.8 or later)
- Confirm that Doxygen and Graphviz are accessible from the command line

**Build Performance Issues:**
- Use selective generation for development (`-t <module>` or `--board <board>`)
- Ensure sufficient disk space for full builds (several GB required)
- Consider using faster storage (SSD) for improved build times

**Path and Configuration Issues:**
- Ensure you're running commands from the correct workspace root directory
- Verify that the west tool is properly initialized and configured
- Check that all required repositories are properly cloned via west

**Documentation Rendering Issues:**
- Clear the `_build` directory if experiencing stale content issues
- Verify that all referenced files and images exist in the source tree
- Check Sphinx error messages for missing dependencies or syntax errors

## Contributions

Currently, community contributions are not accepted. Guidelines for the external contributions/contributors would be published as the project evolves and the contribution workflow is established.

## Support

For details on the recent updates, see:

- **Official Documentation:** https://mcuxpresso.nxp.com/mcuxsdk/latest/html/
- **Installation Guide:** [Getting Started with SDK - Detailed Installation Instructions](https://mcuxpresso.nxp.com/mcuxsdk/latest/html/gsd/installation.html#installation)
- **SDK Manifest Repository:** [mcuxsdk-manifests](https://github.com/nxp-mcuxpresso/mcuxsdk-manifests)

## License

This project is licensed under the BSD-3-Clause License. For details, see the LICENSE file.