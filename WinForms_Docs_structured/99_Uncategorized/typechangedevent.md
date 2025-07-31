---
title: typechangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\typechangedevent.md
created_at: 2025-07-03
---






##### TypeChanged Event {#typechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **PanelType** property is changed. The PanelType property indicates the type of the panel.

 

The event handler receives an argument of type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Set the type of the panel using the PanelType property of the control.]                                                                                                         |
|                                                                                                                                                                                                                                       |
| [this][.statusBarAdvPanel1.PanelType = Syncfusion.Windows.Forms.Tools.[StatusBarAdvPanelType].ScrollLockState;]             |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Handle the TypeChanged event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [this][.statusBarAdvPanel1.TypeChanged+=[new] [EventHandler](statusBarAdvPanel1_TypeChanged);]         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] statusBarAdvPanel1_TypeChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                        |
|                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\" TypeChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Set the type of the panel using the PanelType property of the control. ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.statusBarAdvPanel1.PanelType = Syncfusion.Windows.Forms.Tools.StatusBarAdvPanelType.ScrollLockState ]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Handle the TypeChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                             |
| [AddHandler][ [Me].statusBarAdvPanel1.TypeChanged, [AddressOf] statusBarAdvPanel1_TypeChanged ]                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] statusBarAdvPanel1_TypeChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                             |
| [    Console.WriteLine([\" TypeChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

