# Connectivity framework

The Connectivity Framework is a software component that provides hardware abstraction modules to the upper layer connectivity stacks and components. It also provides a list of services and APIs (see *Supported services*). The Connectivity Framework modules are located in the *middleware\\wireless\\framework SDK* folder.

## Supported services

- **FSCI** - Framework Serial Communication Interface
- **FunctionLib** - Common function library utilities
- **HWParameter** - Hardware parameter management
- **LowPower** - Low power mode management
- **ModuleInfo** - Module information and versioning
- **NVS** - Non-Volatile Storage
- **NVM** - Non-Volatile Memory management
- **OtaSupport** - Over-The-Air update support
- **SecLib_RNG** - Security library and Random Number Generator
- **Sensors** - Sensor abstraction layer
- **SFC** - Smart Frequency Calibration
- **WorkQ** - Work queue management

## Supported platform

- **KW45_MCXW71**
- **KW47_MCXW72**
- **MCXW23**
- **RW61X**
- **RT1060** and **RT1170**
- **i.MX RT595s**

## Advanced features supported on platforms

### KW45_MCXW71

 - FRO32K with smart frequency calibration (see SFC)
 - Power down mode support (for evaluation only)

### KW47_MCXW72

 - FRO32K with smart frequency calibration (see SFC)
 - Power down mode support (for evaluation only)
 - Crystal 32M trimming with temperature
 - Debug module for NBU
 - Extended NBU support with SecLib and pseudo RNG support