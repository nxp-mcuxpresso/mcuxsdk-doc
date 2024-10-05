.. _zephyr_doc:

Documentation Generation
########################

These instructions will walk you through generating the MCUXpresso SDK's
documentation on your local system using the same documentation sources
as we use to create the online documentation found at
https://nl2-nxrm.sw.nxp.com/repository/elastic-jenkins/sdk3_doc/latest_build/index.html

.. _documentation-overview:

Documentation overview
**********************

As inspired by Zephyr Project, MCUXPresso SDK content is written using the reStructuredText markup
language (.rst file extension), markdown with Sphinx extensions, and processed
using Sphinx to create a formatted stand-alone website. Developers can
view this content either in its raw form as .rst markup, .md files, or you
can generate the HTML content and view it with a web browser directly on
your workstation. This same .rst/.md content is also fed into the Zephyr
Project's public website documentation area (with a different theme
applied).

You can read details about `reStructuredText`_, and `Sphinx`_ from
their respective websites.

The project's documentation contains the following items:

* ReStructuredText/Markdown source files used to generate documentation found at the
  https://docs.zephyrproject.org website. Most of the reStructuredText/Markdown sources
  are found in the ``/docs`` directory, but others are stored within the
  code source tree near their specific component (such as ``/examples`` and
  ``/boards``)

* Doxygen-generated material used to create all API-specific documents
  also found at https://docs.zephyrproject.org

.. graphviz::
   :caption: Schematic of the documentation build process

   digraph {
      rankdir=LR

      images [shape="rectangle" label=".png, .jpg\nimages"]
      markdown [shape="rectangle" label=".md\nmarkdown files"]
      rst [shape="rectangle" label="restructuredText\nfiles"]
      modulen [shape="rectangle" label="Module N"]
      module1 [shape="rectangle" label="Module 1\ne,g. mid_wireless"]
      module_file [shape="rectangle" label="Module File\n_cfg/user_config.yml"]
      module_usr [shape="rectangle" label="-t mid_wireless\nUser Specify Modules"]
      conf [shape="rectangle" label="conf.py\nconfiguration"]
      rtd [shape="rectangle" label="read-the-docs\ntheme"]
      header [shape="rectangle" label="c header\ncomments"]
      doxycfg [shape="rectangle" label="Doxyfile\nDoxygen Config File"]
      xml [shape="rectangle" label="XML"]
      html [shape="rectangle" label="HTML\nweb site"]
      pdf [shape="rectangle" label="PDF\nprintable"]
      sphinx[shape="ellipse" label="sphinx +\nbreathe,\ndocutils"]

      images -> module1
      rst -> module1
      markdown -> module1
      module1 -> module_file
      modulen -> module_file
      module_file -> sphinx
      module_usr -> sphinx
      conf -> sphinx
      header -> doxygen
      doxycfg -> doxygen
      doxygen -> xml
      xml-> sphinx
      rtd -> sphinx
      sphinx -> html
      sphinx -> pdf
   }


The reStructuredText/Markdown files are processed by the Sphinx documentation system,
and make use of the breathe extension for including the doxygen-generated API
material.  Additional tools are required to generate the
documentation locally, as described in the following sections.

.. _documentation-processors:

Installing the documentation processors
***************************************

Our documentation processing has been tested to run with:

* Doxygen version 1.8.13
* Graphviz 2.43
* Latexmk version 4.56
* All Python dependencies listed in the repository file
  ``doc/requirements.txt``

In order to install the documentation tools, first install Zephyr as
described in :ref:`getting_started`. Then install additional tools
that are only required to generate the documentation,
as described below:

.. doc_processors_installation_start

.. tabs::

   .. group-tab:: Linux

      Common to all Linux installations, install the Python dependencies
      required to build the documentation:

      .. code-block:: console

         pip install -r docs/requirements.txt

      On Ubuntu Linux:

      .. code-block:: console

         sudo apt-get install --no-install-recommends doxygen graphviz librsvg2-bin \
         texlive-latex-base texlive-latex-extra latexmk texlive-fonts-recommended

      On Fedora Linux:

      .. code-block:: console

         sudo dnf install doxygen graphviz texlive-latex latexmk \
         texlive-collection-fontsrecommended librsvg2-tools

      On Clear Linux:

      .. code-block:: console

         sudo swupd bundle-add texlive graphviz

      On Arch Linux:

      .. code-block:: console

         sudo pacman -S graphviz doxygen librsvg texlive-core texlive-bin \
         texlive-latexextra texlive-fontsextra

   .. group-tab:: macOS

      Install the Python dependencies required to build the documentation:

      .. code-block:: console

         pip install -r ~/zephyrproject/zephyr/doc/requirements.txt

      Use ``brew`` and ``tlmgr`` to install the tools:

      .. code-block:: console

         brew install doxygen graphviz mactex librsvg
         tlmgr install latexmk
         tlmgr install collection-fontsrecommended

   .. group-tab:: Windows

      Install the Python dependencies required to build the documentation:

      .. code-block:: console

         pip install -r %HOMEPATH$\zephyrproject\zephyr\doc\requirements.txt

      Open a ``cmd.exe`` window as **Administrator** and run the following command:

      .. code-block:: console

         choco install doxygen.install graphviz strawberryperl miktex rsvg-convert

      .. note::
         On Windows, the Sphinx executable ``sphinx-build.exe`` is placed in
         the ``Scripts`` folder of your Python installation path.
         Depending on how you have installed Python, you might need to
         add this folder to your ``PATH`` environment variable. Follow
         the instructions in `Windows Python Path`_ to add those if needed.

