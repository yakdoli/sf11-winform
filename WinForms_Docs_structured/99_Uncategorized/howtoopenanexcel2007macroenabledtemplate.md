---
title: howtoopenanexcel2007macroenabledtemplate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoopenanexcel2007macroenabledtemplate.md
created_at: 2025-07-03
---








  









### How to open an Excel 2007 Macro Enabled Template? {#how-to-open-an-excel-2007-macro-enabled-template style="tab-stops: 0pt"}

**[]** 

XlsIO now provides support to open and save an Excel 2007 Macro Enabled Template to XLSM (Excel 2007 Macro Enabled Document) format. The following code example illustrates this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [// Open an existing XLTM file.]                                                                  |
|                                                                                                                                                     |
| [workbook = application.Workbooks.Open([@\"Template.xltm\"], ExcelOpenType.Automatic);] |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [// Save the file as XLSM.]                                                                       |
|                                                                                                                                                     |
| [workbook.Version = ExcelVersion.Excel2007;]                                                                    |
|                                                                                                                                                     |
| [workbook.SaveAs([\"Sample.xlsm\"], ExcelSaveType.SaveAsTemplate);]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [\' Open an existing XLTM file.]                                                                     |
|                                                                                                                                                        |
| [workbook = application.Workbooks.Open([\"MacroTemplate.xltm\"], ExcelOpenType.Automatic)] |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [\' Save the file as XLSM.]                                                                          |
|                                                                                                                                                        |
| [workbook.Version = ExcelVersion.Excel2007]                                                                        |
|                                                                                                                                                        |
| [workbook.SaveAs([\"Sample.xlsm\"], ExcelSaveType.SaveAsTemplate)]                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

