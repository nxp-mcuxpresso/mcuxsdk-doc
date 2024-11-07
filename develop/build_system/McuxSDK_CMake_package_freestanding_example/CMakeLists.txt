cmake_minimum_required(VERSION 3.30.0)

# include(${SdkRootDirPath}/cmake/extension/mcux.cmake)

find_package(McuxSDK 3.0.0 EXACT REQUIRED)

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
# target_sources(app PRIVATE
#     hello_world.c
    # pin_mux.c
    # pin_mux.h
    # hardware_init.c
    # app.h
# )

# target_include_directories(app PRIVATE
#   .
# )

# include(${SdkRootDirPath}/examples/${board}/demo_apps/hello_world/reconfig.cmake OPTIONAL)

# mcux_convert_binary(BINARY ${APPLICATION_BINARY_DIR}/${MCUX_SDK_PROJECT_NAME}.bin)
