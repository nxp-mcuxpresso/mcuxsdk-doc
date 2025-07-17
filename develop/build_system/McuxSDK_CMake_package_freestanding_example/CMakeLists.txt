cmake_minimum_required(VERSION 3.30.0)

# include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

find_package(McuxSDK 3.0.0 EXACT REQUIRED)

project(hello_world LANGUAGES C CXX ASM)

mcux_add_source(
  SOURCES     
    hello_world.c
    hardware_init.c
    app.h
)

mcux_add_include(
  INCLUDES 
    .
)
