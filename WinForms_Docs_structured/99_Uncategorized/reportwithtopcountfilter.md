---
title: reportwithtopcountfilter.md
original_path: WinForms_Docs/99_Uncategorized/reportwithtopcountfilter.md
created_at: 2025-08-05
---






##### Report with Top count Filter {#report-with-top-count-filter style="tab-stops: 0pt"}

 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                               |
|                                                                                                                                                      |
| [OlapReport][ olapReport = [new] [OlapReport]();\   |
| olapReport.Name = [\"Customer Report\"];\                                                                                    |
| olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                         |
|  \                                                                                                                                                   |
| [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\        |
| [//Specifying the Name for the Dimension Element]\                                                                             |
| dimensionElementColumn.Name = [\"Customer\"];\                                                                               |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                           |
|  \                                                                                                                                                   |
| [//Creating Measure Element]\                                                                                                  |
| [MeasureElements] measureElementColumn = [new] [MeasureElements]();\            |
| measureElementColumn.Elements.Add([new] [MeasureElement] { Name = ] |
|                                                                                                                                                      |
| [                                                [\"Internet Sales Amount\"] });\                                            |
|  \                                                                                                                                                   |
| [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\           |
| [//Specifying the Dimension Name]\                                                                                             |
| dimensionElementRow.Name = [\"Date\"];\                                                                                      |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                      |
|  \                                                                                                                                                   |
| [//Filter the top 5 elements of \"Internet Sales Amount\".]\                                                                   |
| [TopCountElement] topCountElement = [new] ]                         |
|                                                                                                                                                      |
| [TopCountElement][([AxisPosition].Categorical, 5);\                      |
| topCountElement.MeasureName = [\"Internet Sales Amount\"];\                                                                  |
|  \                                                                                                                                                   |
| [///][ Adding Column Members]\                                                                            |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                         |
| [///][Adding Measure Element]\                                                                            |
| olapReport.CategoricalElements.Add(measureElementColumn);\                                                                                           |
| [///][Adding Measure Element]\                                                                            |
| olapReport.CategoricalElements.Add(topCountElement);\                                                                                                |
| [///][Adding Row Members]\                                                                                |
| olapReport.SeriesElements.Add(dimensionElementRow);]                                                             |
|                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                      |
| []                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                               |
| ][Dim][ olapReport [As] OlapReport = [New] OlapReport()]      |
|                                                                                                                                                                                                                                  |
| [olapReport.Name = [\"Customer Report\"]][]                                                                                      |
|                                                                                                                                                                                                                                  |
| [olapReport.CurrentCubeName = \"Adventure Works\"]                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [Dim][ dimensionElementColumn [As] DimensionElement = [New] DimensionElement()]                   |
|                                                                                                                                                                                                                                  |
| [\'Specifying the Name for the Dimension Element][]                                                                                        |
|                                                                                                                                                                                                                                  |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                                       |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\'Creating Measure Element][]                                                                                                             |
|                                                                                                                                                                                                                                  |
| [Dim][ measureElementColumn [As] MeasureElements = [New] MeasureElements()]                       |
|                                                                                                                                                                                                                                  |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Internet Sales Amount\"})]                                               |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [Dim][ dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                      |
|                                                                                                                                                                                                                                  |
| [\'Specifying the Dimension Name][]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [dimensionElementRow.Name = \"Date\"]                                                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\'Filter the top 5 elements of \"Internet Sales Amount\".][]                                                                              |
|                                                                                                                                                                                                                                  |
| [Dim][ topCountElement [As] TopCountElement = [New] TopCountElement(AxisPosition.Categorical, 5)] |
|                                                                                                                                                                                                                                  |
| [topCountElement.MeasureName = \"Internet Sales Amount\"]                                                                                                                                    |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\'\'\' Adding Column Members][]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [\'\'\'Adding Measure Element][]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [\'\'\'Adding Measure Element][]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [olapReport.CategoricalElements.Add(topCountElement)]                                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [\'\'\'Adding Row Members][]                                                                                                               |
|                                                                                                                                                                                                                                  |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

