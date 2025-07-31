---
title: summaryelements.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\summaryelements.md
created_at: 2025-07-03
---








  









### Summary Elements {#summary-elements style="tab-stops: 0pt"}

Summary elements come when the base deals with Non-OLAP data. This is similar to the measure element in the OLAP data. This element will be considered as the measure and this value will be displayed in the value cell.

The following codes will describe the creation of the Summary elements:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                                                  ]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| [                                                      ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [ [// Specifying the Summary Elements]\                                                                                                                                                                                                                                                            |
| [SummaryElements] summaries = [new] [SummaryElements]();\                                                                                                                                                                                           |
| summaries.Add([new] [SummaryInfo] { Column = [\"Quantity\"], Key = [\"Quantity\"], Type = [SummaryType].Sum });\                                                                                    |
| summaries.Add([new] [SummaryInfo] { Column = [\"Amount\"], Key = [\"Amount\"], Type = [SummaryType].Sum, FormatString = [\"{0:c}\"] })] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Specifying the Summary Elements][]                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ summaries [As] SummaryElements = [New] SummaryElements()]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [summaries.Add([New] SummaryInfo [With] {.Column = ][\"Quantity\"][, .Key = ][\"Quantity\"][, .Type = SummaryType.Sum})]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [summaries.Add([New] SummaryInfo [With] {.Column = ][\"Amount\"][, .Key = ][\"Amount\"][, .Type = SummaryType.Sum, .FormatString = ][\"{0:c}\"][})] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

