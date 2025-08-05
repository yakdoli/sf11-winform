---
title: settingweekdayproperties.md
original_path: WinForms_Docs/99_Uncategorized/settingweekdayproperties.md
created_at: 2025-08-05
---






#### Setting Week Day Properties {#setting-week-day-properties style="tab-stops: 0pt"}

The following code snippet illustrates how to set the Week day properties of a project.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [// Creating a new Project instance]                                                                 |
|                                                                                                                                                        |
| [Project][ project = new [Project();]] |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Setting week day properties]                                                                     |
|                                                                                                                                                        |
| [project.WeekStartDay = [WeekStartDay].Monday;]                                            |
|                                                                                                                                                        |
| [project.DaysPerMonth = 24;]                                                                                       |
|                                                                                                                                                        |
| [project.MinutesPerDay = 480;]                                                                                     |
|                                                                                                                                                        |
| [project.MinutesPerWeek = 2880;]                                                                                   |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [//Saving the project]                                                                               |
|                                                                                                                                                        |
| [project.Save([\"WeekDayProperties.xml\"]);]                                               |
|                                                                                                                                                        |
| []                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [\' Creating a new Project instance]                                                                                        |
|                                                                                                                                                                               |
| [Dim][ project [As] Project = [New] Project()] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Setting Week day properties]                                                                                            |
|                                                                                                                                                                               |
| [project.WeekStartDay = WeekStartDay.Monday]                                                                                              |
|                                                                                                                                                                               |
| [project.DaysPerMonth = 24]                                                                                                               |
|                                                                                                                                                                               |
| [project.MinutesPerDay = 480]                                                                                                             |
|                                                                                                                                                                               |
| [project.MinutesPerWeek = 2880]                                                                                                           |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Saving the Project]                                                                                                     |
|                                                                                                                                                                               |
| [project.Save([\"WeekDayProperties.xml\"])]                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

