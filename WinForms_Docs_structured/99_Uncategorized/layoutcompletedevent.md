---
title: layoutcompletedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\layoutcompletedevent.md
created_at: 2025-07-03
---








  









### LayoutCompleted Event {#layoutcompleted-event style="tab-stops: 0pt"}

[] 

This event is handled every time, a resizing of chart is caused and when the chart re-renders itself. Listening to this event helps in cases where you render custom images over the chart or position custom controls over the chart.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [private][ [static] [void] ChartWebControl1_LayoutCompleted([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [Console.WriteLine(\"Layout Completed event is raised\");]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] ChartWebControl1_LayoutCompleted([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\"Layout Completed event is raised\"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p266} 

[]{#related-topics}

