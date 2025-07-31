---
title: definingpivotcomputationinfoandcodebehind1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingpivotcomputationinfoandcodebehind1.md
created_at: 2025-07-03
---








  









### Defining PivotComputationInfo and Code-Behind {#defining-pivotcomputationinfo-and-code-behind style="tab-stops: 0pt"}

The *PivotComputationInfo* can be defined in C# or VB code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [// Defining PivotComputationInfo]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [PivotComputationInfo][ m_PivotComputationInfo = [new] [PivotComputationInfo]() { CalculationName=[\"Amount\"], FieldName=[\"Amount\"], SummaryType= [SummaryType].Count };] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [// Adding PivotComputationInfo to PivotCalculations]                                                                                                                                                                                                                                                                                   |
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
| [\' Defining PivotComputationInfo][]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ m_PivotComputationInfo [As] PivotComputationInfo = [New] PivotComputationInfo() [With] {.CalculationName=\"Amount\", .FieldName=\"Amount\", .SummaryType= SummaryType.Count}] |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Adding PivotComputationInfo to PivotCalculations][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                          |
| [Me][.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

