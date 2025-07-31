---
title: howtosaveexportedexcelfileinserver.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosaveexportedexcelfileinserver.md
created_at: 2025-07-03
---








  









## How to save exported excel file in server {#how-to-save-exported-excel-file-in-server style="tab-stops: 0pt"}

 

You can save the exported excel file in server by setting *SaveIn* type while creating object for *GridExcelExport* class. By default *SaveIn* type is set to client. The constructor for *GridExcelExport* class contains 3 arguments:

[] 

[·      ]**GridGroupingControl** - GridGroupingControl object

[·      ]**String filename** - Name of the file to be saved

[·      ]**GridExcelExport.SaveIn** - Enum value to specify where the file has to be saved

[o  ]**Client**  - Saving in client

[o  ]**Server** -  Saving in server

**[]** 

Example

Saving file in server

The following code illustrates how to save the exported excel file in server.

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                          |
| [String][ file = Server.MapPath([\"\~/Sample.xls\"]);]                   |
|                                                                                                                                                                                          |
| [// Save the file in server.][]                                                    |
|                                                                                                                                                                                          |
| [GridExcelExport][ excel = [new] [GridExcelExport]] |
|                                                                                                                                                                                          |
| [([this].GridGroupingControl1,file,[GridExcelExport].[SaveIn].Server);]         |
|                                                                                                                                                                                          |
| [excel.ExportNestedTable = [true];]                                                                                             |
|                                                                                                                                                                                          |
| [excel.Export();]                                                                                                                                    |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [Dim][ file [As] [String] = Server.MapPath(\"\~/Sample.xls\")]                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [// Save the file in server.][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [Dim][ excel [As] GridExcelExport = [New] GridExcelExport ([Me].GridGroupingControl1,file,GridExcelExport.SaveIn.Server)] |
|                                                                                                                                                                                                                                                                               |
| [excel.ExportNestedTable = [True]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [excel.Export()]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Saving file in client

The following code illustrates how to save the exported excel file in client.

**           **

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                          |
| [String][ file = Server.MapPath([\"\~/Sample.xls\"]);]                   |
|                                                                                                                                                                                          |
| [// Save the file in client.][]                                                    |
|                                                                                                                                                                                          |
| [GridExcelExport][ excel = [new] [GridExcelExport]] |
|                                                                                                                                                                                          |
| [([this].GridGroupingControl1,file,[GridExcelExport].[SaveIn].Client);]         |
|                                                                                                                                                                                          |
| [excel.ExportNestedTable = [true];]                                                                                             |
|                                                                                                                                                                                          |
| [excel.Export();]                                                                                                                                    |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [Dim][ file [As] [String] = Server.MapPath(\"\~/Sample.xls\")]                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [// Save the file in client.][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [Dim][ excel [As] GridExcelExport = [New] GridExcelExport ([Me].GridGroupingControl1,file,GridExcelExport.SaveIn.Client)] |
|                                                                                                                                                                                                                                                                               |
| [excel.ExportNestedTable = [True]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [excel.Export()]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[] 

[] 

[]{#related-topics}

