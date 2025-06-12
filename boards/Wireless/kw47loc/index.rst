:pdf-download: ../../../_assets/boards/kw47loc/mcuxsdk-kw47loc.pdf
.. _kw47loc:

KW47-LOC
####################

Overview
********

The KW47 LOC is an evaluation kit for KW47 Automotive MCU with 2.4 GHz Bluetooth Low Energy and generic FSK wireless connectivity and dual CAN/LIN connectivity. This localization platform is dedicated to Bluetooth Channel Sounding Ranging solution development with a dedicated on-chip Localization Compute Engine to reduce ranging latency. The KW47's highly sensitive, optimized 2.4 GHz radio features is featured with dual antenna diversity via RF switch which can be bypassed to test via SMA RF connection.
The board includes an advanced  MCU-Link debug probe, Power and low power option, dual CAN transceiver, buttons, switches, LEDs and a MikroE Click connector.



.. image:: ./kw47loc.png
   :width: 240px
   :align: center
   :alt: KW47-LOC

MCU device and part on board is shown below:

 - Device: KW47B42ZB7
 - PartNumber: KW47B42ZB7AFTA

Getting Started with MCUXpresso SDK Package
*******************************************
.. toctree::
   :maxdepth: 1

   gettingStarted/gsindex.md

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

:ref:`KW47B42ZB7_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Wireless Bluetooth LE host stack and applications
=================================================

:ref:`examples__wireless_examples__bluetooth_docs`

Wireless Connectivity Framework
===============================

.. toctree::
   :maxdepth: 1

   ../../../middleware/wireless/framework/index.rst



Multicore
=========

:ref:`multicore`

FreeMASTER
==========

.. toctree::
   :maxdepth: 1

   ../../../middleware/freemaster/doc/index.md



FreeRTOS
========

:ref:`freertos`
