---
title: howtoimproveperformance.md
original_path: WinForms_Docs/99_Uncategorized/howtoimproveperformance.md
created_at: 2025-08-05
---






#### How To Improve Performance? {#how-to-improve-performance style="tab-stops: 0pt"}

 

Performance is the one of the initial requirements of Essential PDF. This section describes performance tips that help using the product in the most appropriate way.

 

**Text and Font**

 

[·      ]It is good to use PdfStandardFont during text output than Unicode characters. Standard fonts take less space in the file than other fonts.

[·      ]If PdfTrueType font is used, and it is not expected to use Unicode characters, switching off the Unicode support will reduce the size of the output PDF file. Support of Unicode by PdfTrueTypeFont is specified in the constructor.

[·      ]Do not enable RightToLeft property of PdfStringFormat, if right-to-left language is not used. Setting this property to true enables a special RTL engine that decreases the text layouting speed.

 

Compression and File Structure

 

Changing these can change the resulting file size, however it can increase the time spent on saving.

 

**Compression** is responsible for compressing internal data streams in PDF. You might be surprised by the number of streams in an ordinary PDF document. High quality compression involves longer file saves, but requires less space.

 

If **CrossReferenceType** property is specified by CrossReferenceStream, the cross-reference is represented by cross-reference stream. It may reduce the file size, especially if compression is turned on, but increases the file generation time.

 

 

[]{#related-topics}

