---
title: exportingmultiplegrids.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\exportingmultiplegrids.md
created_at: 2025-07-03
---






#### Exporting Multiple Grids {#exporting-multiple-grids style="tab-stops: 0pt"}

[] 

It is possible to save multiple grids to a single XLS file as worksheets. The following code example illustrates how to do this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [using][ Syncfusion.XlsIO;]                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [using][ Syncfusion.GridExcelConverter;]                                                                                                           |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [private][ [void] buttonExport_Click([object] sender, System.[EventArgs] e)]     |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [    [SaveFileDialog] saveFileDialog = [new] [SaveFileDialog]();]                                                              |
|                                                                                                                                                                                                                                         |
| [    saveFileDialog.Filter = [\"Files(\*.XLS)\|\*.XLS\"];]                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [    saveFileDialog.AddExtension = [true];]                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [    saveFileDialog.DefaultExt = [\".XLS\"];]                                                                                                                               |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [    [if](saveFileDialog.ShowDialog() == [DialogResult].OK && saveFileDialog.CheckPathExists)]                                                         |
|                                                                                                                                                                                                                                         |
| [    {]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [        [GridExcelConverterControl] gec = [new] [GridExcelConverterControl]();]                                               |
|                                                                                                                                                                                                                                         |
| [        IWorkbook workBook = ExcelUtils.CreateWorkbook([new] [string]\[\] {[\"Sheet1\"],[\"Sheet2\"]});] |
|                                                                                                                                                                                                                                         |
| [        gec.GridToExcel([this].gridControl1.Model, workBook.Worksheets\[0\]);]                                                                                                |
|                                                                                                                                                                                                                                         |
| [        gec.GridToExcel([this].gridControl2.Model, workBook.Worksheets\[1\]);]                                                                                                |
|                                                                                                                                                                                                                                         |
| [        workBook.SaveAs(saveFileDialog.FileName);]                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [        workBook.Close();]                                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [        ExcelUtils.ThrowNotSavedOnDestroy = [false];]                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [    }]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [Imports][ Syncfusion.XlsIO]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [Imports][ Syncfusion.GridExcelConverter]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] buttonExport_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                        |
| [Dim][ saveFileDialog [As] SaveFileDialog = [New] SaveFileDialog()]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| [saveFileDialog.Filter = [\"Files(\*.XLS)\|\*.XLS\"]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [saveFileDialog.AddExtension = [True]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                        |
| [saveFileDialog.DefaultExt = [\".XLS\"]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [If][ saveFileDialog.ShowDialog() = DialogResult.OK [And] Also saveFileDialog.CheckPathExists [Then]]                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [Dim][ gec [As] GridExcelConverterControl = [New] GridExcelConverterControl]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [Dim][ workbook [As] IWorkbook = ExcelUtils.CreateWorkbook([New] [String]() {[\"Sheet1\"], [\"Sheet2\"]})]         |
|                                                                                                                                                                                                                                                                                                                        |
| [gec.GridToExcel([Me].gridControl1.Model, workBook.Worksheets(0))]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [gec.GridToExcel([Me].gridDataBoundGrid1.Model, workbook.Worksheets(1))]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [workbook.SaveAs(saveFileDialog.FileName)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [workBook.Close()]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [ExcelUtils.ThrowNotSavedOnDestroy = [False]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

