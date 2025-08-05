---
title: retrievethemdxqueryofacurrentreport.md
original_path: WinForms_Docs/99_Uncategorized/retrievethemdxqueryofacurrentreport.md
created_at: 2025-08-05
---








  









## Retrieve the MDX Query of a CurrentReport {#retrieve-the-mdx-query-of-a-currentreport style="tab-stops: 0pt"}

The MDX query of a current report is used to display data in Grid/Chart control and it can be retrieved by calling the GetMdxQuery() method.

The following code explains how to retrieve MDX Query from the OlapDataManager:

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| [olapDataManager.GetMDXQuery();]  |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| **[\[VB\]]**                      |
|                                                                       |
| [olapDataManager.GetMDXQuery()]   |
+-----------------------------------------------------------------------+

 

In Silverlight:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [string][ currentMdxQuery =][ null][;] |
|                                                                                                                                                                                                                                              |
| [//// Invoke the service call to retrieve the MDX query from the Server based on current report.][ ]                                     |
|                                                                                                                                                                                                                                              |
| [\_olapDataManager.GetMdxQuery(\_olapDataManager.CurrentReport);]                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [\_olapDataManager.MdxQueryObtained += () =\>]                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                              |
| [    ////MDX Query retrieved.]                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [ ][   currentMdxQuery = \_olapDataManager.CurrentReport.CurrentMdxQuery;]                                                               |
|                                                                                                                                                                                                                                              |
| [};][]                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [Dim][ currentMdxQuery ][As][ ][String] |
|                                                                                                                                                                                                                                                                    |
| [\'Invoke the service call to retrieve the MDX query from the Server based on current report.][ ]                                                              |
|                                                                                                                                                                                                                                                                    |
| [\_olapDataManager.GetMdxQuery(\_olapDataManager.CurrentReport)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [\_olapDataManager.MdxQueryObtained += ][Function][() ]                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [\'MDX Query retrieved.][]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [currentMdxQuery = \_olapDataManager.CurrentReport.CurrentMdxQuery]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [End Function][]                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[]{#related-topics}

