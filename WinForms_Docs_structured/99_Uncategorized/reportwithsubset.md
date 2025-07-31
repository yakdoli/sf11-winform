---
title: reportwithsubset.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\reportwithsubset.md
created_at: 2025-07-03
---






##### Report with subset {#report-with-subset style="tab-stops: 0pt"}

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [OlapReport][ olapReport = [new] [OlapReport]();\                      |
| olapReport.Name = [\"Customer Report\"]; olapReport.CurrentCubeName = [\"Adventure Works\"];\                           |
| [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                           |
| [//Specifying the Name for the Dimension Element]\                                                                                                |
| dimensionElementColumn.Name = [\"Customer\"];\                                                                                                  |
| [//Specifying the Hierarchy Name]\                                                                                                                |
| dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                               |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                              |
|  \                                                                                                                                                                      |
| [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                               |
| measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\ |
|  \                                                                                                                                                                      |
| [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                              |
| [//Specifying the Dimension Name]\                                                                                                                |
| dimensionElementRow.Name = [\"Date\"];\                                                                                                         |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                         |
|  \                                                                                                                                                                      |
| [//Specifying the SubsetElement]\                                                                                                                 |
| [//Specify the start index and end index to retrieve the records.]\                                                                               |
| [SubsetElement] subSetElementColumn = [new] [SubsetElement](5);\                                   |
| subSetElementColumn.Name = [\"Top 5 Elements\"];\                                                                                               |
|  \                                                                                                                                                                      |
| [SubsetElement] subSetElementRow = [new] [SubsetElement](3);\                                      |
| subSetElementRow.Name = [\"Top 3 Elements\"];\                                                                                                  |
|  \                                                                                                                                                                      |
| [///][Adding Column Members]\                                                                                                |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                                            |
| [///][Adding Measure Element]\                                                                                               |
| olapReport.CategoricalElements.Add(measureElementColumn);\                                                                                                              |
| olapReport.CategoricalElements.SubSetElement = subSetElementColumn;\                                                                                                    |
| [///][Adding Row Members]\                                                                                                   |
| olapReport.SeriesElements.Add(dimensionElementRow);\                                                                                                                    |
| olapReport.SeriesElements.SubSetElement = subSetElementRow;]                                                                        |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [\'Specifying the Name for the Dimension Element][]                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                                  |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Creating Measure Element][]                                                                                                        |
|                                                                                                                                                                                                                             |
| [Dim][ olapReport [As] OlapReport = [New] OlapReport()]                                      |
|                                                                                                                                                                                                                             |
| [olapReport.CurrentCubeName = \"Adventure Works\"]                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ dimensionElementColumn [As] DimensionElement = [New] DimensionElement()]              |
|                                                                                                                                                                                                                             |
| [\'Specifying the Name for the Dimension Element][]                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [\'Specifying the Hierarchy Name][]                                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.HierarchyName = \"Customer Geography\"]                                                                                                                         |
|                                                                                                                                                                                                                             |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                                  |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ measureElementColumn [As] MeasureElements = [New] MeasureElements()]                  |
|                                                                                                                                                                                                                             |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Internet Sales Amount\"})]                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                 |
|                                                                                                                                                                                                                             |
| [\'Specifying the Dimension Name][]                                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementRow.Name = \"Date\"]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Specifying the SubsetElement][]                                                                                                    |
|                                                                                                                                                                                                                             |
| [\'Specify the start index and end index to retrieve the records.][]                                                                  |
|                                                                                                                                                                                                                             |
| [Dim][ subSetElementColumn [As] SubsetElement = [New] SubsetElement(5)]                      |
|                                                                                                                                                                                                                             |
| [subSetElementColumn.Name = \"Top 5 Elements\"]                                                                                                                                         |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [Dim][ subSetElementRow [As] SubsetElement = [New] SubsetElement(3)]                         |
|                                                                                                                                                                                                                             |
| [subSetElementRow.Name = \"Top 3 Elements\"]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'\'\'Adding Column Members][]                                                                                                       |
|                                                                                                                                                                                                                             |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [\'\'\'Adding Measure Element][]                                                                                                      |
|                                                                                                                                                                                                                             |
| [olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                                              |
|                                                                                                                                                                                                                             |
| [olapReport.CategoricalElements.SubSetElement = subSetElementColumn]                                                                                                                    |
|                                                                                                                                                                                                                             |
| [\'\'\'Adding Row Members][]                                                                                                          |
|                                                                                                                                                                                                                             |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [olapReport.SeriesElements.SubSetElement = subSetElementRow]                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

