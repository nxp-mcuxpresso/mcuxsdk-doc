# Blits for compositing and blending

This part of the API performs the hardware accelerated blit operations.

Compositing rules describes how two areas are combined to form a single area. Blending rules describes how combining the colors of the overlapping areas are combined. VGLite supports two blending operations and a subset of the Porter-Duff operations \[PD84\]. The Porter-Duff operators assume that the pixels have the alpha associated \(premultiplied\), it means that the pixels are premultiplied prior to the blending operation. GC555, GC355, and some GCNanoUltraV hardware support alpha premultiply for RGB image, but GCNanoLiteV does not.

The source image is copied to the destination window with a specified matrix that can include translation, rotation, scaling, and perspective correction.

-   The blit function can be used with or without the blend mode.
-   The blit function can be used with or without specifying any color value.
-   The blit function can be used for color conversion with an identity matrix and appropriate formats specified for the source and the destination buffers. In this case, do not specify blend mode and color value.




```{include} ../topics/blit_enumerations.md
:heading-offset: 1
```

```{include} ../topics/blit_structures.md
:heading-offset: 1
```

```{include} ../topics/blit_functions.md
:heading-offset: 1
```

```{include} ../topics/premultiply_and_scissor_functions.md
:heading-offset: 1
```

