---
title: retrievingdefaultprojectproperties.md
original_path: WinForms_Docs/99_Uncategorized/retrievingdefaultprojectproperties.md
created_at: 2025-08-05
---






#### Retrieving Default Project Properties {#retrieving-default-project-properties style="tab-stops: 0pt"}

The following example illustrates how to retrieve default project properties.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [// Calling Open method of ProjectReader to get the Project object]                                                                                         |
|                                                                                                                                                                                                               |
| [Project][ project = [ProjectReader].Open([\"Sample Project.xml\"]);] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [// Retrieving Project Default information]                                                                                                                 |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Start Time: \"] + project.DefaultStartTime);]                 |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Finish Time: \"] + project.DefaultFinishTime);]               |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Standard Rate: \"] + project.DefaultStandardRate);]           |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Overtime Rate: \"] + project.DefaultOvertimeRate);]           |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Task EV Method: \"] + project.DefaultTaskEVMethod);]          |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Default Cost Accrual: \"] + project.DefaultFixedCostAccrual);]        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [\' Creating an instance of Project]                                                                                                                        |
|                                                                                                                                                                                                               |
| [Dim][ project [As] Project = ProjectReader.Open([\"Sample Project.xml\"])] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [\' Retriving Project information]                                                                                                                          |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Start Time: \"] & project.DefaultStartTime.ToString())]                                                             |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Finish Time: \"] & project.DefaultFinishTime.ToString())]                                                           |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Standard Rate: \"] & project.DefaultStandardRate)]                                                                  |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Overtime Rate: \"] & project.DefaultOvertimeRate)]                                                                  |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Task EV Method: \"] & project.DefaultTaskEVMethod)]                                                                 |
|                                                                                                                                                                                                               |
| [Console.WriteLine([\"Default Cost Accrual: \"] & project.DefaultFixedCostAccrual)]                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

