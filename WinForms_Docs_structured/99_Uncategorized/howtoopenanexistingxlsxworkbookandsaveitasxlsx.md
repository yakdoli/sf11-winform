---
title: howtoopenanexistingxlsxworkbookandsaveitasxlsx.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoopenanexistingxlsxworkbookandsaveitasxlsx.md
created_at: 2025-07-03
---








  









### How to open an existing Xlsx workbook and save it as Xlsx? {#how-to-open-an-existing-xlsx-workbook-and-save-it-as-xlsx style="tab-stops: 0pt"}

 

You can open and save an existing Excel 2007 file to the .xlsx format by using XlsIO. The following code example illustrates how to do this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [// Open an existing Excel 2007 file.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [IWorkbook][ workbook = excelEngine.Excel.Workbooks.Open([@\"..\\..\\..\\Data\\Excel2007.xlsx\"], [ExcelOpenType].Automatic);] |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [// Select the version to be saved.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [workbook.Version = [ExcelVersion].Excel2007;]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [// Save it as \"Excel 2007\" format.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [workbook.SaveAs([\"Sample.xlsx\"]);]                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\' Open an existing Excel 2007 file.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Dim][ workbook [As] IWorkbook = excelEngine.Excel.Workbooks.Open([\"..\\..\\..\\Data\\Excel2007.xlsx\"], ExcelOpenType.Automatic)] |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\' Select the version to be saved.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [workbook.Version = ExcelVersion.Excel2007]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\' Save it as \"Excel 2007\" format.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [workbook.SaveAs([\"Sample.xlsx\"])]                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You need to change the Excel Version, if you want to save to another version.


 

[]{#related-topics}

