---
title: htmltopdf.md
original_path: WinForms_Docs/99_Uncategorized/htmltopdf.md
created_at: 2025-08-05
---








  









### HTML To PDF {#html-to-pdf style="tab-stops: 0pt"}

 

WebPages and HTML pages can be imported to PDF using the *HtmlConverter*. The HTMLConverter converts the HTML web page to a *Bitmap* or *Metafile* image using *MSHTML*.

 

{border="0"} MSHTML is a rendering library that is used to render HTML documents. The MSHTML library is like an engine that is used to drive the Internet Explorer.

 

Essential PDF renders the converted image into the PDF. You can convert a web page to PDF, either as Bitmap or Metafile types.

 

[·      ]Rendering web pages as Bitmap provides reasonable performance

[·      ]Rendering web pages as Metafile provides high resolution

 

This section covers the following:

 

[·      ]Converting Methods

[·      ]HTMLConvertor Options

 

Converting Methods

 

HTML documents can be converted to PDF through the following methods:

 

[·      ]ConvertToImage

[·      ]FromString

[] 

1\. ConvertToImage

 

The *ConvertToImage* method converts the URL into an image. It recognizes tables, images, lists, and so on. The URL parameter can be a HTTP or HTTPS address such as \"http://www.server.com/path/file.html\", or a local physical path such as \"c:\\path\\file.html\".

 


{border="0"}Note: If you want to open a dynamically generated document such as .asp or aspx file, you need to invoke it through HTTP even if this file is local to your own script.


[] 