.. doc_processors_installation_end

Documentation presentation theme
********************************

Sphinx supports easy customization of the generated documentation
appearance through the use of themes. Replace the theme files and do
another ``west doc html`` and the output layout and style is changed.
The ``read-the-docs`` theme is installed as part of the
:ref:`install_py_requirements` step you took in the getting started
guide.

Running the documentation processors
************************************

The ``/doc`` directory in your cloned copy of the Zephyr project git
repo has all the .rst source files, extra tools, and Makefile for
generating a local copy of the Zephyr project's technical documentation.
Assuming the local Zephyr project copy is in a folder ``zephyr`` in your home
folder, here are the commands to generate the html content locally:

.. code-block:: console

   cd ~/mcu-sdk-3.0/doc

   west doc html

   west doc pdf

.. warning::

   The documentation build system creates copies in the build
   directory of every .rst file used to generate the documentation,
   along with dependencies referenced by those .rst files.

   This means that Sphinx warnings and errors refer to the **copies**,
   and **not the version-controlled original files in Zephyr**. Be
   careful to make sure you don't accidentally edit the copy of the
   file in an error message, as these changes will not be saved.

Depending on your development system, it will take up to 15 minutes to
collect and generate the HTML content.  When done, you can view the HTML
output with your browser started at ``docs/_build/html/index.html`` and
if generated, the PDF file is available at ``doc/_build/latex/mcuxsdk.pdf``.

If you want to build the documentation from scratch just delete the contents
of the build folder and run ``west doc html`` again.

.. note::

   If you add or remove a file from the documentation, you need to re-run CMake.

On Unix platforms a convenience :zephyr_file:`doc/Makefile` can be used to
build the documentation directly from there:

.. code-block:: console

   cd docs

   # To generate HTML output
   make html

   # To generate PDF output
   make pdf

Filtering expected warnings
***************************

There are some known issues with Sphinx/Breathe that generate Sphinx warnings
even though the input is valid C code. While these issues are being considered
for fixing we have created a Sphinx extension that allows to filter them out
based on a set of regular expressions. The extension is named
``zephyr.warnings_filter`` and it is located at
``doc/_extensions/zephyr/warnings_filter.py``. The warnings to be filtered out
can be added to the ``doc/known-warnings.txt`` file.

The most common warning reported by Sphinx/Breathe is related to duplicate C
declarations. This warning may be caused by different Sphinx/Breathe issues:

- Multiple declarations of the same object are not supported
- Different objects (e.g. a struct and a function) can not share the same name
- Nested elements (e.g. in a struct or union) can not share the same name

Developer-mode Document Building
********************************

When making and testing major changes to the documentation, we provide an option
to only build the HTML output with specified modules so the doc build process run
faster.

To enable this mode, set the following option when invoking ``west doc``::

   -t module_name_a,module_name_b,module_name_regex_a,module_name_regex_b

   e,g. -t gsd,dev_.* will only build the HTML with gsd module and other modules
   starts with dev_

Viewing generated documentation locally
***************************************

The generated HTML documentation can be hosted locally with python for viewing
with a web browser:

.. code-block:: console

   $ python3 -m http.server -d _build/html

.. note::

   WSL2 users may need to explicitly bind the address to ``127.0.0.1`` in order
   to be accessible from the host machine:

   .. code-block:: console

      $ python3 -m http.server -d _build/html --bind 127.0.0.1

.. _reStructuredText: http://sphinx-doc.org/rest.html
.. _Sphinx: http://sphinx-doc.org/
.. _Windows Python Path: https://docs.python.org/3/using/windows.html#finding-the-python-executable
.. _Doxygen External Documentation: https://www.doxygen.nl/manual/external.html
