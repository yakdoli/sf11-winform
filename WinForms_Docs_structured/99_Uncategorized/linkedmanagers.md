---
title: linkedmanagers.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\linkedmanagers.md
created_at: 2025-07-03
---






##### Linked Managers {#linked-managers style="tab-stops: 0pt"}

[] 

Linked Manager concept allows the transfer of a docking window from one form to another form or usercontrol. It is done with a single method call.

 

**AddToTargetManagersList** method will let you add the DockingManager to the Target DockingManagers list, and hence transfers the docking window to the selected target form.

 

**RemoveFromTargetManagersList** method, removes the DockingManager from the TargetManagers List.

 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| Method                            | Description                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| AddToTargetManagersList           | Adds the DockingManager to the Target Providers List, belonging to the current manager. The parameter is,      |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   | *dockingmgr* - docking manager to be added to the target list.                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| RemoveFromTargetManagersList      | Removes the DockingManager from the Target Providers List, belonging to the current manager. The parameter is, |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|                                   | *dockingmgr* - docking manager to be removed from the target list.                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [//Control from form2 to be transferred to form1]                                                     |
|                                                                                                                                                         |
| [//dockingManager1 an instance of Form1 and dockingManager2 an instance of Form2]                     |
|                                                                                                                                                         |
| [this][.dockingManager1.AddToTargetManagersList(dockingManager2);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| **[]**                                                                                             |
|                                                                                                                                                      |
| [\'Control from form2 to be transferred to form1]                                                  |
|                                                                                                                                                      |
| [\'dockingManager1 an instance of Form1 and dockingManager2 an instance of Form2]                  |
|                                                                                                                                                      |
| [Me][.dockingManager1.AddToTargetManagersList(dockingManager2)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Events during the Transfer of Docking Manager

[] 

If any control comes from other docking manager, TransferredToManager event will be handled and if a control is transferred out to other docking managers, TransferredFromManager event will be handled.

[] 

Sample

[] 

A sample which demonstrates the Linked Managers concept is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Docking Package\\LinkedManagers

[]{#related-topics}

