---
title: howtodisabletheresizingofrowsandcolumns.md
original_path: WinForms_Docs/99_Uncategorized/howtodisabletheresizingofrowsandcolumns.md
created_at: 2025-08-05
---






#### How to disable the resizing of rows and columns {#how-to-disable-the-resizing-of-rows-and-columns style="tab-stops: 0pt"}

[] 

This can be done using the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [// Code to disable the resizing of rows.]                                                                                                                           |
|                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.TableModel.Options.ResizeRowsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None;] |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Code to disable the column resizing]                                                                                                                              |
|                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.TableModel.Options.ResizeColsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [\'Code to disable the column resizing]                                                                                                                           |
|                                                                                                                                                                                                                     |
| [Me][.gridGroupingControl1.TableModel.Options.ResizeColsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [\'Code to disable the resizing of  rows.]                                                                                                                        |
|                                                                                                                                                                                                                     |
| [Me][.gridGroupingControl1.TableModel.Options.ResizeRowsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p647} 

 

[]{#related-topics}

