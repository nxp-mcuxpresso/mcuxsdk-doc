# `vg_lite_sub_path_t` structure 

The structure `vg_lite_sub_path_ptr` points to the `vg_lite_sub_path` structure that provides sub path detail and a pointer to the next sub path. *\(from March 2022\)*

Used in structure: `vg_lite_stroke_conversion.`





|**vg\_lite\_path\_point\_t members**|**Type**|**Description**|
|------------------------------------|--------|---------------|
|next|vg\_lite\_sub\_path\_ptr|Pointer to the next sub path|
|point\_count|vg\_lite\_uint32\_t|Number of points in the sub path|
|point\_list|vg\_lite\_path\_point\_ptr|Pointer to the point list.|
|end\_point|vg\_lite\_path\_point\_ptr|Pointer to the last point.|
|closed|vg\_lite\_uint8\_t|Indicates whether or not the path is closed.|
|length|vg\_lite\_float\_t|Length of the sub path.|





**Parent topic:**[Stroke structures](../topics/stroke_structures.md)

