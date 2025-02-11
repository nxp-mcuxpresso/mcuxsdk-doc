# Internal representation

For non-32-bit color formats, each pixel is extended to 32 bits as follows:

If the source and destination formats have the same color format, but differ in the number of bits per color channel, the source channel is multiplied by \(2<sup>d</sup>- 1\)/\(2<sup>s</sup>– 1\) and is rounded to the nearest integer, where:

-   **d** is the number of bits in the destination channel
-   **s** is the number of bits in the source channel

**Example**: a b11111 5-bit source channel gets converted to an 8-bit destination b11111000.

The YUV formats are internally converted to RGB. The pixel selection is unified for all formats by using the LSB of the coordinate.

**Parent topic:**[Pixel buffers](../topics/pixel_buffers.md)

