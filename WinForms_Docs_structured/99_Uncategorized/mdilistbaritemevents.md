---
title: mdilistbaritemevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\mdilistbaritemevents.md
created_at: 2025-07-03
---






#### MDIListBarItem Events {#mdilistbaritem-events style="tab-stops: 0pt"}

 

MDIListBarItem includes [Events of BarItem]{.UGHyperlink} and also contains events discussed in this section.

[] 


  Events         Description
  -------------- ------------------------------------------------
  BeforeExpand   Triggers before the MdiListBarItem displays.
  AfterExpand    Triggers when the MdiListBarItem is displayed.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Triggers when the MdiListBarItem is displayed]                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] mdiListBarItem1_AfterExpand([object] sender, [EventArgs] e)]  |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [    [Console].WriteLine(mdiListBarItem1.Text);]                                                                                                                           |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Triggers before the MdiListBarItem displays]                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| [private][ [void] mdiListBarItem1_BeforeExpand([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [    [Console].WriteLine(mdiListBarItem1.Text);]                                                                                                                           |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Triggers when the MdiListBarItem is displayed]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] mdiListBarItem1_AfterExpand([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]  |
|                                                                                                                                                                                                                                                                                                                           |
| [    Console.WriteLine(mdiListBarItem1.Text)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Triggers before the MdiListBarItem displays]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] mdiListBarItem1_BeforeExpand([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                           |
| [    Console.WriteLine(mdiListBarItem1.Text)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

