# Host setup

An MCUXpresso SDK build requires that some packages are installed on the Host. Depending on the used Host operating system, the following tools should be installed.

**Linux**:

-   Cmake

    ```
    $ sudo apt-get install cmake
    $ # Check the version >= 3.0.x
    $ cmake --version
    ```

**Windows:**

-   MinGW

    The Minimalist GNU for Windows OS \(MinGW\) development tools provide a set of tools that are not dependent on third party C-Runtime DLLs \(such as Cygwin\). The build environment used by the SDK does not utilize the MinGW build tools, but does leverage the base install of both MinGW and MSYS. MSYS provides a basic shell with a Unix-like interface and tools.

    1.  Download the latest MinGW mingw-get-setup installer from [sourceforge.net/projects/mingw/files/Installer/](http://sourceforge.net/projects/mingw/files/Installer/).
    2.  Run the installer. The recommended installation path is `C:\MinGW`, however, you may install to any location.

        **Note:** The installation path cannot contain any spaces.

    3.  Ensure that **mingw32-base** and **msys-base** are selected under **Basic Setup**.
    4.  Click **Apply Changes** in the **Installation** menu and follow the remaining instructions to complete the installation.
    5.  Add the appropriate item to the Windows operating system path environment variable. The path is: `<mingw_install_dir>in`.

-   Cmake

    1.  Download CMake 3.0.x from [cmake.org](https://www.cmake.org/).
    2.  Install CMake, ensuring that the option **Add CMake to system PATH** is selected when installing.
    3.  Follow the remaining instructions of the installer.
    4.  You may need to reboot your system for the PATH changes to take effect.
