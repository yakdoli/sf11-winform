---
title: howtoapplyoffice2007silverblueandblackthemestothetabbedmdimanager.md
original_path: WinForms_Docs/02_Concepts/howtoapplyoffice2007silverblueandblackthemestothetabbedmdimanager.md
created_at: 2025-08-05
---






#### How to apply Office2007 Silver, Blue, and Black themes to the TabbedMDIManager {#how-to-apply-office2007-silver-blue-and-black-themes-to-the-tabbedmdimanager style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

You can apply Office2007ColorScheme when TabControl is added as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [private][ [void] tabbedMDIManager_TabControlAdded([object] sender, [TabbedMDITabControlEventArgs] args)] |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [    args.TabControl.Office2007ColorScheme = [Office2007Theme].Black;]                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| [} ]                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] tabbedMDIManager_TabControlAdded([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.TabbedMDITabControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [    tabControl = args.TabControl]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [    args.TabControl.Office2007ColorScheme = Office2007Theme.Black]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p942} 

[]{#related-topics}

