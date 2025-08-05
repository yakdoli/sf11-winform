---
title: positioningnodesingroup.md
original_path: WinForms_Docs/99_Uncategorized/positioningnodesingroup.md
created_at: 2025-08-05
---






#### Positioning nodes in Group {#positioning-nodes-in-group style="tab-stops: 0pt"}

Positioning support

Diagram Group node supports absolute and relative positioning.

[]{#_Positioning_Group_node’s}Positioning Group node's Child

Group Node has an enum property called **GroupNodePosition** of type **GroupNodePositions** to position its child nodes. GroupNodePositions has two values Absolute and Relative. The Absolute will place the nodes inside a group based on their actual pinpoint whereas the Relative will place the nodes based on their default pinpoint. Default value is *Relative*.

 

[]{#OLE_LINK4}[]{#OLE_LINK3} 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                         |
| [//Group]                                                                                                             |
|                                                                                                                                                                         |
| [Group][ group = [new] [Group]();] |
|                                                                                                                                                                         |
| [//Absolute positioning]                                                                                              |
|                                                                                                                                                                         |
| [group.GroupNodePosition = [GroupNodePositions].Absolute;]                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                |
|                                                                                                                                                                                                    |
| [\'Group][]                                                                                                  |
|                                                                                                                                                                                                    |
| [Dim][ group [As] Group = [New] [Group] ()] |
|                                                                                                                                                                                                    |
| [\'Absolute positioning][]                                                                                   |
|                                                                                                                                                                                                    |
| [group.GroupNodePosition = [GroupNodePositions].Absolute][]                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 86: Group Node Absolute positioning

{border="0"}

Figure 87: Group Node Relative positioning

 

 

Properties

+-------------------+--------------------------------------------------------------------------+--------------------+---------------+----------------+-----------------------+
| Name              | Description                                                              | Type               | Default value | Value Accepted | Reference             |
+-------------------+--------------------------------------------------------------------------+--------------------+---------------+----------------+-----------------------+
| GroupNodePosition | Specifies the mode in which the group node's child should be positioned. | GroupNodePositions | Relative      | Absolute,      | [GroupNodePosition]() |
|                   |                                                                          |                    |               |                |                       |
|                   |                                                                          |                    |               | Relative       |                       |
+===================+==========================================================================+====================+===============+================+=======================+

[]{#p50} 

[]{#related-topics}

