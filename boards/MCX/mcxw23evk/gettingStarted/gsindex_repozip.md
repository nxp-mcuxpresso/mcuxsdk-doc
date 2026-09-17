<!--
Template for a board-specific Repository-Layout (repo-zip) Getting Started index.

This file is a template, not a real page - it is excluded from the Sphinx build
(see `exclude_patterns` in conf.py). To create a real getting-started page for a
board's repo-zip package, copy this file to:

    boards/<family>/<board>/gettingStarted/gsindex_repozip.md

and adjust the topics list below:
  - Keep the absolute `/gsd/...` references for shared, board-agnostic content.
  - If the board needs board-specific content (a non-standard debug probe, a
    board-specific COM port note, etc.), add a local `topics/<name>.md` file next
    to this one and list it alongside the shared references, the same way the
    Classic package's `gettingStarted/gsindex.md` mixes local `topics/*.md` files
    with shared `/gsd/package/topics/*.md` references.
-->

# Getting Started with Repository-Layout SDK Package

Starting with version 25.09.00, MCUXpresso SDK introduced the Repository-Layout SDK Package for offline development:

- **Repository-Layout SDK Package**: A board-specific package that preserves the same structure and build system as the GitHub Repository SDK and provides offline access to the Repository SDK development experience. This package is available when you select the ARMGCC toolchain.

Starting with version 25.12.00, the SDK Builder downloads the Repository-Layout SDK Package by default when you select ARMGCC.

Note: MCUXpresso SDK first introduced the Repository-Layout SDK Package in version 25.09.00, but only for MCXW23x platforms.

```{tocTree}
:maxdepth: 4
:caption: Table of Contents

/gsd/installation.md
/gsd/explore_sdk.md
/gsd/first_build.md
/gsd/run_a_demo_using_iar.md
/gsd/run_a_demo_using_mdk.md
/gsd/run_a_demo_using_mcuxvsc.md
topics/how_to_determine_com_port.md
topics/updating_debugger_firmware.md
```
