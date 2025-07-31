---
title: drilldownsupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drilldownsupport1.md
created_at: 2025-07-03
---








  









## Drill Down Support {#drill-down-support style="tab-stops: 0pt"}

[] 

OLAP Chart for Silverlight can load multilevel data that can be displayed in detail by using the drill-up or drill-down feature so data can be visualized in each level of a hierarchy.

The code snippet displayed below provides data to render a chart and is added at the time of page load.

 

The code snippet is displayed below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [OlapReport olapReport = [new] OlapReport();]                                                                             |
|                                                                                                                                                                                    |
| [olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                  |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [DimensionElement dimensionElementColumn = [new] DimensionElement();]                                                     |
|                                                                                                                                                                                    |
| [//Specifying the Name for the Dimension Element]                                                                                |
|                                                                                                                                                                                    |
| [dimensionElementColumn.Name = [\"Customer\"];]                                                                        |
|                                                                                                                                                                                    |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\");]                                                                        |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [MeasureElements measureElementColumn = [new] MeasureElements();]                                                         |
|                                                                                                                                                                                    |
| [measureElementColumn.Elements.Add([new] MeasureElement { Name = [\"Internet Sales Amount\"] });] |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [DimensionElement dimensionElementRow = [new] DimensionElement();]                                                        |
|                                                                                                                                                                                    |
| [//Specifying the Dimension Name]                                                                                                |
|                                                                                                                                                                                    |
| [dimensionElementRow.Name = [\"Date\"];]                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Adding the level Elemnet along with the Hierarchy Name]                                                                       |
|                                                                                                                                                                                    |
| [dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                               |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [///][Adding Measure Element]                                                   |
|                                                                                                                                                                                    |
| [olapReport.CategoricalElements.Add(measureElementColumn);]                                                                                    |
|                                                                                                                                                                                    |
| [///][Adding Column Members]                                                    |
|                                                                                                                                                                                    |
| [olapReport.CategoricalElements.Add(dimensionElementColumn);]                                                                                  |
|                                                                                                                                                                                    |
| [///][Adding Row Members]                                                       |
|                                                                                                                                                                                    |
| [olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                          |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [return][ olapReport;]                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ olapReport [As] OlapReport = [New] OlapReport()]                         |
|                                                                                                                                                                                                                |
| [olapReport.CurrentCubeName = \"Adventure Works\"]                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ dimensionElementColumn [As] DimensionElement = [New] DimensionElement()] |
|                                                                                                                                                                                                                |
| [\'Specifying the Name for the Dimension Element]                                                                                                            |
|                                                                                                                                                                                                                |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                               |
|                                                                                                                                                                                                                |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ measureElementColumn [As] MeasureElements = [New] MeasureElements()]     |
|                                                                                                                                                                                                                |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Internet Sales Amount\"})]                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ dimensionElementRow [As] DimensionElement = [New] DimensionElement()]    |
|                                                                                                                                                                                                                |
| [\'Specifying the Dimension Name]                                                                                                                            |
|                                                                                                                                                                                                                |
| [dimensionElementRow.Name = \"Date\"]                                                                                                                                      |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'Adding the level Element along with the Hierarchy Name]                                                                                                   |
|                                                                                                                                                                                                                |
| [dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                                                |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'\'\'Adding Measure Element]                                                                                                                               |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                                 |
|                                                                                                                                                                                                                |
| [\'\'\'Adding Column Members]                                                                                                                                |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                               |
|                                                                                                                                                                                                                |
| [\'\'\'Adding Row Members]                                                                                                                                   |
|                                                                                                                                                                                                                |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                       |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Return][ olapReport]                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screenshots show the column charts with the above settings:

 

a)   Before drill down.

 

[] 

{border="0"}

 

Figure 38: Before Drill Down

 

b)   After drill down

[] 

{border="0"}

 

Figure 39: After Drill Down

***[]*** 

Sample Location

A sample demo is available at the following location:

[] 

..\\Syncfusion\\\<Version Number\>\\BI\\Silverlight\\Syncfusion.OlapChart.Silverlight.Samples\\Syncfusion.OlapChart.Silverlight.Samples\\Samples\\Creating Reports

 

[]{#related-topics}

