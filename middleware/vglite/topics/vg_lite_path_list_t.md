# `vg_lite_path_list_t` structure 

The structure `vg_lite_path_list_ptr` points to the `vg_lite_path_list` structure that provides divided path data according to `MOVE/MOVE_REL.` *\(from Aug 2023\)*

Used \(`vg_lite_path_list_ptr`\) in structures: `vg_lite_stroke_t.`



|**vg\_lite\_path\_list\_t members**|**Type**|**Description**|
|-----------------------------------|--------|---------------|
|path\_points|vg\_lite\_path\_point\_ptr||
|path\_end|vg\_lite\_path\_point\_ptr||
|point\_count|vg\_lite\_uint32\_t||
|next|vg\_lite\_path\_list\_ptr||
|closed|vg\_lite\_uint8\_t||

**Parent topic:**[Stroke structures](../topics/stroke_structures.md)

