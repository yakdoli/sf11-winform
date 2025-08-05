---
title: images2.md
original_path: WinForms_Docs/99_Uncategorized/images2.md
created_at: 2025-08-05
---






##### Images {#images style="tab-stops: 0pt"}

 

Essential PDF supports both raster and vector images. It supports the following image formats:

 

[·      ]Bmp

[·      ]Jpeg

[·      ]Gif

[·      ]Png

[·      ]Tif

[·      ]Wmf

[·      ]Emf and

[·      ]Emf+

[] 

Images are supported through the **PdfImage** class, which is an abstract base class that provides the common functionality for **PdfBitmap** and **PdfMetafile** classes. There are static methods in PdfImage providing the capability to create a PdfImage instance from different sources.

 

PdfImage as well as graphics elements support layouting multiple pages (see ).

 

Base Properties

[] 

[·      ]**Height**-Specifies image height in pixels

[·      ]**Width**-Specifies image width in pixels

[·      ]**HorizontalResolution**-Specifies horizontal image resolution, which is also known as DpiX

[·      ]**VerticalResolution**-Specifies vertical image resolution, also known as DpiY

[·      ]**PhysicalDimension**-Specifies image dimension in points

[·      ]**Quality**-Gets or sets the quality[]


 

{border="0"}Note: Image quality is 100 by default, which increases the resultant file size and quality. Reducing the quality will reduce the file size.


 

Bitmaps

 

**PdfBitmap** class provides functionality of raster images described above. Masks and alpha channels are supported. There are two different kinds of masks: color mask, which is implemented by the **PdfColorMask** class, and image mask, which is implemented by the **PdfImageMask** class. Masks are set by using the **Mask** property of the PdfBitmap object.

[] 

The active frame is chosen if the image is a multiframe image (Gif, Tif). The **FrameCount** and **ActiveFrame** properties enable to control the active frame.

[] 

Metafiles

[] 

All three types of windows metafiles are supported by Essential PDF through the **PdfMetafile** class. Additionally, **Rich Text Format** (RTF) is supported through the PdfMetafile class. PdfMetafile supports multipage layout as well as graphic elements. Additionally, it supports splitting of text lines through the page breaks, if the text line is shared by pages. **PdfMetafileLayoutFormat** should be used when the **Draw** method is called for handling this feature.

[] 

While rendering a large meta file with images and text in a PDF document, which has page breaks, you will notice that the images and text are not split across the page breaks. This is achieved by disabling the **SplitTextLines** and **SplitImages** properties of the **PdfMetafileLayoutFormat** class as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [PdfMetafileLayoutFormat][ format = [new] [PdfMetafileLayoutFormat]();] |
|                                                                                                                                                                                                        |
| [format.SplitTextLines = [false];]                                                                                                            |
|                                                                                                                                                                                                        |
| [format.SplitImages = [false];]                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [Dim][ format [As] [New] PdfMetafileLayoutFormat()] |
|                                                                                                                                                                                    |
| [format.SplitTextLines = [False]]                                                                                         |
|                                                                                                                                                                                    |
| [format.SplitImages = [False]]                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following are the public properties of the PdfMetafileLayoutFormat class.

[] 


  ------------------- ---------------------------------------------------------------------------------------------------
  Name                Description
  Break               Gets or sets break type of the element.
  Layout              Gets or sets layout type of the element.
  PaginateBounds      Gets or sets the bounds on the next page.
  SplitImages         Gets or sets the value indicating whether the images should be split between the pages or not.
  SplitTextLines      Gets or sets the value indicating whether the text line should be split between the pages or not.
  UsePaginateBounds   Gets a value that indicates whether PaginateBounds should be used or not.
  ------------------- ---------------------------------------------------------------------------------------------------


 

Color Spaces

 

Images retain their original color space. The supported color spaces are as follows.

 

[·      ]**RGB** - Images with 24-bit color space

[·      ]**CMYK** - Images with 48-bit color space

[·      ]**Grayscale** - Images with 8-bit color space

[·      ]**Indexed** - Images with 8-bit indexed color space

 

Transparency

 

Transparency of PdfBitmap images are provided by the abstract PdfMask base class.

 

PdfImageMask

[] 

Using grayscale or monochrome images in PdfImageMask enables to create transparent images depending on the pixel format.

[] 

[·      ]Soft Mask

[] 

A soft mask specifies a transparency level for each pixel of the image. You can create these masks from a grayscale image. The level of gray indicates the level of transparency.

[] 

[·      ]Hard Mask

[] 

A hard mask classifies pixels based on their transparency. You can create these masks from a monochrome image.

[] 


{border="0"}Note: Image masks should be of the same width and height as the base image.


[] 

PdfColorMask

[] 

This mask enables masking colors (making them transparent) by specifying the range of colors. All colors that exist between the start color and the end color will be transparent.

[] 


{border="0"}Note: According to PDF References, it is recommended not to use JPEG images with color key masking.


 

 

 

[]{#related-topics}

