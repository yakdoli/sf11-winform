---
title: settingdefaultprojectproperties.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingdefaultprojectproperties.md
created_at: 2025-07-03
---






#### Setting Default Project Properties {#setting-default-project-properties style="tab-stops: 0pt"}

The following example shows how to set the default project properties.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [// Creating a new instance of the Project object]                                                   |
|                                                                                                                                                        |
| [Project][ project = new [Project();]] |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Setting Project Default information]                                                             |
|                                                                                                                                                        |
| [project.DefaultStartTime = [new] [TimeSpan](8, 0, 0);]               |
|                                                                                                                                                        |
| [project.DefaultFinishTime = [new] [TimeSpan](17, 0, 0);]             |
|                                                                                                                                                        |
| [project.DefaultStandardRate = 0f;]                                                                                |
|                                                                                                                                                        |
| [project.DefaultOvertimeRate = 0f;]                                                                                |
|                                                                                                                                                        |
| [project.DefaultTaskEVMethod = [EarnedValueMethod].PercentComplete;]                       |
|                                                                                                                                                        |
| [project.DefaultFixedCostAccrual = [DefaultFixedCostAccrual].Prorated;]                    |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Saving the Project]                                                                              |
|                                                                                                                                                        |
| [project.Save([\"DefaultProjectProperties.xml\"]);]                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [\' Creating an instance of a Project]                                                                                      |
|                                                                                                                                                                               |
| [Dim][ project [As] Project = [New] Project()] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Setting Project information]                                                                                            |
|                                                                                                                                                                               |
| [project.DefaultStartTime = [New] [TimeSpan](8, 0, 0)]                                       |
|                                                                                                                                                                               |
| [project.DefaultFinishTime = [New] [TimeSpan](17, 0, 0)]                                     |
|                                                                                                                                                                               |
| [project.DefaultStandardRate = 0.0F]                                                                                                      |
|                                                                                                                                                                               |
| [project.DefaultOvertimeRate = 0.0F]                                                                                                      |
|                                                                                                                                                                               |
| [project.DefaultTaskEVMethod = [EarnedValueMethod].PercentComplete]                                               |
|                                                                                                                                                                               |
| [project.DefaultFixedCostAccrual = [DefaultFixedCostAccrual].Prorated]                                            |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [\' Saving the Project]                                                                                                     |
|                                                                                                                                                                               |
| [project.Save([\"DefaultProjectProperties.xml\"])]                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

