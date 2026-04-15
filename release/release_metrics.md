# Development Systems and Metrics

The MCUXpresso SDK provides the following summary of Coverity Static Analysis to help customers assess the quality and security posture of our software. The table includes results for
- Cyclomatic complexity ([CCM](https://en.wikipedia.org/wiki/Cyclomatic_complexity))
- Common Weakness Enumerations ([CWE](https://en.wikipedia.org/wiki/Common_Weakness_Enumeration))
- High Impact Findings ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))
- Memory Leaks for Embedded C/C++ Systems ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))

This enables customers to make informed decisions and meet their own compliance requirements.
The tabulated results cover findings that are classified as issues.

*The 26.03.00 MCUXpresso SDK release excludes the Wireless middleware from the published summary. The 26.06.00 SDK release will reintroduce the wireless results.

|Development boards|HIGH IMPACT|Memory Leaks|CWE|CCM > 20|No. Examples|
|:--               |:--    |:--    |:--    |:--    |:--    |
|FRDM-MCXC162|0|0|0|4|1|
|FRDM-MCXL255|2|0|2|12|48|

