---
title: conversionofhtmltopdfusinggeckorenderingengine.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\conversionofhtmltopdfusinggeckorenderingengine.md
created_at: 2025-07-03
---






##### Conversion of HTML to PDF using Gecko Rendering Engine {#conversion-of-html-to-pdf-using-gecko-rendering-engine style="tab-stops: 0pt"}

 

The following code snippets explain the conversion of HTML to PDF using the Gecko Rendering Engine.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [//Initializing the Gecko Rendering Engine]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [GeckoHtmlRendererControl][ renderer = [new] [GeckoHtmlRendererControl]();]                                                   |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [//Initialzing the html converter]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [HtmlConverter][ converter = [new] [HtmlConverter](renderer);]                                                                |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [//Converting html to pdf]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [HtmlToPdfResult][ result = converter.Convert(txtUrl.Text, [ImageType].Metafile, width, height, [AspectRatio].KeepWidth);] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [//Rendering the image in the PDF document]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [result.Render(document);]                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[   ]

Limitations

 

1.   Formatting / styles created using dynamic scripts will not be rendered in the resultant PDF.

2.   Other features in HTML to PDF conversion such as hyperlinks will not be available for conversion using Gecko rendering engine. However, the page breaks are supported but we can't explicitly control the page break.[ ]

[]{#related-topics}

