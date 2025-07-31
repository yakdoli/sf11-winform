---
title: listbaritemevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\listbaritemevents.md
created_at: 2025-07-03
---






#### ListBarItem Events {#listbaritem-events style="tab-stops: 0pt"}

[] 

ListBarItem includes [Events of BarItem]{.UGHyperlink} and also contains events discussed in this section.

[] 


  Events         Description
  -------------- ---------------------------------------------
  BeforeExpand   Triggers before the ListBarItem displays.
  AfterExpand    Triggers when the ListBarItem is displayed.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [// Triggers when the ListBarItem is displayed]                                                                                                                                   |
|                                                                                                                                                                                                                                     |
| [private][ [void] listBarItem1_AfterExpand([object] sender, [EventArgs] e)]  |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    [Console].WriteLine(listBarItem1.Text);]                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [// Triggers before the ListBarItem displays]                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [private][ [void] listBarItem1_BeforeExpand([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    [Console].WriteLine(listBarItem1.Text);]                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Triggers when the ListBarItem is displayed]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] listBarItem1_AfterExpand([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]  |
|                                                                                                                                                                                                                                                                                                                        |
| [    Console.WriteLine(listBarItem1.Text)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [\' Triggers before the ListBarItem displays]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] listBarItem1_BeforeExpand([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                        |
| [    Console.WriteLine(listBarItem1.Text)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

