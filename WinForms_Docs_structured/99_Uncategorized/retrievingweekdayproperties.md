---
title: retrievingweekdayproperties.md
original_path: WinForms_Docs/99_Uncategorized/retrievingweekdayproperties.md
created_at: 2025-08-05
---






#### Retrieving Week Day Properties {#retrieving-week-day-properties style="tab-stops: 0pt"}

The following code snippets illustrate how to retrieve the Week day properties of a project.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Opening the project file]                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [Project][ project = Syncfusion.ProjIO.[ProjectReader].Open([\"Sample Project.xml\"]);] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Retrieving Week day properties]                                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"Weeks starts on: \"] + project.WeekStartDay);]                                          |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"No. of working days per month: \"] + project.DaysPerMonth);]                            |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"No.of minutes per day: \"] + project.MinutesPerDay);]                                   |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\"No. of minutes per week: \"] + project.MinutesPerWeek);]                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [\' Opening the project file]                                                                                                                               |
|                                                                                                                                                                                                               |
| [Dim][ project [As] Project = ProjectReader.Open([\"Sample Project.xml\"])] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [\' Retrieving Week day properties]                                                                                                                         |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"Weeks starts on: \"] + project.WeekStartDay)]                         |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"No. of working days per month: \"] + project.DaysPerMonth)]           |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"No.of minutes per day: \"] + project.MinutesPerDay)]                  |
|                                                                                                                                                                                                               |
| [Console][.WriteLine([\"No. of minutes per week: \"] + project.MinutesPerWeek)]               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

