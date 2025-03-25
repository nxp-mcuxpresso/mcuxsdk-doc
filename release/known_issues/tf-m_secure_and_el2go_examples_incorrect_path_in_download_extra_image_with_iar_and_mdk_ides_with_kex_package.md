# TF-M secure and EL2GO examples incorrect path in "Download extra image" with iar and mdk IDEs with Kex package

TF-M secure and EL2GO examples are missing the target path for ns binary in "extra download image" with iar and mdk IDEs

**Examples**: tfm_demo_s, tfm_psatest_s, tfm_regression_s, tfm_secureboot_s, el2go_agent_s, el2go_blob_test_s, el2go_import_blob_s, el2go_mqtt_demo_s
**Affected toolchains**: mdk, iar
**Affected platforms**: mcxn5xxevk, frdmmcxn947, mcxn9xxevk, rdrw612bga, frdmrw612
**Workaround**: There are two ways
        1.) Flash secure and non secure bins via Jlink or SPSDK after the build with IDE and providing with correct paths of secure and non-secure binaries.
        or
        2.) Add {target} debug/release in path of "Download extra image" for iar and  for MDK in xxx_flashdownload.ini file.