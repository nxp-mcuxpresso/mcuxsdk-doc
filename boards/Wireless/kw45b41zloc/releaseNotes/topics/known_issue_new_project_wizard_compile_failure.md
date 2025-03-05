# New project wizard compile failure {#known_issue_new_project_wizard_compile_failure}

The following components request the user to manually select other components that they depend upon in order to compile. These components depend on several other components and the New Project Wizard \(NPW\) is not able to decide which one is needed by the user.

**Note:** `xxx` means core variants, such as, `cm0plus`, `cm33`, `cm4`, `cm33_nodsp`.

Also for low-level adapter components, currently the different types of the same adapter cannot be selected at the same time. For example, if there are two types of timer adapters, `gpt_adapter` and `pit_adapter`, only one can be selected as timer adapter in one project at a time. Duplicate implementation of the function results in an error.

**Parent topic:**[Known issues](../topics/known_issues.md)

