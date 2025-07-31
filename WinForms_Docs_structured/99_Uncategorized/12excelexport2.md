---
title: 12excelexport2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\12excelexport2.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### 1.2 Excel Export {#excel-export style="tab-stops: 0pt"}

 

PivotGrid for WPF can be exported as an XLS file using Essential XlsIO. The user can export the contents of the PivotGrid to the Excel document for future archival, references and analysis purposes.

 

Call Export method

The [GridExcelExport][]class provides support for exporting data from a PivotGrid to an Excel spreadsheet for verification and/or computation. The following dlls should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.PivotGridConverter.Wpf

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| [//// Export to Excel.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                              |
| [SaveFileDialog] [ savedialog = [new][SaveFileDialog]();]                                               |
|                                                                                                                                                                                                                                              |
| [savedialog.AddExtension = [true];]                                                                                                                                                 |
|                                                                                                                                                                                                                                              |
| [savedialog.FileName = [\"Sample\"];]                                                                                                                                            |
|                                                                                                                                                                                                                                              |
| [savedialog.DefaultExt = [\"xls\"];]                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [savedialog.Filter = [\"Excel file (.xls)\|\*.xls\"];]                                                                                                                           |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [if] [ (savedialog.ShowDialog() == [true])]                                                                                        |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [     fileName = savedialog.FileName;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| [     GridExcelExport] [ excelExport = [new][GridExcelExport]([this].pivotGrid1);] |
|                                                                                                                                                                                                                                              |
| [     excelExport.Export(fileName);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [}] []                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [\' ] [Export to Excel.]                                                                                  |
|                                                                                                                                                                                                               |
| [Dim] [ savedialog [As] SaveFileDialog = [New] SaveFileDialog()]               |
|                                                                                                                                                                                                               |
| [savedialog.AddExtension = [True]]                                                                                                                   |
|                                                                                                                                                                                                               |
| [savedialog.FileName = [\"Sample\"]]                                                                                                              |
|                                                                                                                                                                                                               |
| [savedialog.DefaultExt = [\"xls\"]]                                                                                                               |
|                                                                                                                                                                                                               |
| [savedialog.Filter = [\"Excel file (.xls)\|\*.xls\"]]                                                                                             |
|                                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [If] [ savedialog.ShowDialog() = [True][Then]]                                 |
|                                                                                                                                                                                                               |
| [    fileName = savedialog.FileName]                                                                                                                                      |
|                                                                                                                                                                                                               |
| [    [Dim] excelExport [As] GridExcelExport = [New] GridExcelExport([Me].pivotGrid1)] |
|                                                                                                                                                                                                               |
| [    excelExport.Export(fileName)]                                                                                                                                        |
|                                                                                                                                                                                                               |
| [End] [ [If] ] **[]**                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 24:  Exported Excel document from PivotGrid

 

[]{#related-topics}

