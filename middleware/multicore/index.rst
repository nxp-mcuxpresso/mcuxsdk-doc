.. _multicore:

Multicore SDK
#############

Multicore Software Development Kit (MCSDK) provides comprehensive software support for NXP multicore devices. The MCSDK is combined with the MCUXpresso SDK to form a framework for easy development of multicore applications.

.. only:: html

   .. raw:: html

      <div class="mcsdk-stack-figure" style="max-width: 1100px; margin: 0 auto;">
        <style>
          .mcsdk-stack-figure svg.mcsdk-stack-svg {
            width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
          }
        </style>

   .. raw:: html
      :file: multicore-software-stack.svg

   .. raw:: html

        <p style="text-align:center; margin-top: 0.75rem; color: var(--pst-color-text-muted, #57606a);">Multicore SDK software stack (simplified).</p>
      </div>

.. only:: not html

   .. figure:: multicore-software-stack.svg
      :alt: Multicore SDK software stack
      :align: center
      :width: 85%

      Multicore SDK software stack (simplified).

Quick links
===========

* :doc:`Release Notes <mcsdk-release-notes>`
* :doc:`Getting Started <mcsdk-getting-started>`
* :doc:`Multicore SDK Changelog <CHANGELOG>`

Components
==========

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Component
     - Description
   * - :doc:`RPMSG-Lite <rpmsg-lite/index>`
     - Lightweight implementation of the Remote Processor Messaging (RPMsg) protocol for inter-core messaging.
   * - :doc:`Multicore Manager <mcmgr/index>`
     - Services for multicore systems (core start/stop, events, and monitoring).
   * - :doc:`eRPC <erpc>`
     - Embedded RPC system suitable for multicore and multiprocessor designs.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Quick links

   Release Notes <mcsdk-release-notes>
   Getting Started <mcsdk-getting-started>
   Multicore SDK Changelog <CHANGELOG>

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Components

   RPMSG-Lite <rpmsg-lite/index>
   Multicore Manager (MCMGR) <mcmgr/index>
   eRPC <erpc>
