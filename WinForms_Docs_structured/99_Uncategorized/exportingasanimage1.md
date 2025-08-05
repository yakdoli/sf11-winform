---
title: exportingasanimage1.md
original_path: WinForms_Docs/99_Uncategorized/exportingasanimage1.md
created_at: 2025-08-05
---








  









### Exporting as an Image {#exporting-as-an-image style="tab-stops: 0pt"}

 

The chart image can easily be exported as an image file in several different formats.

 

Programmatically

 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                  |
|                                                                                                                                                 |
| **[]**                                                                                        |
|                                                                                                                                                 |
| [private][ [string] fileName;]        |
|                                                                                                                                                 |
| [fileName = [Application].StartupPath + [\"\\\\chartexport\"];] |
|                                                                                                                                                 |
| [fileName = fileName + [\".gif\"];]                                                  |
|                                                                                                                                                 |
| []                                                                                             |
|                                                                                                                                                 |
| [this][.chartControl1.SaveImage(fileName);]  |
|                                                                                                                                                 |
| []                                                                                            |
|                                                                                                                                                 |
| [// Launches the file. ]                                                                      |
|                                                                                                                                                 |
| [System.Diagnostics.Process.Start(exportFileName);]                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]** |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [Private][ fileName [As] [String]]          |
|                                                                                                                                                                            |
| [fileName = Application.StartupPath + [\"\\chartexport\"]]                                                      |
|                                                                                                                                                                            |
| [fileName = fileName + [\".gif\"]]                                                                              |
|                                                                                                                                                                            |
| []                                                                                                                        |
|                                                                                                                                                                            |
| [Me][.chartControl1.SaveImage(fileName)]                                |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [\' Launches the file. ]                                                                                                 |
|                                                                                                                                                                            |
| [System.Diagnostics.Process.Start(exportFileName)]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Based on the filename extension the chart has built-in support to save the image in the following formats.

 


  -------------------------------------- --------------------------------
  File Extension                         File Type
  .bmp                                   BMP
  .jpg                                   JPEG
  .jpeg                                  JPEG
  .gif                                   GIF
  .tiff                                  TIFF
  .Wmf                                   WMF
  .emf                                   EMF
  .svg                                   SVG (Scalable Vector Graphics)
  .eps                                   Post Script
  -------------------------------------- --------------------------------


 

If the specified extension is none of the above, then the chart is exported as a bitmap.

 

During runtime, chart control can be saved as a file using the **Chart Toolbar** save option.

[]{#p253} 

 

[]{#related-topics}

