---
title: settingprojectproperties.md
original_path: WinForms_Docs/99_Uncategorized/settingprojectproperties.md
created_at: 2025-08-05
---






#### Setting Project Properties {#setting-project-properties style="tab-stops: 0pt"}

The Project class can be used to set Project properties such as Start Date, Finish Date, Calendar and so on.

The following code snippet shows how to set the Project properties:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [// Creating a new instance of the Project object]                                                                          |
|                                                                                                                                                                               |
| [Project][ project = [new] [Project]();] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Setting Project information]                                                                                            |
|                                                                                                                                                                               |
| [project.ScheduleFromStart = [true];]                                                                                |
|                                                                                                                                                                               |
| [project.StartDate = [new] [DateTime](2011, 7, 9);]                                          |
|                                                                                                                                                                               |
| [project.CurrentDate = [new] [DateTime](2011, 7, 9);]                                        |
|                                                                                                                                                                               |
| [project.StatusDate = [new] [DateTime](2011, 7, 9);]                                         |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Saving the Project]                                                                                                     |
|                                                                                                                                                                               |
| [project.Save([\"ProjectProperties.xml\"]);]                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [\' Setting Project information]                                                                                            |
|                                                                                                                                                                               |
| [project.ScheduleFromStart = [True]]                                                                                 |
|                                                                                                                                                                               |
| [project.StartDate = [New] DateTime(2011, 7, 9)]                                                                     |
|                                                                                                                                                                               |
| [project.CurrentDate = [New] DateTime(2011, 7, 9)]                                                                   |
|                                                                                                                                                                               |
| [project.StatusDate = [New] DateTime(2011, 7, 9)]                                                                    |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Saving the Project]                                                                                                     |
|                                                                                                                                                                               |
| [project.Save([\"ProjectProperties.xml\"])]                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

