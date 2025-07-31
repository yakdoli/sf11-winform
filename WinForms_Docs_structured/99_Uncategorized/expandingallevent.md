---
title: expandingallevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\expandingallevent.md
created_at: 2025-07-03
---






#### ExpandingAll Event {#expandingall-event style="tab-stops: 0pt"}

 

This event is raised when the **ExpandAll** method is called.

 

The event handler receives an argument of type **CancelEventArgs**. The following CancellableEventArgs member provides information, specific to this event.

 


  -------- -----------------------------------------------------------------------
  Member   Description
  Cancel   Gets / sets a value indicating whether the event should be cancelled.
  -------- -----------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [// Handle the ExpandingAll event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [this][.editControl1.ExpandingAll+=[new] [EventHandler](editControl1_ExpandingAll);]                    |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Call the ExpandAll method.]                                                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [this][.editControl1.ExpandAll();]                                                                                                                |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] editControl1_ExpandingAll([object] sender, [CancelEventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [// The below given line will be displayed in the output window at runtime.]                                                                                                         |
|                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" ExpandingAll event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [// Cancels the event.]                                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [e.Cancel = [true];]                                                                                                                                                          |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the ExpandingAll event.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.editControl1.ExpandingAll+=[New] EventHandler(editControl1_ExpandingAll)]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Call the ExpandAll method.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.editControl1.ExpandAll()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] editControl1_ExpandingAll([ByVal] sender [As] [Object], [ByVal] e [As] CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [\' The below given line will be displayed in the output window at runtime.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| [Console.WriteLine([\" CollapsingAll event is raised \"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Cancels the event.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                              |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p139} 

[]{#related-topics}

