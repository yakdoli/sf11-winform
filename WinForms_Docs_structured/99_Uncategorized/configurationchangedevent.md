---
title: configurationchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/configurationchangedevent.md
created_at: 2025-08-05
---








  









### ConfigurationChanged Event {#configurationchanged-event style="tab-stops: 0pt"}

 

This event is fired on changing the configuration of the Edit Control. Configuration can be set for the Edit Control using the **ApplyConfiguration** method.

 

The event handler receives an argument of type **EventArgs**.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [this][.editControl1.ConfigurationChanged+=[new] [EventHandler](editControl1_ConfigurationChanged);]      |
|                                                                                                                                                                                                                                          |
| [this][.editControl1.ApplyConfiguration([\"XML\"]);]                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [private][ [void] editControl1_ConfigurationChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [this][.editControl1.ApplyConfiguration([\"XML\"]);]                                                                         |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [AddHandler][ [Me].editControl1.ConfigurationChanged, [AddressOf] editControl1_ConfigurationChanged ]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.ApplyConfiguration([\"XML\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] editControl1_ConfigurationChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\" ConfigurationChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p118} 

[]{#related-topics}

