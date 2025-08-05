---
title: toolbarlistbaritemevents.md
original_path: WinForms_Docs/99_Uncategorized/toolbarlistbaritemevents.md
created_at: 2025-08-05
---






#### ToolbarListBarItem Events {#toolbarlistbaritem-events style="tab-stops: 0pt"}

[] 

ToolbarListBarItem includes [Events of BarItem]{.UGHyperlink} and also contains events discussed in this section.

[] 


  Events         Description
  -------------- ---------------------------------------
  BeforePopup    Triggers before the Pop-up displays
  Popup          Triggers when the Pop-up is displayed
  PopupClosed    Triggers when the Pop-up is closed
  PopupClosing   Triggers before the Pop-up closes


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Triggers before the Popup displays]                                                                                                                                                 |
|                                                                                                                                                                                                                                           |
| [private][ [void] toolbarListBarItem1_BeforePopup([object] sender, CancelEventArgs e)]                     |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [Console].WriteLine([\"BeforePopup event triggered\"]);]                                                                                         |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Triggers when the Popup is displayed]                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [private][ [void] toolbarListBarItem1_Popup([object] sender, [EventArgs] e)]       |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [Console].WriteLine([\"Popup event is triggered\"]);]                                                                                            |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Triggers when the Popup is closed]                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [private][ [void] toolbarListBarItem1_PopupClosed([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [Console].WriteLine([\"PopupClosed event is triggered\"]);]                                                                                      |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [// Triggers before the Popup closes]                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [private][ [void] toolbarListBarItem1_PopupClosing([object] sender, CancelEventArgs e)]                    |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [Console].WriteLine([\"PopupClosing event is triggered\"]);]                                                                                     |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Triggers before the Popup displays]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] toolbarListBarItem1_BeforePopup([ByVal] sender [As] [Object], [ByVal] e [As] CancelEventArgs)]  |
|                                                                                                                                                                                                                                                                                                                                     |
| [    Console.WriteLine([\"BeforePopup event triggered\"])]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Triggers when the Popup is displayed]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] toolbarListBarItem1_Popup([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]              |
|                                                                                                                                                                                                                                                                                                                                     |
| [    Console.WriteLine([\"Popup event is triggered\"])]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Triggers when the Popup is closed]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] toolbarListBarItem1_PopupClosed([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]        |
|                                                                                                                                                                                                                                                                                                                                     |
| [    Console.WriteLine([\"PopupClosed event is triggered\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Triggers before the Popup closes]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] toolbarListBarItem1_PopupClosing([ByVal] sender [As] [Object], [ByVal] e [As] CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                     |
| [    Console.WriteLine([\"PopupClosing event is triggered\"])]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

