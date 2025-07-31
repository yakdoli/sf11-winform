---
title: exporting2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporting2.md
created_at: 2025-07-03
---








  









## Exporting {#exporting style="tab-stops: 0pt"}

Essential Chart has built-in support for exporting the Chart control into various image formats. Also, by using the complementary products such as Essential XlsIO, DocIO, and PDF you can export the chart image into Excel, Word documents, and PDF documents.

 

[E]{#line157}asy Exporting:

To export to the required format, it is enough to call the appropriate function.

 

Methods:

 


  Name               Parameters                                                                                                    Return Type   Description[]
  ------------------ ------------------------------------------------------------------------------------------------------------- ------------- --------------------------------------------------------------
  ExportToImage      (string filename, ChartImageFormat ImageFormat)                                                               None          This function is used to export the chart as an image.
  ExportToDocument   (string filename, ChartImageFormat ImageFormat, bool IsSaveImagetoDisk, Syncfusion.DocIO.FormatType format)   None          This function is used to export the chart as a document.
  ExportToExcel      (string filename, ChartImageFormat ImageFormat, bool IsSaveImagetoDisk)                                       None          This function is used to export the chart in an Excel sheet.
  ExportToPDF        (string filename, ChartImageFormat ImageFormat, bool IsSaveImagetoDisk)                                       None          This function is used to export the chart in a PDF document.


[] 

More:















