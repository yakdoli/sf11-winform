---
title: howtogroupacollection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogroupacollection.md
created_at: 2025-07-03
---








  









## How to Group a Collection? {#how-to-group-a-collection style="tab-stops: 0pt"}

 

To sort your data, add the name of the property you want to sort to the **Engine.TableDescriptor.GroupedColumns** collection. 

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                          |
|                                                                                                                                          |
| []                                                                     |
|                                                                                                                                          |
| [// Group column A.]                                                   |
|                                                                                                                                          |
| [groupingEngine.TableDescriptor.GroupedColumns.Add([\"A\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                           |
|                                                                                                                              |
| []                                                         |
|                                                                                                                              |
| [\' Group column A.]                                       |
|                                                                                                                              |
| [groupingEngine.TableDescriptor.GroupedColumns.Add(\"A\")] |
+------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

