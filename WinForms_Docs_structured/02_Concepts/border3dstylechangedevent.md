---
title: border3dstylechangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\border3dstylechangedevent.md
created_at: 2025-07-03
---






##### Border3DStyleChanged Event {#border3dstylechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is handled when the value of the **Border3DStyle** property is changed. The Border3DStyle property indicates the style of the 3D border.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Set the 3D border style for the StatusBarAdv control using the Border3DStyle property.]                                                                                             |
|                                                                                                                                                                                                                                           |
| [this][.statusBarAdv1.Border3DStyle = System.Windows.Forms.[Border3DStyle].Bump;]                                               |
|                                                                                                                                                                                                                                           |
| [// Set the BorderStyle property to \'Fixed3D\' to view the 3D border style.]                                                                                                           |
|                                                                                                                                                                                                                                           |
| [this][.statusBarAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].Fixed3D;]                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Handle the Border3DStyleChanged event.]                                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [this][.statusBarAdv1.Border3DStyleChanged+=[new] [EventHandler](statusBarAdv1_Border3DStyleChanged);]     |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [private][ [void] statusBarAdv1_Border3DStyleChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                            |
|                                                                                                                                                                                                                                           |
| [Console][.WriteLine([\" Border3DStyleChanged event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Set the 3D border style for the StatusBarAdv control using the Border3DStyle property. ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.statusBarAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Set the BorderStyle property to \'Fixed3D\' to view the 3D border style. ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| [Me][.statusBarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D ]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Handle the Border3DStyleChanged event. ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| [AddHandler][ [Me].statusBarAdv1.Border3DStyleChanged, [AddressOf] statusBarAdv1_Border3DStyleChanged ]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] statusBarAdv1_Border3DStyleChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [    Console.WriteLine([\" Border3DStyleChanged event is raised \"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

