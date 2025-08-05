---
title: expandedallevent.md
original_path: WinForms_Docs/99_Uncategorized/expandedallevent.md
created_at: 2025-08-05
---






#### ExpandedAll Event {#expandedall-event style="tab-stops: 0pt"}

 

This event is raised when the **ExpandAll** method is called.

 

The event handler receives an argument of type **EventArgs**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Handle the ExpandedAll event.]                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [this][.editControl1.ExpandedAll+=[new] [EventHandler](editControl1_ExpandedAll);]               |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Call the ExpandAll method.]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [this][.editControl1.ExpandAll();]                                                                                                         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [private][ [void] editControl1_ExpandedAll([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                 |
| [{ ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [  [// The below line will be displayed in the output window at runtime].]                                                                                            |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\" ExpandedAll event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Handle the ExpandedAll event.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.editControl1.ExpandedAll+=[New] EventHandler(editControl1_ExpandedAll)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Call the ExpandAll method.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.editControl1.ExpandAll()]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] editControl1_ExpandedAll([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                       |
| [  \' The below line will be displayed in the output window at runtime]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                       |
| [Console.WriteLine([\" ExpandedAll event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p138} 

[]{#related-topics}

