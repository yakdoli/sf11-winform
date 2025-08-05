---
title: howtoclearagrouping.md
original_path: WinForms_Docs/99_Uncategorized/howtoclearagrouping.md
created_at: 2025-08-05
---








  









## How to Clear a Grouping? {#how-to-clear-a-grouping style="tab-stops: 0pt"}

[] 

To clear all grouping, call the groupingEngine.TableDescriptor.GroupedColumns.Clear method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                                            |
|                                                                                                                                                                     |
| [// Removes the grouping of all the grouped columns.]                                                             |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();  ]        |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [// Removes grouping of the column mentioned as an argument.]                                                     |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove(Name);  ]   |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [// Removes grouping of the column mentioned as column index.]                                                    |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(index); ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                                                 |
|                                                                                                                                                                          |
| [\' Removes the grouping of all the grouped columns.]                                                                  |
|                                                                                                                                                                          |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()  ]  |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [\' Removes grouping of the column mentioned as an argument.]                                                          |
|                                                                                                                                                                          |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove();]  |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [\' Removes grouping of the column mentioned as column index.]                                                         |
|                                                                                                                                                                          |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To remove a particular grouping, use groupingEngine.TableDescriptor.GroupedColumns.Remove or groupingEngine.TableDescriptor.SortedColumns.RemoveAt.


[]{#related-topics}

