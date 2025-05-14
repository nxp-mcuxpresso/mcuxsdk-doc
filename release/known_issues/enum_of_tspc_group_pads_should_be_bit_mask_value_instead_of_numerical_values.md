# Enum of tspc group pads should be bit mask value instead of numerical values

TSPC cases can't run successfully. The enum of tspc group pads recorded in MCXE31B_COMMON.h is wrongly written with numerical value.

**Solution:** The enum of tspc group pads should be bit mask value

**Examples:** tspc

**Affected toolchains:** mcux, iar, armgcc

**Affected platforms:** frdmmcxe31b