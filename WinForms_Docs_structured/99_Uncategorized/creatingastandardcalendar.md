---
title: creatingastandardcalendar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingastandardcalendar.md
created_at: 2025-07-03
---








  









### [[Creating a Standard Calendar]]{.Heading4Char} {#creating-a-standard-calendar style="tab-stops: 0pt"}

The static method StandardCalendar is used to create a standard calendar and add it to the project.

This method contains two overloads namely:

[·      ]StandardCalendar() -- Creates a standard calendar

[·      ]StandardCalendar(string calendarName) -- Creates a standard calendar by passing the calendar name

The following code snippet shows how to make use of this method:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [// Creating a standard calendar]                                                                                                                           |
|                                                                                                                                                                                                               |
| [Calendar][ calendar = [Calendar].StandardCalendar();]                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [// Creating a standard calendar by passing the calendar name]                                                                                              |
|                                                                                                                                                                                                               |
| [Calendar][ calendar1 = [Calendar].StandardCalendar([\"Standard\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [\' Creating a standard calendar]                                                                                                                           |
|                                                                                                                                                                                                               |
| [Dim][ calendar [As] Calendar = Calendar.StandardCalendar()]                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [\' Creating a standard calendar by passing the calendar name]                                                                                              |
|                                                                                                                                                                                                               |
| [Dim][ calendar1 [As] Calendar = Calendar.StandardCalendar([\"Standard\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

