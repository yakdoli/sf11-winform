---
title: dockvisibilitystate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dockvisibilitystate.md
created_at: 2025-07-03
---






##### Dock Visibility State {#dock-visibility-state style="tab-stops: 0pt"}

[] 

This section covers the following events:

[] 

###### []{#_DockVisibilityChanged_Event}3.2.3.8.6.1 DockVisibilityChanged Event {#dockvisibilitychanged-event style="tab-stops: 0pt"}

[] 

This event occurs after a control\'s DockVisibility state has changed. When the user clicks on the close button, the control\'s visibility changes and at this moment DockVisibilityChanged event will be handled. We can also use dockingManager.GetDockVisibility(control) method to know the current status of the docking window.

**[]** 

Event Data

[] 

The event handler receives an argument of type DockVisibilityChangedEventArgs containing data related to this event. The following DockVisibilityChangedEventArgs properties provide information specific to this event.

[] 


  --------- ----------------------------------------------------
  Member    Description
  Control   Gets the control undergoing the visibility change.
  --------- ----------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [//this event triggers when the control\'s visibility has changed. ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [private][ [void] dockingManager1_DockVisibilityChanged([object] sender, Syncfusion.Windows.Forms.Tools.[DockVisibilityChangedEventArgs] arg)] |
|                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [    [//GetDockVisibility method gives the detail of the docked control visibility ]]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [    [if] ([this].dockingManager1.GetDockVisibility(arg.Control) == [false])]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| [        [//DockVisibilityChangedEventArgs instance arg holds the control being changed the visibility  ]]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [        [MessageBox].Show([this].dockingManager1.GetDockLabel(arg.Control) + [\" \"] + [\" window is closed.\"]);]                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [} ]                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\'this event triggers when the control\'s visibility has changed. ]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] dockingManager1_DockVisibilityChanged([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockVisibilityChangedEventArgs) [Handles]  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    dockingManager1.DockVisibilityChanged()]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\'GetDockVisibility method gives the detail of the docked control visibility ]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [If] [Me].dockingManager1.GetDockVisibility(arg.Control) = [False] [Then]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        [\'DockVisibilityChangedEventArgs instance arg holds the control being changed the visibility  ]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        MessageBox.Show([Me].dockingManager1.GetDockLabel(arg.Control) + [\" \"] + [\" window is closed.\"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [If]]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p108}[]{#_DockVisibilityChanging_Event}3.2.3.8.6.2 DockVisibilityChanging Event {#dockvisibilitychanging-event style="tab-stops: 0pt"}

 

An use case demonstrating this event is available at How to prevent closing of docked window?.

 

[]{#p109} 

[]{#related-topics}

