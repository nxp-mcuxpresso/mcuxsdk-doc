# Setup -- armgcc + J-Link

## Build

Run `west build` with any of the seven supported targets:

```
west build -p always -b mimxrt2660evk <example_path> \
     --toolchain armgcc --config <target>
```

Replace `<target>` with one of:

| Target | Build configs |
|---|---|
| debug | `debug` / `release` |
| xspi_nor | `xspi_nor_debug` / `xspi_nor_release` |
| xspi_nor_psram | `xspi_nor_psram_debug` / `xspi_nor_psram_release` |
| psram | `psram_debug` / `psram_release` |
| psram_txt | `psram_txt_debug` / `psram_txt_release` |
| ram_only | `ram_only_debug` / `ram_only_release` |
| psram_only | `psram_only_debug` / `psram_only_release` |

Output: standard `.elf`.

## Debug in Ozone with an armgcc ELF

Take the `.elf` to Ozone and follow the Ozone setup page in this guide.
