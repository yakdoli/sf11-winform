---
title: paging6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\paging6.md
created_at: 2025-07-03
---








  









### Paging {#paging style="tab-stops: 0pt"}

Paging enables the user to view large records by breaking them into smaller segments.

Paging feature can be achieved by setting the *EnablePaging* property to *true* in a report.

The following code snippet demonstrates how to enable paging in current report:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [olapDataManager.CurrentReport.EnablePaging = ][true][;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| [olapDataManager.CurrentReport.EnablePaging = ][True][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The user can customize the page settings such as current page, page size (for both row and column).

The following code explains how to customize current page and page size settings:

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                             |
| [olapDataManager.CurrentReport.PagerOptions.CategorialCurrentPage = 1;] |
|                                                                                                             |
| [olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2;]     |
|                                                                                                             |
| [olapDataManager.CurrentReport.PagerOptions.CategorialPageSize = 50;]   |
|                                                                                                             |
| [olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50;]       |
+-------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                           |
|                                                                                                            |
| [olapDataManager.CurrentReport.PagerOptions.CategorialCurrentPage = 1] |
|                                                                                                            |
| [olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2]     |
|                                                                                                            |
| [olapDataManager.CurrentReport.PagerOptions.CategorialPageSize = 50]   |
|                                                                                                            |
| [olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50]       |
+------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

