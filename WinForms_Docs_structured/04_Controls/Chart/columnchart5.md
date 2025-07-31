---
title: columnchart5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\columnchart5.md
created_at: 2025-07-03
---








  









### Column Chart {#column-chart style="tab-stops: 0pt"}

Column chart is the default chart type. Column charts are often used for comparison analysis over a different period of time. []{#OLE_LINK2}[The following code snippet shows how to select this chart type.]{#OLE_LINK1}

[] 

4.   Add an Instance of **OLAP Chart** with **ShowSeriesToolTip** set to "true", to an application.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][sfchart][:][OlapChart][ OlapChartType][=\"Column\" /\>]**[]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                 |
| [OlapChart][ olapChart1 = [new] [OlapChart]();]                            |
|                                                                                                                                                                                                                 |
| [//// Selecting the column chart.]                                                                                                                            |
|                                                                                                                                                                                                                 |
| [this][.olapChart1.OlapChartType = [OlapChartTypes].Column;][] |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ olapChart1 [As] ][OlapChart][ = [New] ][OlapChart][()] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Selecting the column chart.][]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.olapChart1.OlapChartType = ][OlapChartTypes][.Column][]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   []{#OLE_LINK7}[Create a report.]{#OLE_LINK6}

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [private][ [OlapReport] SimpleDimensions()]                      |
|                                                                                                                                                                               |
| [{\                                                                                                                                                                           |
|       [OlapReport] olapReport = [new] [OlapReport]();\                                                   |
|       olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                            |
|  \                                                                                                                                                                            |
|       [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                           |
|            \                                                                                                                                                                  |
|       [//// Specifying the Name for the Dimension Element]\                                                                                             |
|       dimensionElementColumn.Name = [\"Customer\"];\                                                                                                  |
|  \                                                                                                                                                                            |
|       dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                               |
|  \                                                                                                                                                                            |
|       dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                              |
|  \                                                                                                                                                                            |
|  \                                                                                                                                                                            |
|       [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                               |
|       measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\ |
|  \                                                                                                                                                                            |
|       [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                              |
|       [//// Specifying the Dimension Name]\                                                                                                             |
|       dimensionElementRow.Name = [\"Date\"];\                                                                                                         |
|       dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                         |
|  \                                                                                                                                                                            |
|       [//// Adding Measure Element]\                                                                                                                    |
|       olapReport.CategoricalElements.Add([new] [Item] { ElementValue = measureElementColumn });\                                 |
|  \                                                                                                                                                                            |
|       [//// Adding Column Members]\                                                                                                                     |
|       olapReport.CategoricalElements.Add([new] [Item] { ElementValue = dimensionElementColumn });\                               |
|             \                                                                                                                                                                 |
|       [//// Adding Row Members]\                                                                                                                        |
|       olapReport.SeriesElements.Add([new] [Item] { ElementValue = dimensionElementRow });\                                       |
|  \                                                                                                                                                                            |
|       [return] olapReport;\                                                                                                                              |
| }]                                                                                                                                        |
|                                                                                                                                                                               |
| []                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Function] SimpleDimensions() [As] ][OlapReport][]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] olapReport [As] OlapReport = [New] ][OlapReport][()]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CurrentCubeName = ][\"Adventure Works\"][]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] dimensionElementColumn [As] ][DimensionElement][ = [New] ][DimensionElement][()] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Specifying the Name for the Dimension Element]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.Name = ][\"Customer\"][]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.HierarchyName = ][\"Customer Geography\"][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementColumn.AddLevel(][\"Customer Geography\"][, ][\"Country\"][)]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] measureElementColumn [As] ][MeasureElements][ = [New] ][MeasureElements][()]     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = ][\"Internet Sales Amount\"][})]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Dim] dimensionElementRow [As] ][DimensionElement][ = [New] ][DimensionElement][()]    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Specifying the Dimension Name]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementRow.Name = ][\"Date\"][]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      dimensionElementRow.AddLevel(][\"Fiscal\"][,][ \"Fiscal Year\"][)]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding Measure Element]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = measureElementColumn})]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding Column Members]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.CategoricalElements.Add([New] Item [With] {.ElementValue = dimensionElementColumn})]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [\' Adding Row Members]]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      olapReport.SeriesElements.Add([New] Item [With] {.ElementValue = dimensionElementRow})]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [      [Return] olapReport]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Function]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Add the report to the OLAP DataManager and bind it with the chart.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                         |
|                                                                                                                                                                       |
| [      [this].olapDataManager.SetCurrentReport(][SimpleDimensions][());\ |
|       [this].olapChart1.OlapDataManager = olapDataManager;]                                                  |
|                                                                                                                                                                       |
| []                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                 |
|                                                                                                                                                                  |
| []                                                                                                              |
|                                                                                                                                                                  |
| [      [Me].olapDataManager.SetCurrentReport(SimpleDimensions())]                                       |
|                                                                                                                                                                  |
| [      [Me].olapChart1.OlapDataManager = olapDataManager][ ] |
|                                                                                                                                                                  |
| []                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following image shows a simple Column chart:

[] 

{border="0"}

 

Figure 16: A Simple Column Chart

[]{#related-topics}

