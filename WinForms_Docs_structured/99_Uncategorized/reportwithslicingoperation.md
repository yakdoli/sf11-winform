---
title: reportwithslicingoperation.md
original_path: WinForms_Docs/99_Uncategorized/reportwithslicingoperation.md
created_at: 2025-08-05
---






##### Report with slicing operation {#report-with-slicing-operation style="tab-stops: 0pt"}

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [OlapReport][ olapReport = [new] [OlapReport]();] |
|                                                                                                                                                                                        |
| [olapReport.Name = [\"Customer Report\"];\                                                                                                                     |
| olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                                           |
|  \                                                                                                                                                                                     |
| [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                                          |
|  \                                                                                                                                                                                     |
| [//Specifying the dimension Name]\                                                                                                                               |
| dimensionElementColumn.Name = [\"Customer\"];\                                                                                                                 |
|  \                                                                                                                                                                                     |
| [//Adding the Level Name along with the Hierarchy Name]\                                                                                                         |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                                             |
|  \                                                                                                                                                                                     |
| [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                                             |
|  \                                                                                                                                                                                     |
| [//Specifying the dimension Name]\                                                                                                                               |
| dimensionElementRow.Name = [\"Date\"];\                                                                                                                        |
|  \                                                                                                                                                                                     |
| [//Adding the Level Name along with the Hierarchy Name]\                                                                                                         |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                                        |
|  \                                                                                                                                                                                     |
| [DimensionElement] dimensionElementSlicer = [new] [DimensionElement]();]      |
|                                                                                                                                                                                        |
| [dimensionElementSlicer.Name = [\"Sales Channel\"];\                                                                                                           |
| dimensionElementSlicer.AddLevel([\"Sales Channel\"], [\"Sales Channel\"]);\                                                            |
|  \                                                                                                                                                                                     |
| [MeasureElements] measureElementRow = [new] [MeasureElements]();\                                                 |
| measureElementRow.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\                   |
|  \                                                                                                                                                                                     |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                                                           |
| olapReport.SeriesElements.Add(dimensionElementRow);\                                                                                                                                   |
| olapReport.SlicerElements.Add(dimensionElementSlicer);\                                                                                                                                |
| olapReport.SeriesElements.Add(measureElementRow);]                                                                                                 |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [\                                                                                                                                                                                                                          |
| ][Dim][ olapReport [As] OlapReport = [New] OlapReport()] |
|                                                                                                                                                                                                                             |
| [olapReport.Name = [\"Customer Report\"]][]                                                                                 |
|                                                                                                                                                                                                                             |
| [olapReport.CurrentCubeName = \"Adventure Works\"]                                                                                                                                      |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ dimensionElementColumn [As] DimensionElement = [New] DimensionElement()]              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Specifying the dimension Name][]                                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Adding the Level Name along with the Hierarchy Name][]                                                                             |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                                  |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                 |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Specifying the dimension Name][]                                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementRow.Name = \"Date\"]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Adding the Level Name along with the Hierarchy Name][]                                                                             |
|                                                                                                                                                                                                                             |
| [dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ dimensionElementSlicer [As] DimensionElement = [New] DimensionElement()]              |
|                                                                                                                                                                                                                             |
| [dimensionElementSlicer.Name = \"Sales Channel\"]                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [dimensionElementSlicer.AddLevel(\"Sales Channel\", \"Sales Channel\")]                                                                                                                 |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ measureElementRow [As] MeasureElements = [New] MeasureElements()]                     |
|                                                                                                                                                                                                                             |
| [measureElementRow.Elements.Add(New MeasureElement { Name = \"Internet Sales Amount\" });][]                                          |
|                                                                                                                                                                                                                             |
| [measureElementRow.Elements.Add([New] MeasureElement [With] {.Name = \"Internet Sales Amount\"})]                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [olapReport.SlicerElements.Add(dimensionElementSlicer)]                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [olapReport.SeriesElements.Add(measureElementRow)     ][]                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

