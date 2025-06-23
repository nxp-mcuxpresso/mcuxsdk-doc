# MCUXpresso SDK
The NXP MCUXpresso software and tools offer comprehensive development solutions designed to help accelerate embedded system development of applications based on MCUs from NXP. The MCUXpresso SDK includes a flexible set of peripheral drivers designed to speed up and simplify development of embedded applications. Along with the peripheral drivers, the MCUXpresso SDK provides an extensive set of example applications covering everything
from basic peripheral use cases to full technology demonstrations. The MCUXpresso SDK contains optional RTOS integrations such as FreeRTOS, and various other middleware to support rapid development.

The MCUXpresso SDK on GitHub is composed of multiple groups of software distributed among different repositories. The MCUXpresso SDK uses the popular west manifest to specify what software is included. This method of delivering software was inspired by [Zephyr](https://github.com/zephyrproject-rtos/zephyr).  

NXP has organized the SDK software into the groups below:
* Device and Board enablement with shared drivers and components
* RTOS software
* Middleware software
* Example projects. Assist in evaluation of the above software

The MCUXpresso SDK west manifest provides the following benefits:
1. Users can modify the included software to align with their application.
2. Software is in smaller repositories to avoid a single large download requirement. The download size is reduced by selecting a custom manifest.

The [Zephyr west tool](https://docs.zephyrproject.org/latest/guides/west/index.html) is used to manage this multi-repo SDK. By providing different manifest files, the user has the flexibility to:
1. Get software for a specific device by listing a product family manifest file (```RT.yml```/```MCX.yml```). The manifest includes fewer folders/files, and provides a faster download experience.  - Will provide in the 25.09.00 release update
2. Retrieve the full MCUXpresso SDK by using the default *west.yml*. This installs all the available MCUXpresso SDK software repositories, and therefore results in the longest download time.
3. Users can create a custom version of the  ```west.yml``` optimized for the needs of their own projects.

    
## Cloning the Repo 

- To clone the repo from the CLI run the commands:
    ```bash
    west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git mcuxpresso-sdk
    cd mcuxpresso-sdk
    west update
    ```
    

## Additional steps
  - Add ARMGCC_DIR to your environment variables
      - Open your system settings
      - Add ARMGCC_DIR and its path    
