---
title: containercontrolchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\containercontrolchangedevent.md
created_at: 2025-07-03
---






#### ContainerControlChanged Event[]{#p837} {#containercontrolchanged-event style="tab-stops: 0pt"}

[] 

This event is handled, when the **ContainerControl** property is changed.

 

The event handler receives an argument of type **EventArgs** containing data related to this event.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [// Initialize the new ContainerControl.]                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [this][.borderLayout1.ContainerControl = [this].panel1;]                                                                           |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Handle the ContainerControlChanged event.]                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [this][.borderLayout1.ContainerControlChanged+=[new] [EventHandler](borderLayout1_ContainerControlChanged);]  |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [private][ [void] borderLayout1_ContainerControlChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// ContainerControlChanged event is raised when the ContainerControl for the Layout Manager is changed. The below statement can be seen in the output window at runtime.]                 |
|                                                                                                                                                                                                                                              |
| [Console][.Write([\"Container Control is changed to Panel\"] );]                                                                 |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Initialize the new ContainerControl. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.borderLayout1.ContainerControl = [Me].panel1 ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Handle the ContainerControlChanged event. ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                    |
| [AddHandler][ [Me].borderLayout1.ContainerControlChanged, [AddressOf] borderLayout1_ContainerControlChanged ]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] borderLayout1_ContainerControlChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [    [\' ContainerControlChanged event is raised when the ContainerControl for the Layout Manager is changed. The below statement can be seen in the output window at runtime. ]]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [    Console.Write([\"Container Control is changed to Panel\"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

