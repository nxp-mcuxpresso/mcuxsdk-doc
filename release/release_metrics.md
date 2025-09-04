# Development Systems and Metrics

- **CCM** - Cyclomatic complexity. Measured per function. [Definition](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- **CWE** - Common Weakness Enumeration. [Definition](https://en.wikipedia.org/wiki/Common_Weakness_Enumeration)
- **HIGH IMPACT** - High Impact findings classified by Coverity Analysis. [Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html)
- **Memory Leaks** - Set of checkers specified by Coverity SA [Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html)
  - RESOURCE_LEAK
  - CTOR_DTOR_LEAK
  - COM.ADDROF_LEAK
  - AUDIT.SPECULATIVE_EXECUTION_DATA_LEAK

|Development boards|HIGH IMPACT|Memory Leaks|CWE|CCM > 20|No. Examples|
|:--               |:--    |:--    |:--    |:--    |:--    |
|EVK-MIMX8MP|0|0|0|30|44|
|EVK-MIMX8ULP|0|0|0|50|16|
|EVK-MIMXRT1064|6|0|6|565|78|
|EVK-MIMXRT595|4|0|4|251|43|
|EVK-MIMXRT685|0|0|0|9|2|
|EVK9-MIMX8ULP|-|-|-|-|0|
|FRDM-IMXRT1186|2|0|2|117|57|
|FRDM-KE15Z|0|0|0|34|43|
|FRDM-KE16Z|0|0|0|7|5|
|FRDM-KE17Z|0|0|0|12|11|
|FRDM-KE17Z512|0|0|0|3|9|
|FRDM-MCXA153|-|-|-|-|0|
|FRDM-MCXA156|0|0|0|2|2|
|FRDM-MCXA266|1|0|1|34|5|
|FRDM-MCXA344|1|0|1|16|41|
|FRDM-MCXA346|0|0|0|1|1|
|FRDM-MCXA366|-|-|-|-|0|
|FRDM-MCXC041|0|0|0|4|18|
|FRDM-MCXC242|0|0|0|15|35|
|FRDM-MCXC444|0|0|0|8|6|
|FRDM-MCXE247|0|0|0|4|4|
|FRDM-MCXE31B|61|0|61|138|53|
|FRDM-MCXN236|0|0|0|6|1|
|FRDM-MCXN947|12|10|12|295|20|
|FRDM-MCXW23|2|0|2|28|76|
|FRDM-MCXW71|0|0|0|7|2|
|FRDM-MCXW72|0|0|0|1|1|
|FRDM-RW612|43|10|43|777|38|
|IMX943-EVK|20|0|20|137|61|
|IMX95LP4XEVK-15|1|0|1|42|8|
|IMX95LPD5EVK-19|0|0|0|6|2|
|IMX95VERDINEVK|-|-|-|-|0|
|KW45B41Z-EVK|0|0|0|69|4|
|KW45B41Z-LOC|-|-|-|-|0|
|KW47-EVK|10|0|10|187|214|
|KW47-LOC|-|-|-|-|0|
|LPCXpresso55S06|1|0|1|11|13|
|LPCXpresso55S16|0|0|0|21|1|
|LPCXpresso55S28|-|-|-|-|0|
|LPCXpresso55S36|0|0|0|17|18|
|LPCXpresso55S69|0|0|0|42|10|
|LPCXpresso860MAX|0|0|0|6|30|
|MC56F80000-EVK|-|-|-|-|0|
|MC56F81000-EVK|-|-|-|-|0|
|MC56F83000-EVK|-|-|-|-|0|
|MCIMX93-EVK|0|0|0|115|7|
|MCIMX93-QSB|-|-|-|-|0|
|MCIMX93AUTO-EVK|-|-|-|-|0|
|MCX-N5XX-EVK|4|0|4|383|81|
|MCX-N9XX-EVK|-|-|-|-|0|
|MCX-W71-EVK|0|0|0|63|11|
|MCX-W72-EVK|0|0|0|69|14|
|MCXW23-EVK|1|0|1|5|1|
|MCXW72-LOC|-|-|-|-|0|
|MIMXRT1060-EVKB|1|0|1|130|8|
|MIMXRT1060-EVKC|2|0|2|152|5|
|MIMXRT1160-EVK|1|0|1|31|41|
|MIMXRT1170-EVKB|3|0|3|287|16|
|MIMXRT1180-EVK|0|0|0|21|12|
|MIMXRT685-AUD-EVK|0|0|0|24|10|
|MIMXRT700-EVK|12|0|21|821|270|
|RD-RW612-BGA|0|0|0|11|1|

All findings are filtered based on current triage status. Action:Ignore and Classification:False Positive findings are excluded from metrics.<br/>
CWE findings are measured for High Impact findings only.
