---
title: howtobindadatasourcetothegroupingengine.md
original_path: WinForms_Docs/03_Data_Binding/howtobindadatasourcetothegroupingengine.md
created_at: 2025-08-05
---








  









## How to Bind a Datasource to the Grouping Engine? {#how-to-bind-a-datasource-to-the-grouping-engine style="tab-stops: 0pt"}

 

Essential Grouping can use any **IList** object holding objects and a common **System.Type** as its datasource. The public properties of the common type can be used to group, sort and summarize the data in the IList.

 

Example

[] 

The following code shows how to set an IList object to be the data source of a **GroupingEngine** object. Within Essential Grouping, the items in your IList datasource are referred to as records.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [using][ Syncfusion.Grouping;]                                                          |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Create a Grouping.Engine object.]                                                                                      |
|                                                                                                                                                                              |
| [Engine][ groupingEngine = [new] [Engine]();] |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Set its datasource.]                                                                                                   |
|                                                                                                                                                                              |
| [groupingEngine.SetSourceList(list);]                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| **[ ]**[Imports][ Syncfusion.Grouping]                                        |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Create a Grouping.Engine object.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [Dim][ groupingEngine ][As New][ Engine()] |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Set its datasource.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [groupingEngine.SetSourceList(list)]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

