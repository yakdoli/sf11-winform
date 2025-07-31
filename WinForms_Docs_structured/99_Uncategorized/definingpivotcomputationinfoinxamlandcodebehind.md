---
title: definingpivotcomputationinfoinxamlandcodebehind.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingpivotcomputationinfoinxamlandcodebehind.md
created_at: 2025-07-03
---








  









### Defining PivotComputationInfo in XAML and Code-Behind {#defining-pivotcomputationinfo-in-xaml-and-code-behind style="tab-stops: 0pt"}

 

**PivotComputationInfo** can be defined by the following way.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [// Defining PivotComputationInfo.]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [PivotComputationInfo][ m_PivotComputationInfo = [new] [PivotComputationInfo]() { CalculationName=[\"Amount\"], FieldName=[\"Amount\"], SummaryType= [SummaryType].Count };] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [// Adding PivotComputationInfo to PivotCalculations.]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [this][.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo);][]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Defining PivotComputationInfo.][]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ m_PivotComputationInfo [As] PivotComputationInfo = [New] PivotComputationInfo() [With] {.CalculationName=\"Amount\", .FieldName=\"Amount\", .SummaryType= SummaryType.Count}] |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Adding PivotComputationInfo to PivotCalculations.][]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| [Me][.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

