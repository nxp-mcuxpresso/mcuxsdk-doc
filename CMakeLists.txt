# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)
project(Sdk-Doc LANGUAGES)
set(MIN_WEST_VERSION 1.0.0)


#-------------------------------------------------------------------------------
# Options

set(SPHINXOPTS "-j auto -W --keep-going -T" CACHE STRING "Default Sphinx Options")
set(SPHINXOPTS_EXTRA "" CACHE STRING "Extra Sphinx Options (added to defaults)")
set(LATEXMKOPTS "-halt-on-error -no-shell-escape" CACHE STRING "Default latexmk options")
set(DOC_TAG "development" CACHE STRING "Documentation tag, multiple tags are divided by comma")
set(DOC_DEFINE "" CACHE STRING "Documentation scope")

separate_arguments(SPHINXOPTS)
separate_arguments(SPHINXOPTS_EXTRA)
separate_arguments(LATEXMKOPTS)

# Split the DOC_TAG into a list
string(REPLACE "," ";" DOC_TAG_LIST "${DOC_TAG}")
set(SPHINX_DOC_TAGS "" CACHE STRING "Sphinx Documentation tags")
foreach(TAG ${DOC_TAG_LIST})
  set(SPHINX_DOC_TAGS "${SPHINX_DOC_TAGS} -t ${TAG}")
endforeach()
message(STATUS "Sphinx Documentation tags: ${SPHINX_DOC_TAGS}")
separate_arguments(SPHINX_DOC_TAGS)

# Split the DOC_DEFINE into a list and string append with -D
string(REPLACE "," ";" DOC_DEFINE_LIST "${DOC_DEFINE}")
set(SPHINX_DOC_DEFINES "" CACHE STRING "Sphinx Documentation defines")
foreach(DEFINE ${DOC_DEFINE_LIST})
  set(SPHINX_DOC_DEFINES "${SPHINX_DOC_DEFINES} -D ${DEFINE}")
endforeach()
message(STATUS "Sphinx Documentation defines: ${SPHINX_DOC_DEFINES}")
separate_arguments(SPHINX_DOC_DEFINES)

#-------------------------------------------------------------------------------
# Dependencies


find_program(SPHINXBUILD sphinx-build)
if(NOT SPHINXBUILD)
  message(FATAL_ERROR "The 'sphinx-build' command was not found")
endif()

find_package(LATEX COMPONENTS PDFLATEX)
find_program(LATEXMK latexmk)
if(NOT LATEX_PDFLATEX_FOUND OR NOT LATEXMK)
  message(WARNING "LaTeX components not found. PDF build will not be available.")
endif()

#-------------------------------------------------------------------------------
# Environment & Paths

set(SPHINX_ENV
  # DOXYGEN_EXECUTABLE=${DOXYGEN_EXECUTABLE}
  DOT_EXECUTABLE=${DOXYGEN_DOT_EXECUTABLE}
  DOCGEN_BRANCH=${DOCGEN_BRANCH}
  DOCGEN_REV=${DOCGEN_REV}
)

message(STATUS "Generation branch: ${DOCGEN_BRANCH}")
message(STATUS "Generation revision: ${DOCGEN_REV}")

# set(DOCS_CFG_DIR ${CMAKE_CURRENT_LIST_DIR})
# Check if SPHINX_CONF_DIR is passed from command line
if(DEFINED SPHINX_CONF_DIR)
  get_filename_component(SPHINX_CONF_DIR_ABS ${SPHINX_CONF_DIR} ABSOLUTE)
  set(DOCS_CFG_DIR ${SPHINX_CONF_DIR_ABS})
  # set(DOCS_CFG_DIR ${SPHINX_CONF_DIR})
else()
  # Default value if not provided
  set(DOCS_CFG_DIR ${CMAKE_CURRENT_LIST_DIR})
endif()

message(STATUS "CURRENT DIR = ${CMAKE_CURRENT_LIST_DIR}")
message(STATUS "Decided Sphinx configuration directory: ${DOCS_CFG_DIR}")

set(DOCS_DOCTREE_DIR ${CMAKE_CURRENT_BINARY_DIR}/doctrees)
set(DOCS_BUILD_DIR ${CMAKE_CURRENT_BINARY_DIR})
set(DOCS_SRC_DIR ${CMAKE_CURRENT_BINARY_DIR}/src)
set(DOCS_HTML_DIR ${CMAKE_CURRENT_BINARY_DIR}/html)
set(DOCS_LINKCHECK_DIR ${CMAKE_CURRENT_BINARY_DIR}/linkcheck)
set(DOCS_LATEX_DIR ${CMAKE_CURRENT_BINARY_DIR}/latex)

if(WIN32)
  set(SEP $<SEMICOLON>)
