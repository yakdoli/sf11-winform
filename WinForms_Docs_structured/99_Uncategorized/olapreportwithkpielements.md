---
title: olapreportwithkpielements.md
original_path: WinForms_Docs/99_Uncategorized/olapreportwithkpielements.md
created_at: 2025-08-05
---








  









### OlapReport with KPI Elements {#olapreport-with-kpi-elements style="tab-stops: 0pt"}

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [///][ ][\<summary\>]                   |
|                                                                                                                                                                                             |
| [///][ OlapReport with KPI Elements]                                                     |
|                                                                                                                                                                                             |
| [///][ ][\</summary\>]                  |
|                                                                                                                                                                                             |
| [///][ ][\<returns\>\</returns\>]       |
|                                                                                                                                                                                             |
| [private][ [OlapReport] LoadBasicKPI()]                                        |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [   [OlapReport] olapReport = [new] [OlapReport]();]                               |
|                                                                                                                                                                                             |
| [   [// Selecting the Cube]]                                                                                                      |
|                                                                                                                                                                                             |
| [   olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                        |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [   [KpiElements] kpiElement = [new] [KpiElements]();]                             |
|                                                                                                                                                                                             |
| [   [// Specifying the KPI Element name and configuring its Indicators]]                                                          |
|                                                                                                                                                                                             |
| [   kpiElement.Elements.Add([new] [KpiElement] { Name = [\"Internet Revenue\"],  ] |
|                                                                                                                                                                                             |
| [   ShowKPIGoal = [true], ShowKPIStatus = [true], ShowKPIValue = [true], ]               |
|                                                                                                                                                                                             |
| [   ShowKPITrend = [true] });]                                                                                                     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [   [DimensionElement] dimensionElementRow = [new] [DimensionElement]();]          |
|                                                                                                                                                                                             |
| [   [// Specifying the Name for Row Dimension Element]]                                                                           |
|                                                                                                                                                                                             |
| [   dimensionElementRow.Name = [\"Date\"];]                                                                                     |
|                                                                                                                                                                                             |
| [   // Specifying the Hierarchy Name along with the Level Name][       ]                              |
|                                                                                                                                                                                             |
| [   dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [   [// Adding Row Elements]]                                                                                                     |
|                                                                                                                                                                                             |
| [   olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                                |
|                                                                                                                                                                                             |
| [   [// Adding Column Elements]]                                                                                                  |
|                                                                                                                                                                                             |
| [   olapReport.CategoricalElements.Add(kpiElement);]                                                                                                    |
|                                                                                                                                                                                             |
| [            ]                                                                                                                                          |
|                                                                                                                                                                                             |
| [   [return] olapReport;]                                                                                                          |
|                                                                                                                                                                                             |
| [ }][]                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\'\'\' \<summary\>]                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\'\'\' OlapReport with KPI Elements]                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [\'\'\' \</summary\>]                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [\'\'\' \<returns\>\</returns\>\                                                                                                                                                                                                        |
| ][Private][ [Function] LoadBasicKPI() [As] OlapReport] |
|                                                                                                                                                                                                                                         |
| [ [Dim] olapReport [As] OlapReport = [New] OlapReport()]                                                                             |
|                                                                                                                                                                                                                                         |
| [ [\' Selecting the Cube]]                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [ olapReport.CurrentCubeName = [\"Adventure Works\"]]                                                                                                                       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [ [Dim] kpiElement [As] KpiElements = [New] KpiElements()]                                                                           |
|                                                                                                                                                                                                                                         |
| [ [\' Specifying the KPI Element name and configuring its Indicators]]                                                                                                        |
|                                                                                                                                                                                                                                         |
| [ kpiElement.Elements.Add([New] KpiElement [With] {.Name =  ]                                                                                             |
|                                                                                                                                                                                                                                         |
| [ \"Internet Revenue\"][, .ShowKPIGoal = [True], .ShowKPIStatus = [True], ]                           |
|                                                                                                                                                                                                                                         |
| [ .ShowKPIValue = [True], .ShowKPITrend = [True]})]                                                                                                       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [ [Dim] dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                                                        |
|                                                                                                                                                                                                                                         |
| [ [\' Specifying the Name for Row Dimension Element]]                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [ dimensionElementRow.Name = [\"Date\"]]                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [ [\' Specifying the Hierarchy Name along with the Level Name]       ]                                                                                                        |
|                                                                                                                                                                                                                                         |
| [ dimensionElementRow.AddLevel([\"Fiscal\"],[ \"Fiscal Year\"])]                                                                                    |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [ [\' Adding Row Elements]]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [ olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [ [\' Adding Column Elements]]                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [ olapReport.CategoricalElements.Add(kpiElement)]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [ [Return] olapReport]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [End][ [Function]]                                                                                                            |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

