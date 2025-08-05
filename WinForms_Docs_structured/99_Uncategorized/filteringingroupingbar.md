---
title: filteringingroupingbar.md
original_path: WinForms_Docs/99_Uncategorized/filteringingroupingbar.md
created_at: 2025-08-05
---








  









### Filtering in Grouping Bar {#filtering-in-grouping-bar style="tab-stops: 0pt"}

Data filtering displays only a subset of data that meets criteria specified by you and hides data that you don't want to be displayed. The items present in the filter header area, column header area and row header area, provide the option of run-time filtering which is represented as a funnel symbol on it. On clicking the symbol, it opens a filter popup which displays a list of elements through which filtering can be applied.

[] 

{border="0"}

Figure 11: Filter Popup

 

The following code example illustrates how to disable the filtering in the Grouping Bar.

 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| [// Disabling Filtering][]              |
|                                                                                                                               |
| [pivotGridControl1.AllowFiltering = [false];[]] |
|                                                                                                                               |
| []                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [// Disabling Filtering]**[]** |
|                                                                                                                      |
| [pivotGridControl1.AllowFiltering = [False] ]               |
|                                                                                                                      |
| []                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

