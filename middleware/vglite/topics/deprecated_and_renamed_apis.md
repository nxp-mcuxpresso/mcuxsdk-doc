# Deprecated and renamed APIs 

The following functions are deprecated and are either obsolete or replaced by a more efficient implementation. Their use is discouraged and will produce unpredictable behaviors.

The names of some functions, enums and structures were modified during code refinements in 2022Q3. If the parameters did not change, the deprecated syntax detail is not provided below. Changes to enums and structs are not mentioned here, instead refer to the item itself.



|**Deprecated or renamed API**|**Recommended replacement API**|**Source file**|**Date deprecated**|
|-----------------------------|-------------------------------|---------------|-------------------|
|vg\_lite\_perspective|n/a|vg\_lite.h|August 2022|
|vg\_lite\_set\_dither|vg\_lite\_enable\_dither vg\_lite\_disable\_dither|vg\_lite.h|August 2022|
|vg\_lite\_append\_path|vg\_lite\_path\_append|vg\_lite.h|Sept 2022|
|vg\_lite\_path\_calc\_length|vg\_lite\_get\_path\_length|vg\_lite.h|Sept 2022|
|vg\_lite\_set\_image\_global\_alpha|vg\_lite\_set\_source\_global\_alpha|vg\_lite.h|Sept 2022|
|vg\_lite\_dest\_global\_alpha|vg\_lite\_set\_dest\_global\_alpha|vg\_lite.h|Sept 2022|
|vg\_lite\_mem\_avail|vg\_lite\_get\_mem\_size|vg\_lite.h|Sept 2022|
|vg\_lite\_enable\_premultiply|n/a|vg\_lite.h|Dec 2022|
|vg\_lite\_disable\_premultiply|n/a|vg\_lite.h|Dec 2022|
|vg\_lite\_set\_premultiply|n/a|vg\_lite.h|Aug 2023|
|vg\_lite\_radial\_gradient\_spreadmode\_t enum|vg\_lite\_gradient\_spreadmode\_t enum|vg\_lite.h|March 2023|
|**API Name Refinement**|***\(no change to parameters\)***| | |
|vg\_lite\_buffer\_upload|vg\_lite\_upload\_buffer\_|vg\_lite.h|Sept 2022|
|vg\_lite\_\*mask\*|*most vg\_lite\_\*mask\_layer*|vg\_lite.h|Sept 2022|
|vg\_lite\_\*\_grad|vg\_lite\_\*\_gradient *\(parameters unchanged\)*|vg\_lite.h|Sept 2022|
|vg\_lite\_\*\_radial\_grad\*|vg\_lite\_\*\_rad\_grad\*|vg\_lite.h|Sept 2022|
|vg\_lite\_buffer\_image\_mode\_t|vg\_lite\_image\_mode\_t|vg\_lite.h|Sept 2022|
|vg\_lite\_transparency\_mode\_t|vg\_lite\_transparency\_t|vg\_lite.h|Sept 2022|
|vg\_lite\_set\_update\_stroke|vg\_lite\_update\_stroke|vg\_lite.h|Sept 2022|
|vg\_lite\_set\_draw\_path\_type|vg\_lite\_set\_path\_type|vg\_lite.h|Sept 2022|




```{include} ../topics/deprecated_vg_lite_syntax.md
:heading-offset: 1
```

