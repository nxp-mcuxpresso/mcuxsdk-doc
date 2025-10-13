.. _gsd_pack_index:

Getting Started with MCUXpresso SDK Package
===========================================

Starting with version 25.09.00, MCUXpresso SDK introduced two package versions for offline development:
   - **Classic SDK Package**: Traditional board-specific packages with pre-configured IDE projects for MCUXpresso IDE, IAR, Keil, and other toolchains.
   - **Repository-Layout SDK Package**: Board-specific packages that maintain the same structure and build system as the GitHub Repository SDK, providing offline access to the repository SDK development experience. Available when selecting the ARMGCC toolchain.

From version 25.12.00 onward:
   - When you select ARMGCC, the SDK download will use the Repository-Layout version.
   - For all other toolchains, the SDK download will remain in the Classic version.

Note: The Repository-Layout SDK package was first introduced in version 25.09.00, but initially only for MCXW23x platforms.

Classic SDK Package
-------------------

.. toctree::
   :maxdepth: 1

   package/overview.md
   package/mcuxpresso_sdk_board_support_package_folders.md
   package/run_a_demo_using_mcuxpresso_ide.md
   package/run_a_demo_application_using_iar.md
   package/run_a_demo_using_keil__mdk_vision.md
   package/run_a_demo_using_arm__gcc.md
   package/mcuxpresso_config_tools.md
   package/how_to_determine_com_port.md
   package/on_board_debugger.md
   package/default_debug_interfaces.md
   package/how_to_define_irq_handler_in_cpp_files.md

Repository-Layout SDK Package
------------------------------

.. toctree::
   :maxdepth: 1

   installation
   first_build
   run_a_demo_using_mcuxvsc
   run_project
   explore_sdk
