:pdf-download: ../../../_assets/boards/evkcmimxrt1060/mcuxsdk-evkcmimxrt1060.pdf
.. _evkcmimxrt1060:

MIMXRT1060-EVKC
####################

Overview
********

The i.MX RT1060 EVKC is a 4-layer through-hole USB-powered PCB. At its heart lies the i.MX RT1060 crossover MCU, featuring NXPs advanced implementation of the Arm Cortex-M7 core. This core operates at speeds up to 600 MHz to provide high CPU performance and excellent real-time response.



Support for FreeRTOS available within the MCUXpresso SDK.



The i.MX RT1060 Evaluation Kit is supported by Zephyr OS for developing the Internet of Things with a free, open-source embedded operating system.



Rev B includes M.2 and audio interfaces.



.. image:: ./evkcmimxrt1060.png
   :width: 240px
   :align: center
   :alt: MIMXRT1060-EVKC

MCU device and part on board is shown below:

 - Device: MIMXRT1062
 - PartNumber: MIMXRT1062DVL6B

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

:ref:`MIMXRT1062_drivers`

Middleware Documentation
*****************************

Find links to detailed middleware documentation for key components. While not all onboard middleware is covered, this serves as a useful reference for configuration and development.


Multicore
=========

:ref:`multicore`

MCU Boot
========

.. toctree::
   :maxdepth: 1

   ../../../middleware/mcuboot_opensource/README.md



Audio Voice components
======================

:ref:`components`

Maestro Audio Framework for MCU
===============================

:ref:`maestro`

eIQ
===

:ref:`eiq`

FreeMASTER
==========

.. toctree::
   :maxdepth: 1

   ../../../middleware/freemaster/doc/index.md



AWS IoT
=======

:ref:`aws_iot`

NXP Wi-Fi
=========

:ref:`wifi-bluetooth-802.15.4`

FreeRTOS
========

:ref:`freertos`

Wireless EdgeFast Bluetooth PAL
===============================

:ref:`edgefast_bluetooth`

lwIP
====

:ref:`lwip`

File systemFatfs
================

:ref:`fatfs`
