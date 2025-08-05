---
title: howtocompressapdfdocument.md
original_path: WinForms_Docs/99_Uncategorized/howtocompressapdfdocument.md
created_at: 2025-08-05
---






#### How To Compress a PDF Document? {#how-to-compress-a-pdf-document style="tab-stops: 0pt"}

[] 

Compression is used for reducing the size of the created PDF document. Essential PDF controls the compression level of the document by using the **PdfCompressionLevel** class with the help of the LZW and zlib/deflate compression algorithms. Both LZW and Flate methods compress either binary data or ASCII text, but always produce binary data, even if the original data is text.

 

The following compression levels are supported by Essential PDF.

[] 

[·      ]Best

[·      ]BestSpeed

[·      ]BelowNormal

[·      ]AboveNormal

[·      ]None

[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                             |
|                                                                                                            |
| []                                                       |
|                                                                                                            |
| [// Compressing PDF document]                            |
|                                                                                                            |
| [doc.Compression = [PdfCompressionLevel].Normal;] |
+------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                 |
|                                                                                                    |
| []                               |
|                                                                                                    |
| [\' Compressing PDF document]    |
|                                                                                                    |
| [doc.Compression = PdfCompressionLevel.Normal] |
+----------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

