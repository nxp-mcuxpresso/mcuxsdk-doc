cmake_minimum_required(VERSION 3.30.0)

include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

# No PROJECT_BOARD_PORT_PATH in project
project(hello_world LANGUAGES C CXX ASM)

include(${SdkRootDirPath}/CMakeLists.txt)

mcux_add_source(
    SOURCES hello_world.c
        pin_mux.c
        hardware_init.c
)

mcux_add_include(
    INCLUDES .
)

mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
