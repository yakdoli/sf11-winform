---
title: reducingsizeofexcel2007excel2010files.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\reducingsizeofexcel2007excel2010files.md
created_at: 2025-07-03
---






#### Reducing size of Excel 2007 & Excel 2010 files {#reducing-size-of-excel-2007-excel-2010-files style="tab-stops: 0pt"}

 

The default compression technique, using which Essential XlsIO compresses files uses .NET compression. A new compression technique has been implemented that will considerably reduce the size of the compressed XLSX files.

 

**Use Case Scenarios**

The reduced size of the compressed file will result in reduced data transfer between applications.

 

**How Compression level can be set**

The Compression level can be set at IApplication interface. This will set the level for all the workbooks created using the same instance of Excel Engine.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]**[]** |
|                                                                                                                                                                                                                                     |
| [IApplication][ application = excelEngine.Excel;]                                                                                           |
|                                                                                                                                                                                                                                     |
| [application.DefaultVersion = [ExcelVersion].Excel2007; [// or ExcelVersion = ExcelVersion.Excel2010;]]                                           |
|                                                                                                                                                                                                                                     |
| [application.CompressionLevel = Syncfusion.Compression.[CompressionLevel].Best;]                                                                                        |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [workbook.SaveAs(fileName);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [workbook.Close();]                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [excelEngine.Dispose();][]                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| [Dim][ excelEngine [As] [New] [ExcelEngine]()]                 |
|                                                                                                                                                                                                                     |
| [Dim][ application [As] [IApplication ][= excelEngine.Excel]] |
|                                                                                                                                                                                                                     |
| [application.DefaultVersion = ExcelVersion][.Excel2007 [\' or ExcelVersion = ExcelVersion.Excel2010]]   |
|                                                                                                                                                                                                                     |
| [application.CompressionLevel = Syncfusion.Compression.[CompressionLevel].Best]                                                                           |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [workbook.SaveAs(fileName)]                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [workbook.Close()]                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [excelEngine.Dispose()][]                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Following are the list of enumerations available:

 


  Enum            Description
  --------------- ------------------------------------------------------------------
  NoCompression   File will not be compressed.
  BestSpeed       Fast compression with more size than normal compression.
  BelowNormal     Compression speed and size will be between Normal and BestSpeed.
  Normal          Both size and speed will be Normal.
  AboveNormal     Takes more time to compress, with reduced file size.
  Best            Slow compression, file size reduced to the best level.


 

[]{#p28}**[]** 

[]{#related-topics}

