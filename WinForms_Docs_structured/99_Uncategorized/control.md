---
title: control.md
original_path: WinForms_Docs/99_Uncategorized/control.md
created_at: 2025-08-05
---






##### Control {#control style="tab-stops: 0pt"}

[] 

You can place an arbitrary control in a grid cell through the **Control** cell type. This cell type differs from most other cell types shipped with Essential Grid in which it cannot be shared among several cells. The Control cell type requires you to instantiate a control object for each cell that uses this cell type, and set that object to *style.Control*. A different control object is required for every cell that makes use of the Control cell type.

[] 

The following code example illustrates how to set the cell type to Control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| []                                                                                                                                  |
|                                                                                                                                                                                       |
| [// Set up a Control Cell.]                                                                                                         |
|                                                                                                                                                                                       |
| [this][.radioButton1.Checked = [true]; ]                                    |
|                                                                                                                                                                                       |
| [this][.gridControl1.CoveredRanges.Add([GridRangeInfo].Cells(2,2,8,2));] |
|                                                                                                                                                                                       |
| [this][.gridControl1.ColWidths\[2\] = 200; ]                                                     |
|                                                                                                                                                                                       |
| [this][.gridControl1\[2,2\].CellType = [\"Control\"]; ]                  |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [// Set the control object.]                                                                                                        |
|                                                                                                                                                                                       |
| [this][.gridControl1\[2,2\].Control = [this].dataPanel;]                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [\' Set up a Control Cell.]                                                                                   |
|                                                                                                                                                                 |
| [Me][.radioButton1.Checked = [True]]                  |
|                                                                                                                                                                 |
| [Me][.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(2, 2, 8, 2))]     |
|                                                                                                                                                                 |
| [Me][.gridControl1.ColWidths(2) = 200]                                     |
|                                                                                                                                                                 |
| [Me][.gridControl1(2, 2).CellType = [\"Control\"]] |
|                                                                                                                                                                 |
| []                                                                                                          |
|                                                                                                                                                                 |
| [\' Set the control object.]                                                                                  |
|                                                                                                                                                                 |
| [Me][.gridControl1(2, 2).Control = [Me].dataPanel]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot shows a panel holding two radio buttons and a push button in the cell.

[] 

{border="0"}

[] 

Figure 77: Control Cells

 

[]{#p54} 

 

[]{#related-topics}

