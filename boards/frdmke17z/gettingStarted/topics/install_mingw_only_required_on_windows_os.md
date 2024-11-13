# Install MinGW \(only required on Windows OS\) {#GUID-E392D63C-7DEE-489F-899A-262E66657B56}

The Minimalist GNU for Windows \(MinGW\) development tools provide a set of tools that are not dependent on third-party C-Runtime DLLs \(such as Cygwin\). The build environment used by the MCUXpresso SDK does not use the MinGW build tools, but does leverage the base install of both MinGW and MSYS. MSYS provides a basic shell with a Unix-like interface and tools.

1.  Download the latest MinGW mingw-get-setup installer from [MinGW](http://sourceforge.net/projects/mingw/files/Installer/).
2.  Run the installer. The recommended installation path is `C:\MinGW`, however, you may install to any location.

    **Note:** The installation path cannot contain any spaces.

3.  Ensure that the **mingw32-base** and **msys-base** are selected under **Basic Setup**.

    |![](../images/arm_gcc_setup_mingw_and_msys.png "Set up MinGW and MSYS")

|

4.  In the **Installation** menu, click **Apply Changes** and follow the remaining instructions to complete the installation.

    |![](../images/arm_gcc_complete_mingw_and_msys_installation.png "Complete MinGW and MSYS installation")

|

5.  Add the appropriate item to the Windows operating system path environment variable. It can be found under **Control Panel**-\>**System and Security**-\>**System**-\>**Advanced System Settings** in the **Environment Variables...** section. The path is:

    ```
    <mingw_install_dir>\bin
    ```

    Assuming the default installation path, `C:\MinGW`, an example is as shown in [Figure 3](install_mingw_only_required_on_windows_os.md#FIG_ADDPATH). If the path is not set correctly, the toolchain will not work.

    **Note:** If you have `C:\MinGW\msys\x.x\bin` in your PATH variable \(as required by Kinetis SDK 1.0.0\), remove it to ensure that the new GCC build system works correctly.

    |![](../images/arm_gcc_add_path_systems_environment.png "Add Path to systems environment")

|


**Parent topic:**[Set up toolchain](../topics/set_up_toolchain.md)

