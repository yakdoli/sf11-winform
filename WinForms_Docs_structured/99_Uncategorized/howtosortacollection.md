---
title: howtosortacollection.md
original_path: WinForms_Docs/99_Uncategorized/howtosortacollection.md
created_at: 2025-08-05
---








  









## How to Sort a Collection? {#how-to-sort-a-collection style="tab-stops: 0pt"}

 

To sort your data, add the name of the property that you want to sort to the **Engine.TableDescriptor.SortedColumns** collection.

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [// Sort column A.]                                                   |
|                                                                                                                         |
| [groupingEngine.TableDescriptor.SortedColumns.Add([\"A\"]);] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                          |
|                                                                                                             |
| []                                                        |
|                                                                                                             |
| [\' Sort column A.]                                       |
|                                                                                                             |
| [groupingEngine.TableDescriptor.SortedColumns.Add(\"A\")] |
+-------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

