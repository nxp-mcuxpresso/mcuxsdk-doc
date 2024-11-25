This is a Practical examples for external module integration:

1. Download zcbor library from https://github.com/NordicSemiconductor/zcbor.git
2. Copy "mcux" to zcbor repo root path
3. Add `CONFIG_MCUX_COMPONENT_ZCBOR=y` in prj.conf
4. Build with command `west build -b frdmk64f ./examples/src/demo_apps/hello_world  -p always --toolchain armgcc -DEXTRA_MCUX_MODULES=path/to/zcbor`