# ------------------------------------------------------------------------------
# Makefile for documentation build
# SPDX-License-Identifier: Apache-2.0

BUILDDIR ?= _build
DOC_TAG ?= development
SPHINXOPTS ?= -j auto --keep-going -T
SPHINXOPTS_EXTRA ?=
LATEXMKOPTS ?= -halt-on-error -no-shell-escape
DT_TURBO_MODE ?= 0
DOCGEN_BRANCH ?= main
DOCGEN_REV ?= 851c5ddabe8

# ------------------------------------------------------------------------------
# Documentation targets

.PHONY: configure clean html latex pdf doxygen

html latex pdf linkcheck doxygen: configure
	cmake --build ${BUILDDIR} --target $@

# Define multiple configuration options for conf.py from different directory
SPHINX_CONF_DIR ?=.

configure:
	cmake \
		-GNinja \
		-B${BUILDDIR} \
		-S. \
		-DDOC_TAG=${DOC_TAG} \
		-DSPHINXOPTS="${SPHINXOPTS}" \
		-DSPHINXOPTS_EXTRA="${SPHINXOPTS_EXTRA}" \
		-DLATEXMKOPTS="${LATEXMKOPTS}" \
		-DDOCGEN_BRANCH=$(DOCGEN_BRANCH) \
		-DDOCGEN_REV=$(DOCGEN_REV) \
		-DSPHINX_CONF_DIR=${SPHINX_CONF_DIR}

clean:
	cmake --build ${BUILDDIR} --target clean
