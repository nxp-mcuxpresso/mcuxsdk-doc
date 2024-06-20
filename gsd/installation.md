# Installation

## Python

Install python 3.8 or above, please follow the guideline at [Python Download](https://wiki.python.org/moin/BeginnersGuide/Download).

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

West is the tool used in SDK to do repository management. It was installed when you executed the python installation. The minimum west version is ***1.2.0***.

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

### Python dependencies

There are several needed python packages for documentation generation, such as Sphinx tool, which we used to do the generation process. Run below command to install those python dependencies.
```
cd mcu-sdk-3.0/docs
pip install -r requirements.txt
```

### make

Install make for windows using choco, other OS has make installed by default. Ensure you are running command in administrator mode.
```cmd
choco install make
```
If you do not have choco installed, you can install it from [chocolatey](https://chocolatey.org/install)

### doxygen

The doxygen installation is needed if you want to try documentation generation. The versions for the doxygen tools are as below:
- Doxygen version 1.8.13
- Graphviz 2.43
- Latexmk version 4.56

For installation, you can refer to the guideline as below, which is referenced from the [Zephyr documentation generation guideline](https://docs.zephyrproject.org/latest/contribute/documentation/generation.html#installing-the-documentation-processors)
- Linux
  - On Ubuntu Linux:
	```
	sudo apt-get install --no-install-recommends doxygen graphviz librsvg2-bin \
	texlive-latex-base texlive-latex-extra latexmk texlive-fonts-recommended imagemagick
    ```
	
  - On Fedora Linux:
	```
	sudo dnf install doxygen graphviz texlive-latex latexmk \
	texlive-collection-fontsrecommended librsvg2-tools ImageMagick
    ```	

  - On Clear Linux:
	```
	sudo swupd bundle-add texlive graphviz ImageMagick
	```	
	
  - On Arch Linux:
	```
	sudo pacman -S graphviz doxygen librsvg texlive-core texlive-bin \
	texlive-latexextra texlive-fontsextra imagemagick
	```

- macOS
  Use ``brew`` and ``tlmgr`` to install the tools:
  ```
  brew install doxygen graphviz mactex librsvg imagemagick
  ```
  ```
  tlmgr install latexmk
  ```
  ```
  tlmgr install collection-fontsrecommended
  ```

- Windows
  Open a ``cmd.exe`` window as **Administrator** and run the following command:
  ```
  choco install doxygen.install graphviz strawberryperl miktex rsvg-convert imagemagick
  ```
