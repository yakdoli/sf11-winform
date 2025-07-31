---
title: exportingtopdf1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exportingtopdf1.md
created_at: 2025-07-03
---








  









### Exporting to PDF {#exporting-to-pdf style="tab-stops: 0pt"}

 

The chart control can be exported into a PDF file as an image using Essential PDF. The chart control provides APIs to convert it to an image, while Essential PDF lets you insert this image into a Word Document file programmatically.

 

{border="0"}

 

Figure 353: Exporting Chart to PDF

 

1.   1. Add the Syncfusion.Pdf.Base and Syncfusion.Pdf.Windows assemblies.

 

2.   2. Add the namespace **Syncfusion.Pdf** in your form.

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [using][ Syncfusion.Pdf;]          |
|                                                                                                                                       |
| [using][ Syncfusion.Pdf.Graphics;] |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]** |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [Imports][ Syncfusion.Pdf]                                              |
|                                                                                                                                                                            |
| [Imports][ Syncfusion.Pdf.Graphics]                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   3. Add the code snippet that is given below in your form.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| **[]**                                                                                                                       |
|                                                                                                                                                                                |
| [string][ fileName=Application.StartupPath+[\"\\\\chartexport\"];] |
|                                                                                                                                                                                |
| [string][ exportFileName = fileName + [\".pdf\"];]                 |
|                                                                                                                                                                                |
| [string][ file = fileName + [\".gif\"];]                           |
|                                                                                                                                                                                |
| [this][.chartControl1.SaveImage(file);]                                                   |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [//Create a PDF document]                                                                                                    |
|                                                                                                                                                                                |
| [PdfDocument pdfDoc = [new] PdfDocument();]                                                                           |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [//Add a page to the empty PDF document]                                                                                     |
|                                                                                                                                                                                |
| [pdfDoc.Pages.Add();                   ]                                                                                                   |
|                                                                                                                                                                                |
| [                                                                                ]                                                         |
|                                                                                                                                                                                |
| [//Draw chart image in the first page]                                                                                       |
|                                                                                                                                                                                |
| [pdfDoc.Pages\[0\].Graphics.DrawImage(PdfImage.FromFile(file), [new] PointF(10, 30));]                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [//Save the PDF Document to disk.]                                                                                           |
|                                                                                                                                                                                |
| [pdfDoc.Save(exportFileName);]                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [  [// Launches the file.                         ]]                                                                 |
|                                                                                                                                                                                |
| [System.Diagnostics.Process.Start(exportFileName);]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                           |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [Dim][ fileName [As] [String] = Application.StartupPath & [\"\\chartexport\"]] |
|                                                                                                                                                                                                                                      |
| [Dim][ exportFileName [As] [String] = fileName & [\".pdf\"]]                   |
|                                                                                                                                                                                                                                      |
| [Dim][ file [As] [String] = fileName & [\".gif\"]]                             |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.SaveImage(file)]                                                                                                            |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [\'Create a PDF document]                                                                                                                                                          |
|                                                                                                                                                                                                                                      |
| [Dim][ pdfDoc [As] PdfDocument = [New] PdfDocument()]                                                 |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [\'Add a page to the empty PDF document]                                                                                                                                           |
|                                                                                                                                                                                                                                      |
| [pdfDoc.Pages.Add()]                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [\'Draw chart image in the first page]                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [pdfDoc.Pages(0).Graphics.DrawImage(PdfImage.FromFile(file), [New] PointF(10, 30))]                                                                                         |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [\'Save the PDF Document to disk.]                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [pdfDoc.Save(exportFileName)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [\' Launches the file.                         ]                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| [System.Diagnostics.Process.Start(exportFileName)]                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the above is available in our installation at the following location:

 

[\"My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\Export\\Chart Export Data\"]{.UGHyperlink}

 

[]{#related-topics}