else()
  set(SEP :)
endif()

file(MAKE_DIRECTORY ${DOCS_SRC_DIR})

#-------------------------------------------------------------------------------
# Functions

# Create a custom doc target.
#
# This function has the same signature as `add_custom_target()`
#
# The function will create two targets for the doc build system.
# - Target 1 named: `<name>`
# - Target 2 named: `<name>-nodeps`
#
# Both targets will produce same result, but target 2 must have no dependencies.
# This is useful to, e.g. re-run the Sphinx build without dependencies such as
# latex generator.
#
function(add_doc_target name)
  add_custom_target(${name} ${ARGN})
  add_custom_target(${name}-nodeps ${ARGN})
endfunction()

#-------------------------------------------------------------------------------
# Doxygen (standalone)

message(STATUS "Config Doxygen Setup")
find_package(Doxygen REQUIRED dot)
list(APPEND SHPINX_ENV DOXYGEN_EXECUTABLE=${DOXYGEN_EXECUTABLE})
set(DOXY_OUT ${CMAKE_CURRENT_BINARY_DIR}/doxygen)
message(STATUS "DOXY_OUT: ${DOXY_OUT}")
set(DOXYFILE_IN ${CMAKE_CURRENT_LIST_DIR}/drivers/Doxyfile_lib_PDF_RM_Drivers)
set(DOXYFILE_OUT ${CMAKE_CURRENT_BINARY_DIR}/sdk.doxyfile)

configure_file(${DOXYFILE_IN} ${DOXYFILE_OUT} @ONLY)

add_custom_target(
  doxygen
  COMMAND
    ${DOXYGEN_EXECUTABLE} ${DOXYFILE_OUT}
  COMMENT "Running Doxygen..."
)

set_target_properties(
  doxygen
  PROPERTIES
    ADDITIONAL_CLEAN_FILES "${DOXY_OUT}"
)

#-------------------------------------------------------------------------------
# html

add_doc_target(
  html
  COMMAND ${CMAKE_COMMAND} -E env ${SPHINX_ENV}
  ${SPHINXBUILD}
    -b html
    -c ${DOCS_CFG_DIR}
    -d ${DOCS_DOCTREE_DIR}
    -w ${DOCS_BUILD_DIR}/html.log
    -D example_scope=${EXAMPLE_SCOPE}
    ${SPHINX_DOC_TAGS}
    ${SPHINX_DOC_DEFINES}
    ${SPHINXOPTS}
    ${SPHINXOPTS_EXTRA}
    ${DOCS_SRC_DIR}
    ${DOCS_HTML_DIR}
  USES_TERMINAL
  COMMENT "Running Sphinx HTML build..."
)

set_target_properties(
  html html-nodeps
  PROPERTIES
    ADDITIONAL_CLEAN_FILES "${DOCS_SRC_DIR};${DOCS_HTML_DIR};${DOCS_DOCTREE_DIR}"
)


#-------------------------------------------------------------------------------
# pdf

add_doc_target(
  latex
  COMMAND ${CMAKE_COMMAND} -E env ${SPHINX_ENV}
  ${SPHINXBUILD}
    -b latex
    -c ${DOCS_CFG_DIR}
    -d ${DOCS_DOCTREE_DIR}
    -w ${DOCS_BUILD_DIR}/latex.log
    -D example_scope=${EXAMPLE_SCOPE}
    # -t ${DOC_TAG}
    ${SPHINX_DOC_TAGS}
    -t svgconvert
    ${SPHINXOPTS}
    ${SPHINXOPTS_EXTRA}
    ${DOCS_SRC_DIR}
    ${DOCS_LATEX_DIR}
  USES_TERMINAL
  COMMENT "Running Sphinx LaTeX build..."
)

set_target_properties(
  latex latex-nodeps
  PROPERTIES
    ADDITIONAL_CLEAN_FILES "${DOCS_LATEX_DIR};${DOCS_DOCTREE_DIR}"
)

if(LATEX_PDFLATEX_FOUND AND LATEXMK)
  if(WIN32)
    set(PDF_BUILD_COMMAND "make.bat")
  else()
    find_program(MAKE make)
    if(NOT MAKE)
      message(FATAL_ERROR "The 'make' command was not found")
    endif()
    set(PDF_BUILD_COMMAND ${MAKE})
  endif()

  add_custom_target(
    pdf
    COMMAND ${CMAKE_COMMAND} -E env LATEXMKOPTS="${LATEXMKOPTS}"
    ${PDF_BUILD_COMMAND}
    WORKING_DIRECTORY ${DOCS_LATEX_DIR}
    COMMENT "Building PDF file..."
    USES_TERMINAL
  )

  add_dependencies(pdf latex)
endif()

