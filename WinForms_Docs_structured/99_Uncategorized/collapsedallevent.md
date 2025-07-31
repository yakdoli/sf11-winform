---
title: collapsedallevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\collapsedallevent.md
created_at: 2025-07-03
---






#### CollapsedAll Event {#collapsedall-event style="tab-stops: 0pt"}

 

This event is raised when the **CollapseAll** method is called.

 

The event handler receives an argument of type **EventArgs**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [// Handle the CollapsedAll event.]                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [this][.editControl1.CollapsedAll+=[new] [EventHandler](editControl1_CollapsedAll);]              |
|                                                                                                                                                                                                                                  |
| [// Call the CollapseAll method.]                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [this][.editControl1.CollapseAll();]                                                                                                        |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [private][ [void] editControl1_CollapsedAll([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                  |
| [{ ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  // The below line will be displayed ]                                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [Console][.WriteLine([\" CollapsedAll event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Handle the CollapsedAll event.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.CollapsedAll+=[New] EventHandler(editControl1_CollapsedAll)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Call the CollapseAll method.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.CollapseAll()]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_CollapsedAll([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\" CollapsedAll event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p120} 

[]{#related-topics}

