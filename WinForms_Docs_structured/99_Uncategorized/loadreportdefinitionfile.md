---
title: loadreportdefinitionfile.md
original_path: WinForms_Docs/99_Uncategorized/loadreportdefinitionfile.md
created_at: 2025-08-05
---








  









### LoadReportDefinitionFile {#loadreportdefinitionfile style="tab-stops: 0pt"}

You can bind the OlapReport as xml file to OlapDataManager using the LoadReportDefinitionFile method. This contains two steps as follows:

1.   Loading the report definition file and

2.   Loading a specific report in that file by giving its name

 

The following code snippet will illustrate the loading of the report definition file:

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                            |
|                                                                                                                                                   |
| [olapDataManager.LoadReportDefinitionFile([@\"C:\\SampleReports\\SalesAnalysis.xml\"]);\                                  |
| olapDataManager.LoadReport([\"SalesOn2003\"]);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[      ]                                                     |
|                                                                                                                                                  |
| [olapDataManager.LoadReportDefinitionFile([\"C:\\SampleReports\\SalesAnalysis.xml\"])\                                   |
| olapDataManager.LoadReport([\"SalesOn2003\"])][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

