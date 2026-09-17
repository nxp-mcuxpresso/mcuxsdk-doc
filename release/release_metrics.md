# Development Systems and Metrics

The MCUXpresso SDK provides the following summary of Coverity Static Analysis to help customers assess the quality and security posture of our software. The table includes results for
- Cyclomatic complexity ([CCM](https://en.wikipedia.org/wiki/Cyclomatic_complexity))
- Common Weakness Enumerations ([CWE](https://en.wikipedia.org/wiki/Common_Weakness_Enumeration))
- High Impact Findings ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))
- Memory Leaks for Embedded C/C++ Systems ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))

This enables customers to make informed decisions and meet their own compliance requirements.
The tabulated results cover findings that are classified as issues.

|Component name|HIGH IMPACT|Memory Leaks|CWE|CCM > 20|
|:--               |:--    |:--    |:--    |:--    |
|[Arch_ARM](# "arch\/arm\/.*")|0|0|0|0|
|[Arch_xtensa](# "arch\/xtensa\/.*")|0|0|0|0|
|[version](# "^.*\/mcuxsdk_version\.h$")|0|0|0|0|
|[DSC_build_targets](# "arch\/dsp56800\/.*")|0|0|0|0|
|[devices_arch/arm](# "devices\/arm\/.*")|0|0|0|0|
|[devices_arch/dsp56800](# "devices\/dsp56800\/.*")|0|0|0|0|
|[devices_arch/xtensa](# "devices\/xtensa\/.*")|0|0|0|0|
|[devices_arch/ezhv](# "devices\/ezhv\/.*")|0|0|0|0|
|[devices_arch](# "devices\/[^\/]*$")|0|0|0|0|
|[devices_DSC/MC56F80xxx](# "devices\/DSC\/MC56F80xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F81xxx](# "devices\/DSC\/MC56F81xxx\/.*")|0|0|1|0|
|[devices_DSC/MC56F82xxx](# "devices\/DSC\/MC56F82xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F83xxx](# "devices\/DSC\/MC56F83xxx\/.*")|0|0|1|0|
|[devices_DSC/MC56F84xxx](# "devices\/DSC\/MC56F84xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F85xxx](# "devices\/DSC\/MC56F85xxx\/.*")|0|0|0|0|
|[devices_DSC](# "(devices&#124;devices_int)\/DSC\/.*")|0|0|0|0|
|[devices_Kinetis/K](# "devices\/Kinetis\/K\/.*")|0|0|0|0|
|[devices_Kinetis/K32L](# "devices\/Kinetis\/K32L\/.*")|0|0|0|0|
|[devices_Kinetis/KE](# "devices\/Kinetis\/KE\/.*")|0|0|0|0|
|[devices_Kinetis/KM](# "devices\/Kinetis\/KM\/.*")|0|0|0|0|
|[devices_Kinetis](# "devices\/Kinetis\/.*")|0|0|0|0|
|[devices_LPC/LPC51U68](# "devices\/LPC\/LPC51U68\/.*")|0|0|0|0|
|[devices_LPC/LPC800](# "devices\/LPC\/LPC800\/.*")|0|0|0|0|
|[devices_LPC/LPC54000](# "devices\/LPC\/LPC54000\/.*")|0|0|0|1|
|[devices_LPC/LPC5500](# "devices\/LPC\/LPC5500\/.*")|0|0|0|7|
|[devices_LPC](# "devices\/LPC\/.*")|0|0|0|0|
|[devices_MCX/MCXA](# "devices\/MCX\/MCXA\/.*")|0|0|0|0|
|[devices_MCX/MCXC444](# "devices\/MCX\/MCXC\/MCXC[124]4[34]\/.*; devices\/MCX\/MCXC\/periph2\/.*")|0|0|0|0|
|[devices_MCX/MCXC242](# "devices\/MCX\/MCXC\/MCXC[12]4[12]\/.*; devices\/MCX\/MCXC\/periph1\/.*")|0|0|0|0|
|[devices_MCX/MCXC041](# "devices\/MCX\/MCXC\/MCXC041\/.*; devices\/MCX\/MCXC\/periph\/.*")|0|0|0|0|
|[devices_MCX/MCXE24](# "devices\/MCX\/MCXE\/MCXE24[0-9]\/.*; devices\/MCX\/MCXE\/periph[023]\/.*")|0|0|0|0|
|[devices_MCX/MCXE31](# "devices\/MCX\/MCXE\/MCXE31[0-9A-F]\/.*; devices\/MCX\/MCXE\/periph[145]\/.*")|0|0|0|0|
|[devices_MCX/MCXL](# "devices.*\/MCX\/MCXL\/.*")|0|0|0|1|
|[devices_MCX/MCXN](# "devices\/MCX\/MCXN\/.*")|0|0|0|1|
|[devices_MCX/MCXW](# "devices\/MCX\/MCXW\/(?!.*\/fsl_power\.[ch]$&#124;.*\/drivers\/fsl_system\.[ch]$&#124;.*\/drivers\/timer_manager_mcxw23\/.*$&#124;.*\/drivers\/power_manager_mcxw23\/.*$).*$")|0|0|0|2|
|[devices_MCX/MCXW23_Timer_Manager](# "devices\/MCX\/MCXW\/MCXW236\/drivers\/timer_manager_mcxw23\/.*")|0|0|0|0|
|[devices_MCX/MCXW23_Power_Manager](# "devices\/MCX\/MCXW\/MCXW236\/drivers\/power_manager_mcxw23\/.*; devices\/MCX\/MCXW\/MCXW236\/drivers\/fsl_power.[ch]; devices\/MCX\/MCXW\/MCXW236\/drivers\/fsl_system.[ch]")|0|0|0|0|
|[devices_MCX](# "(devices&#124;devices_int)\/MCX\/.*")|0|0|0|0|
|[devices_RT/RT1010](# "devices\/RT\/RT1010\/.*")|0|0|0|0|
|[devices_RT/RT1015](# "devices\/RT\/RT1015\/.*")|0|0|0|0|
|[devices_RT/RT1020](# "devices\/RT\/RT1020\/.*")|0|0|0|0|
|[devices_RT/RT1040](# "devices\/RT\/RT1040\/.*")|0|0|0|0|
|[devices_RT/RT1050](# "devices\/RT\/RT1050\/.*")|0|0|0|0|
|[devices_RT/RT1060](# "devices\/RT\/RT1060\/.*")|0|0|0|0|
|[devices_RT/RT1064](# "devices\/RT\/RT1064\/.*")|0|0|0|0|
|[devices_RT/RT1160](# "devices\/RT\/RT1160\/.*")|0|0|0|0|
|[devices_RT/RT1170](# "devices\/RT\/RT1170\/.*")|0|0|0|1|
|[devices_RT/RT1180](# "devices\/RT\/RT1180\/.*")|0|0|0|1|
|[devices_RT/RT500](# "devices\/RT\/RT500\/.*")|0|0|0|0|
|[devices_RT/RT600](# "devices\/RT\/RT600\/.*")|0|0|0|0|
|[devices_RT/RT700](# "devices\/RT\/RT700\/.*")|0|0|0|4|
|[devices_RT](# "(devices&#124;devices_int)\/RT\/.*")|0|0|0|0|
|[devices_Wireless/KW](# "devices\/Wireless\/KW\/.*")|0|0|4|0|
|[devices_Wireless/RW](# "devices\/Wireless\/RW\/(?!.*\/fsl_iped\.[ch]$&#124;.*\/drivers\/romapi\/.*$).*$")|0|0|1|0|
|[devices_Wireless/RW_iped](# "devices\/Wireless\/RW\/.*\/fsl_iped\.[ch]$")|0|0|0|0|
|[devices_Wireless/RW_romapi](# "devices\/Wireless\/RW\/.*\/drivers\/romapi\/.*")|0|0|0|0|
|[devices_Wireless](# "(devices&#124;devices_int)\/Wireless\/.*")|0|0|0|0|
|[devices_iMX/iMX7ULP](# "devices\/i.MX\/i.MX7ULP\/.*")|0|0|0|0|
|[devices_iMX/iMX8M](# "devices\/i.MX\/i.MX8M\/.*")|0|0|0|0|
|[devices_iMX/iMX8MM](# "devices\/i.MX\/i.MX8MM\/.*")|0|0|0|0|
|[devices_iMX/iMX8MN](# "devices\/i.MX\/i.MX8MN\/.*")|0|0|0|0|
|[devices_iMX/iMX8MP](# "devices\/i.MX\/i.MX8MP\/.*")|0|0|0|0|
|[devices_iMX/iMX8ULP](# "devices\/i.MX\/i.MX8ULP\/.*")|0|0|0|1|
|[devices_iMX/iMX93](# "devices\/i.MX\/i.MX93\/.*")|0|0|0|0|
|[devices_iMX/iMX95](# "devices\/i.MX\/i.MX95\/.*")|0|0|0|0|
|[devices_iMX/iMX943](# "devices\/i.MX\/i.MX943\/.*")|0|0|0|0|
|[devices_iMX](# "(devices&#124;devices_int)\/i.MX\/.*")|0|0|0|0|
|[drivers/sbom](# "SBOM\.spdx\.json; SBOM.spdx.json")|0|0|0|0|
|[drivers/biss](# "drivers\/biss\/.*")|0|0|0|0|
|[drivers/endat2](# "drivers\/endat2p2\/.*")|0|0|0|0|
|[drivers/endat3](# "drivers\/endat3\/.*")|0|0|4|2|
|[drivers/hiperface](# "drivers\/hiperface\/.*")|0|0|0|0|
|[drivers/acmp](# "drivers\/acmp\/.*")|0|0|0|0|
|[drivers/acmp_1](# "drivers\/acmp_1\/.*")|0|0|0|0|
|[drivers/adc12](# "drivers\/adc12\/.*")|0|0|0|0|
|[drivers/adc16](# "drivers\/adc16\/.*")|0|0|0|0|
|[drivers/adc_12b1msps_sar](# "drivers\/adc_12b1msps_sar\/.*")|0|0|0|0|
|[drivers/adc_5v12b_ll18_015](# "drivers\/adc_5v12b_ll18_015\/.*")|0|0|0|0|
|[drivers/adc_etc](# "drivers\/adc_etc\/.*")|0|0|0|0|
|[drivers/aes](# "drivers\/aes\/.*")|0|0|0|0|
|[drivers/afe](# "drivers\/afe\/.*")|0|0|0|0|
|[drivers/aipstz](# "drivers\/aipstz\/.*")|0|0|0|0|
|[drivers/anactrl](# "drivers\/anactrl\/.*")|0|0|0|0|
|[drivers/aoi](# "drivers\/aoi\/.*")|0|0|0|0|
|[drivers/aon_lpadc](# "drivers\/aon_lpadc\/.*")|0|0|0|0|
|[drivers/asmc](# "drivers\/asmc\/.*")|0|0|0|0|
|[drivers/asrc](# "drivers\/asrc\/.*")|0|0|0|0|
|[drivers/audmix](# "drivers\/audmix\/.*")|0|0|0|0|
|[drivers/bbnsm](# "drivers\/bbnsm\/.*; examples\/_boards\/.*\/driver_examples\/bbnsm\/.*; examples\/driver_examples\/bbnsm\/.*")|0|0|0|0|
|[drivers/bctu](# "drivers\/bctu\/.*")|0|0|0|0|
|[drivers/bee](# "drivers\/bee\/.*")|0|0|0|0|
|[drivers/caam](# "drivers\/caam\/.*")|0|0|0|0|
|[drivers/cache_armv7_a](# "drivers\/cache\/armv7-a\/.*")|0|0|0|0|
|[drivers/cache_armv7_m7](# "drivers\/cache\/armv7-m7\/.*")|0|0|0|0|
|[drivers/cache_cache64](# "drivers\/cache\/cache64\/.*")|0|0|0|0|
|[drivers/cache_lmem](# "drivers\/cache\/lmem\/.*")|0|0|0|0|
|[drivers/cache_lpcac](# "drivers\/cache\/lpcac_n4a_mcxn\/.*")|0|0|0|0|
|[drivers/cache_lpcac_n4a_mcxn](# "drivers\/cache\/lpcac_n4a_mcxn\/.*")|0|0|0|0|
|[drivers/cache_lplmem](# "drivers\/cache\/lplmem\/.*")|0|0|0|0|
|[drivers/cache_xcache](# "drivers\/cache\/xcache\/.*")|0|0|0|0|
|[drivers/cache_llc](# "drivers\/cache\/llc\/.*")|0|0|0|0|
|[drivers/cache_example](# "examples\/driver_examples\/cache\/.*; examples\/driver_examples\/llc\/.*")|0|0|0|0|
|[drivers/camera_csr](# "drivers\/camera_csr\/.*")|0|0|0|0|
|[drivers/capt](# "drivers\/capt\/.*")|0|0|0|0|
|[drivers/casper](# "drivers\/casper\/.*")|0|0|0|0|
|[drivers/cau3](# "drivers\/cau3\/.*")|0|0|0|0|
|[drivers/ccm32k](# "drivers\/ccm32k\/.*")|0|0|0|0|
|[drivers/cdog](# "drivers\/cdog\/.*")|0|0|0|0|
|[drivers/ce](# "drivers\/ce\/.*")|0|0|0|0|
|[drivers/ci_pi](# "drivers\/ci_pi\/.*")|0|0|0|0|
|[drivers/cic_irb](# "drivers\/cic_irb\/.*")|0|0|0|0|
|[drivers/clock](# "drivers\/clock\/.*")|0|0|0|0|
|[drivers/cmc](# "drivers\/cmc\/.*")|0|0|0|0|
|[drivers/cmp](# "drivers\/cmp\/.*")|0|0|0|0|
|[drivers/cmp_1](# "drivers\/cmp_1\/.*")|0|0|0|0|
|[drivers/cmt](# "drivers\/cmt\/.*")|0|0|0|0|
|[drivers/cns_acomp](# "drivers\/cns_acomp\/.*")|0|0|0|0|
|[drivers/cns_adc](# "drivers\/cns_adc\/.*")|0|0|0|0|
|[drivers/cns_dac](# "drivers\/cns_dac\/.*")|0|0|0|0|
|[drivers/common](# "drivers\/common\/.*")|0|0|0|0|
|[drivers/cop](# "drivers\/cop\/.*")|0|0|0|0|
|[drivers/crc](# "drivers\/crc\/.*; examples\/driver_examples\/crc\/.*")|0|0|0|0|
|[drivers/ela_csec](# "drivers\/ela_csec\/.*")|0|0|0|0|
|[drivers/csi](# "drivers\/csi\/.*")|0|0|2|0|
|[drivers/ctimer](# "drivers\/ctimer\/.*")|0|0|0|0|
|[drivers/dac](# "drivers\/dac\/.*")|0|0|0|0|
|[drivers/dac12](# "drivers\/dac12\/.*")|0|0|0|0|
|[drivers/dac14](# "drivers\/dac14\/.*")|0|0|0|0|
|[drivers/dac_1](# "drivers\/dac_1\/.*")|0|0|0|0|
|[drivers/dcdc_1](# "drivers\/dcdc_1\/.*")|0|0|0|0|
|[drivers/dcic](# "drivers\/dcic\/.*")|0|0|0|0|
|[drivers/dcif](# "drivers\/dcif\/.*")|0|0|0|0|
|[drivers/dcif_1](# "drivers\/dcif_1\/.*")|0|0|0|0|
|[drivers/dcp](# "drivers\/dcp\/.*")|0|0|0|0|
|[drivers/dma](# "drivers\/dma\/.*")|0|0|0|0|
|[drivers/dma3](# "drivers\/dma3\/.*")|0|0|0|1|
|[drivers/dmamux](# "drivers\/dmamux\/.*")|0|0|0|0|
|[drivers/dmic](# "drivers\/dmic\/.*")|0|0|0|0|
|[drivers/dpr](# "drivers\/dpr\/.*")|0|0|0|0|
|[drivers/dpu](# "drivers\/dpu\/.*")|0|0|0|0|
|[drivers/dpu_1](# "drivers\/dpu_1\/.*")|0|0|0|0|
|[drivers/dpu_irqsteer](# "drivers\/dpu_irqsteer\/.*")|0|0|0|0|
|[drivers/dryice](# "drivers\/dryice\/.*")|0|0|0|0|
|[drivers/dryice_digital](# "drivers\/dryice_digital\/.*")|0|0|0|0|
|[drivers/dsc_adc16](# "drivers\/dsc_adc16\/.*")|0|0|0|0|
|[drivers/dsc_cadc](# "drivers\/dsc_cadc\/.*")|0|0|0|0|
|[drivers/dsc_cmp](# "drivers\/dsc_cmp\/.*")|0|0|0|0|
|[drivers/dsc_cop](# "drivers\/dsc_cop\/.*")|0|0|0|0|
|[drivers/dsc_crc](# "drivers\/dsc_crc\/.*")|0|0|0|0|
|[drivers/dsc_crc16](# "drivers\/dsc_crc16\/.*")|0|0|0|0|
|[drivers/dsc_dac](# "drivers\/dsc_dac\/.*")|0|0|0|0|
|[drivers/dsc_dma](# "drivers\/dsc_dma\/.*")|0|0|0|0|
|[drivers/dsc_dmamux](# "drivers\/dsc_dmamux\/.*")|0|0|0|0|
|[drivers/dsc_edma](# "drivers\/dsc_edma\/.*")|0|0|0|0|
|[drivers/dsc_edma3](# "drivers\/dsc_edma3\/.*")|0|0|0|0|
|[drivers/dsc_eqdc](# "drivers\/dsc_eqdc\/.*")|0|0|0|0|
|[drivers/dsc_ewm](# "drivers\/dsc_ewm\/.*")|0|0|0|0|
|[drivers/dsc_flash](# "drivers\/dsc_flash\/.*")|0|0|0|0|
|[drivers/dsc_flexcan](# "drivers\/dsc_flexcan\/.*")|0|0|2|1|
|[drivers/dsc_freqme](# "drivers\/dsc_freqme\/.*")|0|0|0|0|
|[drivers/dsc_mau](# "drivers\/dsc_mau\/.*")|0|0|0|0|
|[drivers/dsc_gpio](# "drivers\/dsc_gpio\/.*")|0|0|0|1|
|[drivers/dsc_i2c](# "drivers\/dsc_i2c\/.*")|0|0|0|0|
|[drivers/dsc_inputmux](# "drivers\/dsc_inputmux\/.*")|0|0|0|0|
|[drivers/dsc_lpi2c](# "drivers\/dsc_lpi2c\/.*")|0|0|0|1|
|[drivers/dsc_mscan](# "drivers\/dsc_mscan\/.*")|0|0|0|0|
|[drivers/dsc_opamp](# "drivers\/dsc_opamp\/.*")|0|0|0|0|
|[drivers/dsc_opamp_1](# "drivers\/dsc_opamp_1\/.*")|0|0|0|0|
|[drivers/dsc_pdb](# "drivers\/dsc_pdb\/.*")|0|0|0|0|
|[drivers/dsc_pit](# "drivers\/dsc_pit\/.*")|0|0|0|0|
|[drivers/dsc_pmc](# "drivers\/dsc_pmc\/.*")|0|0|0|0|
|[drivers/dsc_pwm](# "drivers\/dsc_pwm\/.*")|0|0|0|0|
|[drivers/dsc_qdc](# "drivers\/dsc_qdc\/.*")|0|0|0|0|
|[drivers/dsc_qtmr](# "drivers\/dsc_qtmr\/.*")|0|0|0|0|
|[drivers/dsc_rgpio](# "drivers\/dsc_rgpio\/.*")|0|0|0|0|
|[drivers/dsc_sim](# "drivers\/dsc_sim\/.*")|0|0|0|0|
|[drivers/dsc_wrap](# "drivers\/dsc_wrap\/.*")|0|0|0|0|
|[drivers/dsc_xbara](# "drivers\/dsc_xbara\/.*")|0|0|0|0|
|[drivers/dspi](# "drivers\/dspi\/.*")|0|0|0|0|
|[drivers/dual_adc](# "drivers\/dual_adc\/.*")|0|0|0|0|
|[drivers/easrc](# "drivers\/easrc\/.*")|0|0|0|1|
|[drivers/ecspi](# "drivers\/ecspi\/.*")|0|0|0|0|
|[drivers/edma](# "drivers\/edma\/.*")|0|0|0|0|
|[drivers/edma4](# "drivers\/edma4\/.*")|0|0|0|0|
|[drivers/edma4_trigger](# "drivers\/edma4\/.*")|0|0|0|0|
|[drivers/eeprom](# "drivers\/eeprom\/.*")|0|0|0|0|
|[drivers/eim](# "drivers\/eim\/.*")|0|0|0|0|
|[drivers/elcdif](# "drivers\/elcdif\/.*")|0|0|0|0|
|[drivers/elec_spec](# "drivers\/elec_spec\/.*")|0|0|0|0|
|[drivers/elemu](# "drivers\/elemu\/.*")|0|0|0|0|
|[drivers/emc](# "drivers\/emc\/.*")|0|0|0|0|
|[drivers/emios](# "drivers\/emios\/.*")|0|0|0|0|
|[drivers/enc](# "drivers\/enc\/.*")|0|0|0|0|
|[drivers/lpc_enet](# "drivers\/lpc_enet\/.*")|0|0|0|0|
|[drivers/mcx_enet](# "drivers\/mcx_enet\/.*")|0|0|0|0|
|[drivers/enet](# "drivers\/enet\/.*")|0|0|0|2|
|[drivers/enet_qos](# "drivers\/enet_qos\/.*")|0|0|0|2|
|[drivers/netc](# "drivers\/netc\/.*")|0|0|2|2|
|[drivers/netc_timer_trigger](# "drivers\/netc\/.*")|0|0|0|0|
|[drivers/netc_hsr_switch](# "drivers\/netc\/.*")|0|0|0|0|
|[drivers/epdc](# "drivers\/epdc\/.*")|0|0|0|0|
|[drivers/eqdc](# "drivers\/eqdc\/.*")|0|0|0|0|
|[drivers/erm](# "drivers\/erm\/.*")|0|0|0|0|
|[drivers/esai](# "drivers\/esai\/.*")|0|0|0|0|
|[drivers/espi](# "drivers\/espi\/.*")|0|0|0|0|
|[drivers/evtg](# "drivers\/evtg\/.*")|0|0|0|0|
|[drivers/ewm](# "drivers\/ewm\/.*; examples\/driver_examples\/ewm\/.*")|0|0|0|0|
|[drivers/flash](# "drivers\/flash\/.*")|0|0|0|0|
|[drivers/flash_ftmr](# "drivers\/flash_ftmr\/.*")|0|0|0|0|
|[drivers/flash_k4](# "drivers\/flash_k4\/.*")|0|0|0|0|
|[drivers/flash_k4_iap](# "drivers\/flash_k4_iap\/.*")|0|0|0|0|
|[drivers/flashiap](# "drivers\/flashiap\/.*")|0|0|0|0|
|[drivers/flash_c40](# "drivers\/flash_c40\/.*")|0|0|0|0|
|[drivers/flexbus](# "drivers\/flexbus\/.*")|0|0|0|0|
|[drivers/flexcan](# "drivers\/flexcan\/.*")|0|0|0|0|
|[drivers/flexcomm](# "drivers\/flexcomm\/.*")|0|0|6|6|
|[drivers/flexcomm_usart](# "drivers\/flexcomm\/usart\/.*")|0|0|0|0|
|[drivers/flexcomm_i2s](# "drivers\/flexcomm\/i2s\/.*")|0|0|0|0|
|[drivers/flexcomm_spi](# "drivers\/flexcomm\/spi\/.*")|0|0|0|0|
|[drivers/flexcomm_i2c](# "drivers\/flexcomm\/i2c\/.*")|0|0|0|0|
|[drivers/flexio_i2s](# "drivers\/flexio\/i2s\/.*")|0|0|0|0|
|[drivers/flexio](# "drivers\/flexio\/fsl_flexio.*")|0|0|0|0|
|[drivers/flexio_camera](# "drivers\/flexio\/camera\/.*")|0|0|0|0|
|[drivers/flexio_i2c](# "drivers\/flexio\/i2c\/.*")|0|0|0|0|
|[drivers/flexio_mculcd](# "drivers\/flexio\/mculcd\/.*")|0|0|0|0|
|[drivers/flexio_spi](# "drivers\/flexio\/spi\/.*")|0|0|0|1|
|[drivers/flexio_uart](# "drivers\/flexio\/uart\/.*")|0|0|0|1|
|[drivers/flexio_trigger](# "drivers\/flexio\/.*")|0|0|0|2|
|[drivers/flexpwm](# "drivers\/flexpwm\/.*")|0|0|0|0|
|[drivers/flexram](# "drivers\/flexram\/.*")|0|0|0|0|
|[drivers/flexspi](# "drivers\/flexspi\/.*")|0|0|0|1|
|[drivers/flexspi_flr](# "drivers\/flexspi_flr\/.*")|0|0|0|0|
|[drivers/fmc](# "drivers\/fmc\/.*")|0|0|0|0|
|[drivers/fmeas](# "drivers\/fmeas\/.*")|0|0|0|0|
|[drivers/fract_pll](# "drivers\/fract_pll\/.*")|0|0|0|0|
|[drivers/ftm](# "drivers\/ftm\/.*")|0|0|0|0|
|[drivers/gdet](# "drivers\/gdet\/.*")|0|0|0|0|
|[drivers/gdma](# "drivers\/gdma\/.*")|0|0|0|0|
|[drivers/gint](# "drivers\/gint\/.*")|0|0|0|0|
|[drivers/glikey](# "drivers\/glikey\/.*")|0|0|0|0|
|[drivers/gpc](# "drivers\/gpc\/.*")|0|0|0|0|
|[drivers/gpc_1](# "drivers\/gpc_1\/.*")|0|0|0|0|
|[drivers/gpc_2](# "drivers\/gpc_2\/.*")|0|0|0|0|
|[drivers/gpio](# "drivers\/gpio\/.*")|0|0|0|0|
|[drivers/gpio_1](# "drivers\/gpio_1\/.*")|0|0|0|0|
|[drivers/gpt](# "drivers\/gpt\/.*")|0|0|0|0|
|[drivers/hashcrypt](# "drivers\/hashcrypt\/.*")|0|0|0|0|
|[drivers/hscmp](# "drivers\/hscmp\/.*")|0|0|0|0|
|[drivers/i2c](# "drivers\/i2c\/.*")|0|0|0|0|
|[drivers/i3c](# "drivers\/i3c\/.*")|0|0|0|4|
|[drivers/iap](# "drivers\/iap\/.*")|0|0|0|0|
|[drivers/iap1](# "drivers\/iap1\/.*")|0|0|4|0|
|[drivers/iap3](# "drivers\/iap3\/.*")|0|0|0|0|
|[drivers/npx](# "drivers\/npx\/.*")|0|0|0|0|
|[drivers/iee](# "drivers\/iee\/.*")|0|0|0|0|
|[drivers/iee_apc](# "drivers\/iee_apc\/.*")|0|0|0|0|
|[drivers/ieer](# "drivers\/ieer\/.*")|0|0|0|0|
|[drivers/igpio](# "drivers\/igpio\/.*")|0|0|0|0|
|[drivers/ii2c](# "drivers\/ii2c\/.*")|0|0|0|0|
|[drivers/imu](# "drivers\/imu\/.*")|0|0|0|0|
|[drivers/inputmux](# "drivers\/inputmux\/.*")|0|0|0|0|
|[drivers/intc](# "drivers\/intc\/.*")|0|0|0|0|
|[drivers/intm](# "drivers\/intm\/.*")|0|0|0|0|
|[drivers/intmux](# "drivers\/intmux\/.*")|0|0|0|0|
|[drivers/iped](# "drivers\/iped\/.*")|0|0|0|0|
|[drivers/ipwm](# "drivers\/ipwm\/.*")|0|0|0|0|
|[drivers/irq](# "drivers\/irq\/.*")|0|0|0|0|
|[drivers/irqsteer](# "drivers\/irqsteer\/.*")|0|0|0|0|
|[drivers/irqsteer_1](# "drivers\/irqsteer_1\/.*")|0|0|0|0|
|[drivers/irtc](# "drivers\/irtc\/.*")|0|0|0|0|
|[drivers/isi](# "drivers\/isi\/.*; examples\/driver_examples\/isi\/.*")|0|0|1|0|
|[drivers/itrc](# "drivers\/itrc\/.*")|0|0|0|0|
|[drivers/itrc_1](# "drivers\/itrc_1\/.*")|0|0|0|0|
|[drivers/iuart](# "drivers\/iuart\/.*")|0|0|0|0|
|[drivers/jpegdec](# "drivers\/jpegdec\/.*")|0|0|0|1|
|[drivers/kbi](# "drivers\/kbi\/.*")|0|0|0|0|
|[drivers/key_manager](# "drivers\/key_manager\/.*")|0|0|0|0|
|[drivers/kpp](# "drivers\/kpp\/.*")|0|0|0|0|
|[drivers/lcdic](# "drivers\/lcdic\/.*")|0|0|0|0|
|[drivers/lcdif](# "drivers\/lcdif\/.*")|0|0|0|0|
|[drivers/lcdifv2](# "drivers\/lcdifv2\/.*")|0|0|0|0|
|[drivers/lcdifv3](# "drivers\/lcdifv3\/.*")|0|0|0|0|
|[drivers/lcu](# "drivers\/lcu\/.*")|0|0|0|0|
|[drivers/ldb](# "drivers\/ldb\/.*")|0|0|0|0|
|[drivers/ldb_1](# "drivers\/ldb_1\/.*")|0|0|0|0|
|[drivers/ldb_combo_phy](# "drivers\/ldb_combo_phy\/.*")|0|0|0|0|
|[drivers/lin](# "drivers\/lin\/.*")|0|0|0|0|
|[drivers/llwu](# "drivers\/llwu\/.*")|0|0|0|0|
|[drivers/lmem](# "drivers\/lmem\/.*")|0|0|0|0|
|[drivers/lpadc](# "drivers\/lpadc\/.*")|0|0|0|0|
|[drivers/lpacmp](# "drivers\/lpacmp\/.*")|0|0|0|0|
|[drivers/lpc_acomp](# "drivers\/lpc_acomp\/.*")|0|0|0|0|
|[drivers/lpc_adc](# "drivers\/lpc_adc\/.*")|0|0|0|0|
|[drivers/lpc_crc](# "drivers\/lpc_crc\/.*; examples\/driver_examples\/lpc_crc\/.*")|0|0|0|0|
|[drivers/lpc_dac](# "drivers\/lpc_dac\/.*")|0|0|0|0|
|[drivers/lpc_dma](# "drivers\/lpc_dma\/.*")|0|0|0|0|
|[drivers/lpc_freqme](# "drivers\/lpc_freqme\/.*")|0|0|0|0|
|[drivers/lpc_gpio](# "drivers\/lpc_gpio\/.*")|0|0|0|0|
|[drivers/lpc_i2c](# "drivers\/lpc_i2c\/.*")|0|0|0|0|
|[drivers/lpc_i2c_1](# "drivers\/lpc_i2c_1\/.*")|0|0|0|0|
|[drivers/lpc_iocon](# "drivers\/lpc_iocon\/.*")|0|0|0|0|
|[drivers/lpc_iocon_lite](# "drivers\/lpc_iocon_lite\/.*")|0|0|0|0|
|[drivers/lpc_iopctl](# "drivers\/lpc_iopctl\/.*")|0|0|0|0|
|[drivers/lpc_lcdc](# "drivers\/lpc_lcdc\/.*")|0|0|0|0|
|[drivers/lpc_minispi](# "drivers\/lpc_minispi\/.*")|0|0|0|0|
|[drivers/lpc_miniusart](# "drivers\/lpc_miniusart\/.*")|0|0|0|0|
|[drivers/lpc_rit](# "drivers\/lpc_rit\/.*")|0|0|0|0|
|[drivers/lpc_rtc](# "drivers\/lpc_rtc\/.*")|0|0|0|0|
|[drivers/lpc_spi_ssp](# "drivers\/lpc_spi_ssp\/.*")|0|0|0|0|
|[drivers/lpc_vspi](# "drivers\/lpc_vspi\/.*")|0|0|0|0|
|[drivers/lpc_vusart](# "drivers\/lpc_vusart\/.*")|0|0|0|0|
|[drivers/lpcmp](# "drivers\/lpcmp\/.*")|0|0|0|0|
|[drivers/lpflexcomm](# "drivers\/lpflexcomm\/.*")|0|0|11|5|
|[drivers/lpi2c](# "drivers\/lpi2c\/.*")|0|0|0|0|
|[drivers/lpit](# "drivers\/lpit\/.*")|0|0|0|0|
|[drivers/lpit_trigger](# "drivers\/lpit\/.*")|0|0|0|0|
|[drivers/lpsci](# "drivers\/lpsci\/.*")|0|0|0|0|
|[drivers/lpspi](# "drivers\/lpspi\/.*")|0|0|5|0|
|[drivers/lpspi_trigger](# "drivers\/lpspi\/.*")|0|0|0|0|
|[drivers/lptmr](# "drivers\/lptmr\/.*")|0|0|0|0|
|[drivers/lptmr_trigger](# "drivers\/lptmr\/.*")|0|0|0|0|
|[drivers/lpuart](# "drivers\/lpuart\/.*")|0|0|1|1|
|[drivers/lpuart_trigger](# "drivers\/lpuart\/.*")|0|0|0|0|
|[drivers/ltc](# "drivers\/ltc\/.*")|0|0|0|0|
|[drivers/mailbox](# "drivers\/mailbox\/.*")|0|0|0|0|
|[drivers/mau](# "drivers\/mau\/.*")|0|0|0|0|
|[drivers/mcan](# "drivers\/mcan\/.*")|0|0|0|0|
|[drivers/mcg](# "drivers\/mcg\/.*")|0|0|0|0|
|[drivers/mcglite](# "drivers\/mcglite\/.*")|0|0|0|0|
|[drivers/mcm](# "drivers\/mcm\/.*")|0|0|0|0|
|[drivers/mcx_cmc](# "drivers\/mcx_cmc\/.*")|0|0|0|0|
|[drivers/mcx_romapi](# "devices\/MCX\/MCXN\/MCXN947\/drivers\/romapi\/.*")|0|0|0|0|
|[drivers/mcx_spc](# "drivers\/mcx_spc\/.*")|0|0|0|0|
|[drivers/mcx_vbat](# "drivers\/mcx_vbat\/.*")|0|0|0|0|
|[drivers/mcxa_romapi](# "devices\/MCX\/MCXA\/MCXA153\/drivers\/romapi\/.*")|0|0|0|0|
|[drivers/mecc](# "drivers\/mecc\/.*")|0|0|0|0|
|[drivers/mipi_csi2rx](# "drivers\/mipi_csi2rx\/.*")|0|0|0|0|
|[drivers/mipi_csi2rx_dwc](# "drivers\/mipi_csi2rx_dwc\/.*")|0|0|0|0|
|[drivers/mipi_csi2rx_dwc_1](# "drivers\/mipi_csi2rx_dwc_1\/.*")|0|0|0|0|
|[drivers/mipi_dsi](# "drivers\/mipi_dsi\/.*")|0|0|0|0|
|[drivers/mipi_dsi_imx](# "drivers\/mipi_dsi_imx\/.*")|0|0|0|0|
|[drivers/mipi_dsi_split](# "drivers\/mipi_dsi_split\/.*")|0|0|0|0|
|[drivers/mipi_dsi2_dwc](# "drivers\/mipi_dsi2_dwc\/.*")|0|0|0|0|
|[drivers/mmau](# "drivers\/mmau\/.*")|0|0|0|0|
|[drivers/mmdvsq](# "drivers\/mmdvsq\/.*")|0|0|0|0|
|[drivers/mmu](# "drivers\/mmu\/.*")|0|0|0|0|
|[drivers/mpu](# "drivers\/mpu\/.*")|0|0|0|0|
|[drivers/mrt](# "drivers\/mrt\/.*")|0|0|0|0|
|[drivers/mscan](# "drivers\/mscan\/.*")|0|0|0|0|
|[drivers/msgintr](# "drivers\/msgintr\/.*")|0|0|0|0|
|[drivers/msmc](# "drivers\/msmc\/.*")|0|0|0|0|
|[drivers/mu](# "drivers\/mu\/.*")|0|0|0|0|
|[drivers/mu1](# "drivers\/mu1\/.*")|0|0|0|1|
|[drivers/nfc](# "drivers\/nfc\/.*")|0|0|0|0|
|[drivers/lpc553x_romapi](# "devices\/LPC\/LPC5500\/LPC55S36\/drivers\/romapi\/.*")|0|0|0|0|
|[drivers/ocotp](# "drivers\/ocotp\/.*")|0|0|0|0|
|[drivers/opamp](# "drivers\/opamp\/.*")|0|0|0|0|
|[drivers/opamp_1](# "drivers\/opamp_1\/.*")|0|0|0|0|
|[drivers/opamp_fast](# "drivers\/opamp_fast\/.*")|0|0|0|0|
|[drivers/ostimer](# "drivers\/ostimer\/.*")|0|0|0|0|
|[drivers/otfad](# "drivers\/otfad\/.*")|0|0|0|0|
|[drivers/otp](# "drivers\/otp\/.*")|0|0|0|0|
|[drivers/pdb](# "drivers\/pdb\/.*")|0|0|0|0|
|[drivers/pdm](# "drivers\/pdm\/.*")|0|0|0|1|
|[drivers/phd](# "drivers\/phd\/.*")|0|0|0|0|
|[drivers/pint](# "drivers\/pint\/.*")|0|0|0|0|
|[drivers/pit](# "drivers\/pit\/.*")|0|0|0|0|
|[drivers/plu](# "drivers\/plu\/.*")|0|0|0|0|
|[drivers/pmc](# "drivers\/pmc\/.*")|0|0|0|0|
|[drivers/pmc0](# "drivers\/pmc0\/.*")|0|0|0|0|
|[drivers/pmu](# "drivers\/pmu\/.*")|0|0|0|0|
|[drivers/pls_pmu](# "drivers\/pls_pmu\/.*")|0|0|0|0|
|[drivers/pn76](# "drivers\/pn76\/.*")|0|0|0|0|
|[drivers/pngdec](# "drivers\/pngdec\/.*")|0|0|0|0|
|[drivers/port](# "drivers\/port\/.*")|0|0|0|0|
|[drivers/power](# "drivers\/power\/.*")|0|0|0|0|
|[drivers/powerquad](# "drivers\/powerquad\/.*")|0|0|0|0|
|[drivers/prince](# "drivers\/prince\/.*")|0|0|0|0|
|[drivers/puf](# "drivers\/puf\/.*")|0|0|0|0|
|[drivers/puf_v3](# "drivers\/puf_v3\/.*")|0|0|0|0|
|[drivers/pwm](# "drivers\/pwm\/.*")|0|0|0|0|
|[drivers/pwt](# "drivers\/pwt\/.*")|0|0|0|0|
|[drivers/pwt_1](# "drivers\/pwt_1\/.*")|0|0|0|0|
|[drivers/pxp](# "drivers\/pxp\/.*")|0|0|0|1|
|[drivers/qdc](# "drivers\/qdc\/.*")|0|0|0|0|
|[drivers/qsci](# "drivers\/qsci\/.*")|0|0|0|1|
|[drivers/qspi](# "drivers\/qspi\/.*")|0|0|0|0|
|[drivers/qtmr_1](# "drivers\/qtmr_1\/.*")|0|0|0|0|
|[drivers/qtmr_1_trigger](# "drivers\/qtmr_1\/.*")|0|0|0|0|
|[drivers/qtmr_2](# "drivers\/qtmr_2\/.*")|0|0|0|0|
|[drivers/queued_spi](# "drivers\/queued_spi\/.*")|0|0|0|1|
|[drivers/rcm](# "drivers\/rcm\/.*")|0|0|0|0|
|[drivers/rdc](# "drivers\/rdc\/.*")|0|0|0|0|
|[drivers/rdc_sema42](# "drivers\/rdc_sema42\/.*")|0|0|0|0|
|[drivers/reset](# "drivers\/reset\/.*")|0|0|0|0|
|[drivers/rgpio](# "drivers\/rgpio\/.*")|0|0|0|0|
|[drivers/rng](# "drivers\/rng\/.*")|0|0|0|0|
|[drivers/rng_1](# "drivers\/rng_1\/.*")|0|0|0|0|
|[drivers/rnga](# "drivers\/rnga\/.*")|0|0|0|0|
|[drivers/rtc](# "drivers\/rtc\/.*")|0|0|0|0|
|[drivers/rtc_1](# "drivers\/rtc_1\/.*")|0|0|0|0|
|[drivers/rtc_jdp](# "drivers\/rtc_jdp\/.*")|0|0|0|0|
|[drivers/rtc_analog](# "drivers\/rtc_analog\/.*")|0|0|0|0|
|[drivers/rtd_cmc](# "drivers\/rtd_cmc\/.*")|0|0|0|0|
|[drivers/rtwdog](# "drivers\/rtwdog\/.*")|0|0|0|0|
|[drivers/s3mu](# "drivers\/s3mu\/.*")|0|0|0|0|
|[drivers/sai](# "drivers\/sai\/.*")|0|0|0|8|
|[drivers/sar_adc](# "drivers\/sar_adc\/.*")|0|0|0|1|
|[drivers/sar_adc_trigger](# "drivers\/sar_adc\/.*")|0|0|0|0|
|[drivers/scg](# "drivers\/scg\/.*")|0|0|0|0|
|[drivers/sctimer](# "drivers\/sctimer\/.*")|0|0|0|2|
|[drivers/sdadc](# "drivers\/sdadc\/.*")|0|0|0|0|
|[drivers/sdhc](# "drivers\/sdhc\/.*")|0|0|0|0|
|[drivers/sdif](# "drivers\/sdif\/.*")|0|0|0|0|
|[drivers/sdioslv](# "drivers\/sdioslv\/.*")|0|0|0|0|
|[drivers/sdma](# "drivers\/sdma\/.*")|0|0|0|0|
|[drivers/sdu](# "drivers\/sdu\/.*")|0|0|0|0|
|[drivers/sema4](# "drivers\/sema4\/.*")|0|0|0|0|
|[drivers/sema42](# "drivers\/sema42\/.*")|0|0|0|0|
|[drivers/semc](# "drivers\/semc\/.*")|0|0|0|0|
|[drivers/sfa](# "drivers\/sfa\/.*")|0|0|0|0|
|[drivers/sha](# "drivers\/sha\/.*")|0|0|0|0|
|[drivers/sim](# "drivers\/sim\/.*")|0|0|0|0|
|[drivers/sim0](# "drivers\/sim0\/.*")|0|0|0|0|
|[drivers/sinc](# "drivers\/sinc\/.*")|0|0|0|0|
|[drivers/sinc_trigger](# "drivers\/sinc\/.*")|0|0|0|0|
|[drivers/slcd](# "drivers\/slcd\/.*")|0|0|0|0|
|[drivers/slcd_split](# "drivers\/slcd_split\/.*")|0|0|0|0|
|[drivers/smartcard](# "drivers\/smartcard\/.*")|0|0|0|2|
|[drivers/smartdma](# "drivers\/smartdma\/.*")|0|0|0|0|
|[drivers/smc](# "drivers\/smc\/.*")|0|0|0|0|
|[drivers/smm](# "drivers\/smm\/.*")|0|0|0|0|
|[drivers/smscm](# "drivers\/smscm\/.*")|0|0|0|0|
|[drivers/snvs_hp](# "drivers\/snvs_hp\/.*")|0|0|0|0|
|[drivers/snvs_lp](# "drivers\/snvs_lp\/.*")|0|0|0|0|
|[drivers/software_i2s](# "drivers\/software_i2s\/.*")|0|0|0|0|
|[drivers/spc](# "drivers\/spc\/.*")|0|0|0|0|
|[drivers/spdif](# "drivers\/spdif\/.*")|0|0|2|1|
|[drivers/spi](# "drivers\/spi\/.*")|0|0|0|1|
|[drivers/spifi](# "drivers\/spifi\/.*")|0|0|0|0|
|[drivers/spm](# "drivers\/spm\/.*")|0|0|0|0|
|[drivers/sramc](# "drivers\/sramc\/.*")|0|0|0|0|
|[drivers/sramctl](# "drivers\/sramctl\/.*")|0|0|0|0|
|[drivers/src](# "drivers\/src\/.*")|0|0|0|0|
|[drivers/src1](# "drivers\/src1\/.*")|0|0|0|0|
|[drivers/ssarc](# "drivers\/ssarc\/.*")|0|0|0|0|
|[drivers/supply](# "drivers\/supply\/.*")|0|0|0|0|
|[drivers/swm](# "drivers\/swm\/.*")|0|0|0|0|
|[drivers/swt](# "drivers\/swt\/.*")|0|0|0|0|
|[drivers/syscon](# "drivers\/syscon\/.*")|0|0|0|0|
|[drivers/sysctl](# "drivers\/sysctl\/.*")|0|0|0|0|
|[drivers/sysctr](# "drivers\/sysctr\/.*")|0|0|0|0|
|[drivers/sysmpu](# "drivers\/sysmpu\/.*")|0|0|0|0|
|[drivers/syspm](# "drivers\/syspm\/.*")|0|0|0|0|
|[drivers/tdet](# "drivers\/tdet\/.*")|0|0|0|0|
|[drivers/tempmon](# "drivers\/tempmon\/.*")|0|0|0|0|
|[drivers/tempsense](# "drivers\/tempsense\/.*")|0|0|0|0|
|[drivers/tempsensor](# "drivers\/tempsensor\/.*")|0|0|0|0|
|[drivers/tenbaset_phy](# "drivers\/tenbaset_phy\/.*")|0|0|0|0|
|[drivers/tmu](# "drivers\/tmu\/.*")|0|0|0|0|
|[drivers/tmu_1](# "drivers\/tmu_1\/.*")|0|0|0|0|
|[drivers/tmu_2](# "drivers\/tmu_2\/.*")|0|0|0|0|
|[drivers/tmu_3](# "drivers\/tmu_3\/.*")|0|0|0|0|
|[drivers/tpm](# "drivers\/tpm\/.*")|0|0|0|3|
|[drivers/tpm_trigger](# "drivers\/tpm\/.*")|0|0|0|0|
|[drivers/trdc](# "drivers\/trdc\/.*")|0|0|0|0|
|[drivers/trdc_1](# "drivers\/trdc_1\/.*")|0|0|0|0|
|[drivers/dsc_mbc](# "drivers\/dsc_mbc\/.*")|0|0|0|0|
|[drivers/trgmux](# "drivers\/trgmux\/.*")|0|0|0|0|
|[drivers/trng](# "drivers\/trng\/.*")|0|0|0|1|
|[drivers/tsc](# "drivers\/tsc\/.*")|0|0|0|0|
|[drivers/tsi](# "drivers\/tsi\/.*")|0|0|0|0|
|[drivers/tspc](# "drivers\/tspc\/.*")|0|0|0|0|
|[drivers/tstmr](# "drivers\/tstmr\/.*")|0|0|0|0|
|[drivers/uart](# "drivers\/uart\/.*")|0|0|0|0|
|[drivers/usdhc](# "drivers\/usdhc\/.*")|0|0|0|0|
|[drivers/utick](# "drivers\/utick\/.*")|0|0|0|0|
|[drivers/vbat](# "drivers\/vbat\/.*")|0|0|0|0|
|[drivers/virt_wrapper](# "drivers\/virt_wrapper\/.*")|0|0|0|0|
|[drivers/vref](# "drivers\/vref\/.*")|0|0|0|0|
|[drivers/vref_1](# "drivers\/vref_1\/.*")|0|0|0|0|
|[drivers/waketimer](# "drivers\/waketimer\/.*")|0|0|0|0|
|[drivers/wdog](# "drivers\/wdog\/.*")|0|0|0|0|
|[drivers/wdog01](# "drivers\/wdog01\/.*")|0|0|0|0|
|[drivers/wdog32](# "drivers\/wdog32\/.*")|0|0|0|0|
|[drivers/wdog8](# "drivers\/wdog8\/.*")|0|0|0|0|
|[drivers/wkt](# "drivers\/wkt\/.*")|0|0|0|0|
|[drivers/wuu](# "drivers\/wuu\/.*")|0|0|0|0|
|[drivers/wkpu](# "drivers\/wkpu\/.*")|0|0|0|0|
|[drivers/wwdt](# "drivers\/wwdt\/.*")|0|0|0|0|
|[drivers/stm](# "drivers\/stm\/.*")|0|0|0|0|
|[drivers/cmu_fc](# "drivers\/cmu_fc\/.*")|0|0|0|0|
|[drivers/cmu_fm](# "drivers\/cmu_fm\/.*")|0|0|0|0|
|[drivers/xbar](# "drivers\/xbar\/.*")|0|0|0|0|
|[drivers/xbar_1](# "drivers\/xbar_1\/.*")|0|0|0|0|
|[drivers/xbara](# "drivers\/xbara\/.*")|0|0|0|0|
|[drivers/xbarb](# "drivers\/xbarb\/.*")|0|0|0|0|
|[drivers/xbic](# "drivers\/xbic\/.*")|0|0|0|0|
|[drivers/xecc](# "drivers\/xecc\/.*")|0|0|0|0|
|[drivers/xrdc](# "drivers\/xrdc\/.*")|0|0|0|0|
|[drivers/xrdc2](# "drivers\/xrdc2\/.*")|0|0|0|0|
|[drivers/xspi](# "drivers\/xspi\/.*")|0|0|0|2|
|[drivers](# "drivers\/.*")|0|0|0|16|
|[midware_coex](# "middleware\/wireless\/coex\/.*")|0|0|1|2|
|[midware_audio_voice_components](# "middleware\/audio_voice\/components\/.*")|0|0|0|0|
|[midware_edgefast_bluetooth](# "middleware\/edgefast_bluetooth\/.*")|0|0|0|0|
|[midware_edgefast_open](# "middleware\/edgefast_open\/(?!examples\/).*")|0|0|0|160|
|[midware_eiq](# "middleware\/eiq\/.*")|0|0|22|33|
|[midware_eiq_int](# "middleware\/eiq_int\/.*")|0|0|0|0|
|[middleware_wireless/framework](# "middleware\/wireless\/framework\/.*; examples\/frdmmcxw72\/wireless_examples\/linker\/.*; examples\/frdmmcxw71\/wireless_examples\/linker\/.*; examples\/mcxw72evk\/wireless_examples\/linker\/.*")|0|0|3|1|
|[middleware_wireless/ethermind](# "middleware\/wireless\/ethermind\/.*")|0|0|0|0|
|[middleware_wireless/bluetooth](# "middleware\/wireless\/bluetooth\/.*")|0|0|139|1|
|[middleware_wireless/XCVR](# "middleware\/wireless\/XCVR\/.*")|0|0|0|0|
|[middleware_wireless/ble_controller](# "middleware\/wireless\/ble_controller\/.*; middleware\/wireless\/fw_v19_nb\/.*")|0|0|1|0|
|[middleware_wireless/genfsk](# "middleware\/wireless\/genfsk\/.*")|0|0|0|0|
|[middleware_wireless/ieee_802_15_4](# "middleware\/wireless\/ieee-802.15.4\/.*; examples\/wireless_examples\/ieee-802.15.4\/.*; examples/mcxw72evk/wireless_examples\/ieee-802.15.4\/.*; examples/frdmmcxw71/wireless_examples\/ieee-802.15.4\/.*; examples/frdmmcxw72/wireless_examples\/ieee-802.15.4\/.*")|0|0|0|0|
|[midware_fatfs/mmc_disk](# "middleware\/fatfs\/source\/fsl_mmc_disk.*")|0|0|0|0|
|[midware_fatfs/nand_disk](# "middleware\/fatfs\/source\/fsl_nand_disk.*")|0|0|0|0|
|[midware_fatfs/ram_disk](# "middleware\/fatfs\/source\/fsl_ram_disk.*")|0|0|0|0|
|[midware_fatfs/sd_disk](# "middleware\/fatfs\/source\/fsl_sd_disk.*")|0|0|0|0|
|[midware_fatfs/sdspi_disk](# "middleware\/fatfs\/source\/fsl_sdspi_disk.*")|0|0|0|0|
|[midware_fatfs/usb_disk](# "middleware\/fatfs\/source\/fsl_usb_disk.*")|0|0|0|0|
|[midware_freemaster](# "middleware\/freemaster\/.*")|0|0|0|2|
|[midware_freemaster_internal](# "middleware\/freemaster_internal\/.*")|0|0|0|0|
|[midware_issdk](# "middleware\/issdk\/.*")|0|0|0|0|
|[midware_linstack](# "middleware\/lin_stack\/.*")|0|0|0|0|
|[midware_littlefs/mflash](# "middleware\/littlefs\/mflash\/.*")|0|0|0|0|
|[midware_g2d_dpu](# "middleware\/g2d_dpu.*")|0|0|0|0|
|[midware_soem](# "middleware\/soem\/.*")|0|0|0|0|
|[midware_freemodbus](# "middleware\/freemodbus\/.*")|0|0|0|0|
|[midware_canopennode](# "middleware\/canopennode\/.*")|0|0|0|17|
|[midware_maestro](# "middleware\/audio_voice\/maestro\/.*")|0|0|2|29|
|[midware_mbed-crypto](# "middleware\/mbed-crypto\/.*")|0|0|0|0|
|[midware_mbedtls](# "middleware\/mbedtls\/.*")|0|0|0|8|
|[midware_mflash](# "middleware\/mflash\/.*")|0|0|0|0|
|[midware_mmcau](# "middleware\/mmcau\/.*")|0|0|0|0|
|[midware_motor_control](# "middleware\/motor_control\/.*")|0|0|0|0|
|[midware_metering](# "middleware\/metering\/.*")|0|0|2|0|
|[midware_multicore/erpc](# "middleware\/multicore\/erpc\/.*")|0|0|0|0|
|[midware_multicore/mcmgr](# "middleware\/multicore\/mcmgr\/.*")|0|0|0|0|
|[midware_multicore/rpmsg](# "middleware\/multicore\/rpmsg-lite\/.*")|0|0|1|0|
|[midware_multicore](# "middleware\/multicore\/.*")|0|0|0|0|
|[midware_neo_isp](# "middleware\/neo_isp\/.*; examples\/demo_apps\/isp_ccl\/.*; examples\/.*\/demo_apps\/isp_ccl\/.*")|0|0|1|1|
|[midware_ntag_i2c_plus](# "middleware\/ntag_i2c_plus\/.*")|0|0|0|0|
|[midware_nxp_iot_agent_int](# "middleware\/nxp_iot_agent_int\/.*")|0|0|0|0|
|[midware_nxp_iot_agent](# "middleware\/nxp_iot_agent\/.*")|0|1|12|28|
|[midware_rtcesl](# "middleware\/rtcesl\/.*")|0|0|6|0|
|[midware_sdmmc](# "middleware\/sdmmc\/.*")|0|0|0|9|
|[midware_se_hostlib](# "middleware\/se_hostlib\/.*")|0|0|0|0|
|[midware_secure-subsystem](# "middleware\/secure-subsystem\/.*")|0|0|0|0|
|[midware_touch](# "middleware\/touch\/.*")|0|0|17|12|
|[midware_usb](# "middleware\/usb\/.*; ecosystem\/middleware\/usb\/.*")|0|0|0|39|
|[midware_voice_seeker](# "middleware\/audio_voice\/components\/voice_seeker\/.*")|0|0|0|0|
|[midware_voice_spot](# "middleware\/audio_voice\/components\/voice_spot\/.*")|0|0|0|0|
|[midware_vit](# "middleware\/audio_voice\/components\/vit\/.*")|0|0|0|0|
|[midware_wifi](# "middleware\/wifi_nxp\/.*")|0|1|13|100|
|[multicore_examples/rpmsg_lite_pingpong_rtos_linux](# "examples\/multicore_examples\/rpmsg_lite_pingpong_rtos_linux\/.*")|0|0|0|0|
|[multicore_examples/rpmsg_lite_pingpong_rtos_no_mcmgr](# "examples\/multicore_examples\/rpmsg_lite_pingpong_rtos_no_mcmgr\/.*")|0|0|0|0|
|[multicore_examples/rpmsg_lite_str_echo_rtos](# "examples\/multicore_examples\/rpmsg_lite_str_echo_rtos\/.*")|0|0|0|0|
|[rtos_amazon_freertos/freertos_nxp](# "rtos\/freertos\/freertos-kernel\/.*")|0|0|0|0|
|[freertos-drivers](# "rtos\/freertos\/freertos-drivers\/.*")|0|0|0|0|
|[edgelock_firmware](# "firmware\/edgelock\/.*")|0|0|0|0|
|[riscv](# "arch\/riscv\/.*")|0|0|0|0|
|[midware_wpa_supplicant-rtos/nxp_custom](# "middleware\/wireless\/wpa_supplicant-rtos\/freertos\/.*; middleware\/wireless\/wpa_supplicant-rtos\/port\/mbedtls\/.*; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/block_alloc\.h; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/block_alloc\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/drivers\/driver_wifi_nxp\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/crc32\.h; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/crc32\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/drivers\/driver\.h")|0|0|0|10|
|[midware_mcu-bootloader](# "middleware\/mcu_bootloader\/.*; ecosystem\/middleware\/mcu_bootloader\/.*")|0|0|0|0|
|[midware_safety](# ".*\/safety_iec60730b.*")|0|0|0|0|
|[MCUXSDK_Environment_Setup](# "mcux-env.*")|0|0|0|0|
|[docs](# "docs\/.*")|0|0|0|0|
|[cmake_extension](# "cmake\/extension\/.*")|0|0|0|0|
|[cmake_toolchain](# "cmake\/toolchain\/.*")|0|0|0|0|
|[west_scripts](# "scripts\/.*")|0|0|0|0|
|[submanifests_dsc](# "submanifests\/devices\/.*")|0|0|0|0|
|[tool_data](# "tool_data\/.*")|0|0|0|0|
|[Kconfig_CMake_entry_point](# "CMakeLists.txt; Kconfig; Kconfig.mcuxpresso")|0|0|0|0|
|[mcuxsdk_cmake_package](# "share\/.*")|0|0|0|0|
|[mcuxsdk_misc](# "cmake_format_config.yml; yamllint_config.yml; README.md")|0|0|0|0|
|[mcuxsdk_license](# "MCUX_VERSION; tool.yml; LA_OPT_NXP_Software_License.htm; LA_OPT_NXP_Software_License.txt; COPYING-BSD-3; SCR.txt")|0|0|0|0|
|[conn_prebuild_generated](# "_build\/pdum_gen\.(c&#124;h); _build\/zps_gen\.(c&#124;h)")|0|0|0|0|
|[components/sbom](# "components\/SBOM\.spdx\.json")|0|0|0|0|
|[components/adp5585](# "components\/expander\/adp5585\/.*")|0|0|0|0|
|[components/assert](# "components\/assert\/.*")|0|0|0|0|
|[components/audio](# "components\/audio\/.*")|0|0|0|2|
|[components/aws_iot](# "components\/aws_iot\/.*")|0|0|0|0|
|[components/button](# "components\/button\/.*")|0|0|0|0|
|[components/clock](# "components\/clock\/.*")|0|0|0|0|
|[components/cmsis_drivers_dspi](# "components\/cmsis_drivers\/cmsis_dspi\/.*; examples\/.*\/cmsis_driver_examples\/dspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_ecspi](# "components\/cmsis_drivers\/cmsis_ecspi\/.*; examples\/.*\/cmsis_driver_examples\/ecspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_enet](# "components\/cmsis_drivers\/cmsis_enet\/.*; examples\/.*\/cmsis_driver_examples\/enet\/.*; components\/cmsis_drivers\/cmsis_enet_phy\/.*; components\/cmsis_drivers\/cmsis_mcx_enet\/.*")|0|0|0|0|
|[components/cmsis_drivers_flash](# "components\/cmsis_drivers\/cmsis_flash\/.*; components\/cmsis_drivers\/cmsis_mcx_flash\/.*; examples\/.*\/cmsis_driver_examples\/flash\/.*")|0|0|0|0|
|[components/cmsis_drivers_flexcomm](# "components\/cmsis_drivers\/cmsis_flexcomm\/.*; examples\/.*\/cmsis_driver_examples\/usart\/.*")|0|0|4|4|
|[components/cmsis_drivers_gpio](# "components\/cmsis_drivers\/cmsis_gpio\/.*; components\/cmsis_drivers\/cmsis_lpc_gpio\/.*; examples\/.*\/cmsis_driver_examples\/gpio\/.*")|0|0|0|0|
|[components/cmsis_drivers_i2c](# "components\/cmsis_drivers\/cmsis_i2c\/.*; examples\/.*\/cmsis_driver_examples\/i2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_ii2c](# "components\/cmsis_drivers\/cmsis_ii2c\/.*; examples\/.*\/cmsis_driver_examples\/ii2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_iuart](# "components\/cmsis_drivers\/cmsis_iuart\/.*; examples\/.*\/cmsis_driver_examples\/iuart\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpc_i2c](# "components\/cmsis_drivers\/cmsis_lpc_i2c\/.*; examples\/.*\/cmsis_driver_examples\/lpc_i2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpc_vspi](# "components\/cmsis_drivers\/cmsis_lpc_vspi\/.*; examples\/.*\/cmsis_driver_examples\/lpc_vspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpi2c](# "components\/cmsis_drivers\/cmsis_lpi2c\/.*; examples\/.*\/cmsis_driver_examples\/lpi2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpspi](# "components\/cmsis_drivers\/cmsis_lpspi\/.*; examples\/.*\/cmsis_driver_examples\/lpspi\/.*")|0|0|0|1|
|[components/cmsis_drivers_lpuart](# "components\/cmsis_drivers\/cmsis_lpuart\/.*; examples\/.*\/cmsis_driver_examples\/lpuart\/.*")|0|0|0|0|
|[components/cmsis_drivers_spi](# "components\/cmsis_drivers\/cmsis_spi\/.*; examples\/.*\/cmsis_driver_examples\/spi\/.*")|0|0|0|1|
|[components/cmsis_drivers_uart](# "components\/cmsis_drivers\/cmsis_uart\/.*; examples\/.*\/cmsis_driver_examples\/uart\/.*")|0|0|0|0|
|[components/cmsis_drivers_prj_conf](# "examples\/_boards\/.*\/cmsis_driver_examples\/prj.conf")|0|0|0|0|
|[components/codec](# "components\/codec\/.*")|0|0|0|22|
|[components/common_task](# "components\/common_task\/.*")|0|0|0|0|
|[components/conn_fwloader](# "components\/conn_fwloader\/.*")|0|0|0|3|
|[components/crc](# "components\/crc\/.*")|0|0|0|0|
|[components/debug_console](# "components\/debug_console\/.*")|0|0|0|0|
|[components/debug_console_lite](# "components\/debug_console_lite\/.*")|0|0|0|0|
|[components/debug_console_rtt](# "components\/debug_console_rtt\/.*")|0|0|0|0|
|[components/display](# "components\/display\/.*")|0|0|0|0|
|[components/touch](# "components\/touch\/.*")|0|0|0|0|
|[components/camera](# "components\/video\/camera\/.*")|0|0|0|4|
|[components/video](# "components\/video\/.*")|0|0|0|3|
|[components/edgefast_wifi](# "components\/edgefast_wifi\/.*")|0|0|0|1|
|[components/ele_base_api](# "components\/ele_base_api\/.*")|0|0|0|0|
|[components/ele_crypto](# "components\/ele_crypto\/.*; examples\/ele_crypto\/.*")|0|0|0|0|
|[components/ele_hseb](# "components\/ele_hseb\/.*")|0|0|0|4|
|[components/crypto_benchmark](# "components\/crypto_benchmark\/.*")|0|0|0|0|
|[components/exception_handling](# "components\/exception_handling\/.*")|0|0|0|0|
|[components/expander](# "components\/expander\/.*; examples\/component_examples\/io_expander\/interrupt_demo\/.*")|0|0|0|0|
|[components/flash_nand_semc](# "components\/flash\/nand\/semc\/.*; examples\/demo_apps\/nand_flash_management\/semc\/.*; examples\/component_examples\/flash_component\/nand\/semc\/.*; examples\/_boards\/.*\/demo_apps\/nand_flash_management\/semc\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/nand\/semc\/.*; examples\/_boards\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/component_examples\/flash_component\/nand\/semc\/?.*")|0|0|0|0|
|[components/flash_nand_flexspi](# "components\/flash\/nand\/flexspi\/.*; examples\/component_examples\/flash_component\/nand\/flexspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/flexspi_nand\/.*; examples\/.*\/component_examples\/flash_component\/flexspi_nand\/.*; examples\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/.*\/component_examples\/flash_component\/nand\/flexspi\/.*")|0|0|0|0|
|[components/flash_nand_xspi](# "components\/flash\/nand\/xspi\/.*; examples\/component_examples\/flash_component\/nand\/xspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/xspi_nand\/.*; examples\/demo_apps\/nand_flash_management\/xspi\/.*; examples\/_boards\/.*\/demo_apps\/nand_flash_management\/xspi\/.*")|0|0|0|0|
|[components/flash_nor_flexspi](# "components\/flash\/nor\/flexspi\/.*; examples\/component_examples\/flash_component\/nor\/flexspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/flexspi_nor\/.*; examples\/.*\/component_examples\/flash_component\/flexspi_nor\/.*; examples\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/.*\/component_examples\/flash_component\/nor\/flexspi\/.*; examples\/component_examples\/flash_component\/nor\/flexspi\/?.*")|0|0|0|0|
|[components/flash_nor_lpspi](# "components\/flash\/nor\/lpspi\/.*; examples\/component_examples\/flash_component\/nor\/lpspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/lpspi_nor\/.*; examples\/.*\/component_examples\/flash_component\/lpspi_nor\/.*")|0|0|0|0|
|[components/flash_nor_xspi](# "components\/flash\/nor\/xspi\/.*; components\/flash\/nor\/fsl_sfdp_parser.*; examples\/component_examples\/flash_component\/octal\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/[^\/]*octal[^\/]*\/.*")|0|0|0|4|
|[components/flash_nor_spifi](# "components\/flash\/nor\/spifi\/.*; examples\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/spifi_nor\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/.*\/component_examples\/flash_component\/spifi_nor\/.*; examples\/.*\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/component_examples\/flash_component\/nor\/spifi\/?.*")|0|0|0|1|
|[components/format](# "components\/format\/.*")|0|0|0|0|
|[components/gpio](# "components\/gpio\/.*")|0|0|0|0|
|[components/i2c](# "components\/i2c\/.*")|0|0|0|0|
|[components/i3c_bus](# "components\/i3c_bus\/.*; examples\/_boards\/.*\/component_examples\/i3c_bus\/.*; examples\/component_examples\/i3c_bus\/.*")|0|0|0|0|
|[components/imu_adapter](# "components\/imu_adapter\/.*")|0|0|0|3|
|[components/imx_sm_crc](# "components\/imx_sm_crc\/.*")|0|0|0|0|
|[components/internal_flash](# "components\/internal_flash\/.*")|0|0|0|0|
|[components/eeprom_emulation](# "components\/eeprom_emulation\/.*; examples.*\/driver_examples\/eeprom_emulation.*")|0|0|0|0|
|[components/mflash](# "components\/flash\/mflash\/.*")|0|0|0|0|
|[components/IS42SM16800H](# "components\/IS42SM16800H\/.*")|0|0|0|0|
|[components/led](# "components\/led\/(?!example\/).*")|0|0|0|0|
|[components/lists](# "components\/lists\/.*")|0|0|0|0|
|[components/log](# "components\/log\/(?!example\/).*")|0|0|0|0|
|[components/mem_manager](# "components\/mem_manager\/.*")|0|0|0|0|
|[components/messaging](# "components\/messaging\/.*")|0|0|0|0|
|[components/misc_utilities](# "components\/misc_utilities\/.*")|0|0|0|0|
|[components/mpi_loader](# "components\/mpi_loader\/.*")|0|0|0|0|
|[components/mt48lc2m32b2](# "components\/mt48lc2m32b2\/.*")|0|0|0|0|
|[components/mt48lc4m16a2](# "components\/mt48lc4m16a2\/.*")|0|0|0|0|
|[components/mx25l_flash](# "components\/mx25l_flash\/.*")|0|0|0|0|
|[components/mx25r_flash](# "components\/mx25r_flash\/.*")|0|0|0|0|
|[components/notifier](# "components\/notifier\/.*")|0|0|0|0|
|[components/osa](# "components\/osa\/.*")|0|0|0|0|
|[components/panic](# "components\/panic\/.*")|0|0|0|0|
|[components/phy](# "components\/phy\/.*")|0|0|0|2|
|[components/pinctrl](# "components\/pinctrl\/.*")|0|0|0|0|
|[components/pmic_pf5020](# "components\/pmic\/pf5020\/.*")|0|0|0|0|
|[components/pmic_pf3000](# "components\/pmic\/pf3000\/.*")|0|0|0|0|
|[components/pmic_pf1550](# "components\/pmic\/pf1550\/.*")|0|0|0|0|
|[components/pmic_pca9422](# "components\/pmic\/pca9422\/.*")|0|0|0|2|
|[components/pmic_pca9420](# "components\/pmic\/pca9420\/.*")|0|0|0|0|
|[components/pmic_pf9453](# "components\/pmic\/pf9453\/.*; examples\/component_examples\/pmic/pf9453\/.*")|0|0|0|0|
|[components/power](# "components\/power\/.*")|0|0|0|0|
|[components/power_manager](# "components\/power_manager\/.*; examples\/demo_apps\/(power_manager(_[a-zA-Z0-9]*)?)\/.*; examples\/_boards\/.*\/demo_apps\/(power_manager(_[a-zA-Z0-9]*)?)\/.*")|0|0|0|1|
|[components/psa_crypto_driver](# "components\/psa_crypto_driver\/.*")|0|1|2|48|
|[components/pwm](# "components\/pwm\/.*")|0|0|0|0|
|[components/reset](# "components\/reset\/.*")|0|0|0|0|
|[components/reset1](# "components\/reset\/.*")|0|0|0|0|
|[components/rng](# "components\/rng\/.*")|0|0|0|0|
|[components/rpmsg](# "components\/rpmsg\/.*")|0|0|0|0|
|[components/rtc](# "components\/rtc\/.*")|0|0|0|0|
|[components/rtt](# "components\/rtt\/.*")|0|0|0|0|
|[components/scmi](# "components\/scmi\/.*")|0|0|0|0|
|[components/sdu](# "components\/sdu\/.*")|0|0|0|1|
|[components/sensor_fxls8974cf](# "components\/sensor\/fxls8974cf\/.*")|0|0|0|0|
|[components/sensor_fxos8700cq](# "components\/sensor\/fxos8700cq\/.*")|0|0|0|0|
|[components/sensor_icm42688p](# "components\/sensor\/icm42688p\/.*")|0|0|0|0|
|[components/sensor_p3t1755](# "components\/sensor\/p3t1755\/.*; examples\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*; examples\/_boards\/.*\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*; boards/.*\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*")|0|0|0|0|
|[components/sensor_lsm6dso](# "components\/sensor\/lsm6dso\/.*")|0|0|0|1|
|[components/sensor_nmh1000](# "components\/sensor\/nmh1000\/.*; examples\/demo_apps\/magnetic_switch\/.*")|0|0|0|0|
|[components/sensor_tmp117](# "components\/sensor\/tmp117\/.*")|0|0|0|0|
|[components/serial_manager](# "components\/serial_manager\/.*")|0|0|0|0|
|[components/serial_mwm](# "components\/serial_mwm\/.*")|0|0|0|0|
|[components/shell](# "components\/shell\/.*")|0|0|0|0|
|[components/silicon_id](# "components\/silicon_id\/.*")|0|0|0|0|
|[components/slcd_engine](# "components\/slcd_engine\/.*")|0|0|0|0|
|[components/sm](# "components\/sm\/.*")|0|0|0|0|
|[components/smbus](# "components\/smbus\/.*")|0|0|0|0|
|[components/smt](# "components\/smt\/.*")|0|0|0|0|
|[components/spi](# "components\/spi\/.*")|0|0|0|0|
|[components/srtm](# "components\/srtm\/.*")|0|0|0|3|
|[components/str](# "components\/str\/.*")|0|0|0|1|
|[components/sx1502](# "components\/sx1502\/.*; examples\/component_examples\/sx1502_led_control\/.*; examples\/_boards\/.*\/component_examples\/sx1502_led_control\/.*; boards\/.*\/component_examples\/sx1502_led_control\/.*")|0|0|0|1|
|[components/systick_timer](# "components\/systick_timer\/.*")|0|0|0|0|
|[components/time_stamp](# "components\/time_stamp\/.*")|0|0|0|0|
|[components/timer](# "components\/timer\/.*")|0|0|0|0|
|[components/timer_manager](# "components\/timer_manager\/.*")|0|0|0|0|
|[components/uart](# "components\/uart\/.*")|0|0|0|2|
|[components/memfault_integration](# "components\/debug\/memfault\/sdk_port\/.*; components\/debug\/memfault\/Kconfig; components\/debug\/memfault\/CMakeLists.txt")|0|0|0|0|
|[components/unity](# "components\/unity\/.*")|0|0|0|0|
|[components/wifi_bt_module](# "components\/wifi_bt_module\/.*")|0|0|0|0|
|[components/coredump](# "components\/debug\/coredump\/.*; examples\/component_examples\/coredump_fault\/.*; examples\/_boards\/.*\/component_examples\/coredump_fault\/.*")|0|0|1|0|
|[components/gen_hal](# "components\/gen_hal\/.*")|0|0|0|0|
|[components/semihost](# "components\/semihost\/.*; examples\/component_examples\/semihost\/.*; examples\/_boards\/.*\/component_examples\/semihost\/.*")|0|0|0|0|
|[components](# "components\/.*")|0|0|0|0|

