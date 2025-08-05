---
title: olapreportwithsimpledimensionsandmeasure.md
original_path: WinForms_Docs/99_Uncategorized/olapreportwithsimpledimensionsandmeasure.md
created_at: 2025-08-05
---








  









### OlapReport with Simple Dimensions and Measure {#olapreport-with-simple-dimensions-and-measure style="tab-stops: 0pt"}

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [///][ ][\<summary\>]                                            |
|                                                                                                                                                                                                                      |
| [///][ Defining OlapReport with Dimensions and Measures]                                                          |
|                                                                                                                                                                                                                      |
| [///][ ][\</summary\>]                                           |
|                                                                                                                                                                                                                      |
| [///][ ][\<returns\>\</returns\>]                                |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [private][ [OlapReport] ][CreateOlapReport()]                       |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [        [OlapReport] olapReport = [new] [OlapReport]();]                                                   |
|                                                                                                                                                                                                                      |
| [        [// Selecting the Cube]]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [        olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                                            |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();]                           |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Name for Column Dimension Element]]                                                                                            |
|                                                                                                                                                                                                                      |
| [        dimensionElementColumn.Name = [\"Customer\"];]                                                                                                  |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                      |
| [        dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);]                                              |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [MeasureElements] measureElementColumn = [new] [MeasureElements]();]                               |
|                                                                                                                                                                                                                      |
| [        [//Specifying the Measure Elements]]                                                                                                              |
|                                                                                                                                                                                                                      |
| [        measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [DimensionElement] dimensionElementRow = [new] [DimensionElement]();]                              |
|                                                                                                                                                                                                                      |
| [        [//Specifying the Name for Row Dimension Element]]                                                                                                |
|                                                                                                                                                                                                                      |
| [        dimensionElementRow.Name = [\"Date\"];]                                                                                                         |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                      |
| [        dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                         |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [///][Adding Column Members]]                                                                                                |
|                                                                                                                                                                                                                      |
| [        olapReport.CategoricalElements.Add(dimensionElementColumn);]                                                                                                            |
|                                                                                                                                                                                                                      |
| [        [///][Adding Measure Element]]                                                                                               |
|                                                                                                                                                                                                                      |
| [        olapReport.CategoricalElements.Add(measureElementColumn);]                                                                                                              |
|                                                                                                                                                                                                                      |
| [        [///][Adding Row Members]]                                                                                                   |
|                                                                                                                                                                                                                      |
| [        olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                                                    |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [return] olapReport;    ]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [ }][]                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [\'\'\' \<summary\>][]                                                                                                             |
|                                                                                                                                                                                                                          |
| [\'\'\' Defining OlapReport with Dimensions and Measures][]                                                                        |
|                                                                                                                                                                                                                          |
| [\'\'\' \</summary\>][]                                                                                                            |
|                                                                                                                                                                                                                          |
| [\'\'\' \<returns\>\</returns\>][]                                                                                                 |
|                                                                                                                                                                                                                          |
| [Private][ [Function] CreateOlapReport() [As] OlapReport]                                 |
|                                                                                                                                                                                                                          |
| [            [Dim] olapReport [As] OlapReport = [New] OlapReport()]                                                   |
|                                                                                                                                                                                                                          |
| [            [\' Selecting the Cube]]                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            olapReport.CurrentCubeName = [\"Adventure Works\"]]                                                                                             |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [Dim] dimensionElementColumn [As] DimensionElement = [New] DimensionElement()]                           |
|                                                                                                                                                                                                                          |
| [            [\' Specifying the Name for Column Dimension Element]]                                                                                            |
|                                                                                                                                                                                                                          |
| [            dimensionElementColumn.Name = [\"Customer\"]]                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [\' Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                          |
| [            dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"])]                                               |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [Dim] measureElementColumn [As] MeasureElements = [New] MeasureElements()]                               |
|                                                                                                                                                                                                                          |
| [            [\'Specifying the Measure Elements]]                                                                                                              |
|                                                                                                                                                                                                                          |
| [            measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = [\"Internet Sales Amount\"]})] |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [Dim] dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                              |
|                                                                                                                                                                                                                          |
| [            [\'Specifying the Name for Row Dimension Element]]                                                                                                |
|                                                                                                                                                                                                                          |
| [            dimensionElementRow.Name = [\"Date\"]]                                                                                                          |
|                                                                                                                                                                                                                          |
| [            [\' Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                          |
| [            dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\")]]                                                          |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [\'\'\'Adding Column Members]]                                                                                                                    |
|                                                                                                                                                                                                                          |
| [            olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                             |
|                                                                                                                                                                                                                          |
| [            [\'\'\'Adding Measure Element]]                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                               |
|                                                                                                                                                                                                                          |
| [            [\'\'\'Adding Row Members]]                                                                                                                       |
|                                                                                                                                                                                                                          |
| [            olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                     |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [            [Return] olapReport]                                                                                                                               |
|                                                                                                                                                                                                                          |
| [End][ [Function]]                                                                                             |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

