cmake_minimum_required(VERSION 3.30.0)

# Get MCUXSDK_MAIN_VERSION from MCUX_VERSION file
include(${SdkRootDirPath}/cmake/extension/mcux_version.cmake)

find_package(McuxSDK ${MCUXSDK_MAIN_VERSION} EXACT REQUIRED)

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
