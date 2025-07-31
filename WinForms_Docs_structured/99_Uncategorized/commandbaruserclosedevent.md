---
title: commandbaruserclosedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\commandbaruserclosedevent.md
created_at: 2025-07-03
---






##### CommandBarUserClosed Event {#commandbaruserclosed-event style="tab-stops: 0pt"}

[] 

This event is raised when a floating CommandBar is hidden by the user, i.e., when the user presses the close button of the CommandBar that exists in the float state.

 

The event handler receives an argument of type **EventArgs** containing data related to this event.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Set the CommandBar control to its Floating state.]                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [this][.commandBar1.DisableDocking = [true];]                                                                                 |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Handle the CommandBarUserClosed event.]                                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [this][.commandBar1.CommandBarUserClosed+=[new] [EventHandler](commandBar1_CommandBarUserClosed);]       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [private][ [void] commandBar1_CommandBarUserClosed([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [{   ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [   // This event is fired when the Floating CommandBar is closed. The below line will be displayed in the output window at runtime.]                                                 |
|                                                                                                                                                                                                                                         |
| [   MessageBox][.Show([\" CommandBarUserClosed Event is raised \"]);]                                                       |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Set the CommandBar control to its Floating state. ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.commandBar1.DisableDocking = [True] ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Handle the CommandBarUserClosed event. ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [AddHandler][ [Me].commandBar1.CommandBarUserClosed, [AddressOf] commandBar1_CommandBarUserClosed]                                                                                             |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] commandBar1_CommandBarUserClosed([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                               |
| [    [\' This event is fired when the Floating CommandBar is closed. The below line will be displayed in the output window at runtime. ]]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                               |
| [    MessageBox.Show([\" CommandBarUserClosed Event is raised \"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

