# Installation

## Python

To isolate your development environment, suggest use [python venv](https://docs.python.org/3/library/venv.html).
In sdk-next workspace root directory, create and activate a virtual environment:

```bash
# Please ensure your system python version >= 3.8
python -m venv .venv

# For Linux/MacOS
source .venv/bin/activate

# For Windows
.\.venv\Scripts\activate
```

Then install required packages

```bash
# Note: you can add option '--default-timeout=1000' if you meet connection issue.
pip install -r mcu-sdk-3.0/scripts/requirements.txt
```

## West

West is the tool used in SDK to do repository management. It was installed when you executed the python installation.

## Build System

### Cmake

Follow the [CMake](https://cmake.org/getting-started/) doc to install CMake. The minimum version is ***3.22.0***.

### Ninja

Install the [Ninja](https://ninja-build.org/). The minimum ninja version is ***1.11.0***.

### Kconfig

Kconfig is installed during python library installation

### Toolchains

You need to set environment variables to specify the toolchain installation so that build system can find it.

Here are the toolchain environment variable table

| Toolchain | Environment variable   | Cmd Line Argument           |
| --------- | ---------------------- | :-------------------------- |
| IAR       | IAR_DIR                | --toolchain iar             |
| MDK       | MDK_DIR                | --toolchain mdk             |
| Armgcc    | ARMGCC_DIR             | --toolchain armgcc(default) |
| Zephyr    | ZEPHYR_SDK_INSTALL_DIR | --toolchain zephyr          |

#### armgcc


#### iar


#### mdk


## Document

It is only needed when you want to generate the HTML version of the document in your local environment

### Sphinx

Sphinx is installed during python lib installation

### make

Install make for windows using choco, other OS has make installed by default. Ensure you are running command in administrator mode.
```cmd
choco install make
```

### doxygen