The overloaded **ConvertToImage** method enables to convert a HTML page to an image with *AspectRatio*, to maintain the ratio of the image dimension. This prevents text truncation at the corners.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                                      |
|                                                                                                                                                                                               |
| [Image] img = html.ConvertToImage([\"http://www.google.com\"], ImageType.Metafile, ([int])width, -1, AspectRatio.KeepWidth); |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [Dim] img [As] Image = html.ConvertToImage([\"http://www.google.com\"], ImageType.Metafile, [CInt](width), -1, AspectRatio.KeepWidth) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 


![.]{.UGHyperlink}


**[]** 

Authentication

[] 

You can use the *ConvertToImage* method to access the authenticated web pages, by passing its user credential values as arguments. The following code example illustrates this:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [Image] img = html.ConvertToImage([\"http://www.google.com\"], ImageType.Metafile, ([int])width, -1, AspectRatio.KeepWidth,\"UserName\", \"Password\"); |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| [Dim] img [As] Image = html.ConvertToImage([\"http://www.google.com\"], ImageType.Metafile, [CInt](width), -1, AspectRatio.KeepWidth, \"UserName\", \"Password\") |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2\. FromString

 

*FromString* method renders HTML from the string to the image. The following code example illustrates this:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [public] [Image] FromString( [string] html, ImageType type );                                                                                               |
|                                                                                                                                                                                                                            |
| [public] [Image] FromString( [string] html, ImageType type, [int] width );                                                             |
|                                                                                                                                                                                                                            |
| [public] [Image] FromString( [string] html, ImageType type, [int] width, [int] height );                          |
|                                                                                                                                                                                                                            |
| [public] [Image] FromString( [string] html, ImageType type, [int] width, [int] height, AspectRatio aspectRatio ); |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [Public] Image FromString([String] html, ImageType type)                                                                                                       |
|                                                                                                                                                                                                          |
| [Public] Image FromString([String] html, ImageType type, [Integer] width)                                                                 |
|                                                                                                                                                                                                          |
| [Public] Image FromString([String] html, ImageType type, [Integer] width, [Integer] height)                          |
|                                                                                                                                                                                                          |
| [Public] Image FromString([String] html, ImageType type, [Integer] width, [Integer] height, AspectRatio aspectRatio) |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample code:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [//initialze the html converter]                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [HtmlConverter] converter = [new] [HtmlConverter]();                                                                                      |
|                                                                                                                                                                                                                |
| [//convert html to pdf]                                                                                                                                                                  |
|                                                                                                                                                                                                                |
| [Image] result  = converter.FromString(html, [ImageType].Metafile, ([int])imgWidth, -1, [AspectRatio].KeepWidth); |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [//Render the image in the Pdf document]                                                                                                                                                 |
|                                                                                                                                                                                                                |
| [PdfImage] pdfImage=[PdfImage].FromImage(result);                                                                                                              |
|                                                                                                                                                                                                                |
| pdfImage.Draw(pdfPage,[PointF].Empty,format);                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [\'Initialize the HTML Converter]                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
|  [Dim] converter [As New] HtmlConverter                                                                                                                                                    |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [\'Convert the HTML file to Image]                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [Dim] result [As] Image = converter.FromString(htmlFilePath, ImageType.Metafile,        [CType](imgWidth, [Integer]), -1, AspectRatio.KeepWidth) |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [\'Render the image in the Pdf document]                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| [Dim] pdfImage [As] PdfImage = pdfImage.FromImage(result)[]                                                                                                          |
|                                                                                                                                                                                                                                      |
| pdfImage.Draw(pdfPage, PointF.Empty, format)                                                                                                                                                                                         |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 


{border="0"}Note: Both ConvertToImage() and FromString() methods are used to convert the HTML pages whose height is less than 32767 pixels as image and the options like  EnableHyperlinks, EnableJavascript  and AutoDetectPageBreak has no effect.


 

[] 

{border="0"}

*Figure* *63: HTML to PDF Conversion Through FromString Method*

[] 

HtmlConverter Options

 

HtmlConverter provides the following options to control HtmlToPDF conversions.

 

[·      ]EnableJavaScript

[·      ]AutoDetectPageBreak

[·      ]Enable Hyperlinks

[] 

EnableJavaScript

 

You can control the JavaScript by using the *EnableJavaScript* property of the HtmlConverter class library. By default this property are set to *False.* So the JavaScript code is disabled during conversion. Set[ ]the *EnableJavaScript* property to True to activate the JavaScript code during conversion.

 

The following code example illustrates this:

 

+----------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                     |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| [HtmlConverter] html = [new] [HtmlConverter](); |
|                                                                                                                |
| []                                                                                       |
|                                                                                                                |
| [//Activating JavaScript]                                                                |
|                                                                                                                |
| html.EnableJavaScript = [true];                                                           |
+----------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                       |
|                                                                                                                      |
|                                                                                                                      |
|                                                                                                                      |
| [Dim] html [As] HtmlConverter = [New] HtmlConverter() |
|                                                                                                                      |
| []                                                                                             |
|                                                                                                                      |
| [\'Activating JavaScript]                                                                      |
|                                                                                                                      |
| html.EnableJavaScript = [True]                                                                  |
+----------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: If JavaScript code is not executed by setting the EnableJavaScript property, it means the Internet Security Settings on the server does not allow the JavaScript execution.


[] 

Enable Hyperlink

 

Essential PDF supports enabling/ disabling live hyperlinks in PDF while converting web pages to PDF. The following code example illustrates this:

 

+-----------------------------------------------------------------------+
| **\[C#\]**                                                            |
|                                                                       |
| []                                              |
|                                                                       |
| HtmlConverter html = [new] HtmlConverter();      |
|                                                                       |
| []                                              |
|                                                                       |
| [// Enabling Hyperlink]                         |
|                                                                       |
| html.EnableHyperlinks = [true];                  |
+-----------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                       |
|                                                                                                      |
|                                                                                                      |
|                                                                                                      |
| [Dim] html [As] [New] HtmlConverter() |
|                                                                                                      |
| []                                                                             |
|                                                                                                      |
| [\'Enabling Hyperlink]                                                         |
|                                                                                                      |
| html.EnableHyperlinks = [True]                                                  |
+------------------------------------------------------------------------------------------------------+

**[]** 

AutoDetectPageBreak

[] 

The *HtmlConverter* supports custom page breaks with standard CSS styles like *page-break-before:always* and *page-break-after:always* that can be applied to any HTML object. You can enable custom page breaks by setting the *AutoDetectPageBreak* property to *True*.

 

The following code example illustrates this:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [HtmlConverter] html = [new] [HtmlConverter]();                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [// Activate the Page Break]                                                                                                                                                         |
|                                                                                                                                                                                                            |
| html.AutoDetectPageBreak = [true];                                                                                                                                                    |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [// Convert the Html file as an image]                                                                                                                                               |
|                                                                                                                                                                                                            |
| [HtmlToPdfResult] result = html.Convert(txtUrl.Text, [ImageType].Metafile, ([int])width, -1, [AspectRatio].KeepWidth); |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [// Specify the quality of the metafile]                                                                                                                                             |
|                                                                                                                                                                                                            |
| [PdfMetafile] mf = new [PdfMetafile](result.RenderedImage as [Metafile]);                                                                   |
|                                                                                                                                                                                                            |
| mf.Quality = 100;                                                                                                                                                                                          |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
| [PdfMetafileLayoutFormat] format = [new] [PdfMetafileLayoutFormat]();                                                                       |
|                                                                                                                                                                                                            |
| format.Break = [PdfLayoutBreakType].FitPage;                                                                                                                                          |
|                                                                                                                                                                                                            |
| format.Layout = [PdfLayoutType].Paginate;                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [//Render the image in PDF document]                                                                                                                                                 |
|                                                                                                                                                                                                            |
| mf.Draw(page, [new] [PointF](0, 0), format);                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                                                                                                  |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [Dim] html [As] HtmlConverter = [New] HtmlConverter()                                                                            |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                 |
| [\' Activate the Page Break]                                                                                                                                              |
|                                                                                                                                                                                                 |
| html.AutoDetectPageBreak = [True]                                                                                                                                          |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [\' Convert the Html file as an image]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [Dim] result [As] HtmlToPdfResult = html.Convert(txtUrl.Text, ImageType.Metafile, [CInt](Fix(width)), -1, AspectRatio.KeepWidth) |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [\' Specify the quality of the metafile]                                                                                                                                  |
|                                                                                                                                                                                                 |
| [Dim] mf [As ]PdfMetafile = [New] PdfMetafile([TryCast](result.RenderedImage, Metafile))                    |
|                                                                                                                                                                                                 |
| mf.Quality = 100                                                                                                                                                                                |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [Dim] format [As] PdfMetafileLayoutFormat = [New] PdfMetafileLayoutFormat()                                                      |
|                                                                                                                                                                                                 |
| format.Break = PdfLayoutBreakType.FitPage                                                                                                                                                       |
|                                                                                                                                                                                                 |
| format.Layout = PdfLayoutType.Paginate                                                                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                 |
| [\' Render the image in PDF document]                                                                                                                                     |
|                                                                                                                                                                                                 |
| mf.Draw(page, [New] PointF(0, 0), format)                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 


{border="0"}Note:[ ]The custom page breaks is supported only when converting MetaFile to PDF. They are not supported when converting Bitmap to PDF.


**[]** 

Rendering HTML page without Splitting

 

To avoid the images and text split across the page breaks, while rendering a large meta file with images and text in a PDF document, disable the *SplitTextLines* and *SplitImages* properties of the *PdfMetafileLayoutFormat* class. The following code illustrates this:

 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                           |
|                                                                                                                                      |
| []                                                                                                             |
|                                                                                                                                      |
| [PdfMetafileLayoutFormat] format = [new] [PdfMetafileLayoutFormat](); |
|                                                                                                                                      |
| format.SplitTextLines = [false];                                                                                |
|                                                                                                                                      |
| format.SplitImages = [false];                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                   |
|                                                                                                                  |
|                                                                                                                  |
|                                                                                                                  |
| [Dim] format [As] [New] PdfMetafileLayoutFormat() |
|                                                                                                                  |
| format.SplitTextLines = [False]                                                             |
|                                                                                                                  |
| format.SplitImages = [False]                                                                |
+------------------------------------------------------------------------------------------------------------------+

 

More:







