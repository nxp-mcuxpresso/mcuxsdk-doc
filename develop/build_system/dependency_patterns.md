# Dependency Patterns

Here are frequently used dependency patterns.

- Pattern1: start with allOf, with one level anyOf and not

  ```yaml
  componentA:
    allOf:
      - component1
      - component2
      - anyOf:
        - component3
        - component4
      - anyOf:
        - component5
        - component6
      - not: 
          device:
          - MK64F12
          - MK63F12
  ```

  The recommended dependency patterns for this.

  ```bash
      config MCUX_COMPONENT_componentA
          bool "Component A, pattern 1"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on !MCUX_HW_DEVICE_MK64F12 && !MCUX_HW_DEVICE_MK63F12 # not
          choice
              prompt "Component A anyOf1"
              default MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_1
              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_1
                  bool "Select component3"
                  select MCUX_COMPONENT_component3

              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_2
                  bool "Select component4"
                  select MCUX_COMPONENT_component4
          endchoice  
          choice
              prompt "Component A anyOf2"
              default MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_3
              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_3
                  bool "Select component5"
                  select MCUX_COMPONENT_component5

              config MCUX_DEPENDENCY_COMPONENT_componentA_DEPEND_ANYOF_4
                  bool "Select component6"
                  select MCUX_COMPONENT_component6
          endchoice
  ```

- Pattern 2: start with allOf, with 2 level anyOf/allOf

  ```yaml
  componentB:
    dependency:
      allOf:
      - component1
      - component2
      - compiler:
        - iar
        - mdk
      - anyOf:
          - allOf:
            - component3
            - component4
            - device:
              - MK64F12
              - MK63F12
          - allOf:
            - component5
            - component6
            - device:
              - LPC54005
              - LPC54016
  ```

  The Kconfig dependency pattern is like

  ```bash
      config MCUX_COMPONENT_componentB
          bool "Component B, pattern 2 choise"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on MCUX_COMPILER_IAR || MCUX_COMPILER_MDK
          # All device scope shall be explicitly specified here, otherwise for a device which is not in the scope which means the dependency is not satisfied, but componentC is still showed and configurable
          depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12 || MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016

          if MCUX_COMPONENT_componentB
              choice
                  prompt "ComponentB anyOf"
                  default MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_1
                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_1
                      bool "Select component3 and component 4 in device MK64F12, MK63F12"
                      select MCUX_COMPONENT_component3
                      select MCUX_COMPONENT_component4
                      depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12

                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_2
                      bool "Select component5 and component4"
                      select MCUX_COMPONENT_component5
                      select MCUX_COMPONENT_component6
                      depends on MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016
              endchoice   
          endif
  ```

  If under each allOf, there is only one component, then you can use "select"

  ```yaml
  componentB:
    dependency:
      allOf:
      - component1
      - component2
      - compiler:
        - iar
        - mdk
      - anyOf:
          - allOf:
            - component3
            - device:
              - MK64F12
              - MK63F12
          - allOf:
            - component5
            - device:
              - LPC54005
              - LPC54016
  ```

  ```bash
     config MCUX_COMPONENT_componentB
          bool "Component B, pattern 2 select"
          select MCUX_COMPONENT_component1 
          select MCUX_COMPONENT_component2
          depends on MCUX_COMPILER_IAR || MCUX_COMPILER_MDK
          # All device scope shall be explicitly specified here, otherwise for a device which is not in the scope which means the dependency is not satisfied, but componentC is still showed and configurable
          depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12 || MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016
          select MCUX_COMPONENT_component3 if MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12
          select MCUX_COMPONENT_component5 if MCUX_HW_DEVICE_LPC54005 || MCUX_HW_DEVICE_LPC54016 
  ```

- Pattern 3: start with anyOf, with one level allOf

  ```yaml
  componentE:
    dependency:
      anyOf:
      - allOf:
        - component1
        - component2
        - core:
          - cm4
          - cm4f
        - device:
          - MK64F12
          - MK63F12
      - allOf:
        - component3
        - component4
  ```

  The Kconfig dependency pattern is like

  ```bash
      config MCUX_COMPONENT_componentC
          bool "Component C, pattern 3"
          if MCUX_COMPONENT_componentC
              choice
                  prompt "Component C anyOf"
                  default MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component1_component2
                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component1_component2
                      bool "Select component1 and component2"
                      select MCUX_COMPONENT_component1
                      select MCUX_COMPONENT_component2
                      depends on MCUX_HW_CORE_CM4 || MCUX_HW_CORE_CM4F
                      depends on MCUX_HW_DEVICE_MK64F12 || MCUX_HW_DEVICE_MK63F12

                  config MCUX_DEPENDENCY_COMPONENT_componentC_DEPEND_ALLOF_component3_component4
                      bool "Select component3 and component4"
                      select MCUX_COMPONENT_component3
                      select MCUX_COMPONENT_component4
              endchoice   
          endif
  ```

## 