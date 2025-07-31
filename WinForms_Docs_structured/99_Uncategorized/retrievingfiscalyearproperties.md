---
title: retrievingfiscalyearproperties.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\retrievingfiscalyearproperties.md
created_at: 2025-07-03
---






#### Retrieving Fiscal Year Properties {#retrieving-fiscal-year-properties style="tab-stops: 0pt"}

The following code snippets retrieve Fiscal year properties from a project:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [// Calling Open method of ProjectReader to get the Project object]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                       |
| [Project][ project = [ProjectReader].Open([\"Sample Project.xml\"]);]                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [// Retrieving Fiscal Year information]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\"Fiscal Year Start Month: \"] + project.FYStartDate);]                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [Console][.WriteLine(project.FiscalYearStart ? [\"Fiscal Year Numbering is used in the Project\"] : [\"Fiscal Year Numbering is not used in the Project\"]);] |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [\' Calling Read method of ProjectReader to get the Project object]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [Dim][ project [As] Project = ProjectReader.Open([\"Sample Project.xml\"])]                                                           |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [\' Retrieving Fiscal Year information]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Fiscal Year Start Month: \"] + project.FYStartDate)]                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([If](project.FiscalYearStart, [\"Fiscal Year Numbering is used in the Project\"], [\"Fiscal Year Numbering is not used in the Project\"]))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

