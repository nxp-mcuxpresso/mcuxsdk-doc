# Run a Demo Using IAR

The Repository-Layout SDK Package does not ship pre-generated IDE projects. Instead,
you generate an IAR Embedded Workbench project on demand from the CMake build, the same
way you would from a GitHub Repository SDK checkout.

## Prerequisite: Ruby

IDE project generation is implemented in Ruby and is only needed if you want to use IAR
instead of the command line or VS Code. See
[Ruby - IDE Project Generation (Optional)](installation.md#ruby---ide-project-generation-optional)
for setup instructions before continuing.

## 1. Generate the IAR project

If this is a pristine build, specify board, example, toolchain and core on the command
line:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug -p always -t guiproject
```

If you already built the example with `west build`, you can regenerate the project with
the shorter form:

```bash
west build -t guiproject
```

The project files are generated into `mcuxsdk/build/iar`, using relative paths to refer
to source files and include paths in the repository. For the full set of `guiproject`
options, see [IDE Project Generation](/develop/build_system/IDE_Project.md).

### Generate into a custom folder

By default the project is generated into `mcuxsdk/build/<toolchain>`. To generate into a
different location instead — for example to keep projects for several examples or
boards side by side — pass `-d` with the pristine build command:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain iar -Dcore_id=cm7 --config flexspi_nor_debug -p always -t guiproject -d build_hello_world_iar
```

## 2. Open the project in IAR Embedded Workbench

Open the generated workspace or project file from:

```
mcuxsdk/build/iar
```

## 3. Build the demo application

1. Select the desired build target from the drop-down menu, for example
   **hello_world - flexspi_nor_debug**.
2. Click **Make** to build the demo application.
3. The build completes without errors.

## 4. Run the demo application

1. Open a terminal application on the PC, such as PuTTY or TeraTerm, and connect to the
   debug COM port (see
   [How to determine COM port](/gsd/package/how_to_determine_com_port.md)).
2. Click **Download and Debug** to flash and start debugging.
3. Click **Go** to run to the entry point and resume execution.
4. The terminal displays the demo application output.

## Next steps

- [Run a demo using MDK](run_a_demo_using_mdk.md) — the same flow for Keil MDK
- [Building Your First Project](first_build.md) — build and run from the command line
