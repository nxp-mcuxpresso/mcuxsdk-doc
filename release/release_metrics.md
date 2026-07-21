# Development Systems and Metrics

The MCUXpresso SDK provides the following summary of Coverity Static Analysis to help customers assess the quality and security posture of our software. The table includes results for
- Cyclomatic complexity ([CCM](https://en.wikipedia.org/wiki/Cyclomatic_complexity))
- Common Weakness Enumerations ([CWE](https://en.wikipedia.org/wiki/Common_Weakness_Enumeration))
- High Impact Findings ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))
- Memory Leaks for Embedded C/C++ Systems ([Definition](https://documentation.blackduck.com/bundle/coverity-docs/page/checker-ref/tables/coverity-checker-coverage.html))

This enables customers to make informed decisions and meet their own compliance requirements.
The tabulated results cover findings that are classified as issues.

|Development boards|HIGH IMPACT|Memory Leaks|CWE|CCM > 20|
|:--               |:--    |:--    |:--    |:--    |
|[Arch_ARM](# "arch\/arm\/.*")|0|0|0|0|
|[Arch_xtensa](# "arch\/xtensa\/.*")|0|0|0|0|
|[version](# "^.*\/mcuxsdk_version\.h$")|0|0|0|0|
|[DSC_build_targets](# "arch\/dsp56800\/.*")|0|0|0|0|
|[audio_examples/voice_spot_demo](# "examples_int\/audio_examples\/voice_spot_demo\/.*")|0|0|0|0|
|[audio_examples](# "examples\/.*\/audio_examples\/.*; examples\/audio_examples\/.*; ecosystem\/.*\/examples\/.*\/audio_examples\/.*")|0|0|0|0|
|[aws_examples](# "examples\/.*\/aws_examples\/.*; examples\/aws_examples\/.*; ecosystem\/.*\/examples\/.*\/aws_examples\/.*")|0|0|0|0|
|[azure_examples](# "examples\/.*\/azure_examples\/.*; examples\/azure_examples\/.*")|0|0|0|0|
|[display_examples](# "examples\/.*\/display_examples\/.*; examples\/display_examples\/.*; examples\/_boards\/.*\/display_examples\/.*")|0|0|0|0|
|[lvgl_examples](# "examples\/.*\/lvgl_examples\/.*; examples\/lvgl_examples\/.*")|0|0|0|0|
|[lin_examples](# "examples\/.*\/lin_stack\/.*; examples\/lin_stack\/.*")|0|0|0|0|
|[devices_arch/arm](# "devices\/arm\/.*")|0|0|0|0|
|[devices_arch/dsp56800](# "devices\/dsp56800\/.*")|0|0|0|0|
|[devices_arch/xtensa](# "devices\/xtensa\/.*")|0|0|0|0|
|[devices_arch/ezhv](# "devices\/ezhv\/.*")|0|0|0|0|
|[devices_arch](# "devices\/[^\/]*$")|0|0|0|0|
|[devices_DSC/MC56F80xxx](# "devices\/DSC\/MC56F80xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F81xxx](# "devices\/DSC\/MC56F81xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F82xxx](# "devices\/DSC\/MC56F82xxx\/.*")|0|0|0|0|
|[devices_DSC/MC56F83xxx](# "devices\/DSC\/MC56F83xxx\/.*")|0|0|0|0|
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
|[devices_LPC/LPC54000](# "devices\/LPC\/LPC54000\/.*")|0|0|0|0|
|[devices_LPC/LPC5500](# "devices\/LPC\/LPC5500\/.*")|0|0|0|0|
|[devices_LPC](# "devices\/LPC\/.*")|0|0|0|0|
|[devices_MCX/MCXA](# "devices\/MCX\/MCXA\/.*")|0|0|0|0|
|[devices_MCX/MCXC444](# "devices\/MCX\/MCXC\/MCXC[124]4[34]\/.*; devices\/MCX\/MCXC\/periph2\/.*")|0|0|0|0|
|[devices_MCX/MCXC242](# "devices\/MCX\/MCXC\/MCXC[12]4[12]\/.*; devices\/MCX\/MCXC\/periph1\/.*")|0|0|0|0|
|[devices_MCX/MCXC041](# "devices\/MCX\/MCXC\/MCXC041\/.*; devices\/MCX\/MCXC\/periph\/.*")|0|0|0|0|
|[devices_MCX/MCXE24](# "devices\/MCX\/MCXE\/MCXE24[0-9]\/.*; devices\/MCX\/MCXE\/periph[023]\/.*")|0|0|0|0|
|[devices_MCX/MCXE31](# "devices\/MCX\/MCXE\/MCXE31[0-9A-F]\/.*; devices\/MCX\/MCXE\/periph[145]\/.*")|0|0|0|0|
|[devices_MCX/MCXL](# "devices.*\/MCX\/MCXL\/.*")|0|0|0|0|
|[devices_MCX/MCXN](# "devices\/MCX\/MCXN\/.*")|0|0|0|0|
|[devices_MCX/MCXW](# "devices\/MCX\/MCXW\/(?!.*\/fsl_power\.[ch]$&#124;.*\/drivers\/fsl_system\.[ch]$&#124;.*\/drivers\/timer_manager_mcxw23\/.*$&#124;.*\/drivers\/power_manager_mcxw23\/.*$).*$")|0|0|0|0|
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
|[devices_RT/RT1170](# "devices\/RT\/RT1170\/.*")|0|0|0|0|
|[devices_RT/RT1180](# "devices\/RT\/RT1180\/.*")|0|0|0|0|
|[devices_RT/RT500](# "devices\/RT\/RT500\/.*")|0|0|0|0|
|[devices_RT/RT600](# "devices\/RT\/RT600\/.*")|0|0|0|0|
|[devices_RT/RT700](# "devices\/RT\/RT700\/.*")|0|0|0|0|
|[devices_RT](# "(devices&#124;devices_int)\/RT\/.*")|0|0|0|0|
|[devices_Wireless/KW](# "devices\/Wireless\/KW\/.*")|0|0|0|0|
|[devices_Wireless/RW](# "devices\/Wireless\/RW\/(?!.*\/fsl_iped\.[ch]$&#124;.*\/drivers\/romapi\/.*$).*$")|0|0|0|0|
|[devices_Wireless/RW_iped](# "devices\/Wireless\/RW\/.*\/fsl_iped\.[ch]$")|0|0|0|0|
|[devices_Wireless/RW_romapi](# "devices\/Wireless\/RW\/.*\/drivers\/romapi\/.*")|0|0|0|0|
|[devices_Wireless](# "(devices&#124;devices_int)\/Wireless\/.*")|0|0|0|0|
|[devices_iMX/iMX7ULP](# "devices\/i.MX\/i.MX7ULP\/.*")|0|0|0|0|
|[devices_iMX/iMX8M](# "devices\/i.MX\/i.MX8M\/.*")|0|0|0|0|
|[devices_iMX/iMX8MM](# "devices\/i.MX\/i.MX8MM\/.*")|0|0|0|0|
|[devices_iMX/iMX8MN](# "devices\/i.MX\/i.MX8MN\/.*")|0|0|0|0|
|[devices_iMX/iMX8MP](# "devices\/i.MX\/i.MX8MP\/.*")|0|0|0|0|
|[devices_iMX/iMX8ULP](# "devices\/i.MX\/i.MX8ULP\/.*")|0|0|0|0|
|[devices_iMX/iMX93](# "devices\/i.MX\/i.MX93\/.*")|0|0|0|0|
|[devices_iMX/iMX95](# "devices\/i.MX\/i.MX95\/.*")|0|0|0|0|
|[devices_iMX/iMX943](# "devices\/i.MX\/i.MX943\/.*")|0|0|0|0|
|[devices_iMX](# "(devices&#124;devices_int)\/i.MX\/.*")|0|0|0|0|
|[drivers/sbom](# "SBOM\.spdx\.json; SBOM.spdx.json")|0|0|0|0|
|[drivers/endat2](# "drivers\/endat2p2\/.*")|0|0|0|0|
|[drivers/endat3](# "drivers\/endat3\/.*")|0|0|0|0|
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
|[drivers/cache_example](# "examples\/driver_examples\/cache\/.*")|0|0|0|0|
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
|[drivers/csi](# "drivers\/csi\/.*")|0|0|0|0|
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
|[drivers/dma3](# "drivers\/dma3\/.*")|0|0|0|0|
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
|[drivers/dsc_eqdc](# "drivers\/dsc_eqdc\/.*")|0|0|0|0|
|[drivers/dsc_ewm](# "drivers\/dsc_ewm\/.*")|0|0|0|0|
|[drivers/dsc_flash](# "drivers\/dsc_flash\/.*")|0|0|0|0|
|[drivers/dsc_flexcan](# "drivers\/dsc_flexcan\/.*")|0|0|0|0|
|[drivers/dsc_freqme](# "drivers\/dsc_freqme\/.*")|0|0|0|0|
|[drivers/dsc_mau](# "drivers\/dsc_mau\/.*")|0|0|0|0|
|[drivers/dsc_gpio](# "drivers\/dsc_gpio\/.*")|0|0|0|0|
|[drivers/dsc_i2c](# "drivers\/dsc_i2c\/.*")|0|0|0|0|
|[drivers/dsc_inputmux](# "drivers\/dsc_inputmux\/.*")|0|0|0|0|
|[drivers/dsc_lpi2c](# "drivers\/dsc_lpi2c\/.*")|0|0|0|0|
|[drivers/dsc_mscan](# "drivers\/dsc_mscan\/.*")|0|0|0|0|
|[drivers/dsc_opamp](# "drivers\/dsc_opamp\/.*")|0|0|0|0|
|[drivers/dsc_opamp_1](# "drivers\/dsc_opamp_1\/.*")|0|0|0|0|
|[drivers/dsc_pdb](# "drivers\/dsc_pdb\/.*")|0|0|0|0|
|[drivers/dsc_pit](# "drivers\/dsc_pit\/.*")|0|0|0|0|
|[drivers/dsc_pmc](# "drivers\/dsc_pmc\/.*")|0|0|0|0|
|[drivers/dsc_pwm](# "drivers\/dsc_pwm\/.*")|0|0|0|0|
|[drivers/dsc_qdc](# "drivers\/dsc_qdc\/.*")|0|0|0|0|
|[drivers/dsc_qtmr](# "drivers\/dsc_qtmr\/.*")|0|0|0|0|
|[drivers/dsc_sim](# "drivers\/dsc_sim\/.*")|0|0|0|0|
|[drivers/dsc_wrap](# "drivers\/dsc_wrap\/.*")|0|0|0|0|
|[drivers/dsc_xbara](# "drivers\/dsc_xbara\/.*")|0|0|0|0|
|[drivers/dspi](# "drivers\/dspi\/.*")|0|0|0|0|
|[drivers/easrc](# "drivers\/easrc\/.*")|0|0|0|0|
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
|[drivers/enet](# "drivers\/enet\/.*")|0|0|0|0|
|[drivers/enet_qos](# "drivers\/enet_qos\/.*")|0|0|0|0|
|[drivers/netc](# "drivers\/netc\/.*")|0|0|0|0|
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
|[drivers/flexcomm](# "drivers\/flexcomm\/.*")|0|0|0|2|
|[drivers/flexcomm_usart](# "drivers\/flexcomm\/usart\/.*")|0|0|0|0|
|[drivers/flexcomm_i2s](# "drivers\/flexcomm\/i2s\/.*")|0|0|0|0|
|[drivers/flexcomm_spi](# "drivers\/flexcomm\/spi\/.*")|0|0|0|0|
|[drivers/flexcomm_i2c](# "drivers\/flexcomm\/i2c\/.*")|0|0|0|0|
|[drivers/flexio_i2s](# "drivers\/flexio\/i2s\/.*")|0|0|0|0|
|[drivers/flexio](# "drivers\/flexio\/fsl_flexio.*")|0|0|0|0|
|[drivers/flexio_camera](# "drivers\/flexio\/camera\/.*")|0|0|0|0|
|[drivers/flexio_i2c](# "drivers\/flexio\/i2c\/.*")|0|0|0|0|
|[drivers/flexio_mculcd](# "drivers\/flexio\/mculcd\/.*")|0|0|0|0|
|[drivers/flexio_spi](# "drivers\/flexio\/spi\/.*")|0|0|0|0|
|[drivers/flexio_uart](# "drivers\/flexio\/uart\/.*")|0|0|0|0|
|[drivers/flexio_trigger](# "drivers\/flexio\/.*")|0|0|0|0|
|[drivers/flexpwm](# "drivers\/flexpwm\/.*")|0|0|0|0|
|[drivers/flexram](# "drivers\/flexram\/.*")|0|0|0|0|
|[drivers/flexspi](# "drivers\/flexspi\/.*")|0|0|0|0|
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
|[drivers/i3c](# "drivers\/i3c\/.*")|0|0|0|0|
|[drivers/iap](# "drivers\/iap\/.*")|0|0|0|0|
|[drivers/iap1](# "drivers\/iap1\/.*")|0|0|0|0|
|[drivers/iap3](# "drivers\/iap3\/.*")|0|0|0|0|
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
|[drivers/isi](# "drivers\/isi\/.*; examples\/driver_examples\/isi\/.*")|0|0|0|0|
|[drivers/itrc](# "drivers\/itrc\/.*")|0|0|0|0|
|[drivers/itrc_1](# "drivers\/itrc_1\/.*")|0|0|0|0|
|[drivers/iuart](# "drivers\/iuart\/.*")|0|0|0|0|
|[drivers/jpegdec](# "drivers\/jpegdec\/.*")|0|0|0|0|
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
|[drivers/lpflexcomm](# "drivers\/lpflexcomm\/.*")|0|0|0|0|
|[drivers/lpi2c](# "drivers\/lpi2c\/.*")|0|0|0|0|
|[drivers/lpit](# "drivers\/lpit\/.*")|0|0|0|0|
|[drivers/lpit_trigger](# "drivers\/lpit\/.*")|0|0|0|0|
|[drivers/lpsci](# "drivers\/lpsci\/.*")|0|0|0|0|
|[drivers/lpspi](# "drivers\/lpspi\/.*")|0|0|0|0|
|[drivers/lpspi_trigger](# "drivers\/lpspi\/.*")|0|0|0|0|
|[drivers/lptmr](# "drivers\/lptmr\/.*")|0|0|0|0|
|[drivers/lptmr_trigger](# "drivers\/lptmr\/.*")|0|0|0|0|
|[drivers/lpuart](# "drivers\/lpuart\/.*")|0|0|0|0|
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
|[drivers/mu1](# "drivers\/mu1\/.*")|0|0|0|0|
|[drivers/nfc](# "drivers\/nfc\/.*")|0|0|0|0|
|[drivers/lpc553x_romapi](# "devices\/LPC\/LPC5500\/LPC55S36\/drivers\/romapi\/.*")|0|0|0|0|
|[drivers/ocotp](# "drivers\/ocotp\/.*")|0|0|0|0|
|[drivers/opamp](# "drivers\/opamp\/.*")|0|0|0|0|
|[drivers/opamp_fast](# "drivers\/opamp_fast\/.*")|0|0|0|0|
|[drivers/ostimer](# "drivers\/ostimer\/.*")|0|0|0|0|
|[drivers/otfad](# "drivers\/otfad\/.*")|0|0|0|0|
|[drivers/otp](# "drivers\/otp\/.*")|0|0|0|0|
|[drivers/pdb](# "drivers\/pdb\/.*")|0|0|0|0|
|[drivers/pdm](# "drivers\/pdm\/.*")|0|0|0|0|
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
|[drivers/pxp](# "drivers\/pxp\/.*")|0|0|0|0|
|[drivers/qdc](# "drivers\/qdc\/.*")|0|0|0|0|
|[drivers/qsci](# "drivers\/qsci\/.*")|0|0|0|0|
|[drivers/qspi](# "drivers\/qspi\/.*")|0|0|0|0|
|[drivers/qtmr_1](# "drivers\/qtmr_1\/.*")|0|0|0|0|
|[drivers/qtmr_1_trigger](# "drivers\/qtmr_1\/.*")|0|0|0|0|
|[drivers/qtmr_2](# "drivers\/qtmr_2\/.*")|0|0|0|0|
|[drivers/queued_spi](# "drivers\/queued_spi\/.*")|0|0|0|0|
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
|[drivers/sai](# "drivers\/sai\/.*")|0|0|0|0|
|[drivers/sar_adc](# "drivers\/sar_adc\/.*")|0|0|0|0|
|[drivers/sar_adc_trigger](# "drivers\/sar_adc\/.*")|0|0|0|0|
|[drivers/scg](# "drivers\/scg\/.*")|0|0|0|0|
|[drivers/sctimer](# "drivers\/sctimer\/.*")|0|0|0|0|
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
|[drivers/smartcard](# "drivers\/smartcard\/.*")|0|0|0|0|
|[drivers/smartdma](# "drivers\/smartdma\/.*")|0|0|0|0|
|[drivers/smc](# "drivers\/smc\/.*")|0|0|0|0|
|[drivers/smm](# "drivers\/smm\/.*")|0|0|0|0|
|[drivers/smscm](# "drivers\/smscm\/.*")|0|0|0|0|
|[drivers/snvs_hp](# "drivers\/snvs_hp\/.*")|0|0|0|0|
|[drivers/snvs_lp](# "drivers\/snvs_lp\/.*")|0|0|0|0|
|[drivers/software_i2s](# "drivers\/software_i2s\/.*")|0|0|0|0|
|[drivers/spc](# "drivers\/spc\/.*")|0|0|0|0|
|[drivers/spdif](# "drivers\/spdif\/.*")|0|0|0|0|
|[drivers/spi](# "drivers\/spi\/.*")|0|0|0|0|
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
|[drivers/tpm](# "drivers\/tpm\/.*")|0|0|0|0|
|[drivers/tpm_trigger](# "drivers\/tpm\/.*")|0|0|0|0|
|[drivers/trdc](# "drivers\/trdc\/.*")|0|0|0|0|
|[drivers/trdc_1](# "drivers\/trdc_1\/.*")|0|0|0|0|
|[drivers/dsc_mbc](# "drivers\/dsc_mbc\/.*")|0|0|0|0|
|[drivers/trgmux](# "drivers\/trgmux\/.*")|0|0|0|0|
|[drivers/trng](# "drivers\/trng\/.*")|0|0|0|0|
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
|[drivers/xspi](# "drivers\/xspi\/.*")|0|0|0|0|
|[drivers](# "drivers\/.*")|0|0|0|0|
|[driver_examples/endat2](# "examples\/.*\/digital_encoder_examples\/endat2p2\/.*; examples\/digital_encoder_examples\/endat2p2\/.*")|0|0|0|0|
|[driver_examples/endat3](# "examples\/.*\/digital_encoder_examples\/endat3\/.*; examples\/digital_encoder_examples\/endat3\/.*")|0|0|0|0|
|[driver_examples/aoi](# "examples\/driver_examples\/aoi\/.*; examples\/_boards\/.*\/driver_examples\/aoi\/.*")|0|0|0|0|
|[driver_examples/asrc](# "examples\/_boards\/.*\/demo_apps\/(asrc(_[a-zA-Z0-9]*)?)\/.*; examples\/_boards\/.*\/driver_examples\/(asrc(_[a-zA-Z0-9]*)?)\/.*; examples\/demo_apps\/(asrc(_[a-zA-Z0-9]*)?)\/.*; examples\/driver_examples\/(asrc(_[a-zA-Z0-9]*)?)\/.*")|0|0|0|0|
|[driver_examples/audmix](# "examples\/_boards\/.*\/driver_examples\/(audmix(_[a-zA-Z0-9]*)?)\/.*; examples\/driver_examples\/(audmix(_[a-zA-Z0-9]*)?)\/.*")|0|0|0|0|
|[driver_examples/capt](# "examples\/driver_examples\/capt\/.*; examples\/_boards\/.*\/driver_examples\/capt\/.*")|0|0|0|0|
|[driver_examples/ccm](# "examples\/driver_examples\/(ccm_clockout(_[a-zA-Z0-9]*)?)(\/.*)?$; examples\/_boards\/.*\/driver_examples\/(ccm_clockout(_[a-zA-Z0-9]*)?)(\/.*)?$; examples\/_boards\/.*\/driver_examples\/(clockout(_[a-zA-Z0-9]*)?)(\/.*)?$; examples\/_boards\/.*\/driver_examples\/(clockout(_[a-zA-Z0-9]*)?)\/?.*")|0|0|0|0|
|[driver_examples/cmt](# "drivers\/cmt\/.*")|0|0|0|0|
|[driver_examples/cop](# "examples\/driver_examples\/cop\/.*")|0|0|0|0|
|[driver_examples/csi](# "examples\/driver_examples\/csi\/.*; examples\/_boards\/.*\/driver_examples\/csi\/.*")|0|0|0|0|
|[driver_examples/ctimer](# "examples\/driver_examples\/ctimer\/.*; examples\/_boards\/.*\/driver_examples\/ctimer\/.*")|0|0|0|0|
|[driver_examples/dcic](# "examples\/driver_examples\/dcic\/.*; examples\/_boards\/.*\/driver_examples\/dcic\/.*")|0|0|0|0|
|[driver_examples/dcif](# "examples\/driver_examples\/dcif\/.*")|0|0|0|0|
|[driver_examples/dma](# "examples\/driver_examples\/dma\/.*; examples\/_boards\/.*\/driver_examples\/dma\/.*")|0|0|0|0|
|[driver_examples/dma3](# "examples\/driver_examples\/dma3\/.*; examples\/_boards\/.*\/driver_examples\/dma3\/.*")|0|0|0|0|
|[driver_examples/dmic](# "examples\/driver_examples\/dmic\/.*; examples\/_boards\/.*\/driver_examples\/dmic\/.*")|0|0|0|0|
|[driver_examples/dpr](# "drivers\/dpr\/.*")|0|0|0|0|
|[driver_examples/dpu](# "drivers\/dpu\/.*")|0|0|0|0|
|[driver_examples/dpu_1](# "examples\/driver_examples\/dpu_1\/.*")|0|0|0|0|
|[driver_examples/dpu_irqsteer](# "drivers\/dpu_irqsteer\/.*")|0|0|0|0|
|[driver_examples/dsc_dma](# "examples\/driver_examples\/dsc_dma\/.*; examples\/_boards\/.*\/driver_examples\/dsc_dma\/.*")|0|0|0|0|
|[driver_examples/dsc_dmamux](# "examples\/driver_examples\/dsc_edma\/.*; examples\/_boards\/.*\/driver_examples\/dsc_edma\/.*")|0|0|0|0|
|[driver_examples/dsc_edma](# "examples\/driver_examples\/dsc_edma\/.*; examples\/_boards\/.*\/driver_examples\/dsc_edma\/.*")|0|0|0|0|
|[driver_examples/dsc_eqdc](# "examples\/driver_examples\/dsc_eqdc\/.*")|0|0|0|0|
|[driver_examples/dsc_flexcan](# "examples\/driver_examples\/dsc_flexcan\/.*")|0|0|0|0|
|[driver_examples/dsc_freqme](# "examples\/driver_examples\/dsc_freqme\/.*; examples\/_boards\/.*\/driver_examples\/freqme\/.*")|0|0|0|0|
|[driver_examples/dsc_gpio](# "examples\/driver_examples\/dsc_gpio\/.*; examples\/_boards\/.*\/driver_examples\/dsc_gpio\/.*")|0|0|0|0|
|[driver_examples/dsc_mau](# "examples\/driver_examples\/dsc_mau\/.*; examples\/_boards\/.*\/driver_examples\/dsc_mau\/.*")|0|0|0|0|
|[driver_examples/dsc_i2c](# "examples\/driver_examples\/dsc_i2c\/.*")|0|0|0|0|
|[driver_examples/dsc_lpi2c](# "examples\/driver_examples\/dsc_lpi2c\/.*")|0|0|0|0|
|[driver_examples/dsc_mscan](# "examples\/driver_examples\/dsc_mscan\/.*")|0|0|0|0|
|[driver_examples/dsc_pdb](# "examples\/driver_examples\/dsc_pdb\/.*")|0|0|0|0|
|[driver_examples/dsc_pit](# "examples\/driver_examples\/dsc_pit\/.*")|0|0|0|0|
|[driver_examples/dsc_pwm](# "examples\/driver_examples\/dsc_pwm\/.*")|0|0|0|0|
|[driver_examples/dsc_qdc](# "examples\/driver_examples\/dsc_qdc\/.*")|0|0|0|0|
|[driver_examples/dsc_qtmr](# "examples\/driver_examples\/dsc_qtmr\/.*")|0|0|0|0|
|[driver_examples/dsc_xbara](# "examples\/driver_examples\/dsc_xbara\/.*")|0|0|0|0|
|[driver_examples/dspi](# "examples\/driver_examples\/dspi\/.*")|0|0|0|0|
|[driver_examples/easrc](# "examples\/driver_examples\/easrc\/.*")|0|0|0|0|
|[driver_examples/ecspi](# "examples\/driver_examples\/ecspi\/.*")|0|0|0|0|
|[driver_examples/edma](# "examples\/driver_examples\/edma\/.*; examples\/_boards\/.*\/driver_examples\/edma\/.*")|0|0|0|0|
|[driver_examples/edma4](# "examples\/driver_examples\/edma4\/.*; examples\/_boards\/.*\/driver_examples\/edma4\/.*; examples\/driver_examples\/edma3\/.*; examples\/_boards\/.*\/driver_examples\/edma3\/.*")|0|0|0|0|
|[driver_examples/edma4_trigger](# "examples\/driver_examples\/edma4\/memory_to_memory_trigger\/.*; examples\/_boards\/.*\/driver_examples\/edma4\/memory_to_memory_trigger\/.*")|0|0|0|0|
|[driver_examples/elcdif](# "examples\/driver_examples\/elcdif\/.*; examples\/_boards\/.*\/driver_examples\/elcdif\/.*")|0|0|0|0|
|[driver_examples/emios](# "examples\/driver_examples\/emios\/.*; examples\/_boards\/.*\/driver_examples\/emios\/.*")|0|0|0|0|
|[driver_examples/enc](# "examples\/driver_examples\/enc\/.*; examples\/_boards\/.*\/driver_examples\/enc\/.*")|0|0|0|0|
|[driver_examples/lpc_enet](# "examples\/driver_examples\/lpc_enet\/.*; examples\/_boards\/lpc.*\/driver_examples\/enet\/.*")|0|0|0|0|
|[driver_examples/mcx_enet](# "examples\/driver_examples\/mcx_enet\/.*; examples\/.*\/.*mcx.*\/driver_examples\/enet\/.*")|0|0|0|0|
|[driver_examples/enet](# "examples\/driver_examples\/enet\/.*; examples\/driver_examples\/enet_1g\/.*; examples\/_boards\/.*\/driver_examples\/enet\/.*; examples\/_boards\/.*\/driver_examples\/enet_1g\/.*")|0|0|0|0|
|[driver_examples/enet_qos](# "examples\/driver_examples\/enet_qos\/.*; examples\/_boards\/.*\/driver_examples\/enet_qos\/.*")|0|0|0|0|
|[driver_examples/netc](# "examples\/driver_examples\/netc\/.*; examples\/_boards\/.*\/driver_examples\/netc\/.*")|0|0|0|0|
|[driver_examples/netc_timer_trigger](# "examples\/driver_examples\/netc\/txrx_transfer_trigger\/.*; examples\/_boards\/.*\/driver_examples\/netc\/txrx_transfer_trigger\/.*")|0|0|0|0|
|[driver_examples/netc_hsr_switch](# "examples\/driver_examples\/netc\/hsr_switch\/.*; examples\/_boards\/.*\/driver_examples\/netc\/hsr_switch\/.*")|0|0|0|0|
|[driver_examples/netc_prp_switch](# "examples\/driver_examples\/netc\/prp_switch\/.*; examples\/_boards\/.*\/driver_examples\/netc\/prp_switch\/.*")|0|0|0|0|
|[driver_examples/eqdc](# "examples\/driver_examples\/eqdc\/.*; examples\/_boards\/.*\/driver_examples\/eqdc\/.*")|0|0|0|0|
|[driver_examples/esai](# "examples\/driver_examples\/esai\/.*; examples\/_boards\/.*\/driver_examples\/esai\/.*")|0|0|0|0|
|[driver_examples/espi](# "examples\/driver_examples\/espi\/.*; examples\/_boards\/.*\/driver_examples\/espi\/.*")|0|0|0|0|
|[driver_examples/evtg](# "examples\/driver_examples\/evtg\/.*; examples\/_boards\/.*\/driver_examples\/evtg\/.*")|0|0|0|0|
|[driver_examples/flexcan](# "examples\/driver_examples\/flexcan\/.*; examples\/_boards\/.*\/driver_examples\/flexcan\/.*; examples\/_boards\/.*\/driver_examples\/canfd\/.*")|0|0|0|0|
|[driver_examples/flexcomm_usart](# "examples\/driver_examples\/flexcomm\/usart\/.*")|0|0|0|0|
|[driver_examples/flexcomm_i2s](# "examples\/driver_examples\/flexcomm\/i2s\/.*; examples\/_boards\/.*\/driver_examples\/flexcomm\/i2s\/.*")|0|0|0|0|
|[driver_examples/flexcomm_spi](# "examples\/driver_examples\/flexcomm\/spi\/.*")|0|0|0|0|
|[driver_examples/flexcomm_i2c](# "examples\/driver_examples\/flexcomm\/i2c\/.*")|0|0|0|0|
|[driver_examples/flexio_i2s](# "examples\/driver_examples\/flexio\/i2s\/.*; examples\/_boards\/.*\/driver_examples\/flexio\/i2s\/.*")|0|0|0|0|
|[driver_examples/flexio_i2c](# "examples\/driver_examples\/flexio\/i2c\/.*")|0|0|0|0|
|[driver_examples/flexio_mculcd](# "examples\/driver_examples\/flexio\/mculcd\/.*; examples\/_boards\/.*\/driver_examples\/flexio\/mculcd\/.*")|0|0|0|0|
|[driver_examples/flexio_spi](# "examples\/driver_examples\/flexio\/spi\/.*")|0|0|0|0|
|[driver_examples/flexio_uart](# "examples\/driver_examples\/flexio\/uart\/.*")|0|0|0|0|
|[driver_examples/flexio_trigger](# "examples\/driver_examples\/flexio\/pwm_trgout\/.*; examples\/driver_examples\/flexio\/pwm_trigger\/.*; examples\/_boards\/.*\/driver_examples\/flexio\/pwm_trgout\/.*; examples\/_boards\/.*\/driver_examples\/flexio\/pwm_trigger\/.*")|0|0|0|0|
|[driver_examples/flexspi](# "examples\/driver_examples\/flexspi\/.*; examples\/_boards\/.*\/driver_examples\/flexspi\/.*")|0|0|0|0|
|[driver_examples/flexspi_flr](# "examples\/driver_examples\/flexspi_flr\/.*; examples\/_boards\/.*\/driver_examples\/flexspi_flr\/.*")|0|0|0|0|
|[driver_examples/fmeas](# "examples\/driver_examples\/fmeas\/.*; examples\/_boards\/.*\/driver_examples\/fmeas\/.*")|0|0|0|0|
|[driver_examples/ftm](# "examples\/driver_examples\/ftm\/.*; examples\/demo_apps\/ftm\/.*; examples\/_boards\/.*\/driver_examples\/ftm\/.*; examples\/_boards\/.*\/demo_apps\/ftm.*")|0|0|0|0|
|[driver_examples/gdma](# "examples\/driver_examples\/gdma\/.*; examples\/_boards\/.*\/driver_examples\/gdma\/.*")|0|0|0|0|
|[driver_examples/gpio](# "examples\/driver_examples\/gpio\/.*; examples\/_boards\/.*\/driver_examples\/gpio\/.*")|0|0|0|0|
|[driver_examples/gpio_1](# "examples\/driver_examples\/gpio_1\/.*; examples\/_boards\/.*\/driver_examples\/gpio_1\/.*")|0|0|0|0|
|[driver_examples/i2c](# "examples\/driver_examples\/i2c\/.*")|0|0|0|0|
|[driver_examples/i3c](# "examples\/driver_examples\/i3c\/.*; examples\/_boards\/.*\/driver_examples\/i3c\/.*")|0|0|0|0|
|[driver_examples/igpio](# "examples\/driver_examples\/igpio\/.*; examples\/_boards\/.*\/driver_examples\/igpio\/.*")|0|0|0|0|
|[driver_examples/ipwm](# "examples\/driver_examples\/ipwm\/.*; examples\/_boards\/.*\/driver_examples\/pwm\/.*")|0|0|0|0|
|[driver_examples/irtc](# "examples\/driver_examples\/irtc\/.*")|0|0|0|0|
|[driver_examples/iuart](# "examples\/driver_examples\/iuart\/.*")|0|0|0|0|
|[driver_examples/jpegdec](# "examples\/driver_examples\/jpegdec\/.*; examples\/_boards\/.*\/driver_examples\/jpegdec\/.*")|0|0|0|0|
|[driver_examples/kbi](# "examples\/driver_examples\/kbi\/.*; examples\/_boards\/.*\/driver_examples\/kbi\/.*")|0|0|0|0|
|[driver_examples/key_manager](# "examples\/driver_examples\/key_manager\/.*; examples\/_boards\/.*\/driver_examples\/key_manager\/.*")|0|0|0|0|
|[driver_examples/kpp](# "examples\/driver_examples\/kpp\/.*; examples\/_boards\/.*\/driver_examples\/kpp\/.*")|0|0|0|0|
|[driver_examples/lcdic](# "examples\/driver_examples\/lcdic\/.*; examples\/_boards\/.*\/driver_examples\/lcdic\/.*")|0|0|0|0|
|[driver_examples/lcdif](# "examples\/driver_examples\/lcdif\/.*; examples\/_boards\/.*\/driver_examples\/lcdif\/.*")|0|0|0|0|
|[driver_examples/lcdifv2](# "examples\/driver_examples\/lcdifv2\/.*; examples\/_boards\/.*\/driver_examples\/lcdifv2\/.*")|0|0|0|0|
|[driver_examples/lcdifv3](# "drivers\/lcdifv3\/.*")|0|0|0|0|
|[driver_examples/lcu](# "examples\/driver_examples\/lcu\/.*; examples\/_boards\/.*\/driver_examples\/lcu\/.*")|0|0|0|0|
|[driver_examples/ldb](# "drivers\/ldb\/.*")|0|0|0|0|
|[driver_examples/lin](# "examples\/demo_apps\/lin_stack\/.*; examples\/_boards\/.*\/demo_apps\/lin_stack\/.*")|0|0|0|0|
|[driver_examples/lpc_dma](# "examples\/driver_examples\/lpc_dma\/.*; examples\/_boards\/.*\/driver_examples\/lpc_dma\/.*")|0|0|0|0|
|[driver_examples/lpc_freqme](# "examples\/driver_examples\/lpc_freqme\/.*; examples\/_boards\/.*\/driver_examples\/freqme\/.*")|0|0|0|0|
|[driver_examples/lpc_gpio](# "examples\/driver_examples\/lpc_gpio\/.*; examples\/_boards\/.*\/driver_examples\/lpc_gpio\/.*")|0|0|0|0|
|[driver_examples/lpc_i2c](# "examples\/driver_examples\/lpc_i2c\/.*")|0|0|0|0|
|[driver_examples/lpc_iocon](# "examples\/driver_examples\/lpc_iocon\/.*; examples\/_boards\/.*\/driver_examples\/lpc_iocon\/.*")|0|0|0|0|
|[driver_examples/lpc_iocon_lite](# "examples\/driver_examples\/lpc_iocon_lite\/.*; examples\/_boards\/.*\/driver_examples\/lpc_iocon_lite\/.*")|0|0|0|0|
|[driver_examples/lpc_iopctl](# "examples\/driver_examples\/lpc_iopctl\/.*; examples\/_boards\/.*\/driver_examples\/lpc_iopctl\/.*")|0|0|0|0|
|[driver_examples/lpc_lcdc](# "examples\/driver_examples\/lpc_lcdc\/.*; examples\/_boards\/.*\/driver_examples\/lpc_lcdc\/.*")|0|0|0|0|
|[driver_examples/lpc_minispi](# "examples\/driver_examples\/lpc_minispi\/.*")|0|0|0|0|
|[driver_examples/lpc_miniusart](# "examples\/driver_examples\/lpc_miniusart\/.*")|0|0|0|0|
|[driver_examples/lpc_rit](# "examples\/driver_examples\/lpc_rit\/.*; examples\/_boards\/.*\/driver_examples\/rit\/.*")|0|0|0|0|
|[driver_examples/lpc_rtc](# "examples\/driver_examples\/lpc_rtc\/.*")|0|0|0|0|
|[driver_examples/lpi2c_trigger](# "examples\/driver_examples\/lpi2c\/polling_trigger\/.*; examples\/_boards\/.*\/driver_examples\/lpi2c\/polling_trigger\/.*")|0|0|0|0|
|[driver_examples/lpi2c_examples](# "examples\/driver_examples\/lpi2c\/.*")|0|0|0|0|
|[driver_examples/lpit_trigger](# "examples\/driver_examples\/lpit\/single_channel_trigger\/.*; examples\/_boards\/.*\/driver_examples\/lpit\/single_channel_trigger\/.*")|0|0|0|0|
|[driver_examples/lpspi](# "examples\/driver_examples\/lpspi\/.*")|0|0|0|0|
|[driver_examples/lpspi_trigger](# "examples\/driver_examples\/lpspi\/interrupt_trigger\/.*; examples\/_boards\/.*\/driver_examples\/lpspi\/interrupt_trigger\/.*")|0|0|0|0|
|[driver_examples/lptmr_trigger](# "examples\/driver_examples\/lptmr\/lptmr_trigger_out\/.*; examples\/_boards\/.*\/driver_examples\/lptmr\/lptmr_trigger_out\/.*")|0|0|0|0|
|[driver_examples/lpuart](# "examples\/driver_examples\/lpuart\/.*")|0|0|0|0|
|[driver_examples/lpuart_trigger](# "examples\/driver_examples\/lpuart\/polling_trigger\/.*; examples\/_boards\/.*\/driver_examples\/lpuart\/polling_trigger\/.*")|0|0|0|0|
|[driver_examples/mailbox](# "examples\/driver_examples\/mailbox\/.*; examples\/.*\/.*\/driver_examples\/mailbox\/.*; ecosystem\/examples\/driver_examples\/mailbox\/.*")|0|0|0|0|
|[driver_examples/mau](# "examples\/driver_examples\/mau\/.*; examples\/.*\/.*\/driver_examples\/mau\/.*; ecosystem\/examples\/driver_examples\/mau\/.*")|0|0|0|0|
|[driver_examples/mcan](# "examples\/driver_examples\/mcan\/.*; examples\/_boards\/.*\/driver_examples\/mcan\/.*")|0|0|0|0|
|[driver_examples/mmu](# "examples\/driver_examples\/mmu\/.*; examples\/_boards\/.*\/driver_examples\/mmu\/.*")|0|0|0|0|
|[driver_examples/mscan](# "examples\/driver_examples\/mscan\/.*; examples\/_boards\/.*\/driver_examples\/mscan\/.*")|0|0|0|0|
|[driver_examples/mu](# "examples\/driver_examples\/mu\/.*; examples\/.*\/.*\/driver_examples\/mu\/.*; ecosystem\/examples\/driver_examples\/mu\/.*")|0|0|0|0|
|[driver_examples/mu1](# "examples\/driver_examples\/mu\/.*; examples\/.*\/.*\/driver_examples\/mu\/.*; ecosystem\/examples\/driver_examples\/mu\/.*")|0|0|0|0|
|[driver_examples/nfc](# "drivers\/nfc\/.*")|0|0|0|0|
|[driver_examples/pdb](# "examples\/driver_examples\/pdb\/.*; examples\/_boards\/.*\/driver_examples\/pdb\/.*")|0|0|0|0|
|[driver_examples/pdm](# "examples\/driver_examples\/pdm\/.*; examples\/_boards\/.*\/driver_examples\/pdm\/.*")|0|0|0|0|
|[driver_examples/pint](# "examples\/driver_examples\/pint\/.*; examples\/_boards\/.*\/driver_examples\/pint\/.*")|0|0|0|0|
|[driver_examples/pngdec](# "examples\/driver_examples\/pngdec\/.*; examples\/_boards\/.*\/driver_examples\/pngdec\/.*")|0|0|0|0|
|[driver_examples/powerquad](# "examples\/driver_examples\/powerquad\/.*; examples\/_boards\/.*\/driver_examples\/powerquad\/.*")|0|0|0|0|
|[driver_examples/pwm](# "examples\/driver_examples\/pwm\/pwm_3ph\/.*; examples\/driver_examples\/pwm\/force_signal\/.*; examples\/driver_examples\/pwm\/index\.rst; examples\/demo_apps\/pwm\/.*; examples\/_boards\/.*\/driver_examples\/pwm\/.*; examples\/_boards\/.*\/demo_apps\/pwm_fault\/.*")|0|0|0|0|
|[driver_examples/pwm_trigger](# "examples\/driver_examples\/pwm\/pwm_trgout\/.*; examples\/driver_examples\/pwm\/pwm_trigger\/.*; examples\/_boards\/.*\/driver_examples\/pwm\/pwm_trgout\/.*; examples\/_boards\/.*\/driver_examples\/pwm\/pwm_trigger\/.*")|0|0|0|0|
|[driver_examples/pwt](# "examples\/driver_examples\/pwt\/.*; examples\/_boards\/.*\/driver_examples\/pwt\/.*")|0|0|0|0|
|[driver_examples/pwt_1](# "examples\/driver_examples\/pwt_1\/.*; examples\/_boards\/.*\/driver_examples\/pwt_1\/.*")|0|0|0|0|
|[driver_examples/pxp](# "examples\/driver_examples\/pxp\/.*; examples\/_boards\/.*\/driver_examples\/pxp\/.*")|0|0|0|0|
|[driver_examples/qdc](# "examples\/driver_examples\/qdc\/.*; examples\/_boards\/.*\/driver_examples\/qdc\/.*")|0|0|0|0|
|[driver_examples/qspi](# "examples\/driver_examples\/qspi\/.*; examples\/_boards\/.*\/driver_examples\/qspi\/.*")|0|0|0|0|
|[driver_examples/qtmr_1](# "examples\/driver_examples\/qtmr_1\/(?!.*(timer_trigger&#124;outputpwm_trigger)$).*$; examples\/_boards\/.*\/driver_examples\/qtmr\/(?!.*(timer_trigger&#124;outputpwm_trigger)$).*$")|0|0|0|0|
|[driver_examples/qtmr_1_trigger](# "examples\/driver_examples\/qtmr_1\/outputpwm_trigger\/.*; examples\/driver_examples\/qtmr_1\/timer_trigger\/.*; examples\/_boards\/.*\/driver_examples\/qtmr_1\/outputpwm_trigger\/.*; examples\/_boards\/.*\/driver_examples\/qtmr_1\/timer_trigger\/.*")|0|0|0|0|
|[driver_examples/qtmr_2](# "examples\/driver_examples\/qtmr_2\/.*; examples\/_boards\/.*\/driver_examples\/qtmr\/.*")|0|0|0|0|
|[driver_examples/rdc](# "examples\/driver_examples\/rdc\/.*; examples\/_boards\/.*\/driver_examples\/rdc\/.*")|0|0|0|0|
|[driver_examples/rgpio](# "examples\/driver_examples\/rgpio\/.*; examples\/_boards\/.*\/driver_examples\/rgpio\/.*")|0|0|0|0|
|[driver_examples/rtc](# "examples\/demo_apps\/rtc\/.*; examples\/driver_examples\/rtc\/.*; examples\/_boards\/.*\/demo_apps\/rtc_func\/.*")|0|0|0|0|
|[driver_examples/rtc_1](# "examples\/driver_examples\/rtc_1\/.*")|0|0|0|0|
|[driver_examples/rtc_jdp](# "examples\/driver_examples\/rtc_jdp\/.*")|0|0|0|0|
|[driver_examples/rtc_analog](# "examples\/driver_examples\/rtc_analog\/.*")|0|0|0|0|
|[driver_examples/sai](# "examples\/driver_examples\/sai\/.*; examples\/_boards\/.*\/driver_examples\/sai\/.*")|0|0|0|0|
|[driver_examples/sar_adc_trigger](# "examples\/driver_examples\/sar_adc\/polling_trgout\/.*; examples\/driver_examples\/sar_adc\/polling_trigger\/.*; examples\/_boards\/.*\/driver_examples\/sar_adc\/polling_trgout\/.*; examples\/_boards\/.*\/driver_examples\/sar_adc\/polling_trigger\/.*")|0|0|0|0|
|[driver_examples/sctimer](# "examples\/driver_examples\/sctimer\/.*; examples\/_boards\/.*\/driver_examples\/sctimer\/.*")|0|0|0|0|
|[driver_examples/sdma](# "examples\/driver_examples\/sdma\/.*; examples\/_boards\/.*\/driver_examples\/sdma\/.*")|0|0|0|0|
|[driver_examples/sema4](# "examples\/driver_examples\/sema4\/.*; examples\/.*\/.*\/driver_examples\/sema4\/.*; ecosystem\/.*\/examples\/.*\/driver_examples\/.*\/sema4\/.*")|0|0|0|0|
|[driver_examples/sema42](# "examples\/driver_examples\/sema42\/.*; examples\/.*\/.*\/driver_examples\/sema42\/.*; ecosystem\/.*\/examples\/.*\/driver_examples\/.*\/sema42\/.*")|0|0|0|0|
|[driver_examples/sinc_trigger](# "examples\/driver_examples\/sinc\/lpspi_sinc_trigger\/.*; examples\/_boards\/.*\/driver_examples\/sinc\/lpspi_sinc_trigger\/.*")|0|0|0|0|
|[driver_examples/slcd](# "examples\/driver_examples\/slcd\/.*; examples\/_boards\/.*\/driver_examples\/slcd\/.*")|0|0|0|0|
|[driver_examples/slcd_split](# "examples\/driver_examples\/slcd_split\/.*; examples\/_boards\/.*\/driver_examples\/slcd_split\/.*")|0|0|0|0|
|[driver_examples/spi](# "examples\/driver_examples\/spi\/.*")|0|0|0|0|
|[driver_examples/sramc](# "examples\/driver_examples\/sramc\/.*")|0|0|0|0|
|[driver_examples/sramctl](# "examples\/driver_examples\/sramctl\/.*")|0|0|0|0|
|[driver_examples/sysctr](# "examples\/driver_examples\/sysctr\/.*; examples\/_boards\/.*\/driver_examples\/sysctr\/.*")|0|0|0|0|
|[driver_examples/tpm](# "examples\/driver_examples\/tpm\/(?!.*timer_trigger$).*$; examples\/_boards\/.*\/driver_examples\/tpm\/(?!.*timer_trigger$).*$")|0|0|0|0|
|[driver_examples/tpm_trigger](# "examples\/driver_examples\/tpm\/timer_trigger\/.*; examples\/_boards\/.*\/driver_examples\/tpm\/timer_trigger\/.*")|0|0|0|0|
|[driver_examples/trdc](# "examples\/driver_examples\/trdc\/flw; examples\/_boards\/.*\/driver_examples\/trdc\/flw; examples\/driver_examples\/trdc\/basic; examples\/_boards\/.*\/driver_examples\/trdc\/basic; examples\/driver_examples\/trdc\/multicore\/primary_core; examples\/_boards\/.*\/driver_examples\/trdc\/multicore\/primary_core")|0|0|0|0|
|[driver_examples/trdc_1](# "examples\/driver_examples\/trdc\/basic; examples\/_boards\/.*\/driver_examples\/trdc\/basic")|0|0|0|0|
|[driver_examples/tsi](# "examples\/driver_examples\/tsi\/.*; examples\/_boards\/.*\/driver_examples\/tsi\/.*")|0|0|0|0|
|[driver_examples/tspc](# "examples\/driver_examples\/tspc\/.*; examples\/_boards\/.*\/driver_examples\/tspc\/.*")|0|0|0|0|
|[driver_examples/uart](# "examples\/driver_examples\/uart\/.*")|0|0|0|0|
|[driver_examples/waketimer](# "examples\/driver_examples\/waketimer\/.*; examples\/_boards\/.*\/driver_examples\/waketimer\/.*")|0|0|0|0|
|[driver_examples/wkt](# "examples\/driver_examples\/wkt\/.*; examples\/_boards\/.*\/driver_examples\/wkt\/.*")|0|0|0|0|
|[driver_examples/wwdt](# "examples\/driver_examples\/wwdt\/.*")|0|0|0|0|
|[driver_examples/xbar](# "examples\/driver_examples\/xbar\/.*; examples\/_boards\/.*\/driver_examples\/xbar\/.*")|0|0|0|0|
|[driver_examples/xbar_1](# "examples\/demo_apps\/xbar\/xbar_aoi\/.*; examples\/_boards\/.*\/demo_apps\/xbar_aoi\/.*")|0|0|0|0|
|[driver_examples/xbara](# "examples\/driver_examples\/xbara\/.*; examples\/demo_apps\/xbar\/xbar_aoi\/.*; examples\/_boards\/.*\/driver_examples\/xbara\/.*; examples\/_boards\/.*\/demo_apps\/xbar_aoi\/.*")|0|0|0|0|
|[driver_examples/xbarb](# "examples\/demo_apps\/xbar\/xbar_aoi\/.*; examples\/_boards\/.*\/demo_apps\/xbar_aoi\/.*")|0|0|0|0|
|[driver_examples/xbic](# "examples\/driver_examples\/xbic\/.*; examples\/_boards\/.*\/driver_examples\/xbic\/.*")|0|0|0|0|
|[driver_examples/xrdc](# "examples\/driver_examples\/xrdc; examples\/_boards\/.*\/driver_examples\/xrdc")|0|0|0|0|
|[driver_examples/xrdc2](# "examples\/driver_examples\/xrdc2; examples\/_boards\/.*\/driver_examples\/xrdc2")|0|0|0|0|
|[driver_examples/xspi](# "examples\/driver_examples\/xspi; examples\/_boards\/.*\/driver_examples\/xspi")|0|0|0|0|
|[driver_examples](# "examples\/.*\/driver_examples\/.*")|0|0|0|0|
|[dsp_examples](# "examples\/.*\/dsp_examples\/.*; examples\/dsp_examples\/.*; ecosystem\/.*\/examples\/.*\/dsp_examples\/.*")|0|0|0|0|
|[edgefast_bluetooth_examples/edgefast_coex_rt1060_rt1170](# "examples\/_boards\/evkcmimxrt1060\/edgefast_bluetooth_examples\/a2dp_sink\/.*; examples\/_boards\/evkcmimxrt1060\/edgefast_bluetooth_examples\/a2dp_source\/.*; examples\/_boards\/evkcmimxrt1060\/edgefast_bluetooth_examples\/shell\/.*; examples\/_boards\/evkbmimxrt1170\/edgefast_bluetooth_examples\/shell\/.*; examples\/edgefast_bluetooth_examples\/a2dp_sink\/CMakeLists\.txt; examples\/edgefast_bluetooth_examples\/a2dp_sink\/example\.yml; examples\/edgefast_bluetooth_examples\/a2dp_sink\/main\.c; examples\/edgefast_bluetooth_examples\/a2dp_sink\/prj\.conf; examples\/edgefast_bluetooth_examples\/a2dp_source\/app_shell\.c; examples\/edgefast_bluetooth_examples\/a2dp_source\/app_shell\.h; examples\/edgefast_bluetooth_examples\/a2dp_source\/CMakeLists\.txt; examples\/edgefast_bluetooth_examples\/a2dp_source\/example\.yml; examples\/edgefast_bluetooth_examples\/a2dp_source\/main\.c; examples\/edgefast_bluetooth_examples\/a2dp_source\/prj\.conf; examples\/edgefast_bluetooth_examples\/shell\/.*")|0|0|0|0|
|[edgefast_bluetooth_examples](# "examples\/.*\/edgefast_bluetooth_examples\/.*; examples\/edgefast_bluetooth_examples\/.*")|0|0|0|0|
|[bt_ble_examples](# "examples_int\/.*\/bt_ble_examples\/.*; examples_int\/bt_ble_examples\/.*")|0|0|0|0|
|[coex_examples/coex_wifi_btdm](# "examples\/.*\/coex_examples\/coex_wifi_a2dp_sink\/.*; examples\/coex_examples\/coex_wifi_a2dp_sink\/.*; examples\/.*\/coex_examples\/coex_wifi_a2dp_source\/.*; examples\/coex_examples\/coex_wifi_a2dp_source\/.*")|0|0|0|0|
|[coex_examples](# "middleware\/wireless\/coex\/.*; examples\/.*\/coex_examples\/coex_wifi_edgefast\/.*; examples\/coex_examples\/coex_wifi_edgefast\/.*; examples\/.*\/coex_examples\/coex_wifi_central_ht\/.*; examples\/coex_examples\/coex_wifi_central_ht\/.*; examples\/.*\/coex_examples\/coex_wifi_peripheral_ht\/.*; examples\/coex_examples\/coex_wifi_peripheral_ht\/.*; examples\/.*\/coex_examples\/coex_wifi_ums_open\/.*; examples\/coex_examples\/coex_wifi_ums_open\/.*; examples\/.*\/coex_examples\/coex_wifi_bms_open\/.*; examples\/coex_examples\/coex_wifi_bms_open\/.*; examples\/.*\/coex_examples\/coex_wifi_bmr_open\/.*; examples\/coex_examples\/coex_wifi_bmr_open\/.*; examples\/.*\/coex_examples\/coex_wifi_umr_open\/.*; examples\/coex_examples\/coex_wifi_umr_open\/.*; examples\/.*\/coex_examples\/coex_wifi_edgefast_open\/.*; examples\/coex_examples\/coex_wifi_edgefast_open\/.*")|0|0|0|0|
|[eiq_examples](# "examples\/.*\/eiq_examples\/.*; examples\/eiq_examples\/.*")|0|0|0|0|
|[el2go_examples](# "examples_int\/el2go_examples\/.*; examples\/el2go_examples\/.*")|0|0|0|0|
|[emwin_examples](# "examples_int\/.*\/emwin_examples\/.*; ecosystem\/.*\/examples\/.*\/emwin_examples\/.*")|0|0|0|0|
|[fatfs_examples](# "examples\/.*\/fatfs_examples\/.*; examples\/fatfs_examples\/.*")|0|0|0|0|
|[freemaster_examples](# "examples\/freemaster_examples\/.*; examples\/_boards\/.*\/freemaster_examples\/.*")|0|0|0|0|
|[issdk_examples](# "examples\/.*\/issdk_examples\/.*; examples\/issdk_examples\/.*")|0|0|0|0|
|[littlefs_examples](# "examples\/.*\/littlefs_examples\/.*; examples\/littlefs_examples\/.*")|0|0|0|0|
|[lwip_examples/usb_lwip_examples](# "examples\/.*\/lwip_examples\/lwip_dhcp_usb\/.*; examples\/lwip_examples\/lwip_dhcp_usb\/.*")|0|0|0|0|
|[lwip_examples](# "examples\/.*\/lwip_examples\/.*; examples\/lwip_examples\/.*; examples\/httpsrv_common\/.*; examples\/ipv4_ipv6_echo_common\/.*; examples\/mqtt_common\/.*")|0|0|0|0|
|[digital_encoder_examples/biss_example](# "examples\/.*\/digital_encoder_examples\/biss\/.*; examples\/digital_encoder_examples\/biss\/.*; drivers\/biss\/.*")|0|0|0|0|
|[digital_encoder_examples/Endat2_example](# "examples\/.*\/digital_encoder_examples\/endat2p2\/.*; examples\/digital_encoder_examples\/endat2p2\/.*; drivers\/endat2p2\/.*")|0|0|0|0|
|[digital_encoder_examples/hiperface_example](# "examples\/.*\/digital_encoder_examples\/hiperface\/.*; examples\/digital_encoder_examples\/hiperface\/.*; drivers\/hiperface\/.*")|0|0|0|0|
|[digital_encoder_examples/Endat3_example](# "examples\/.*\/digital_encoder_examples\/endat3\/.*; examples\/digital_encoder_examples\/endat3\/.*; drivers\/endat3\/.*")|0|0|0|0|
|[digital_encoder_examples](# "examples\/.*\/digital_encoder_examples\/.*; examples\/digital_encoder_examples\/.*")|0|0|0|0|
|[all_reset_but_netc_examples/all_reset_but_netc_switch_example](# "examples\/demo_apps\/all_reset_but_netc\/switch\/.*")|0|0|0|0|
|[all_reset_but_netc_examples/all_reset_but_netc_trigger_example](# "examples\/demo_apps\/all_reset_but_netc\/trigger\/.*")|0|0|0|0|
|[all_reset_but_netc_examples](# "examples\/demo_apps\/all_reset_but_netc\/.*")|0|0|0|0|
|[soem_examples](# "examples\/.*\/soem_examples\/.*; examples\/soem_examples\/.*")|0|0|0|0|
|[ecat_examples](# "examples\/.*\/ecat_examples\/.*; examples\/ecat_examples\/.*; drivers\/ecat\/.*")|0|0|0|0|
|[modbus_examples](# "examples\/.*\/modbus_examples\/.*; examples\/modbus_examples\/.*")|0|0|0|0|
|[els_pkc_examples](# "examples\/.*\/els_pkc_examples\/.*; examples\/els_pkc_examples\/.*")|0|0|0|0|
|[ele_hseb_services](# "examples\/ele_hseb\/.*")|0|0|0|0|
|[mbedtls_examples](# "examples\/.*\/mbedtls_examples\/.*; examples\/mbedtls_examples\/.*; examples\/_boards\/.*\/mbedtls3x_examples\/.*")|0|0|0|0|
|[midware_audio_voice_components](# "middleware\/audio_voice\/components\/.*")|0|0|0|0|
|[midware_edgefast_bluetooth](# "middleware\/edgefast_bluetooth\/.*")|0|0|0|0|
|[midware_eiq](# "middleware\/eiq\/.*")|0|0|0|0|
|[midware_eiq_int](# "middleware\/eiq_int\/.*")|0|0|0|0|
|[middleware_wireless/framework](# "middleware\/wireless\/framework\/.*; examples\/frdmmcxw72\/wireless_examples\/linker\/.*; examples\/frdmmcxw71\/wireless_examples\/linker\/.*; examples\/mcxw72evk\/wireless_examples\/linker\/.*")|0|0|0|0|
|[middleware_wireless/ethermind](# "middleware\/wireless\/ethermind\/.*")|0|0|0|0|
|[middleware_wireless/bluetooth](# "middleware\/wireless\/bluetooth\/.*")|0|0|0|0|
|[middleware_wireless/XCVR](# "middleware\/wireless\/XCVR\/.*")|0|0|0|0|
|[middleware_wireless/ble_controller](# "middleware\/wireless\/ble_controller\/.*; middleware\/wireless\/fw_v19_nb\/.*")|0|0|0|0|
|[middleware_wireless/genfsk](# "middleware\/wireless\/genfsk\/.*")|0|0|0|0|
|[middleware_wireless/ieee_802_15_4](# "middleware\/wireless\/ieee-802.15.4\/.*; examples\/wireless_examples\/ieee-802.15.4\/.*; examples/mcxw72evk/wireless_examples\/ieee-802.15.4\/.*; examples/frdmmcxw71/wireless_examples\/ieee-802.15.4\/.*; examples/frdmmcxw72/wireless_examples\/ieee-802.15.4\/.*")|0|0|0|0|
|[midware_fatfs/mmc_disk](# "middleware\/fatfs\/source\/fsl_mmc_disk.*")|0|0|0|0|
|[midware_fatfs/nand_disk](# "middleware\/fatfs\/source\/fsl_nand_disk.*")|0|0|0|0|
|[midware_fatfs/ram_disk](# "middleware\/fatfs\/source\/fsl_ram_disk.*")|0|0|0|0|
|[midware_fatfs/sd_disk](# "middleware\/fatfs\/source\/fsl_sd_disk.*")|0|0|0|0|
|[midware_fatfs/sdspi_disk](# "middleware\/fatfs\/source\/fsl_sdspi_disk.*")|0|0|0|0|
|[midware_fatfs/usb_disk](# "middleware\/fatfs\/source\/fsl_usb_disk.*")|0|0|0|0|
|[midware_freemaster](# "middleware\/freemaster\/.*")|0|0|0|0|
|[midware_freemaster_internal](# "middleware\/freemaster_internal\/.*")|0|0|0|0|
|[midware_issdk](# "middleware\/issdk\/.*")|0|0|0|0|
|[midware_linstack](# "middleware\/lin_stack\/.*")|0|0|0|0|
|[midware_littlefs/mflash](# "middleware\/littlefs\/mflash\/.*")|0|0|0|0|
|[midware_g2d_dpu](# "middleware\/g2d_dpu.*")|0|0|0|0|
|[midware_soem](# "middleware\/soem\/.*")|0|0|0|0|
|[midware_freemodbus](# "middleware\/freemodbus\/.*")|0|0|0|0|
|[midware_canopennode](# "middleware\/canopennode\/.*")|0|0|0|0|
|[midware_maestro](# "middleware\/audio_voice\/maestro\/.*")|0|0|0|0|
|[midware_mbed-crypto](# "middleware\/mbed-crypto\/.*")|0|0|0|0|
|[midware_mbedtls](# "middleware\/mbedtls\/.*")|0|0|0|0|
|[midware_mflash](# "middleware\/mflash\/.*")|0|0|0|0|
|[midware_mmcau](# "middleware\/mmcau\/.*")|0|0|0|0|
|[midware_motor_control](# "middleware\/motor_control\/.*")|0|0|0|0|
|[motor_control_examples](# "examples\/.*\/demo_apps\/mc_pmsm\/.*; examples\/demo_apps\/mc_pmsm\/.*")|0|0|0|0|
|[midware_metering](# "middleware\/metering\/.*")|0|0|0|0|
|[metering_examples](# "examples\/.*\/demo_apps\/meterlib1ph_test\/.*; examples\/demo_apps\/meterlib1ph_test\/.*")|0|0|0|0|
|[midware_multicore/erpc](# "middleware\/multicore\/erpc\/.*")|0|0|0|0|
|[midware_multicore/mcmgr](# "middleware\/multicore\/mcmgr\/.*")|0|0|0|0|
|[midware_multicore/rpmsg](# "middleware\/multicore\/rpmsg-lite\/.*")|0|0|0|0|
|[midware_multicore](# "middleware\/multicore\/.*")|0|0|0|0|
|[midware_ntag_i2c_plus](# "middleware\/ntag_i2c_plus\/.*")|0|0|0|0|
|[midware_nxp_iot_agent_int](# "middleware\/nxp_iot_agent_int\/.*")|0|0|0|0|
|[midware_nxp_iot_agent](# "middleware\/nxp_iot_agent\/.*")|0|0|0|0|
|[midware_rtcesl](# "middleware\/rtcesl\/.*")|0|0|0|0|
|[midware_sdmmc](# "middleware\/sdmmc\/.*")|0|0|0|0|
|[midware_se_hostlib](# "middleware\/se_hostlib\/.*")|0|0|0|0|
|[midware_secure-subsystem](# "middleware\/secure-subsystem\/.*")|0|0|0|0|
|[midware_touch](# "middleware\/touch\/.*")|0|0|0|0|
|[touch_examples](# "examples\/.*\/demo_apps\/touch_sensing\/.*; examples\/demo_apps\/touch_sensing\/.*; examples\/.*\/demo_apps\/touch_haptic\/.*; examples\/demo_apps\/touch_haptic\/.*")|0|0|0|0|
|[midware_usb](# "middleware\/usb\/.*; ecosystem\/middleware\/usb\/.*")|0|0|0|0|
|[midware_voice_seeker](# "middleware\/audio_voice\/components\/voice_seeker\/.*")|0|0|0|0|
|[midware_voice_spot](# "middleware\/audio_voice\/components\/voice_spot\/.*")|0|0|0|0|
|[midware_vit](# "middleware\/audio_voice\/components\/vit\/.*")|0|0|0|0|
|[midware_wifi](# "middleware\/wifi_nxp\/.*")|0|0|0|0|
|[mmcau_examples](# "examples\/.*\/mmcau_examples\/.*; examples\/mmcau_examples\/.*")|0|0|0|0|
|[multicore_examples/rpmsg_lite_pingpong_rtos_linux](# "examples\/multicore_examples\/rpmsg_lite_pingpong_rtos_linux\/.*")|0|0|0|0|
|[multicore_examples/rpmsg_lite_pingpong_rtos_no_mcmgr](# "examples\/multicore_examples\/rpmsg_lite_pingpong_rtos_no_mcmgr\/.*")|0|0|0|0|
|[multicore_examples/rpmsg_lite_str_echo_rtos](# "examples\/multicore_examples\/rpmsg_lite_str_echo_rtos\/.*")|0|0|0|0|
|[multicore_examples](# "examples\/multicore_examples\/.*; examples\/_boards\/.*\/multicore_examples\/.*; examples_int\/multicore_examples\/.*; examples_int\/_boards\/.*\/multicore_examples\/.*; ecosystem\/examples\/multicore_examples\/.*; ecosystem\/examples\/_boards\/mcxw72evk\/examples.yml; ecosystem\/examples\/_boards\/kw47evk\/examples.yml")|0|0|0|0|
|[multiprocessor_examples](# "examples_int\/multiprocessor_examples\/.*; examples_int\/_boards\/.*\/multiprocessor_examples\/.*; ecosystem\/examples\/multiprocessor_examples\/.*")|0|0|0|0|
|[rtos_amazon_freertos/freertos_nxp](# "rtos\/freertos\/freertos-kernel\/.*")|0|0|0|0|
|[freertos_examples](# "examples\/freertos_examples\/.*; examples\/_boards/.*\/freertos_examples\/.*; examples\/_common\/project_segments\/freertos\/.*")|0|0|0|0|
|[freertos-drivers](# "rtos\/freertos\/freertos-drivers\/.*")|0|0|0|0|
|[freertos_driver_examples](# "examples\/freertos_driver_examples\/.*; examples\/_boards\/.*\/freertos_driver_examples\/.*; examples_int\/freertos_driver_examples\/.*; examples_int\/_boards\/.*\/freertos_driver_examples\/.*; ecosystem\/examples\/freertos_driver_examples\/.*")|0|0|0|0|
|[sdmmc_examples](# "examples\/.*\/sdmmc_examples\/.*; examples\/sdmmc_examples\/.*")|0|0|0|0|
|[se_hostlib_examples](# "examples_int\/.*\/se_hostlib_examples\/.*; ecosystem\/.*\/examples\/.*\/se_hostlib_examples\/.*")|0|0|0|0|
|[secure-subsystem_examples](# "examples\/.*\/secure-subsystem_examples\/.*; examples\/secure-subsystem_examples\/.*")|0|0|0|0|
|[tfm_examples](# "examples\/tfm_examples\/.*; examples\/_boards\/.*\/lib_example\/.*")|0|0|0|0|
|[trustzone_examples](# "examples\/trustzone_examples\/.*; examples\/_boards\/.*\/trustzone_examples\/.*")|0|0|0|0|
|[edgelock_firmware](# "firmware\/edgelock\/.*")|0|0|0|0|
|[usb_examples](# "examples\/.*\/usb_examples\/.*; examples\/usb_examples\/.*; ecosystem\/.*\/usb_examples\/.*")|0|0|0|0|
|[wifi_cypress_examples](# "examples\/.*\/wifi_cypress_examples\/.*; examples\/wifi_cypress_examples\/.*")|0|0|0|0|
|[wifi_examples/wifi_coex_rt1060_rt1170](# "examples\/wifi_examples\/wifi_cli\/.*; examples\/wifi_examples\/wifi_wpa_supplicant\/.*; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/app_config\/app_config\.h; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/linker\/MIMXRT1062xxxxx_flexspi_nor\.ld; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/linkscripts\/.*; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/app\.h; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/hardware_init\.c; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/common\/pin_mux\.[ch]; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/wifi_cli\/.*; examples\/_boards\/evkcmimxrt1060\/wifi_examples\/wifi_wpa_supplicant\/.*; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/app_config\/app_config\.h; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/cm7\/app\.h; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/cm7\/hardware_init\.c; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/linker\/MIMXRT1176xxxxx_cm7_flexspi_nor\.ld; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/linkscripts\/.*; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/common\/pin_mux\.[ch]; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/wifi_cli\/.*; examples\/_boards\/evkbmimxrt1170\/wifi_examples\/wifi_wpa_supplicant\/.*")|0|0|0|0|
|[wifi_examples](# "examples\/.*\/wifi_examples\/.*; examples\/wifi_examples\/.*")|0|0|0|0|
|[ncp_examples](# "examples\/.*\/ncp_examples\/.*; examples\/ncp_examples\/.*")|0|0|0|0|
|[ota_examples](# "examples\/.*\/ota_examples\/.*; examples\/ota_examples\/.*")|0|0|0|0|
|[riscv](# "arch\/riscv\/.*")|0|0|0|0|
|[midware_wpa_supplicant-rtos/nxp_custom](# "middleware\/wireless\/wpa_supplicant-rtos\/freertos\/.*; middleware\/wireless\/wpa_supplicant-rtos\/port\/mbedtls\/.*; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/block_alloc\.h; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/block_alloc\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/drivers\/driver_wifi_nxp\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/crc32\.h; middleware\/wireless\/wpa_supplicant-rtos\/src\/utils\/crc32\.c; middleware\/wireless\/wpa_supplicant-rtos\/src\/drivers\/driver\.h")|0|0|0|0|
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
|[demo_apps/frdmmcxc242](# "examples\/_boards\/frdmmcxc242\/demo_apps\/.*")|0|0|0|0|
|[demo_apps/frdmmcxc041](# "examples\/_boards\/frdmmcxc242\/demo_apps\/.*")|0|0|0|0|
|[demo_apps/frdmmcxc444](# "examples\/_boards\/frdmmcxc242\/demo_apps\/.*")|0|0|0|0|
|[demo_apps/frdmmcxl255](# "examples.*\/_boards\/frdmmcxl255\/demo_apps\/.*")|0|0|0|0|
|[demo_apps/hello_world](# "examples\/.*\/hello_world\/.*")|0|0|0|0|
|[demo_apps/hello_world_swo](# "examples\/.*\/hello_world_swo\/.*")|0|0|0|0|
|[demo_apps/shell](# "examples\/_boards\/.*\/demo_apps\/shell\/.*")|0|0|0|0|
|[demo_apps/sai](# "examples\/demo_apps\/sai\/.*")|0|0|0|0|
|[demo_apps/tee_fault](# "examples\/demo_apps\/tee_fault\/.*")|0|0|0|0|
|[demo_apps/power_manager](# "examples\/demo_apps\/power_manager\/.*; examples\/demo_apps\/power_manager_lpc\/.*; examples\/demo_apps\/power_manager_lpc_xip\/.*; examples\/demo_apps\/power_manager_test\/.*")|0|0|0|0|
|[demo_apps/power_mode_switch](# "examples\/demo_apps\/power_mode_switch\/.*; examples\/demo_apps\/power_mode_switch_k4\/.*; examples\/demo_apps\/power_mode_switch_lpc\/.*; examples\/demo_apps\/power_mode_switch_lpc_1\/.*")|0|0|0|0|
|[demo_apps/power_mode_switch_mcxw23](# "examples\/demo_apps\/power_mode_switch_mcxw23\/.*")|0|0|0|0|
|[demo_apps/power_mode_switch_rt1xxx](# "examples\/demo_apps\/power_mode_switch_rt10xx\/.*; examples\/demo_apps\/power_mode_switch_rt1xxx\/.*")|0|0|0|0|
|[demo_apps/power_mode_switch_rt7xx](# "examples\/demo_apps\/power_mode_comp_only\/.*; examples\/demo_apps\/power_mode_switch_dualcore\/.*; examples\/demo_apps\/power_mode_with_hifi\/.*")|0|0|0|0|
|[demo_apps/dvs_pvt_with_hifi](# "examples\/demo_apps\/dvs_pvt_with_hifi\/.*")|0|0|0|0|
|[demo_apps/dvs_pvt_comp_only_ml_method](# "examples\/demo_apps\/dvs_pvt_comp_only_ml_method\/.*")|0|0|0|0|
|[demo_apps/power_mode_switch_imx](# "examples\/demo_apps\/power_mode_switch_imx8ulp\/.*; examples\/demo_apps\/power_mode_switch_imx93\/.*; examples\/demo_apps\/power_mode_switch_imx943\/.*; examples\/demo_apps\/power_mode_switch_imx95\/.*")|0|0|0|0|
|[demo_apps/netc_share](# "examples\/demo_apps\/netc_share\/.*")|0|0|0|0|
|[demo_apps/netc_switch_standalone](# "examples\/demo_apps\/netc_switch_standalone\/.*")|0|0|0|0|
|[demo_apps/digital_connected_cluster](# "examples\/demo_apps\/digital_connected_cluster\/.*")|0|0|0|0|
|[demo_apps/coremark_eembc](# "examples\/.*\/coremark_eembc\/.*")|0|0|0|0|
|[demo_apps](# "examples\/.*\/demo_apps\/.*; examples\/demo_apps\/.*")|0|0|0|0|
|[boards/frdmmcxa344](# "examples\/_boards\/frdmmcxa344\/.*")|0|0|0|0|
|[boards/mimxrt700evk](# "examples\/_boards\/mimxrt700evk\/.*")|0|0|0|0|
|[boards](# "examples\/_boards\/.*")|0|0|0|0|
|[sgi_pkc_examples](# "examples\/sgi_pkc_examples\/.*")|0|0|0|0|
|[bluetooth_examples](# "examples\/wireless_examples\/bluetooth.*; examples\/_boards\/[^\/]*\/wireless_examples\/bluetooth.*; examples_int\/wireless_examples\/bluetooth.*; examples_int\/_boards\/[^\/]*\/wireless_examples\/bluetooth.*")|0|0|0|0|
|[ble_examples](# "examples\/wireless_examples\/genfsk.*; examples\/wireless_examples\/ble_controller.*; examples\/_boards\/[^\/]*\/wireless_examples\/ble_controller.*; examples_int\/wireless_examples\/ble_controller.*; examples_int\/unit_tests\/ble_controller.*; examples_int\/_boards\/[^\/]*\/wireless_examples\/ble_controller.*; components\/lce.*")|0|0|0|0|
|[wireless_ref](# "examples\/wireless_examples\/reference_design.*; examples\/_boards\/[^\/]*\/wireless_examples\/reference_design.*; examples_int\/wireless_examples\/reference_design.*; examples_int\/_boards\/[^\/]*\/wireless_examples\/reference_design.*")|0|0|0|0|
|[wireless_15_4](# "examples\/wireless_examples\/ieee.802.15.4.*; examples\/_boards\/[^\/]*\/wireless_examples\/ieee.802.15.4.*; examples_int\/wireless_examples\/ieee.802.15.4.*")|0|0|0|0|
|[wireless_unsort](# "examples\/wireless_examples.*; examples\/_boards\/[^\/]*\/wireless_examples.*; examples_int\/wireless_examples.*; examples_int\/_boards\/[^\/]*\/wireless_examples.*; components\/sensor\/tmp117.*")|0|0|0|0|
|[stec_examples](# "examples\/mbedtls3x_examples.*; examples\/_boards\/[^\/]*\/mbedtls3x_examples.*; examples_int\/mbedtls3x_examples.*; examples_int\/_boards\/[^\/]*\/mbedtls3x_examples.*; examples/driver_examples/itrc.*; examples/driver_examples/glikey.*; examples/driver_examples/prince_rom.*; middleware\/mbedtls3x.*; .*\/npx.*; .*\/puf_v3.*; .*\/iee\/.*; .*\/iped.*; .*\/el2go_examples\/.*; .*\/sgi_pkc_examples\/.*")|0|0|0|0|
|[czech_unsort](# "examples.*\/cmsis_driver_examples.*; components\/flash\/mflash.*; components\/aws_iot.*; components\/eeprom_emulation_k4.*; middleware\/audio_voice.*; examples.*\/driver_examples\/eeprom_emulation_k4.*; examples.*\/driver_examples\/flexio3.*; examples.*\/driver_examples\/pdm.*; examples.*\/driver_examples\/spdif.*; examples.*\/demo_apps\/sai_.*")|0|0|0|0|
|[mpunpi_unsort](# "examples\/driver_examples\/xecc.*; examples\/_boards\/[^\/]*\/driver_examples\/xecc.*")|0|0|0|0|
|[mcunpi_unsort](# "examples\/demo_apps\/power_mode_switch.*; .*\/platformlib.*; .*\/.?led_blinky.*; .*\/new_project.*; examples\/demo_apps\/hello_world.*; examples\/demo_apps\/bubble.*")|0|0|0|0|
|[rom_unsort](# "examples\/bootloader_examples.*; examples\/_boards\/[^\/]*\/bootloader_examples.*")|0|0|0|0|
|[swlib_unsort](# ".*\/mc_.*; .*\/meterlib.*")|0|0|0|0|
|[components/sbom](# "components\/SBOM\.spdx\.json")|0|0|0|0|
|[components/adp5585](# "components\/expander\/adp5585\/.*")|0|0|0|0|
|[components/assert](# "components\/assert\/.*")|0|0|0|0|
|[components/audio](# "components\/audio\/.*")|0|0|0|0|
|[components/aws_iot](# "components\/aws_iot\/.*")|0|0|0|0|
|[components/button](# "components\/button\/.*")|0|0|0|0|
|[components/clock](# "components\/clock\/.*")|0|0|0|0|
|[components/cmsis_drivers_dspi](# "components\/cmsis_drivers\/cmsis_dspi\/.*; examples\/.*\/cmsis_driver_examples\/dspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_ecspi](# "components\/cmsis_drivers\/cmsis_ecspi\/.*; examples\/.*\/cmsis_driver_examples\/ecspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_enet](# "components\/cmsis_drivers\/cmsis_enet\/.*; examples\/.*\/cmsis_driver_examples\/enet\/.*; components\/cmsis_drivers\/cmsis_enet_phy\/.*; components\/cmsis_drivers\/cmsis_mcx_enet\/.*")|0|0|0|0|
|[components/cmsis_drivers_flash](# "components\/cmsis_drivers\/cmsis_flash\/.*; components\/cmsis_drivers\/cmsis_mcx_flash\/.*; examples\/.*\/cmsis_driver_examples\/flash\/.*")|0|0|0|0|
|[components/cmsis_drivers_flexcomm](# "components\/cmsis_drivers\/cmsis_flexcomm\/.*; examples\/.*\/cmsis_driver_examples\/usart\/.*")|0|0|0|0|
|[components/cmsis_drivers_gpio](# "components\/cmsis_drivers\/cmsis_gpio\/.*; components\/cmsis_drivers\/cmsis_lpc_gpio\/.*; examples\/.*\/cmsis_driver_examples\/gpio\/.*")|0|0|0|0|
|[components/cmsis_drivers_i2c](# "components\/cmsis_drivers\/cmsis_i2c\/.*; examples\/.*\/cmsis_driver_examples\/i2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_ii2c](# "components\/cmsis_drivers\/cmsis_ii2c\/.*; examples\/.*\/cmsis_driver_examples\/ii2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_iuart](# "components\/cmsis_drivers\/cmsis_iuart\/.*; examples\/.*\/cmsis_driver_examples\/iuart\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpc_i2c](# "components\/cmsis_drivers\/cmsis_lpc_i2c\/.*; examples\/.*\/cmsis_driver_examples\/lpc_i2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpc_vspi](# "components\/cmsis_drivers\/cmsis_lpc_vspi\/.*; examples\/.*\/cmsis_driver_examples\/lpc_vspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpi2c](# "components\/cmsis_drivers\/cmsis_lpi2c\/.*; examples\/.*\/cmsis_driver_examples\/lpi2c\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpspi](# "components\/cmsis_drivers\/cmsis_lpspi\/.*; examples\/.*\/cmsis_driver_examples\/lpspi\/.*")|0|0|0|0|
|[components/cmsis_drivers_lpuart](# "components\/cmsis_drivers\/cmsis_lpuart\/.*; examples\/.*\/cmsis_driver_examples\/lpuart\/.*")|0|0|0|0|
|[components/cmsis_drivers_spi](# "components\/cmsis_drivers\/cmsis_spi\/.*; examples\/.*\/cmsis_driver_examples\/spi\/.*")|0|0|0|0|
|[components/cmsis_drivers_uart](# "components\/cmsis_drivers\/cmsis_uart\/.*; examples\/.*\/cmsis_driver_examples\/uart\/.*")|0|0|0|0|
|[components/cmsis_drivers_prj_conf](# "examples\/_boards\/.*\/cmsis_driver_examples\/prj.conf")|0|0|0|0|
|[components/codec](# "components\/codec\/.*")|0|0|0|0|
|[components/common_task](# "components\/common_task\/.*")|0|0|0|0|
|[components/conn_fwloader](# "components\/conn_fwloader\/.*")|0|0|0|0|
|[components/crc](# "components\/crc\/.*")|0|0|0|0|
|[components/debug_console](# "components\/debug_console\/.*")|0|0|0|0|
|[components/debug_console_lite](# "components\/debug_console_lite\/.*")|0|0|0|0|
|[components/debug_console_rtt](# "components\/debug_console_rtt\/.*")|0|0|0|0|
|[components/display](# "components\/display\/.*")|0|0|0|0|
|[components/touch](# "components\/touch\/.*")|0|0|0|0|
|[components/camera](# "components\/video\/camera\/.*")|0|0|0|0|
|[components/video](# "components\/video\/.*")|0|0|0|0|
|[components/edgefast_wifi](# "components\/edgefast_wifi\/.*")|0|0|0|0|
|[components/ele_base_api](# "components\/ele_base_api\/.*")|0|0|0|0|
|[components/ele_crypto](# "components\/ele_crypto\/.*; examples\/ele_crypto\/.*")|0|0|0|0|
|[components/ele_hseb](# "components\/ele_hseb\/.*")|0|0|0|0|
|[components/crypto_benchmark](# "components\/crypto_benchmark\/.*")|0|0|0|0|
|[components/exception_handling](# "components\/exception_handling\/.*")|0|0|0|0|
|[components/expander](# "components\/expander\/.*; examples\/component_examples\/io_expander\/interrupt_demo\/.*")|0|0|0|0|
|[components/flash_nand_semc](# "components\/flash\/nand\/semc\/.*; examples\/demo_apps\/nand_flash_management\/semc\/.*; examples\/component_examples\/flash_component\/nand\/semc\/.*; examples\/_boards\/.*\/demo_apps\/nand_flash_management\/semc\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/nand\/semc\/.*; examples\/_boards\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/component_examples\/flash_component\/nand\/semc\/?.*")|0|0|0|0|
|[components/flash_nand_flexspi](# "components\/flash\/nand\/flexspi\/.*; examples\/component_examples\/flash_component\/nand\/flexspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/flexspi_nand\/.*; examples\/.*\/component_examples\/flash_component\/flexspi_nand\/.*; examples\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/.*\/component_examples\/flash_component\/nand\/flexspi\/.*")|0|0|0|0|
|[components/flash_nand_xspi](# "components\/flash\/nand\/xspi\/.*; examples\/component_examples\/flash_component\/nand\/xspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/xspi_nand\/.*; examples\/demo_apps\/nand_flash_management\/xspi\/.*; examples\/_boards\/.*\/demo_apps\/nand_flash_management\/xspi\/.*")|0|0|0|0|
|[components/flash_nor_flexspi](# "components\/flash\/nor\/flexspi\/.*; examples\/component_examples\/flash_component\/nor\/flexspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/flexspi_nor\/.*; examples\/.*\/component_examples\/flash_component\/flexspi_nor\/.*; examples\/.*\/component_examples\/flash_component(?:[\\/][^\\/]+)+[\\/]?; examples\/.*\/component_examples\/flash_component\/nor\/flexspi\/.*; examples\/component_examples\/flash_component\/nor\/flexspi\/?.*")|0|0|0|0|
|[components/flash_nor_lpspi](# "components\/flash\/nor\/lpspi\/.*; examples\/component_examples\/flash_component\/nor\/lpspi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/lpspi_nor\/.*; examples\/.*\/component_examples\/flash_component\/lpspi_nor\/.*")|0|0|0|0|
|[components/flash_nor_xspi](# "components\/flash\/nor\/xspi\/.*; components\/flash\/nor\/fsl_sfdp_parser.*; examples\/component_examples\/flash_component\/octal\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/[^\/]*octal[^\/]*\/.*")|0|0|0|0|
|[components/flash_nor_spifi](# "components\/flash\/nor\/spifi\/.*; examples\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/spifi_nor\/.*; examples\/_boards\/.*\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/.*\/component_examples\/flash_component\/spifi_nor\/.*; examples\/.*\/component_examples\/flash_component\/nor\/spifi\/.*; examples\/component_examples\/flash_component\/nor\/spifi\/?.*")|0|0|0|0|
|[components/format](# "components\/format\/.*")|0|0|0|0|
|[components/gpio](# "components\/gpio\/.*")|0|0|0|0|
|[components/i2c](# "components\/i2c\/.*")|0|0|0|0|
|[components/i3c_bus](# "components\/i3c_bus\/.*; examples\/_boards\/.*\/component_examples\/i3c_bus\/.*; examples\/component_examples\/i3c_bus\/.*")|0|0|0|0|
|[components/imu_adapter](# "components\/imu_adapter\/.*")|0|0|0|0|
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
|[components/phy](# "components\/phy\/.*")|0|0|0|0|
|[components/pinctrl](# "components\/pinctrl\/.*")|0|0|0|0|
|[components/pmic_pf5020](# "components\/pmic\/pf5020\/.*")|0|0|0|0|
|[components/pmic_pf3000](# "components\/pmic\/pf3000\/.*")|0|0|0|0|
|[components/pmic_pf1550](# "components\/pmic\/pf1550\/.*")|0|0|0|0|
|[components/pmic_pca9422](# "components\/pmic\/pca9422\/.*")|0|0|0|0|
|[components/pmic_pca9420](# "components\/pmic\/pca9420\/.*")|0|0|0|0|
|[components/power](# "components\/power\/.*")|0|0|0|0|
|[components/power_manager](# "components\/power_manager\/.*; examples\/demo_apps\/(power_manager(_[a-zA-Z0-9]*)?)\/.*; examples\/_boards\/.*\/demo_apps\/(power_manager(_[a-zA-Z0-9]*)?)\/.*")|0|0|0|0|
|[components/psa_crypto_driver](# "components\/psa_crypto_driver\/.*")|0|0|0|0|
|[components/pwm](# "components\/pwm\/.*")|0|0|0|0|
|[components/reset](# "components\/reset\/.*")|0|0|0|0|
|[components/reset1](# "components\/reset\/.*")|0|0|0|0|
|[components/rng](# "components\/rng\/.*")|0|0|0|0|
|[components/rpmsg](# "components\/rpmsg\/.*")|0|0|0|0|
|[components/rtc](# "components\/rtc\/.*")|0|0|0|0|
|[components/rtt](# "components\/rtt\/.*")|0|0|0|0|
|[components/scmi](# "components\/scmi\/.*")|0|0|0|0|
|[components/sdu](# "components\/sdu\/.*")|0|0|0|0|
|[components/sensor_fxls8974cf](# "components\/sensor\/fxls8974cf\/.*")|0|0|0|0|
|[components/sensor_fxos8700cq](# "components\/sensor\/fxos8700cq\/.*")|0|0|0|0|
|[components/sensor_icm42688p](# "components\/sensor\/icm42688p\/.*")|0|0|0|0|
|[components/sensor_p3t1755](# "components\/sensor\/p3t1755\/.*; examples\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*; examples\/_boards\/.*\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*; boards/.*\/driver_examples\/i3c\/master_read_sensor_p3t1755\/.*")|0|0|0|0|
|[components/sensor_lsm6dso](# "components\/sensor\/lsm6dso\/.*")|0|0|0|0|
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
|[components/srtm](# "components\/srtm\/.*")|0|0|0|0|
|[components/str](# "components\/str\/.*")|0|0|0|0|
|[components/sx1502](# "components\/sx1502\/.*; examples\/component_examples\/sx1502_led_control\/.*; examples\/_boards\/.*\/component_examples\/sx1502_led_control\/.*; boards\/.*\/component_examples\/sx1502_led_control\/.*")|0|0|0|0|
|[components/systick_timer](# "components\/systick_timer\/.*")|0|0|0|0|
|[components/time_stamp](# "components\/time_stamp\/.*")|0|0|0|0|
|[components/timer](# "components\/timer\/.*")|0|0|0|0|
|[components/timer_manager](# "components\/timer_manager\/.*")|0|0|0|0|
|[components/uart](# "components\/uart\/.*")|0|0|0|0|
|[components/memfault_integration](# "components\/debug\/memfault\/sdk_port\/.*; components\/debug\/memfault\/Kconfig; components\/debug\/memfault\/CMakeLists.txt")|0|0|0|0|
|[components/unity](# "components\/unity\/.*")|0|0|0|0|
|[components/wifi_bt_module](# "components\/wifi_bt_module\/.*")|0|0|0|0|
|[components/coredump](# "components\/debug\/coredump\/.*; examples\/component_examples\/coredump_fault\/.*; examples\/_boards\/.*\/component_examples\/coredump_fault\/.*")|0|0|0|0|
|[components/gen_hal](# "components\/gen_hal\/.*")|0|0|0|0|
|[components](# "components\/.*")|0|0|0|0|
|[examples_int/platformlib](# "(^&#124;^\\&#124;^\/)examples_int\/platformlib\/.*")|0|0|0|0|
|[examples_int/coremark](# "examples_int\/.*\/coremark\/.*")|0|0|0|0|
|[examples_int](# "examples_int\/.*")|0|0|0|0|

