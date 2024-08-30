Before you run this example, please make sure that you have already successfully exported the MCUXpresso SDK repo to the your computer system CMake user package registry with "cmake -P <sdk repo root>/share/mcuxsdk-package/cmake/mcuxsdk_export.cmake".

There are 2 ways to run the example:
1. With cmake cmd "cmake -B ./build -G Ninja -Dboard=frdmk22f -DCONF_FILE=<repo root>/docs/develop/build_system/McuxSDK_CMake_package_freestanding_example/prj.conf -DCMAKE_BUILD_TYPE=debug -DCONFIG_TOOLCHAIN=armgcc", then cd into "build" folder and run "ninja".
2. With west cmd "west build -b frdmk22f <repo root>/docs/develop/build_system/McuxSDK_CMake_package_freestanding_example -DCONF_FILE=<repo root>/docs/develop/build_system/McuxSDK_CMake_package_freestanding_example/prj.conf", this cmd will automatically configure and build.
