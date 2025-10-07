# Development Systems and Metrics

The MCUXpresso SDK provides the following summary of Coverity Static Analysis to help customers assess the quality and security posture of our software. The table includes results for
- Cyclomatic complexity ([CCM](https://en.wikipedia.org/wiki/Cyclomatic_complexity))
- Common Weakness Enumerations ([CWE](https://en.wikipedia.org/wiki/Common_Weakness_Enumeration))
- High Impact Findings ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))
- Memory Leaks for Embedded C/C++ Systems ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))

This enables customers to make informed decisions and meet their own compliance requirements.
The tabulated results cover findings that are classified as issues.

|Development boards|HIGH IMPACT|Memory Leaks|CWE|CCM > 20|No. Examples|
|:--               |:--    |:--    |:--    |:--    |:--    |
|FRDM-MCXL255|0|0|0|3|11|
|FRDM-MCXW72|0|0|0|1|1|
|KW47-EVK|4|0|4|190|223|
|KW47-LOC|-|-|-|-|0|
|MCX-W72-EVK|0|0|0|69|14|
|MCXW72-LOC|-|-|-|-|0|

