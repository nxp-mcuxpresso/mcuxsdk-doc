# Run a Demo Using MDK

The Repository-Layout SDK Package does not ship pre-generated IDE projects. Instead,
you generate a Keil MDK (μVision) project on demand from the CMake build, the same way
you would from a GitHub Repository SDK checkout.

## Prerequisites

### Ruby

IDE project generation is implemented in Ruby and is only needed if you want to use MDK
instead of the command line or VS Code. See
[Ruby - IDE Project Generation (Optional)](installation.md#ruby---ide-project-generation-optional)
for setup instructions before continuing.

### CMSIS device pack

Cortex Microcontroller Software Interface Standard (CMSIS) device packs must be
installed in MDK to fully support the device from a debug perspective, including memory
map information, register definitions, and flash programming algorithms. In μVision,
select the **Pack Installer** icon and install the pack for your device before opening
the generated project.

## 1. Generate the MDK project

If this is a pristine build, specify board, example, toolchain and core on the command
line:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain mdk -Dcore_id=cm7 --config flexspi_nor_debug -p always -t guiproject
```

If you already built the example with `west build`, you can regenerate the project with
the shorter form:

```bash
west build -t guiproject
```

The project files are generated into `mcuxsdk/build/mdk`, using relative paths to refer
to source files and include paths in the repository. For the full set of `guiproject`
options, see [IDE Project Generation](/develop/build_system/IDE_Project.md).

### Generate into a custom folder

By default the project is generated into `mcuxsdk/build/<toolchain>`. To generate into a
different location instead — for example to keep projects for several examples or
boards side by side — pass `-d` with the pristine build command:

```bash
west build -b evkbmimxrt1170 examples/demo_apps/hello_world --toolchain mdk -Dcore_id=cm7 --config flexspi_nor_debug -p always -t guiproject -d build_hello_world_mdk
```

## 2. Open the project in μVision

Open the generated `.uvmpw` workspace file from:

```
mcuxsdk/build/mdk
```

## 3. Build the demo application

1. Select **Rebuild** to build the demo project.
2. The build completes without errors.

## 4. Run the demo application

1. Open a terminal application on the PC, such as PuTTY or TeraTerm, and connect to the
   debug COM port (see
   [How to determine COM port](/gsd/package/how_to_determine_com_port.md)).
2. Click the **Download** button to download the application to the target.
3. Click the **Start/Stop Debug Session** button to enter the debug session.
4. Click the **Run** button to start the application.
5. The terminal displays the demo application output.

## Next steps

- [Run a demo using IAR](run_a_demo_using_iar.md) — the same flow for IAR Embedded Workbench
- [Building Your First Project](first_build.md) — build and run from the command line
