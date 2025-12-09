..
    MCUXpresso SDK Documentation master file

.. _mcux-sdk-home:

MCUXpresso SDK Documentation
############################


**Welcome to the MCUXpresso SDK Project documentation**

The whole MCUXpresso SDK delivery is provided under the `LA_OPT_Online_Code_Hosting`_ (as found in
the LA_OPT_Online_Code_Hosting.txt file in the project's `GitHub repo`_). The mcuxsdk-core project, alias the
core project, is the fundamental project of whole MCUXpresso SDK delivery. It is under the
`BSD-3-Clause`_ (as found in the COPYING-BSD-3.txt file in the project's `GitHub repo`_) which is quite a
permissive license. Other MCUXpresso SDK projects may use different licenses. Each repository includes a 
SBOM file with license information. We provide a west extension `sbom_merge` to merge SBOM files across all SDK repositories.

.. _BSD-3-Clause:
   https://github.com/nxp-mcuxpresso/mcuxsdk-core/blob/main/LICENSE

.. _LA_OPT_Online_Code_Hosting:
   https://github.com/nxp-mcuxpresso/mcuxsdk-manifests/blob/main/LICENSE

.. _SW-Content-Register:
   https://github.com/nxp-mcuxpresso/mcuxsdk-manifests/blob/main/SCR.txt

.. _GitHub repo: https://github.com/nxp-mcuxpresso/mcuxsdk-core

.. only:: html

.. toctree::
   :maxdepth: 1
   :caption: Introduction

   Overview <introduction/README.md>

.. toctree::
   :maxdepth: 1
   :caption: Releases

   Device Support <boards/index>
   Release Notes <release/index>
   Migration Guides <release/migration_guides>

.. toctree::
   :maxdepth: 1
   :caption: GETTING STARTED

   Install SDK <gsd/install/index>
   First Build <gsd/first.rst>
   Uninstall SDK <gsd/install/uninstall>

.. toctree::
   :maxdepth: 1
   :caption: User Guide

   Cmake User Guide <gsd/cmake_project_walkthrough.md>
   Kconfig User Guide <gsd/using_kconfig.md>
   Memory Management User Guide <gsd/memory_configuration.md>

.. toctree::
   :maxdepth: 2
   :caption: SDK REFERENCES

   Drivers <drivers/index.rst>
   Examples <examples/index.rst>
   Middleware <middleware/index>
   RTOS <rtos/index>
   develop/build_system/index
   develop/sdk/index

.. todolist::
