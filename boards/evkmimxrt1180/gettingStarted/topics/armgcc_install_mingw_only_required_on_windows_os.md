# Install MinGW \(only required on Windows OS\) {#GUID-C8C4206D-E829-4590-A88B-73966FA3051B}

The Minimalist GNU for Windows \(MinGW\) development tools provide a set of tools that are not dependent on third-party C-Runtime DLLs \(such as Cygwin\). The build environment used by the MCUXpresso SDK does not use the MinGW build tools, but does leverage the base install of both MinGW and MSYS. MSYS provides a basic shell with a Unix-like interface and tools.

1.  Download the latest MinGW mingw-get-setup installer from [SOURCEFORGE](http://sourceforge.net/projects/mingw/files/Installer/).
2.  Run the installer. The recommended installation path is *C:\\MinGW*. However, you may install to any location.

    **Note:** The installation path cannot contain any spaces.

3.  Ensure that the **mingw32-base** and **msys-base** are selected under **Basic Setup**.

    ![](../images/armgcc_set_up_mingw_msys.png "Set up MinGW and MSYS")

4.  In the **Installation** menu, click **Apply Changes** and follow the remaining instructions to complete the installation.

    ![](../images/armgcc_complete_mingw_and_msys.png "Complete MinGW and MSYS installation")

5.  Add the appropriate item to the Windows operating system path environment variable. It can be found under **Control Panel**-&gt;**System and Security**-&gt;**System**-&gt;**Advanced System Settings**in the **Environment Variables...**section. The path is:

    *&lt;mingw\_install\_dir&gt;\\bin*

    Assuming the default installation path is *C:\\MinGW*, an example is as shown in [Figure 3](#FIG_ADDPATH). If the path is not set correctly, the toolchain will not work.

    **Note:** If you have *C:\\MinGW\\msys\\x.x\\bin*in your PATH variable \(as required by Kinetis SDK 1.0.0\), remove it to ensure that the new GCC build system works correctly.

    ![](../images/armgcc_add_path.png "Add Path to systems environment")


**Parent topic:**[Set up toolchain](../topics/armgcc_set_up_toolchain.md)
