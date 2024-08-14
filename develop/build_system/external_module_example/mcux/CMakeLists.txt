cmake_minimum_required(VERSION 3.20.0)

if(CONFIG_MCUX_COMPONENT_ZCBOR)
    add_library(zcbor)

    target_sources(zcbor PRIVATE
            ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_common.c
            ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_decode.c
            ${MCUX_ZCBOR_MODULE_DIR}/src/zcbor_encode.c
    )

    target_include_directories(zcbor PUBLIC
            ${MCUX_ZCBOR_MODULE_DIR}/include
    )

    target_compile_definitions(zcbor PRIVATE _POSIX_C_SOURCE=200809L)

    if(CONFIG_ZCBOR_CANONICAL)
        target_compile_definitions(zcbor PRIVATE ZCBOR_CANONICAL)
    endif ()

    if(CONFIG_ZCBOR_STOP_ON_ERROR)
        target_compile_definitions(zcbor PRIVATE ZCBOR_STOP_ON_ERROR)
    endif ()

    if(CONFIG_ZCBOR_VERBOSE)
        target_compile_definitions(zcbor PRIVATE ZCBOR_VERBOSE)
    endif ()

    if(CONFIG_ZCBOR_ASSERT)
        target_compile_definitions(zcbor PRIVATE ZCBOR_ASSERTS)
    endif ()

    if(CONFIG_ZCBOR_BIG_ENDIAN)
        target_compile_definitions(zcbor PRIVATE ZCBOR_BIG_ENDIAN)
    endif ()

    target_link_libraries(${MCUX_SDK_PROJECT_NAME} PRIVATE zcbor)
endif()