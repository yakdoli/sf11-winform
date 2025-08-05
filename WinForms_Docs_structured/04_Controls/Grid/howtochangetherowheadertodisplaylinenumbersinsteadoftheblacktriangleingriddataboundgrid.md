---
title: howtochangetherowheadertodisplaylinenumbersinsteadoftheblacktriangleingriddataboundgrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtochangetherowheadertodisplaylinenumbersinsteadoftheblacktriangleingriddataboundgrid.md
created_at: 2025-08-05
---








  









### How to change the row header to display line numbers instead of the black triangle in GridDataBoundGrid {#how-to-change-the-row-header-to-display-line-numbers-instead-of-the-black-triangle-in-griddataboundgrid style="tab-stops: 0pt"}

[] 

You can achieve this by setting the row header base style to *Header*, and handling the **PrepareViewStyleInfo** event handler to set the line numbers. Refer the below code snippet which illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [// In the Form Load]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)]                                 |
|                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [this][.gridDataBoundGrid1.DataSource = GetTable();]                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [this][.gridDataBoundGrid1.BaseStylesMap\[[\"Row Header\"]\].StyleInfo.CellType = [\"Header\"];]                      |
|                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [// GridPrepareViewStyleInfo]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [private][ [void] grid_PrepareViewStyleInfo([object] sender, [GridPrepareViewStyleInfoEventArgs] e)] |
|                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [if][ (e.ColIndex == 0 && e.RowIndex \> 0)]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [e.Style.Text = e.RowIndex.ToString();]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                          |
| [e.Style.Font.Bold = [false];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' In the Form Load]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.gridDataBoundGrid1.DataSource = GetTable()]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.gridDataBoundGrid1.BaseStylesMap([\"Row Header\"]).StyleInfo.CellType = [\"Header\"]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub] [\'Form1_Load]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' GridPrepareViewStyleInfo]                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] gridDataBoundGrid1_PrepareViewStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Grid.GridPrepareViewStyleInfoEventArgs) [Handles] gridDataBoundGrid1.PrepareViewStyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.ColIndex = 0 [AndAlso] e.RowIndex \> 0 [Then]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.Text = e.RowIndex.ToString()]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.Font.Bold = [False]]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p588} 

 

[]{#related-topics}

