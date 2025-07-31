---
title: howtogroupacolumnprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogroupacolumnprogrammatically.md
created_at: 2025-07-03
---






#### How to group a column programmatically {#how-to-group-a-column-programmatically style="tab-stops: 0pt"}

[] 

To group a column programmatically, use the following code.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [//Show the GroupDropArea]                                                                                                                                           |
|                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.ShowGroupDropArea = [true];]                                                    |
|                                                                                                                                                                                                                        |
| [// Group by \"Col1\"]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Col1\"], ListSortDirection.Ascending);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [\'Show the GroupDropArea]                                                                                                                                        |
|                                                                                                                                                                                                                     |
| [Me][.gridGroupingControl1.ShowGroupDropArea = [True]]                                                    |
|                                                                                                                                                                                                                     |
| [\' Group by \"Col1\"]                                                                                                                                            |
|                                                                                                                                                                                                                     |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Col1\"], ListSortDirection.Ascending)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p650} 

 

[]{#related-topics}

