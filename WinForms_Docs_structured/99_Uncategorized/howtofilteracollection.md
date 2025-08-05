---
title: howtofilteracollection.md
original_path: WinForms_Docs/99_Uncategorized/howtofilteracollection.md
created_at: 2025-08-05
---








  









## How to Filter a Collection? {#how-to-filter-a-collection style="tab-stops: 0pt"}

 

To add a filter condition, add a **RecordFilterDescriptor** to the **Engine.TableDescriptor.RecordFilters** collection. The constructor on the **RecordFilterDescription** takes an expression, \"\[D\] LIKE \'d1\'\". This expression will be **True** only for those items in the list where the string property D has the value d1. Here are some other valid expressions where B is an integer property:

 

[·      ]\"\[B\] = 5 OR \[B\] \< 0\"

[·      ]\"\[D\] LIKE \'d1\' OR \[B\] = 2\"

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [// Filter on \[D\] = d1]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [RecordFilterDescriptor][ rfd = [new] [RecordFilterDescriptor]([\"\[D\] LIKE \'d1\'\"]);] |
|                                                                                                                                                                                                                                                                                 |
| [this][.groupingEngine.TableDescriptor.RecordFilters.Add(rfd);]                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                            |
| [\' Filter on \[D\] = d1]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ rfd ][As New][ RecordFilterDescriptor(\"\[D\] LIKE \'d1\'\")] |
|                                                                                                                                                                                                                                                                                                                                            |
| [Me][.groupingEngine.TableDescriptor.RecordFilters.Add(rfd)]                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

