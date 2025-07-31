---
title: collapsingallevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\collapsingallevent.md
created_at: 2025-07-03
---






#### CollapsingAll Event {#collapsingall-event style="tab-stops: 0pt"}

 

This event is raised when the **CollapseAll** method is called.

 

The event handler receives an argument of type **CancelEventArgs**. The following CancellableEventArgs member provides information, specific to this event.

 


  -------- -----------------------------------------------------------------------
  Member   Description
  Cancel   Gets / sets a value indicating whether the event should be cancelled.
  -------- -----------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Handle the CollapsingAll event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [this][.editControl1.CollapsingAll+=[new] [EventHandler](editControl1_CollapsingAll);]                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Call the CollapseAll method.]                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [this][.editControl1.CollapseAll();]                                                                                                               |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [private][ [void] editControl1_CollapsingAll([object] sender, [CancelEventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [// The below given line will be displayed in the output window at runtime.]                                                                                                          |
|                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\" CollapsingAll event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                         |
| [// Cancels the event.]                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Handle the CollapsingAll event.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.editControl1.CollapsingAll+=[New] EventHandler(editControl1_CollapsingAll)]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Call the CollapseAll method.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.editControl1.CollapseAll()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] editControl1_CollapsingAll([ByVal] sender [As] [Object], [ByVal] e [As] CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                               |
| [\' The below given line will be displayed in the output window at runtime.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [Console.WriteLine([\" CollapsingAll event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Cancels the event.]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                               |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p121} 

[]{#related-topics}

