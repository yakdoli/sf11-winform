---
title: howtoactivateaparticulardockedcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoactivateaparticulardockedcontrol.md
created_at: 2025-07-03
---






##### How to activate a particular docked control?[] {#how-to-activate-a-particular-docked-control style="tab-stops: 0pt"}

You can call the ActivateControl method inside NewDockStateEndLoad event to achieve this.

**[]** 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ActivateControl                   | Activates the docked control which is passed as a parameter to this method. This method will be effective only when the control is tabbed to other control or controls. This method can be called from a handler for DockingManager.NewDockStateEndLoad Event. The parameter is, |
|                                   |                                                                                                                                                                                                                                                                                  |
|                                   | *[]*                                                                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                  |
|                                   | *Ctrl* - Indicates the docking window.                                                                                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [//The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [private][ [void] dockingManager1_NewDockStateEndLoad([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [this][.dockingManager1.ActivateControl([this].listBox1);]                                                                              |
|                                                                                                                                                                                                                                                   |
| [Console][.WriteLine([\"Listbox is activated\"]);]                                                                                    |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [\'The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] dockingManager1_NewDockStateEndLoad([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.dockingManager1.ActivateControl([Me].listBox1)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\"Listbox is activated\"])]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p123}[]{#_How_to_change} 

[]{#related-topics}

