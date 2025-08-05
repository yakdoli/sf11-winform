---
title: dropdowngridcell.md
original_path: WinForms_Docs/04_Controls/Grid/dropdowngridcell.md
created_at: 2025-08-05
---






##### Drop-Down Grid Cell {#drop-down-grid-cell style="tab-stops: 0pt"}

[] 

Essential Grid has flexible support for displaying drop-down grids in cells. It uses a custom cell derived from the **GridDropDownGridCellModel**/**GridDropDownGridCellRenderer** classes to display a drop-down grid. The GridDropDownGridCellModel gets an instance of the GridControlBase, and displays it through the GridDropDownGridCellRenderer.

 

The actions mentioned can be performed by using the following code examples.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Create and register drop-down grid cells.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [DropDownGridCellModel][ aModel = [new] [DropDownGridCellModel]([this].gridControl1.Model);] |
|                                                                                                                                                                                                                                                        |
| [aModel.EmbeddedGrid = GridA;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [gridControl1.CellModels.Add([\"GridADropCell\"], aModel);]                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Set the drop-downs in the cell.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [this][.gridControl1\[rowIndex,1\].Text = [\"Grid A\"];              ]                                                                    |
|                                                                                                                                                                                                                                                        |
| [this][.gridControl1\[rowIndex,1\].CellType = [\"GridADropCell\"];]                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [\' Create and register drop-down grid cells.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [Dim][ aModel [As] DropDownGridCellModel = [New] DropDownGridCellModel([Me].gridControl1.Model)] |
|                                                                                                                                                                                                                                                      |
| [aModel.EmbeddedGrid = GridA]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [gridControl1.CellModels.Add([\"GridADropCell\"], aModel)]                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [\' Set the drop-downs in the cell.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [Me][.gridControl1(rowIndex,1).Text = [\"Grid A\"]]                                                                                     |
|                                                                                                                                                                                                                                                      |
| [Me][.gridControl1(rowIndex,1).CellType = [\"GridADropCell\"]]                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][116][: Drop-Down Grid Cell]*

 

[]{#p105} 

 

[]{#related-topics}

