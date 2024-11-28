# MCUXpresso SDK: mcux-sdk
The NXP MCUXpresso software and tools offer comprehensive development solutions designed to optimize,
ease, and help accelerate embedded system development of applications based on general purpose,
crossover, and Bluetooth-enabled MCUs from NXP. The MCUXpresso SDK includes a flexible set of peripheral
drivers designed to speed up and simplify development of embedded applications. Along with the peripheral
drivers, the MCUXpresso SDK provides an extensive and rich set of example applications covering everything
from basic peripheral use case examples to full demo applications. The MCUXpresso SDK contains optional
RTOS integrations such as FreeRTOS, and various other middleware to support rapid
development.

The complete MCUXpresso SDK distribution on GitHub is composed of separate project deliveries. The idea we split the whole SDK distribution to separate projects is inspired by [Zephyr](https://github.com/zephyrproject-rtos/zephyr), and the projects are planned as below:
* Fundamental project for device/board enablement with shared drivers and components.
* RTOS projects
* Middleware projects
* Examples project built on above deliveries

In this way we want to benefit user from below aspects:
1. Provide ability for user to select needed projects to build his application.
2. Avoid huge size in a single repository.

We leveraged [Zephyr west tool](https://docs.zephyrproject.org/latest/guides/west/index.html) to do multi-repository management. By providing differnt manifest files, we create flexibility for user to:
1. Get projects for specific device by using device portifolio specific manifest file(such as RT/Kinetis/LPC/MCX). This way could be quicker and repo size consumption is affordable.
2. Retrieve full MCUXpresso SDK projects by using default west.yml. This will clone and check out all the MCUXpresso SDK projects, thus the size consumption could be very huge and the speed maybe slow.
The west tool also allows user to self create ```west.yml``` for customizing needed projects for their use cases.

## Getting Started
See {ref}`Getting Start Guide <gsd_index>` to start explore the project.
