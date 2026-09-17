:pdf-download: ../../../_assets/boards/kw43loc/mcuxsdk-kw43loc.pdf

.. _kw43loc:

KW43-LOC
####################

Overview
********

The KW43-LOC is an automotive evaluation kit development board for advanced development of the KW43 wireless MCU. This localization platform is dedicated to Bluetooth Channel Sounding Ranging solution development with a dedicated on-chip Localization Compute Engine to reduce ranging latency. It offers exhaustive evaluation of KW43 MCUs with 2.4 GHz Bluetooth Low Energy and generic FSK wireless connectivity and CAN connectivity.
The board includes an advanced MCU-Link debug probe, Power and low power option, CAN transceivers, buttons, switches, LEDs and integrated sensors, a MikroE Click connector and other headers.


.. image:: ./kw43loc.png
   :width: 240px
   :align: center
   :alt: KW43-LOC

MCU device and part on board is shown below:

 - Device: KW43B43ZC7
 - PartNumber: KW43B43ZC7MFT

SDK Introduction
*******************

.. only:: html

   For an introduction to the MCUXpresso SDK, see :doc:`MCUXpresso Software Development Kit (SDK) </introduction/README>`.

.. only:: latex

   .. toctree::
      :maxdepth: 1

      /introduction/README

Getting Started with Repository-Layout SDK Package
*******************************************
.. toctree::
   :maxdepth: 1

   gettingStarted/gsindex_repozip.md

Getting Started with MCUXpresso SDK GitHub
*******************************************
.. toctree::
   :maxdepth: 1

   ../../../gsd/repo.rst

Release Notes
*******************************************

**This is an early adopter release provided as preview for development with pre-production devices.**

.. toctree::
   :maxdepth: 1

   releaseNotes/rnindex.md

ChangeLog
*******************************************
.. toctree::
   :maxdepth: 1

   changeLog/clindex.md

Driver API Reference Manual
****************************

This section provides a link to the Driver API RM, detailing available drivers and their usage to help you integrate hardware efficiently.

:ref:`KW43B43ZC7_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Wireless Bluetooth LE host stack and applications
=================================================

:ref:`examples__wireless_examples__bluetooth_docs`

Wireless Connectivity Framework
===============================

:doc:`framework <../../../middleware/wireless/framework/index>`

FreeRTOS
========

:ref:`freertos`

Trusted-Frimware-M
==================

:ref:`tfm`
