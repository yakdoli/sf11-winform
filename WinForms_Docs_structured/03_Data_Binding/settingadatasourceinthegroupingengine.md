---
title: settingadatasourceinthegroupingengine.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\settingadatasourceinthegroupingengine.md
created_at: 2025-07-03
---








  









### Setting a Datasource In the Grouping Engine {#setting-a-datasource-in-the-grouping-engine style="tab-stops: 0pt"}

[] 

Add the following grouping namespace for referring the assemblies deployed in the application.

 

{border="0"} Refer Deploying Essential Grouping section to know about deploying Essential Grouping.

 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
| []                                                                                                          |
|                                                                                                                                   |
| [using][ Syncfusion.Grouping;] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| []                                                                                                           |
|                                                                                                                                    |
| [Imports][ Syncfusion.Grouping] |
+------------------------------------------------------------------------------------------------------------------------------------+

 

Then create a **Grouping.Engine** object and set the ArrayList we created to be its data source.

 

! topic.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                  |
| [// Put this code in the Main function after Console.ReadLine().]                                                                              |
|                                                                                                                                                                                                  |
| [// Create a Grouping.Engine object.]                                                                                                          |
|                                                                                                                                                                                                  |
| [Engine groupingEngine = ][new][ Engine();] |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [// Set its data source.]                                                                                                                      |
|                                                                                                                                                                                                  |
| [groupingEngine.SetSourceList(list);]                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [Imports][ Syncfusion.Grouping]                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [\'\....]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Put this code in the Main function after Console.ReadLine().]                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [\' Create a Grouping.Engine object.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [Dim][ groupingEngine ][As New][ Engine()] |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Set its data source.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [groupingEngine.SetSourceList(list)]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

ArrayList of Objects is set as the datasource for the Grouping engine.

 

[]{#related-topics}

