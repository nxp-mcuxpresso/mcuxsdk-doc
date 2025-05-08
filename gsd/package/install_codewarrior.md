# Install CodeWarrior

Take below codewarrior specific combination as example
- CodeWarrior Development Studio v11.2 + CodeWarrior for DSC v11.2 SP1 \(Service Pack 1\)


Steps to install CodeWarrior
* Download the following packages from [CodeWarrior for 56800 Digital Signal Controller v11.2](https://www.nxp.com/design/design-center/software/development-software/codewarrior-development-tools/codewarrior-legacy/codewarrior-for-56800-digital-signal-controller-v11-2:CW-DSC), and ensure to keep them in the same folder.
  - CodeWarrior for DSC v11.2: `CW_MCU_v11.2_b221206.exe`.
  - DSC support package: `com.freescale.mcu11_2.dsc.updatesite.zip`.
  - DSC device ServicePack1: `com.freescale.mcu11_2.DSC_devices.win.sp.v1.0.26.zip`.
* Install CodeWarrior for DSC v11.2.
* Install ServicePack1 within CodeWarrior from the menu.
  Click the **Help** menu -> select **Install new software -> Add -> Archive** -> select the downloaded SP1 -> open -> check **MCU v11.2 DSC Service Packs** -> click **Next**.
  ![](/gsd/package/images/install_codewarrior.png "Update settings")

**NOTE** 
- CodeWarrior for DSC only support Windows.
- Check the corresponding board release note for specific requirement of codewarrior and service pack version.
