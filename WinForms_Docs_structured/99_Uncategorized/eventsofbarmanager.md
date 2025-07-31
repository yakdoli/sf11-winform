---
title: eventsofbarmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\eventsofbarmanager.md
created_at: 2025-07-03
---






#### Events of BarManager {#events-of-barmanager style="tab-stops: 0pt"}

[] 

This section discusses the events of BarManager.

 

The event handler of the following events receives an argument of type EventArgs.

[] 


  ---------------------------- -----------------------------------------------------------------
  MainFrameBarManager Events   Description
  CustomizationBegin           It triggers when the customization dialog is about to be shown.
  CustomizationDone            It triggers when the customization dialog has been closed.
  ---------------------------- -----------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [//Displays message when CustomizationBegin event occurs]                                                                                                |
|                                                                                                                                                                                                            |
| [private][ [void] Customization_Begin([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [Console.WriteLine(\"CustomizationBegin occurred\");]                                                                                                                  |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [//Displays message when CustomizationDone event occurs]                                                                                                 |
|                                                                                                                                                                                                            |
| [private][ [void] Customization_Done([object] sender, System.EventArgs e)]  |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [Console.WriteLine(\"CustomizationDone occurred\");]                                                                                                                   |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [\'Displays message when CustomizationBegin event occurs]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Customization_Begin([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                         |
| [    Console.WriteLine([\"CustomizationBegin occured.\"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [\'Displays message when CustomizationDone event occurs]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Customization_Done([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]  |
|                                                                                                                                                                                                                                                                                                                         |
| [    Console.WriteLine([\"CustomizationDone occured.\"])]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

