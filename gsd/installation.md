# Installation

## Basic tools

---
**NOTE**

If the installation instruction asks/selects whether to have the tool installation path be added to the PATH variable, please agree/select the choice. This ensures the tool can be used in any terminal in any path. After each tool installation, please [verify the installation](#tool-installation-check).

---

### Git

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. For installation, you could visit the official [Git website](https://git-scm.com/), download the appropriate version(you may use the latest one) for your operating system (Windows, macOS, Linux). Then run the installer and follow the installation instructions.

Then configure your username and email using below commands:

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Python

Install python 3.8 or above, please follow the guideline at [Python Download](https://wiki.python.org/moin/BeginnersGuide/Download). 

### Cmake

Follow the [CMake](https://cmake.org/getting-started/) doc to install CMake. The minimum version is ***3.30.0***.


## Get SDK and install Python dependencies

### Create and activate a virtual environment

To isolate your development environment, suggest use [python venv](https://docs.python.org/3/library/venv.html).
Open your shell window, create and activate a virtual environment with below command. If you are on Windows, please use the command prompt or powershell.

```bash
# Please ensure your system python version >= 3.8
python -m venv sdk-next/.venv

# For Linux/MacOS
source sdk-next/.venv/bin/activate

# For Windows
.\sdk-next\.venv\Scripts\activate

# If you are using powershell and see the issue that the activate script cannot be run. 
# You may fix the issue by opening the powershell as administrator and run below command:
powershell Set-ExecutionPolicy RemoteSigned 
# then run above activate command again.

```

Once activated your shell will be prefixed with (.venv). The virtual environment can be deactivated at any time by running `deactivate` command.

---
**NOTE**

Remember to activate the virtual environment every time you start working.

---

### Install west
```bash
# Note: you can add option '--default-timeout=1000' if you meet connection issue. Or you may set a different source using option '-i'.
# for example, in China you could try: pip install west>=1.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install west>=1.2.0
```

### Get SDK repos
Follow the guide here [repo setup](../bifrost/readme.md#steps-to-try).

### Install required packages

```bash
# Note: you can add option '--default-timeout=1000' if you meet connection issue. Or you may set a different source using option '-i'.
# for example, in China you could try: pip3 install -r mcu-sdk-3.0/scripts/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r mcu-sdk-3.0/scripts/requirements.txt
```

## Build System

### Ninja

Install the [Ninja](https://ninja-build.org/). Please use the latest ninja version 1.12.1.

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
## Tool installation check
Once installed, open a terminal or command prompt and type the associated command to verify the installation. 
- Git:
```
git --version
```
- Python:
```
python --version
```
- cmake:
```
cmake --version
```

If you see the version number, you have successfully installed the tool. Else please check whether the tool installation path be added into the PATH variable, if not, you could check the PATH variable add the tool installation path to the PATH with below commands:

- Windows:
Open command prompt or powershell, run below command to show the user PATH variable.
  ```
  reg query HKEY_CURRENT_USER\Environment /v PATH
  ```
  Assume the tool installation path is under C:\Users\xxx\AppData\Local\Programs\Git\cmd and the path is not seen in above result, you need to append the path value to the PATH variable with below command:

  ```
  reg add HKEY_CURRENT_USER\Environment /v PATH /d "%PATH%;C:\Users\xxx\AppData\Local\Programs\Git\cmd"
  ```
  Then close the command prompt or powershell and verify the tool command again.

- Linux:

  1. Open the $HOME/.bashrc file using a text editor, such as vim.
  2. Go to the end of the file.
  3. Add the line which append the tool installation path to PATH variable and export PATH at the end of the file. For example, export PATH="/Directory1:$PATH"
  4. Save and exit.
  5. Execute the script with `source .bashrc` or reboot the system to make the changes live. To verify the changes, run `echo $PATH`

- macOS:
  1. Open the $HOME/.bash_profile file using a text editor, such as nano.
  2. Go to the end of the file.
  3. Add the line which append the tool installation path to PATH variable and export PATH at the end of the file. For example, export PATH="/Directory1:$PATH"
  4. Save and exit.
  5. Execute the script with `source .bash_profile` or reboot the system to make the changes live. To verify the changes, run `echo $PATH`
