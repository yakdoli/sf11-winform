---
title: howtofindoutwhetheradockedcontrolisfloatingornot.md
original_path: WinForms_Docs/99_Uncategorized/howtofindoutwhetheradockedcontrolisfloatingornot.md
created_at: 2025-08-05
---






##### How to find out whether a docked control is floating or not? {#how-to-find-out-whether-a-docked-control-is-floating-or-not style="tab-stops: 0pt"}

[] 

This can be achieved by calling IsFloating method.

 

This method returns a value indicating whether the control is in docked or floating state. If the control is in floating state, the value returned will be true, and if it is docked, value returned will be false.

[] 


+-----------------------------------+---------------------------------------------------------------------------------+
| Method                            | Description                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------+
| IsFloating                        | Gets the value indicating whether the docked control is floating or not.        |
|                                   |                                                                                 |
|                                   | *[]*                                      |
|                                   |                                                                                 |
|                                   | *Ctrl* - Indicates the control for which dock / floating state is been queried. |
+-----------------------------------+---------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)]                             |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [this][.dockingManager1.IsFloating([this].panel1);]                                                                                    |
|                                                                                                                                                                                                                                                  |
| [Console][.Write([\"Dock state : \"] + [this].dockingManager1.IsFloating([this].panel1));] |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] dockingManager1_NewDockStateEndLoad([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.dockingManager1.IsFloating([Me].panel1)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console][.Write([\"Dock state : \"] + [Me].dockingManager1.IsFloating([Me].panel1))]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

