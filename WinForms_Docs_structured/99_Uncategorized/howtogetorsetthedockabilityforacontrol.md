---
title: howtogetorsetthedockabilityforacontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtogetorsetthedockabilityforacontrol.md
created_at: 2025-08-05
---






##### How to get or set the dock ability for a control? {#how-to-get-or-set-the-dock-ability-for-a-control style="tab-stops: 0pt"}

[] 

The current dock ability for the controls can be retrieved or set using the below methods.

[] 


+-----------------------------------+---------------------------------------------------------------------------------+
| Methods                           | Description                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------+
| GetDockAbility                    | Retrieves the dock ability of the control. The parameter is,                    |
|                                   |                                                                                 |
|                                   | *[]*                                      |
|                                   |                                                                                 |
|                                   | *Ctrl* - Indicates the docked control for which DockAbility has to be obtained. |
+-----------------------------------+---------------------------------------------------------------------------------+
| SetDockAbility                    | Sets the dock ability of the control.                                           |
|                                   |                                                                                 |
|                                   |                                                                                 |
|                                   |                                                                                 |
|                                   | *Ctrl* - Indicates the docked control for which DockAbility need to be set.     |
+-----------------------------------+---------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [//Getting the Dock Ability]                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [this][.dockingManager1.GetDockAbility([this].panel2);]                                                  |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [//Setting the Dock Ability]                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [this][.dockingManager1.SetDockAbility([this].panel2, [\"Bottom, Horizontal\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [\'Getting the Dock Ability]                                                                                                                                |
|                                                                                                                                                                                                               |
| [Me][.dockingManager1.GetDockAbility([Me].panel2)]                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [\'Setting the Dock Ability]                                                                                                                                |
|                                                                                                                                                                                                               |
| [Me][.dockingManager1.SetDockAbility([Me].panel2, [\"Bottom, Horizontal\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

