---
title: savingaworkbook.md
original_path: WinForms_Docs/99_Uncategorized/savingaworkbook.md
created_at: 2025-08-05
---








  









## [][]{#p25}[]{#_Saving_a_Workbook}Saving a Workbook {#saving-a-workbook style="tab-stops: 0pt"}

Essential XlsIO is a Non-UI component that can be used on Windows Forms, Web Forms and WPF applications.

Any changes made in a new or existing worksheet will be affected, only if it is saved to a disk or a stream. XlsIO supports saving files to different formats in stream and disk by using the SaveAs method of IWorkbook. The workbook can be saved to stream/disk/response. The only code that is specific for the usage of XlsIO in a Windows Forms application and WPF application, is the saving of the spreadsheet to disk, and for Web Forms applications, it is the streaming of the spreadsheet to the client browser.

The following is the code snippet to save the document to disk.

 

**Saving Worksheet in Windows and WPF Applications**

 

+--------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ][]**                      |
|                                                                                                              |
| [// ][Saving the workbook to disk.]  |
|                                                                                                              |
| [workbook.SaveAs(\"Sample.xls\");][] |
+--------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                   |
|                                                                                                              |
| [\'Saving the workbook to disk.]                                         |
|                                                                                                              |
| [workbook.SaveAs(\"Sample.xls\");][] |
+--------------------------------------------------------------------------------------------------------------+

**[]** 

Saving Worksheet in Web Applications

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ][]**                                                                                 |
|                                                                                                                                                                         |
| [// Stream the workbook to the client browser.]                                                                                     |
|                                                                                                                                                                         |
| [workbook.SaveAs(\"Sample.xls\", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.Open);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                                             |
|                                                                                                                                                                        |
| [\'Stream the workbook to the client browser.]                                                                                     |
|                                                                                                                                                                        |
| [workbook.SaveAs(\"Sample.xls\", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.Open)][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Similarly, you can open an xlsx file inside the browser by using the following code snippet.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ][]**                                                         |
|                                                                                                                                                 |
| [workbook.Version = ExcelVersion.Excel2007;]                                                                |
|                                                                                                                                                 |
| [// Stream the workbook to the client browser.]                                                             |
|                                                                                                                                                 |
| [workbook.SaveAs(\"Sample.xlsx\", Response, ExcelDownloadType.Open);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\] ]**                                                                                         |
|                                                                                                                                               |
| [workbook.Version = ExcelVersion.Excel2007]                                                               |
|                                                                                                                                               |
| [\'Stream the workbook to the client browser.]                                                            |
|                                                                                                                                               |
| [workbook.SaveAs(\"Sample.xlsx\",Response,ExcelDownloadType.Open);][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

 

Following code snippet allows to prompt for the Save dialog box, to save the created file in some location in disk.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ][]**                                                                                         |
|                                                                                                                                                                                 |
| [// Stream the workbook to the client browser.]                                                                                             |
|                                                                                                                                                                                 |
| [workbook.SaveAs(\"Sample.xls\", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.PromptDialog);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\] ]**                                                                                                                          |
|                                                                                                                                                                                |
| [\'Stream the workbook to the client browser.]                                                                                             |
|                                                                                                                                                                                |
| [workbook.SaveAs(\"Sample.xls\", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.PromptDialog)][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For more information on overloads of the workbook\'s Save method, refer Class Reference in the online documentation.

This section explains saving the files to the below formats.

[]{#p26}**[]** 

More:











