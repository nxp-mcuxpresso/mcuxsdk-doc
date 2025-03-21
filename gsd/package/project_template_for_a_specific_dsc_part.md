# Project template for a specific DSC part

For device with specific part number, the easiest way to set up customer own project based on MCUXpresso DSC SDK peripheral driver, is the project_template. MCUXpresso Config Tool is used to generate the project_template.

The project_template provides basic MCUXpresso DSC SDK software framework, including startup, linker file, device header file, debug setting, peripheral driver, FreeMASTER, and so on.

Steps to generate the project_template for specific derivative part number by MCUXpresso Config Tool
  1. Download the specific device SDK package and unzip it.
     ```note: The project template requires FreeMASTER, middleware FreeMASTER selection is a must when downloading DSC SDK from nxp website```
  2. Use MCUXpresso Config Tool to create a project_template project as below(take MC56F84442 as example).
     ![](/gsd/package/images/cfg_tool_dsc_npw.png "MCUXpresso Config Tool support")
  3. Import the generated template_project into CodeWarrior IDE and start the development.

**NOTE**
  - The default created project template by Config Tool is `project_template_{part_number}`. User could modify the default name in **Project name** textbox.
  - All peripheral drivers files are included in the generated project_template project. They are same as the peripheral drivers within SDK package.
    If some drivers are not used or required, users may delete them in CodeWarrior, or delete them directly under folder *${project_path}/drivers*.