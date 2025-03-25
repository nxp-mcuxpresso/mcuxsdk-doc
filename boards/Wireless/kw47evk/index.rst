.. _kw47evk:

KW47-EVK
####################

Overview
********

The KW47EVK is an automotive evaluation kit development board for advanced development of the KW47B wireless MCU. It offers exhaustive evaluation of KW47 MCUs with 2.4 GHz Bluetooth Low Energy and generic FSK wireless connectivity and CAN/LIN connectivity.
The KW47 highly sensitive, optimized 2.4 GHz radio features a PCB meandered-antenna which can be bypassed to test via µ-RF connection.
The KW47EVK is a modular platform composed of the connectivity mother board KW-MCXW-EVK-MB and an M.2 module KW47-001-M10.
The board includes an advanced  MCU-Link debug probe, Power and low power option, dual CAN and LIN transceivers, buttons, switches, LEDs and integrated sensors, Arduino shield connectors, a MikroE Click connector and other headers.


.. image:: ./kw47evk.png
   :width: 240px
   :align: center
   :alt: KW47-EVK

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
