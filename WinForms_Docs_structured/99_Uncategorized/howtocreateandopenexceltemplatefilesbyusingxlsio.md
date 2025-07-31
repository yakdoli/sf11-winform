---
title: howtocreateandopenexceltemplatefilesbyusingxlsio.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocreateandopenexceltemplatefilesbyusingxlsio.md
created_at: 2025-07-03
---








  









### How to create and open Excel Template files by using XlsIO? {#how-to-create-and-open-excel-template-files-by-using-xlsio style="tab-stops: 0pt"}

**[]** 

[] 

Creating Excel Template Files

[] 

You can create either XLT or XLTX Excel Template files by saving a file with the **ExcelSaveType** property of the **SaveAs** method. The ExcelSaveType property must be set to **SaveAsTemplate** to create a template file of the existing file. The following code example illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Save as XLT.]                                                                                    |
|                                                                                                                                                        |
| [workbook.Version = [ExcelVersion].Excel97to2003;]                                            |
|                                                                                                                                                        |
| [workbook.SaveAs([\"Sample.xlt\"], [ExcelSaveType].SaveAsTemplate);]  |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Save as XLTX.]                                                                                   |
|                                                                                                                                                        |
| [workbook.Version = [ExcelVersion].Excel2007;]                                                |
|                                                                                                                                                        |
| [workbook.SaveAs([\"Sample.xltx\"], [ExcelSaveType].SaveAsTemplate);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                          |
|                                                                                                                               |
| []                                                                                        |
|                                                                                                                               |
| [\' Save as XLT.]                                                           |
|                                                                                                                               |
| [workbook.Version = ExcelVersion.Excel97to2003]                                           |
|                                                                                                                               |
| [workbook.SaveAs([\"Sample.xlt\"],ExcelSaveType.SaveAsTemplate)]  |
|                                                                                                                               |
| []                                                                                        |
|                                                                                                                               |
| [\' Save as XLTX.]                                                          |
|                                                                                                                               |
| [workbook.Version = ExcelVersion.Excel2007]                                               |
|                                                                                                                               |
| [workbook.SaveAs([\"Sample.xltx\"],ExcelSaveType.SaveAsTemplate)] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

Opening Excel Template Files

 

An Excel Template file is opened in the same way a document is opened. The following code example illustrates how to open a template file.

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                        |
| []                                                                                                 |
|                                                                                                                                        |
| [workbook = application.Workbooks.Open(fileName, [ExcelOpenType].Automatic);] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                           |
|                                                                                                                |
| []                                                                         |
|                                                                                                                |
| [workbook = application.Workbooks.Open(fileName, ExcelOpenType.Automatic)] |
+----------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

