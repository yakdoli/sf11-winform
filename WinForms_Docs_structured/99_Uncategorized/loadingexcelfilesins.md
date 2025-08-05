---
title: loadingexcelfilesins.md
original_path: WinForms_Docs/99_Uncategorized/loadingexcelfilesins.md
created_at: 2025-08-05
---








  





## Loading Excel Files in Spreadsheet Control {#loading-excel-files-in-spreadsheet-control style="tab-stops: 0pt"}

You can open the Excel document in the spreadsheet control using *ImportFromExcel* method. The following code illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [OpenFileDialog[ openFileDialog = ][new][ ]OpenFileDialog[();]][] |
|                                                                                                                                                                                                                    |
| [openFileDialog.Filter = [\"Excel 2007 - 2010 Files(\*.xlsx)\|\*.xlsx\|Excel 97 - 2003 Files(\*.xls)\|\*.xls\|All Files(\*.\*)\|\*.\*\"];]             |
|                                                                                                                                                                                                                    |
| [openFileDialog.ShowDialog();]                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [if[ (openFileDialog.File.Exists)]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [    spreadsheet.ImportFromExcel(openFileDialog.File.OpenRead());]                                                                                                             |
|                                                                                                                                                                                                                    |
| [}][]                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ openFileDialog [As] ][OpenFileDialog][ = [New] ][OpenFileDialog][()] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [openFileDialog.Filter = ][\"Excel 2007 - 2010 Files(\*.xlsx)\|\*.xlsx\|Excel 97 - 2003 Files(\*.xls)\|\*.xls\|All Files(\*.\*)\|\*.\*\"][]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [openFileDialog.ShowDialog()]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [If][ openFileDialog.File.Exists [Then]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [      spreadsheet.ImportFromExcel(openFileDialog.File.OpenRead())]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: You can also open the Excel document using ImportFromExcelCommand. When you execute the ImportFromExcelCommand it will display the Open dialog box. Using this Open dialog, you can open the Excel document in the Spreadsheet control.


[] 

[]{#related-topics}

