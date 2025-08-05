---
title: settingfiscalyearproperties.md
original_path: WinForms_Docs/99_Uncategorized/settingfiscalyearproperties.md
created_at: 2025-08-05
---






#### Setting Fiscal Year Properties {#setting-fiscal-year-properties style="tab-stops: 0pt"}

The following code sets the Fiscal year properties for a project.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [// Creating a new instance of Project object]                                                                                                |
|                                                                                                                                                                                                 |
| [Project][ project = [new] Syncfusion.ProjIO.[Project]();] |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Setting Fiscal Year information]                                                                                                          |
|                                                                                                                                                                                                 |
| [project.FYStartDate = [FYStartDate].April;]                                                                                        |
|                                                                                                                                                                                                 |
| [project.FiscalYearStart = [true];]                                                                                                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Saving the Project]                                                                                                                       |
|                                                                                                                                                                                                 |
| [project.Save([\"FiscalProperties.xml\"]);]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [\' Creating an instance of Project]                                                                                        |
|                                                                                                                                                                               |
| [Dim][ project [As] Project = [New] Project()] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Setting Fiscal Year information]                                                                                        |
|                                                                                                                                                                               |
| [project.FYStartDate = FYStartDate.April]                                                                                                 |
|                                                                                                                                                                               |
| [project.FiscalYearStart = [True]]                                                                                   |
|                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                               |
| [\' Saving the Project]                                                                                                     |
|                                                                                                                                                                               |
| [project.Save([\"FiscalProperties.xml\"])]                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

