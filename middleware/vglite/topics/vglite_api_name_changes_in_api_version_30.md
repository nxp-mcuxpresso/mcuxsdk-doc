# VGLite API name changes in API version 3.0

Some original VGLite API names are changed in API version 3.0 for API naming consistency. In the VGLite API version 3.0 header file vg\_lite.h, a set of API name macros are defined for the equivalent API names between API version 3.0 and API version 2.0, so it is not necessary to modify the VGLite API function names in API version 2.0 applications for the application to compile and run with the API version 3.0 driver.

The list of equivalent VGLite API functions between API version 3.0 and API version 2.0 is shown below. These API functions’ parameters are the same between API version 3.0 and API version 2.0.

```
/* API name defines for backward compatibility to VGLite 2.0 APIs */
#define vg_lite_buffer_upload                   vg_lite_upload_buffer
#define vg_lite_path_append                     vg_lite_append_path
#define vg_lite_path_calc_length                vg_lite_get_path_length
#define vg_lite_set_ts_buffer                   vg_lite_set_tess_buffer
#define vg_lite_set_draw_path_type              vg_lite_set_path_type
#define vg_lite_create_mask_layer               vg_lite_create_masklayer
#define vg_lite_fill_mask_layer                 vg_lite_fill_masklayer
#define vg_lite_blend_mask_layer                vg_lite_blend_masklayer
#define vg_lite_generate_mask_layer_by_path     vg_lite_render_masklayer
#define vg_lite_set_mask_layer                  vg_lite_set_masklayer
#define vg_lite_destroy_mask_layer              vg_lite_destroy_masklayer
#define vg_lite_enable_mask                     vg_lite_enable_masklayer
#define vg_lite_enable_color_transformation     vg_lite_enable_color_transform
#define vg_lite_set_color_transformation        vg_lite_set_color_transform
#define vg_lite_set_image_global_alpha          vg_lite_source_global_alpha
#define vg_lite_set_dest_global_alpha           vg_lite_dest_global_alpha
#define vg_lite_clear_rad_grad                  vg_lite_clear_radial_grad
#define vg_lite_update_rad_grad                 vg_lite_update_radial_grad
#define vg_lite_get_rad_grad_matrix             vg_lite_get_radial_grad_matrix
#define vg_lite_set_rad_grad                    vg_lite_set_radial_grad
#define vg_lite_draw_linear_gradient            vg_lite_draw_linear_grad
#define vg_lite_draw_radial_gradient            vg_lite_draw_radial_grad
#define vg_lite_draw_gradient                   vg_lite_draw_grad
#define vg_lite_mem_avail                       vg_lite_get_mem_size
#define vg_lite_set_update_stroke               vg_lite_update_stroke

```

The list of equivalent VGLite API structures and enumerations is shown below:

```
#define vg_lite_buffer_image_mode_t             vg_lite_image_mode_t
#define vg_lite_draw_path_type_t                vg_lite_path_type_t
#define vg_lite_linear_gradient_ext_t           vg_lite_ext_linear_gradient_t
#define vg_lite_buffer_transparency_mode_t      vg_lite_transparency_t
```

**Parent topic:**[VGLite API version 2.0 to 3.0 migration guide](../topics/vglite_api_version_20_to_30_migration_guide.md)

