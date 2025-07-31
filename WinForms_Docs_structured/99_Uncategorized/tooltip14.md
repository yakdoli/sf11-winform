---
title: tooltip14.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tooltip14.md
created_at: 2025-07-03
---






#### ToolTip {#tooltip style="tab-stops: 0pt"}

You can set tooltip for specific days in the CalendarEdit control, using the **SetToolTip** method. The following code snippet illustrates tooltip setting for the current system date.

 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                      |
|                                                                                                     |
| []                                                              |
|                                                                                                     |
| [//Creating an instance date]                     |
|                                                                                                     |
| [Date a = [new] Date();]                   |
|                                                                                                     |
| []                                                              |
|                                                                                                     |
| [//Creating an instance of tooltip]               |
|                                                                                                     |
| [ToolTip toolTip = [new] ToolTip();]       |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [//Setting tooltip text]                          |
|                                                                                                     |
| [toolTip.Content = [\"CurrentDate\"]; ] |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [//Getting the current day]                       |
|                                                                                                     |
| [a.Day = [DateTime].Now.Day;   ]        |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [//Getting the current month]                     |
|                                                                                                     |
| [a.Month = [DateTime].Now.Month;  ]     |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [//Getting the current year]                      |
|                                                                                                     |
| [a.Year = [DateTime].Now.Year;]         |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [//Setting tooltip for current date]              |
|                                                                                                     |
| [calendarEdit.SetToolTip(a, toolTip); ]                         |
+-----------------------------------------------------------------------------------------------------+

 

[]{#p47} 

[]{#related-topics}

