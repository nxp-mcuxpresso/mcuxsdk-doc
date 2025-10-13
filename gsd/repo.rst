.. _gsd_index:

Getting Started with MCUXpresso SDK Repository
==============================================

Welcome to the **GitHub Repository SDK Guide**. This documentation provides instructions for setting up and working with the MCUXpresso SDK distributed in a **multi-repository model**.
The SDK is distributed across multiple GitHub repositories and managed using the **Zephyr West** tool, enabling modular development and streamlined workflows.

Overview
--------

The GitHub Repository SDK approach offers:

- **Modular Structure**: Multiple repositories for flexibility and scalability.
- **Zephyr West Integration**: Simplified repository management and synchronization.
- **Cross-Platform Support**: Designed for MCUXpresso SDK development environments.

Benefits of the Multi-Repository Approach
-----------------------------------------

- **Scalability**: Easily add or update components without impacting the entire SDK.
- **Collaboration**: Enables distributed development across teams and repositories.
- **Version Control**: Independent versioning for components ensures better stability.
- **Automation**: Zephyr West simplifies dependency handling and repository synchronization.

Setup and Configuration
------------------------

Follow these steps to prepare your development environment:

.. toctree::
   :maxdepth: 1

   installation
   repo_setup


.. only:: internal_doc

   Internal Repo Checkout
   ----------------------
   This section provides internal-only instructions for managing private repositories and workflows.

   .. toctree::
      :maxdepth: 1

      ../bifrost/readme.md


Explore SDK Structure and Content
---------------------------------

Learn about the organization of the SDK and its components:

.. toctree::
   :maxdepth: 1

   codebase
   explore_sdk

Development Workflows
----------------------

Get started with building and running projects:

.. toctree::
   :maxdepth: 1

   first_build
   run_a_demo_using_mcuxvsc
   run_project