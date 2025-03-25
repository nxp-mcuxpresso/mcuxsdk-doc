.. _mcxw71evk:

MCX-W71-EVK
####################

Overview
********

The MCXW71 EVK is an IIOT evaluation kit development board for advanced development of the MCX W71 wireless MCU. It offers exhaustive evaluation of the MCX W71's multiprotocol wireless support for Bluetooth LE, Zigbee, Thread and Matter and CAN connectivity.
The MCXW71 highly sensitive, optimized 2.4 GHz radio features a PCB meandered-antenna which can be bypassed to test via µ-RF connection.
The MCXW71 EVK is a modular platform composed of the connectivity mother board KW-MCXW-EVK-MB and an M.2 meandered antenna module MCXW71-M10.
The board includes an advanced  MCU-Link debug probe, Power and low power option, CAN transceiver, buttons, switches, LEDs and integrated sensors, Arduino shield connectors, a MikroE Click connector and other headers.


.. image:: ./mcxw71evk.png
   :width: 240px
   :align: center
   :alt: MCX-W71-EVK

MCU device and part on board is shown below:

 - Device: MCXW716C
 - PartNumber: MCXW716CMFTA

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

:ref:`MCXW716C_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Wireless Bluetooth LE host stack and applications
=================================================

:ref:`examples__wireless_examples__bluetooth_docs`

Wireless zigbee stack
=====================

:ref:`zigbee`

IEEE 802.15.4 MACPHY Software
=============================

:ref:`middleware_wireless_ieee_802_15_4`

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
