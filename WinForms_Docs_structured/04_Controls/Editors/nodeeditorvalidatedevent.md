---
title: nodeeditorvalidatedevent.md
original_path: WinForms_Docs/04_Controls/Editors/nodeeditorvalidatedevent.md
created_at: 2025-08-05
---






##### NodeEditorValidated Event {#nodeeditorvalidated-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is raised after the newly entered text in the Node editor gets stored.

 

**Event Data**

 

The event handler receives an argument of type TreeNodeAdvEditEventArgs containing data related to this event. The following TreeNodeAdvEditEventArgs properties provide information specific to this event.

[] 


  --------- ---------------------------------------------------------
  Members   Description
  Label     Returns the label for the node.
  Node      Returns the TreeNodeAdv that is currently being edited.
  --------- ---------------------------------------------------------


[]{#p999}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [private][ [void] treeViewAdv1\_[NodeEditorValidated]([object] sender, Syncfusion.Windows.Forms.Tools.[TreeNodeAdvEditEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [//This prints the label for the node in the output window at run time.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Console][.Write([\"Label :\"] + e.Label.ToString());]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [//This prints the treenodeadv associated with the event in the output window at run time.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                |
| [Console][.Write([\"TreeNodeAdv :\"] + e.Node.ToString());]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [}][]                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private Sub ][treeViewAdv1\_[NodeEditorValidated(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ Syncfusion.Windows.Forms.Tools.][TreeNodeAdvEditEventArgs][)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \'][This prints the treenodeadv action associated with the event in the output window at run time.]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console][.Write([\"Label :\"] + e.Action.ToString())]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\'This prints the treenodeadv associated with the event in the output window at run time.]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console][.Write([\"TreeNodeAdv :\"] + e.Node.ToString())]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

