---
title: makingachangetoareadonlycell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\makingachangetoareadonlycell.md
created_at: 2025-07-03
---






##### Making a Change to a ReadOnly Cell {#making-a-change-to-a-readonly-cell style="tab-stops: 0pt"}

[] 

If you set the Read-Only behavior, the user will be able to type in the cell and he will also not be able to change the cell\'s value programmatically. So, to make changes to a Read-Only cell, you must use the **GridControl.IgnoreReadOnly** property which, will allow you to change a Read-Only cell.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [this][.gridControl1\[1,1\].ReadOnly = ][true][; ] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [// Cell (1,1) has been set to Read-only. ]                                                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [// To change its value, you need to use the IgnoreReadOnly property.]                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [this][.gridControl1.IgnoreReadOnly = ][true][;]   |
|                                                                                                                                                                                                                                                          |
| [  ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [// Turn off Read-only checking.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [this][.gridControl1\[1,1\].CellValue = 256; ]                                                                                                        |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [// Now you can change the cell value.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [// Turn on Read-only checking.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [this][.gridControl1.IgnoreReadOnly = ][false][;]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1(1, 1).ReadOnly = ][True][ ]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Cell (1,1) has been set to Read-only.]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [\' To change its value, you need to use the IgnoreReadOnly property.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.IgnoreReadOnly = ][True][   ]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Turn off Read-only checking.]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1(1, 1).CellValue = 256  ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Now you can change the cell value.]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Turn on Read-only checking.]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.][Me][.GridControl1.IgnoreReadOnly = ][False][   ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p294} 

 

[]{#related-topics}

