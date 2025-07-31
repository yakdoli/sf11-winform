---
title: calculatortextbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\calculatortextbox.md
created_at: 2025-07-03
---






##### Calculator Text Box {#calculator-text-box style="tab-stops: 0pt"}

[] 

The Calculator Text Box cell type is implemented as a drop-down container, embedded in the cell where the drop-down contains the calculator which displays the value in the cell.

 

The following code examples illustrate how to set the cell type to CalculatorTextBox.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].CalculatorTextBox);] |
|                                                                                                                                                                                                        |
| [CalculatorControl c2 = [new] CalculatorControl();]                                                                                           |
|                                                                                                                                                                                                        |
| [c2.BorderStyle = [Border3DStyle].RaisedOuter;]                                                                                            |
|                                                                                                                                                                                                        |
| [c2.BackColor = [Color].BlanchedAlmond;]                                                                                                   |
|                                                                                                                                                                                                        |
| [style = gridControl1\[6, 2\];]                                                                                                                                    |
|                                                                                                                                                                                                        |
| [style.CellType = [CustomCellTypes].CalculatorTextBox.ToString();]                                                                         |
|                                                                                                                                                                                                        |
| [style.Control = c2;]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [RegisterCellModel.GridCellType([Me].gridControl1, CustomCellTypes.CalculatorTextBox)]                                              |
|                                                                                                                                                                                              |
| [Dim][ c2 [As] CalculatorControl = [New] CalculatorControl()] |
|                                                                                                                                                                                              |
| [c2.BorderStyle = Border3DStyle.RaisedOuter]                                                                                                             |
|                                                                                                                                                                                              |
| [c2.BackColor = Color.BlanchedAlmond]                                                                                                                    |
|                                                                                                                                                                                              |
| [style = gridControl1(6, 2)]                                                                                                                             |
|                                                                                                                                                                                              |
| [style.CellType = CustomCellTypes.CalculatorTextBox.ToString()]                                                                                          |
|                                                                                                                                                                                              |
| [style.Control = c2]                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][106][: Calculator Text Box Cell]*

 

[]{#p95} 

 

[]{#related-topics}

