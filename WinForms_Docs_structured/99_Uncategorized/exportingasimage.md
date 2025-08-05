---
title: exportingasimage.md
original_path: WinForms_Docs/99_Uncategorized/exportingasimage.md
created_at: 2025-08-05
---








  









### Exporting as Image {#exporting-as-image style="tab-stops: 0pt"}

The OLAP Chart can be exported easily as an image file in several different formats.

 

Programmatically:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                   |
|                                                                                                                                                                                                                      |
| [//Exporting OlapChart in \".gif\" format]                                                                                                                         |
|                                                                                                                                                                                                                      |
| [private string exportFileName, file = null;]                                                                                                                      |
|                                                                                                                                                                                                                      |
| [private string fileName = \"Sample\";]                                                                                                                            |
|                                                                                                                                                                                                                      |
| [exportFileName = fileName + \".gif\";                    ]                                                                                                        |
|                                                                                                                                                                                                                      |
| [this.][olapChart1[.ExportToImage(exportFileName);]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                |
|                                                                                                                                                                                                                   |
| [\'Exporting OlapChart in \".gif\" format]                                                                                                                      |
|                                                                                                                                                                                                                   |
| [Private exportFileName As String, file As String = Nothing]                                                                                                    |
|                                                                                                                                                                                                                   |
| [Private fileName As String = \"Sample\"]                                                                                                                       |
|                                                                                                                                                                                                                   |
| [exportFileName = fileName & \".gif\"]                                                                                                                          |
|                                                                                                                                                                                                                   |
| [Me.][olapChart1[.ExportToImage(exportFileName)]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Based on the filename extension, the chart has built-in support to save the image in the following formats.

[] 


  ---------------- -------------------------------
  File Extension   File Type
  .bmp             BMP
  .jpg             JPG
  .jpeg            JPEG
  .gif             GIF
  .tiff            TIFF
  .wmf             WMF(Windows Meta File)
  .emf             EMF
  .svg             SVG(Scalable Vector Graphics)
  ---------------- -------------------------------


[] 

 

If the specified extension is none of the above, then the chart is exported as a bitmap.

[] 

{border="0"}

 

Figure 45: Exported to Image Format

 

 

 

Table 24: ExportToImage

 


  -------------------------------- ---------------------------------------------------------------------------------------------------------- ------------ ------------- ------------- ----------------
  Methods                          Description                                                                                                Parameters   Type          Return Type   Reference Link
  ExportToImage(String fileName)   Exports a chart into a new image file with the specified file name. It takes the file name as parameter.   string       Server side   void          \-
  -------------------------------- ---------------------------------------------------------------------------------------------------------- ------------ ------------- ------------- ----------------


 

Sample Location

 

A sample demo is available at the following location:

 

..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\ Exporting\\Exporting Chart Demo\\[]

[]{#related-topics}

