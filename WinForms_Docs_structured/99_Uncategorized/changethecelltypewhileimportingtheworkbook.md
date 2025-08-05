---
title: changethecelltypewhileimportingtheworkbook.md
original_path: WinForms_Docs/99_Uncategorized/changethecelltypewhileimportingtheworkbook.md
created_at: 2025-08-05
---






##### Change the CellType while importing the Workbook {#change-the-celltype-while-importing-the-workbook style="tab-stops: 0pt"}

You can also change the cell type and other styles while importing the workbook to GridControl, for that you have to pass the delegate handler in the importing method as shown in the following code snippet.

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                          |
| [this][.gridControl.Model.ImportFromExcel([new] [MemoryStream](file), ImportHandler);] |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Then by using the ImportHandler method you can change the particular Cell Type and styles like background and font styles. When this event was handled, it will not import the data from the excel cell only the user specified data will be applied in the Grid. You can change the cell type as shown in the following code snippet

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [private][ [void] ImoprtHandeler([object] sender, [ImportingCellFromExcelEventArgs] e)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [if][ (e.Range.AddressLocal == [\"C5\"])]                                                                                         |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [e.Cell.CellType = [\"Static\"];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| [e.Cell.CellValue = e.Range.DisplayText;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| [e.Cell.Background = [new] [SolidColorBrush]([Colors].Blue);]                                                                         |
|                                                                                                                                                                                                                                                |
| [e.Cell.Font.FontSize = 15;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [e.Cell.Font.FontWeight = [FontWeights].Bold;]                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [e.Handled = [true];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

