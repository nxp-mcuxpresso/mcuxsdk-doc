cmake_minimum_required(VERSION 3.30.0)

# include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

find_package(McuxSDK 3.0.0 EXACT REQUIRED CUSTOM_LINKER)

project(hello_world LANGUAGES C CXX ASM)

mcux_add_source(
  SOURCES     
    hello_world.c
    pin_mux.c
    pin_mux.h
    hardware_init.c
    app.h
)

mcux_add_include(
  INCLUDES 
    .
)

# The following flags are for MK22F51212
target_compile_options(app PRIVATE 
    -mcpu=cortex-m4
    -mfloat-abi=hard 
    -mfpu=fpv4-sp-d16
)

target_link_options(app PRIVATE 
    -mcpu=cortex-m4
    -mfloat-abi=hard 
    -mfpu=fpv4-sp-d16
)
