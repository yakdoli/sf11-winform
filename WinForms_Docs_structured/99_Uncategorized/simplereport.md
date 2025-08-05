---
title: simplereport.md
original_path: WinForms_Docs/99_Uncategorized/simplereport.md
created_at: 2025-08-05
---






##### Simple Report {#simple-report style="tab-stops: 0pt"}

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                                                  ]**                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [OlapReport][ olapReport = [new] [OlapReport]();] |
|                                                                                                                                                                                        |
| [olapReport.Name = [\"Customer Report\"];\                                                                                                                     |
| olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                                           |
|  \                                                                                                                                                                                     |
| [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                                          |
| [//Specifying the Name for the Dimension Element]\                                                                                                               |
| dimensionElementColumn.Name = [\"Customer\"];\                                                                                                                 |
| dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                                              |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                                             |
|  \                                                                                                                                                                                     |
| [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                                              |
| measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\                |
|  \                                                                                                                                                                                     |
| [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                                             |
| [//Specifying the Dimension Name]\                                                                                                                               |
| dimensionElementRow.Name = [\"Date\"];\                                                                                                                        |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                                        |
|  \                                                                                                                                                                                     |
| [///][ Adding Column Members]\                                                                                                              |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                                                           |
| [///][Adding Measure Element]\                                                                                                              |
| olapReport.CategoricalElements.Add(measureElementColumn);\                                                                                                                             |
| [///][Adding Row Members]\                                                                                                                  |
| olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                               |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| [\                                                                                                                                                                                                            |
| [Dim] olapReport [As] [OlapReport] = [New] [OlapReport]()] |
|                                                                                                                                                                                                               |
| [olapReport.Name = [\"Customer Report\"]\                                                                                                                                             |
| olapReport.CurrentCubeName = [\"Adventure Works\"]\                                                                                                                                   |
|  \                                                                                                                                                                                                            |
| [Dim] dimensionElementColumn [As] [DimensionElement] = [New] [DimensionElement]()\             |
| [\'Specifying the Name for the Dimension Element]\                                                                                                                                      |
| dimensionElementColumn.Name = [\"Customer\"]\                                                                                                                                         |
| dimensionElementColumn.HierarchyName = [\"Customer Geography\"]\                                                                                                                      |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"])\                                                                                     |
|  \                                                                                                                                                                                                            |
| [Dim] measureElementColumn [As] [MeasureElements] = [New] [MeasureElements]()\                 |
| measureElementColumn.Elements.Add([New] [MeasureElement] [With] {.Name = [\"Internet Sales Amount\"]})\             |
|  \                                                                                                                                                                                                            |
| [Dim] dimensionElementRow [As] [DimensionElement] = [New] [DimensionElement]()\                |
| [\'Specifying the Dimension Name]\                                                                                                                                                      |
| dimensionElementRow.Name = [\"Date\"]\                                                                                                                                                |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])\                                                                                                |
|  \                                                                                                                                                                                                            |
| [\'\'\' Adding Column Members]\                                                                                                                                                         |
| olapReport.CategoricalElements.Add(dimensionElementColumn)\                                                                                                                                                   |
| [\'\'\'Adding Measure Element]\                                                                                                                                                         |
| olapReport.CategoricalElements.Add(measureElementColumn)\                                                                                                                                                     |
| [\'\'\'Adding Row Members]\                                                                                                                                                             |
| olapReport.SeriesElements.Add(dimensionElementRow)][   ][]                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

