# Installation

**NOTE**

If the installation instruction asks/selects whether to have the tool installation path be added to the PATH variable, please agree/select the choice. This ensures the tool can be used in any terminal in any path. After each tool installation, please [verify the installation](#tool-installation-check).

## Basic tools

### Git

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. For installation, you could visit the official [Git website](https://git-scm.com/), download the appropriate version(you may use the latest one) for your operating system (Windows, macOS, Linux). Then run the installer and follow the installation instructions.

User `git --version` to check the version if you have a version installed.

Then configure your username and email using below commands:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Python

Install python `3.10` or above, please follow the guideline at [Python Download](https://wiki.python.org/moin/BeginnersGuide/Download).

Use `python --version` to check the version if you have a version installed.

### West

```bash
# Note: you can add option '--default-timeout=1000' if you meet connection issue. Or you may set a different source using option '-i'.
# for example, in China you could try: pip install west>=1.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install west>=1.2.0
```
## Build System

### Cmake

Follow the [CMake](https://cmake.org/getting-started/) doc to install CMake. The minimum version is ***3.30.0***.

Use `cmake --version` to check the version if you have a versio installed.

### Ninja

Install the [Ninja](https://ninja-build.org/). Please use the ninja version equal or greater than 1.12.1.

Use `ninja --version` to check the version if you have a version installed.

### Kconfig

Kconfig is installed during python library installation

### Ruby - Optional

> If you don't need GUI based IAR/MDK project, skip this step.

Install ruby for GUI project generation and standalone project generation. Follow the guide here [ruby installation](../develop/build_system/Build_And_Configuration_System_Based_On_CMake_And_Kconfig.md#ide-generation).

### Compiler

> If you don't need to evaluate a specific compiler,  you can skip that step.

#### ARMGCC

Download and install ARMGCC from [Arm GNU Toolchain Downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)

#### IAR

Download and install IAR toolchain [IAR Embedded Workbench for ARM](https://www.iar.com/products/architectures/arm/iar-embedded-workbench-for-arm/)

#### MDK

Download and install MDK toolchain [MDK](https://developer.arm.com/documentation/109350/v6/What-is-MDK-/Download-options).

#### Codewarrior

Download and install CodeWarrior toolchain from [NXP CodeWarrior](https://www.nxp.com/design/design-center/software/development-software/codewarrior-development-tools:CW_HOME).

Follow the installation instructions provided on the website. Ensure that the installation path is added to the PATH environment variable to use the toolchain from any terminal.


#### Environment Variables

| Toolchain   | Environment variable   | Example                                                      | Cmd Line Argument           |
| ----------- | ---------------------- | ------------------------------------------------------------ | :-------------------------- |
| IAR         | IAR_DIR                | C:\iar for Windows OR /opt/iarsystems/bxarm-9.40.2 for Linux | --toolchain iar             |
| MDK         | MDK_DIR                | C:\Keil_v5 for Windows OR /usr/local/ArmCompilerforEmbedded6.21 for Linux | --toolchain mdk             |
| MDK         | ARMCLANG_DIR           | C:\ArmCompilerforEmbedded6.22 for Windows OR /usr/local/ArmCompilerforEmbedded6.21 for Linux | --toolchain mdk             |
| Armgcc      | ARMGCC_DIR             | C:\armgcc                                                    | --toolchain armgcc(default) |
| CodeWarrior | CW_DIR                 | C:\Freescale\CW MCU v11.2                                    | --toolchain codewarrior     |
| Xtensa      | XCC_DIR                | C:\xtensa\XtDevTools\install\tools\RI-2023.11-win32\XtensaTools | --toolchain xtensa          |
| Zephyr      | ZEPHYR_SDK_INSTALL_DIR |                                                              | --toolchain zephyr          |

- For MDK toolchain, only armclang compiler is supported. There are 2 environment variables MDK_DIR and ARMCLANG_DIR for it. Since most Keil users will install MDK IDE instead of standalone armclang compiler, the MDK_DIR has higher priority than ARMCLANG_DIR.
- For Xtensa toolchain, please set XTENSA_CORE environment, depends on your devices, it can be `nxp_rt600_RI23_11_newlib` or `nxp_rt500_RI23_11_newlib` and so on.
- In Windows, the short path name is used in environment variables. If any toolchain is using the long path name, you can open a command window from the toolchain folder and use below command to get the short path name: `for %i in (.) do echo %~fsi`

### Debugger

>  TODO. To add the installation for the linker server

## Document Installation

> It is only needed when you want to generate the HTML version of the document in your local environment


### make

Install make for windows using choco, other OS has make installed by default. Ensure you are running command in administrator mode.

```
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

.. _tool-installation-check:

## Tool installation check
Once installed, open a terminal or command prompt and type the associated command to verify the installation.

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

# Get MCUXpresso SDK Repo

To get the MCUXpresso SDK repository, use the `west` tool to clone the manifest repository and checkout all the west projects.

  ```bash
  - Initialize west with the manifest repository
  - TODO -  To be replaced by the final customer available manifest repository address
  west init -m https://github.com/nxp-mcuxpresso/mcuxsdk-manifest.git

  - Update the west projects
  west update
  ```

# Install Python Dependency
To create a Python virtual environment in the west workspace core repo directory mcuxsdk, follow these steps:

1. Navigate to the core directory:
  ```bash
  cd mcuxsdk
  ```

2. [Optional] Create and activate the virtual environment:
> If you don't want to use the python virtual environment, skip this step.

  ```bash
  python -m venv .venv

  # For Linux/MacOS
  source .venv/bin/activate

  # For Windows
  .\.venv\Scripts\activate
  # If you are using powershell and see the issue that the activate script cannot be run.
  # You may fix the issue by opening the powershell as administrator and run below command:
  powershell Set-ExecutionPolicy RemoteSigned
  # then run above activate command again.

  ```
Once activated, your shell will be prefixed with (.venv). The virtual environment can be deactivated at any time by running `deactivate` command.

3. Install the required Python packages:

  ```bash
  # Note: you can add option '--default-timeout=1000' if you meet connection issue. Or you may set a different source using option '-i'.
  # for example, in China you could try: pip3 install -r mcu-sdk-3.0/scripts/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip install -r scripts/requirements.txt
  ```

> Remember to activate the virtual environment every time you start working in this directory.

## Document Python dependencies

There are several needed python packages for documentation generation, such as Sphinx tool, which we used to do the generation process. Run below command to install those python dependencies.

  ```bash
  cd core/docs
  pip install -r requirements.txt
  ```

