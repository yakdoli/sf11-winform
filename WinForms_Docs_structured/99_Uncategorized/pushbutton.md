---
title: pushbutton.md
original_path: WinForms_Docs/99_Uncategorized/pushbutton.md
created_at: 2025-08-05
---






##### Push Button {#push-button style="tab-stops: 0pt"}

[] 

To display a Push Button in a grid cell, use the **PushButton** cell type. To catch and handle a user, click a button, and you can add a **GridControl.CellButtonClicked** event handler. The event arguments passed into your handler will include the row and column of the click. The **GridStyleInfo** properties that control the behavior of a Push Button cell are listed in the following table.

[] 


  ---------------- ---------------------------------------------------------
  Property         Description
  CellAppearance   Specifies whether the button is raised, sunken or flat.
  CellType         Set to \"PushButton\" for a push button control.
  ---------------- ---------------------------------------------------------


[] 

The following code example illustrates how to set the cell type to PushButton.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [gridControl1\[rowIndex,colIndex\].Description = [\"PushButton1\"];]                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [gridControl1\[rowIndex,colIndex\].CellType = [\"PushButton\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [gridControl1\[rowIndex,colIndex \].CellAppearance = [GridCellAppearance].Raised;]                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [// To catch a click, hook up a CellButtonClicked handler.]                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [gridControl1.CellButtonClicked += [new] [GridCellButtonClickedEventHandler](gridControl1_CellButtonClicked);]                                                               |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [// Add a handler.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [private][ [void] gridControl1_CellButtonClicked([object] sender, [GridCellButtonClickedEventArgs] e)] |
|                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [MessageBox][.Show([\"You clicked row\"]  + e.RowIndex.ToString() + [\"col\"]  + e.ColIndex.ToString());]             |
|                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [gridControl1(rowIndex, colIndex).Description = [\"PushButton1\"]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [gridControl1(rowIndex, colIndex).CellType = [\"PushButton\"]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [gridControl1(rowIndex, colIndex).CellAppearance = GridCellAppearance.Raised]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\' To catch a click, hook up a CellButtonClicked handler.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [AddHandler][ gridControl1.CellButtonClicked, [AddressOf] gridControl1_CellButtonClicked]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\' Add a handler.]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] gridControl1_CellButtonClicked([ByVal] sender [As] [Object], [ByVal] e [As] GridCellButtonClickedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [MessageBox.Show([\"You clicked row \"] + e.RowIndex.ToString() + [\"  col \"] + e.ColIndex.ToString())]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][87][: Push Button Cells]*

 

[]{#p63} 

 

[]{#related-topics}

