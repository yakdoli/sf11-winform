---
title: loadreportdefinitionfromstream.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadreportdefinitionfromstream.md
created_at: 2025-07-03
---








  









### LoadReportDefinitionFromStream {#loadreportdefinitionfromstream style="tab-stops: 0pt"}

You can load the OlapReport as a stream to the OlapDataManager using LoadReportDefinitionFromStream method. This contains two steps as follows:

1.   Loading the report stream

2.   Loading the specific report in that stream by giving its name

The following code snippet will illustrate the loading of the report definition from a stream:

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                            |
|                                                                                                                                                   |
| [olapDataManager.LoadReportDefinitionFromStream(reportStream);\                                                                                   |
| olapDataManager.LoadReport([\"SalesOn2003\"]);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[       ]                                                    |
|                                                                                                                                                  |
| [olapDataManager.LoadReportDefinitionFromStream(reportStream)\                                                                                   |
| olapDataManager.LoadReport([\"SalesOn2003\"])][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

Sequential Diagram

The following sequential diagram shows the workflow of OlapBase when user gives input as OlapReport.

{border="0"}

 

Figure 9: Olap Base sequential diagram

 

[]{#related-topics}

