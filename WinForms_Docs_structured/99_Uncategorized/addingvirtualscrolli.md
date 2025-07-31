---
title: addingvirtualscrolli.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingvirtualscrolli.md
created_at: 2025-07-03
---








  





### Adding Virtual Scrolling to an Application {#adding-virtual-scrolling-to-an-application style="tab-stops: 0pt"}

Virtual scrolling can be added to an application through the following code snippet.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Olap().OlapGrid([\"olapgrid\"], ViewData\[[\"DataManager\"]\] [as] [OlapDataManager]).EnableVirtualScrolling([true]) [%\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[\[RAZOR\]                           ]**                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [@(][Html.Syncfusion().Olap().OlapGrid([\"olapgrid\"], ViewData\[[\"DataManager\"]\] [as] OlapDataManager).EnableVirtualScrolling([true]).ToMvcHtmlString()[)]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                        |
| [//NOTE: Consider the following paging settings as well.]**[]**                                  |
|                                                                                                                                                                                        |
| [OlapReport][ olapReport = [new] [OlapReport]();] |
|                                                                                                                                                                                        |
| [olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                      |
|                                                                                                                                                                                        |
| [olapReport.EnablePaging = [true];]                                                                                           |
|                                                                                                                                                                                        |
| [olapReport.PagerOptions.SeriesPageSize = 14;]                                                                                                     |
|                                                                                                                                                                                        |
| [olapReport.PagerOptions.CategorialPageSize = 10;]                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [\'NOTE: Consider the following paging settings as well.]                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [Dim][ olapReport [As] [OlapReport] = [New] [OlapReport]()] |
|                                                                                                                                                                                                                                            |
| [olapReport.CurrentCubeName = [\"Adventure Works\"]]                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [olapReport.EnablePaging = [True]]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [olapReport.PagerOptions.SeriesPageSize = 14]                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [olapReport.PagerOptions.CategorialPageSize = 10]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 15: Virtual Scrolling**[]**

 

[]{#related-topics}

