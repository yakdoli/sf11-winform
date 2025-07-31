---
title: olapreportwithmemberproperties.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\olapreportwithmemberproperties.md
created_at: 2025-07-03
---








  









### OlapReport with Member Properties {#olapreport-with-member-properties style="tab-stops: 0pt"}

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [///][ ][\<summary\>]                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [///][ OlapReport the with Member properties.]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                           |
| [///][ ][\</summary\>]                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [///][ ][\<returns\>\</returns\>]                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [private][ [OlapReport] ReportWithMemberProperties()]                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [            [OlapReport] olapReport = [new] [OlapReport]();]                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [// Specifying the current cube name]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [            olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [MeasureElements] measureElementColumn = [new] [MeasureElements]();]                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [            [// Specifying the Measure Elements]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [            measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Sales Amount Quota\"] });]                                                                     |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [DimensionElement] dimensionElementRow = [new] [DimensionElement]();]                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [            [// Specifying the Dimension Name]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.Name = [\"Employee\"];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [            [// Specifying the Hierarchy and level name for the Dimension Element]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.AddLevel([\"Employees\"], [\"Employee Level 02\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.Hierarchy.LevelElements\[[\"Employee Level 02\"]\].IncludeAvailableMembers = [true];]                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [// Adding the Member properties to the Dimension Element]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.MemberProperties.Add([new] [MemberProperty]([\"Title\"], [\"\[Employee\].\[Employees\].\[Title\]\"]));]                 |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.MemberProperties.Add([new] [MemberProperty]([\"Phone\"], [\"\[Employee\].\[Employees\].\[Phone\]\"]));]                 |
|                                                                                                                                                                                                                                                                                           |
| [            dimensionElementRow.MemberProperties.Add([new] [MemberProperty]([\"Email Address\"], [\"\[Employee\].\[Employees\].\[Email Address\]\"]));] |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [// Adding Row Members]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [            olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [            [// Adding Column Members]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [            olapReport.CategoricalElements.Add(measureElementColumn);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [return] olapReport;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [ }]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\'\'\' \<summary\>]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\'\'\' OlapReport the with Member properties.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [\'\'\' \</summary\>]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [\'\'\' \<returns\>\</returns\>]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [Private][ [Function] ReportWithMemberProperties() [As] OlapReport]                                                       |
|                                                                                                                                                                                                                                                          |
| [      [Dim] olapReport [As] OlapReport = [New] OlapReport()]                                                                                         |
|                                                                                                                                                                                                                                                          |
| [      [\' Specifying the current cube name]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [      olapReport.CurrentCubeName = [\"Adventure Works\"]]                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [      [Dim] measureElementColumn [As] MeasureElements = [New] MeasureElements()]                                                                     |
|                                                                                                                                                                                                                                                          |
| [      [\' Specifying the Measure Elements]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [       measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = [\"Sales Amount Quota\"]})]                                         |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [      [Dim] dimensionElementRow [As] DimensionElement = [New] DimensionElement()]                                                                    |
|                                                                                                                                                                                                                                                          |
| [      [\' Specifying the Dimension Name]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.Name = [\"Employee\"]]                                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [      [\' Specifying the Hierarchy and level name for the Dimension Element]]                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.AddLevel([\"Employees\"], [\"Employee Level 02\"])]                                                                                       |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.Hierarchy.LevelElements([\"Employee Level 02\"]).IncludeAvailableMembers = [True]]                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [      [\' Adding the Member properties to the Dimension Element]]                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.MemberProperties.Add([New] MemberProperty([\"Title\"], [\"\[Employee\].\[Employees\].\[Title\]\"]))]                 |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.MemberProperties.Add([New] MemberProperty([\"Phone\"], [\"\[Employee\].\[Employees\].\[Phone\]\"]))]                 |
|                                                                                                                                                                                                                                                          |
| [      dimensionElementRow.MemberProperties.Add([New] MemberProperty([\"Email Address\"], [\"\[Employee\].\[Employees\].\[Email Address\]\"]))] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [      [\' Adding Row Members]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [      olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [      [\' Adding Column Members]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [       olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [   [Return] olapReport]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [End][ [Function]][]                                                                                       |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

