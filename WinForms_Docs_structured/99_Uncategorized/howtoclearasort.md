---
title: howtoclearasort.md
original_path: WinForms_Docs/99_Uncategorized/howtoclearasort.md
created_at: 2025-08-05
---








  









## How to Clear a Sort? {#how-to-clear-a-sort style="tab-stops: 0pt"}

[] 

To clear all sorts, call the groupingEngine.TableDescriptor.SortedColumns.Clear method.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [// Removes all the sorting associated with the table.]                                                                                      |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Clear();]                        |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [// Removes the sorting of the column mentioned as argument.]                                                                                |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Remove(Name of the column); ][ \ |
| \                                                                                                                                                                                              |
| ]                                                                                                                                            |
|                                                                                                                                                                                                |
| [// Removes the sorting of the column mentioned as column index.]                                                                            |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.RemoveAt(index); ]               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes all the sorting associated.]                                                                              |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Clear()]    |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes the sorting of the column mentioned as argument.]                                                         |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Remove()]   |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes the sorting of the column mentioned as column index.]                                                     |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.RemoveAt()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To remove a particular sort, use groupingEngine.TableDescriptor.SortedColumns.Remove or groupingEngine.TableDescriptor.SortedColumns.RemoveAt.


 

 

 

[]{#related-topics}

