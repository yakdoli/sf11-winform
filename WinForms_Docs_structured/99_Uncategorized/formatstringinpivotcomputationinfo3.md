---
title: formatstringinpivotcomputationinfo3.md
original_path: WinForms_Docs/99_Uncategorized/formatstringinpivotcomputationinfo3.md
created_at: 2025-08-05
---








  









### Format String in PivotComputationInfo {#format-string-in-pivotcomputationinfo style="tab-stops: 0pt"}

The *PivotComputationInfo* property replaces each format specification in a specified string with the textual equivalent of a corresponding value.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [// Decimal Format][]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PivotComputationInfo][ m_PivotComputationInfo = [new] [PivotComputationInfo]() { CalculationName=[\"Total\"], FieldName=[\"Quantity\"], SummaryType= [SummaryType].Count, Format=[\"0.00\"]};] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Decimal Format][]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ m_PivotComputationInfo [As] PivotComputationInfo = [New] PivotComputationInfo() [With] {.CalculationName=\"Total\", .FieldName=\"Quantity\", .SummaryType= SummaryType.Count, .Format=\"0.00\"}] |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following table lists the different types of format settings.

     Table 7: Types of format settings


  ----------------- --------------------------
  Format            Description
  0.00              Decimal
  C                 Currency
  #,##0             Thousand Separator
  \# \' degrees\'   Literal String Specifier
  D                 Long Date
  ----------------- --------------------------


 

[]{#related-topics}

