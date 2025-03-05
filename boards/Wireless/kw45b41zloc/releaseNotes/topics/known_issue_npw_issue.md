# LIN New Project Wizard \(NPW\) issue {#known_issue_npw_issue}

-   The lin \(LIN Driver\) and lin\_stack \(LIN Stack Driver\) drivers components should not be enabled at the same time while creating the new projects in MCUXpresso. Otherwise there will be the compiling issue.
-   The lin\_stack \(LIN Stack Driver\) is not actually a driver. It is an adapt layer for LIN Stack middleware to adapt to the low level lpuart driver and cannot be used in NPW alone. So, select the LIN Stack middleware and then the lin\_stack is selected automatically since it is required by LIN Stack middleware. Besides, customer need to add the lin\_cfg.c/h in application layer for user definition of frame data and add **FSL\_SDK\_LIN\_STACK\_ENABLE=1** in MCUXpresso preprocessor, otherwise the compiling of LIN Stack will report error.

**Parent topic:**[Known issues](../topics/known_issues.md)

