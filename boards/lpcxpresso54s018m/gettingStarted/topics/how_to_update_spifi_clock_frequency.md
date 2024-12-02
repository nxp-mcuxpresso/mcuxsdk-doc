# How to update SPIFI clock Frequency

The SPIFI clock frequency is defined in the header, offset 0x1C. [Table 1](how_to_update_spifi_clock_frequency.md#SPISPIFICLOCKSPEED) lists the SPIFI serial clock frequencies that are supported. So SPIFI clock frequency can be set to 24 MHz, 32 MHz, 48 MHz, and 96 MHz.

**Note:** If header sets SPIFI clock frequency to zero, the serial clock defaults to 24 MHz. And this setting affects both SPI boot or SPIFI boot clock. For SPIFI, the clock and other configuration settings are retained after boot unless modified by the application program.

|Header SPI/SPIFI clock frequency value|SPI/SPIFI clock speed|
|--------------------------------------|---------------------|
|< 24000000 \(SPI only\)|12000000 \(SPI only\)|
|< 32000000|24000000|
|< 48000000|32000000|
|< 96000000|48000000|
|\>= 96000000|96000000|

The default SPIFI clock frequency is 24 MHz and the corresponding settings is `IMG_BAUDRATE=0`. To change SPIFI clock frequency, just need to add the setting of `IMG_BAUDRATE=X` \(X=24000000, 32000000, 48000000 or 96000000\) in IDEs. The macro of `IMG_BAUDRATE` is also defined in the `startup_LPC54xx.s` \(`.c`,`.cpp`\) file.

The following section takes 96 MHz as an example to introduce how to change SPIFI clock frequency in each IDE.


```{include} ../topics/updating_spifi_clock_frequency_in_iar.md
:heading-offset: 1
```

```{include} ../topics/updating_spifi_clock_frequency_in_keil__mdk_vision.md
:heading-offset: 1
```

```{include} ../topics/updating_spifi_clock_frequency_in_arm__gcc.md
:heading-offset: 1
```

```{include} ../topics/updating_spifi_clock_frequency_in_mcuxpresso_ide.md
:heading-offset: 1
```

