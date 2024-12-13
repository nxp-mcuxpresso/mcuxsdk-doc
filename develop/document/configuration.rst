
Documentation Config
######################

This section describe modularization and configuration of the MCUXpresso SDK Document

Config file
******************

Rather than placing the configuration in the Sphinx configuration file conf.py along with other non-configuration codes,
we place the document configuration in ``_cfg/user_config.yml`` inspected by schema to ease the configuration. The
configuration items includes the following:

* extensions
* document project name

Configuration Items
*********************

Extensions
==================

Extensions are the extension used by Sphinx document

.. code-block:: yaml

    extensions:
    - sphinx_rtd_theme
    - sphinx.ext.extlinks
    - vcs_link
    - sphinx.ext.todo
    - sphinx.ext.extlinks
    - myst_parser
    - external_content
    - page_filter
    - sphinx.ext.graphviz
    - sphinx_tabs.tabs

Source Suffix
==================

Source suffix is the mapping of the source file suffix to the document type, markdown file support require extension
of myst_parser

.. code-block:: yaml

    source_suffix:
      .rst: restructuredtext
      .readme: markdown
      .md: markdown

Contents
==================

MCUXpresso SDK document reuse the zephyr.external_content extension to include the external contents as well as
contents located in the docs/ directory and subdirectories so developer can place the document close to the source code.

Contents are copied into the folder ``_build/src`` according to configuration under the tag of ``external_contents``
in configuration files.

* root root directory of the external content, it will copied to ``_build/src`` with the relative path to this root
* pattern glob pattern to match the files to be copied

.. code-block:: yaml

    external_contents:
    - root: 'docs'
      pattern: 'index.rst'
    - root: 'docs'
      pattern: 'develop/index.rst'
    - root: docs
      pattern: 'generation.rst'
    - root: docs
      pattern: 'develop/document/*'

Cause the contents of these files are in different repositories, another zephyr extension ``vcs_link`` is used to link the
generated html pages to correct repository link
* pattern glob pattern to match the files to be linked
* link leading hyperlink of the repository, which will be conjunct with the relative path of the file to form the hyperlink

.. code-block:: yaml

    vcs_link:
    - pattern: examples/.*\.md
      replace_prefix: "examples/"
      link: "https://github.com/nxp-mcuxpresso/mcuxsdk-examples/"
    - pattern: examples/.*\.rst
      replace_prefix: "examples/"
      link: "https://github.com/nxp-mcuxpresso/mcuxsdk-examples/"

Internal Contents
==================

Some of the contents are internal only for development rather than for production. These contents are recorded
in the ``internal`` field in the configuration file and will be excluded if ``--internal`` flag is not specified
calling the ``west doc`` command.

Modules
==================

Contents of the document are organized in modules, each module can configure its own files, extensions and vcs_link so developer
can develop their own document and generate their concerned HTML contents much faster.

Module owner can add their content into the document by adding module into the module fields. To debug whether the modules is correctly
configured

* Run ``west doc -t your_module_name html``
* Check the log to know whether the tag `your_module_name` as marked as detected
* Check whether configured contents are copied into the ``_build/src`` folder
* Check whether your concerned content is generated into the HTML

.. code-block:: yaml

    modules:
      introduction:
        # Default as True stands include it into HTML if no tag is specified
        default: True
        external_contents:
        - root: 'docs'
          pattern: 'introduction/*'
      gsd:
        default: True
        external_contents:
        - root: 'docs'
          pattern: 'gsd/*'
      doxygen:
        default: true
        # Extensions are added for this module
        extensions:
        - breathe
        - doxyrunner
      examples:
        default: True
        external_contents:
        - root: .
          pattern: 'examples/**/*.md'
        - root: .
          pattern: 'examples/**/*.jpg'
        - root: .
          pattern: 'examples/**/*.png'
        - root: .
          pattern: 'examples/**/index.rst'
        vcs_link:
        - pattern: examples/.*\.md
          replace_prefix: "examples/"
          link: "https://github.com/nxp-mcuxpresso/mcuxsdk-examples/"
        - pattern: examples/.*\.rst
          replace_prefix: "examples/"
          link: "https://github.com/nxp-mcuxpresso/mcuxsdk-examples/"
    
Doxygen Config
==================

Doxygen in C Header/C files are generated into the HTML by the breathe extension, the configuration of the doxygen
is located in `docs/drivers/Doxyfile_lib_PDF_RM_Drivers` and the output is located in `_build/doxygen` folder.

Add contents into doxygen

* Append additional content into the ``INPUT`` field of doxygen configuration files with leading characters of ``@SDk_BASE@`` which
  will be replaced by the SDK base directory by doxyrunner plugin

To verify whether the doxygen is correctly configured
* Run ``west doc -t doxygen html`` to generate the doxygen HTML
* To run the doxygen in faster way, you can temporarily comment out the not needed lines in doxygen configuration files