---
title: treenode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\treenode.md
created_at: 2025-07-03
---






##### TreeNode {#treenode style="tab-stops: 0pt"}

 

This section covers information on the following topics.

 

###### []{#_Node_Editing}5.3.1.2.4.1 Node Editing {#node-editing style="tab-stops: 0pt"}

[] 

Nodes can allowed / denied from being edited at run time. TreeView control supports node editing in client side. You can simply select a node and press F2 or click an already selected node and you\'ll able to edit the node text client side.

 

This can be set by using **EditNode** property programmatically. This property can be set for the entire control or can also be set for individual nodes by setting the property in the TreeView Designer dialog. Also styles can be set for the node on which the editing action is performed by using **EditNodeCssClass**.

[] 


+-----------------------------------+------------------------------------------------------------------------------+
|                                   |                                                                              |
|                                   |                                                                              |
| Property                          | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| EditNode                          | Specifies whether to allow the user to edit the node. Default value is True. |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

Programmatically it can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                   |
|                                                                                                    |
| []                                |
|                                                                                                    |
| [Tree.EditNode = [true];] |
+----------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                          |
|                                                                                                                                                                              |
| [Private][ Tree.EditNode = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 174: Html tags used for the Network node with node editing set at run time

**[]** 

{border="0"}

Figure 175

[] 

CSS styles can be applied to the nodes while editing the node text using **NodeEditCssClass** property. Just assign the class name of the css definition, that should be applied while editing node, to this property.

[] 


  ------------------ -------------------------------------------------------------
  Property           Description
  NodeEditCssClass   Specifies styles for the nodes while editing the node text.
  ------------------ -------------------------------------------------------------


[] 


{border="0"}Note: Set the name of the stylesheet to the CustomCss property.


[] 

Supported Events

[] 

**Server-Side Events**

**[]** 

[·      ][NodeRenamed Event]{.UGHyperlink}: the event that fires, when node text has been changed

[·      ]To fire this event, the AutoPostBackOnNodeRename is set to True.

[] 

Properties

**[]** 

[·      ]**AutoPostBackOnNodeRename** **(TreeView)**: indicates whether to postback the page, when the node text is changed

[·      ]**EditNode** **(TreeView)**: indicates whether to allow the user to edit the node text

[·      ]**NodeEditCssClass**: class name of the css definitions to apply to html text element, on editing the node text

[·      ]**EditNode (TreeViewNode)**: indicates whether to allow the user to edit the node text

Values: True, False, and Inherit.

[] 

Client-Side Events

**[]** 

[·      ][ClientSideOnNodeRename Event]{.UGHyperlink} -- client-side event that is fired on node rename

 

This event is cancelable.

[] 

See Also

[] 

[How to get the node level in the server side]{.UGHyperlink}[, ]{.UGHyperlink}[How to get node level information in the client side]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p272}5.3.1.2.4.2 Node Drag and Drop {#node-drag-and-drop style="tab-stops: 0pt"}

 

TreeView provides support to drag-and-drop the nodes inside the control and also between different controls. The nodes can be moved elsewhere only on setting the **DragAndDropEnabled** property.

 

The drag and drop functionality can also be enabled or the status can be checked using the SetDragAndDropEnabled and GetDragAndDropEnabled methods.

[] 


  ----------------------- ----------- ------------------------------------------------------------------------------ -------------
  Method                  Parameter   Description                                                                    Return Type
  SetDragAndDropEnabled   bool        Set a value that indicates whether to allow nodes to be dragged and dropped.   \-
  GetDragAndDropEnabled   \-          Get a value that indicates whether to allow nodes to be dragged and dropped.   bool
  ----------------------- ----------- ------------------------------------------------------------------------------ -------------


[] 

Here, the drag and drop functionality can be enabled or disabled by when the checkbox is toggled and accordingly the value is set for the control using the SetDragAndDropEnabled property and the value of DragAndDropEnabled will be updated and displayed on the label as and when it is changed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DragDropEnable()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox0\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDragAndDropEnabled(status);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DragDropEnabled: \"] + treeview.GetDragAndDropEnabled();]                |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>\<][td][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox0\"] [OnChange][=\"DragDropEnable()\"] [/\>]Drag Drop Enable]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Additional to just enable dragging and dropping, there are other properties that can be used to control the drag and drop features. In unison with setting DragAndDropEnabled, to facilitate drag and drops, the following properties should be set accordingly.

 

The various drag and drop options supported by tree control are as follows.

[] 


  ---------------------------- ----------------------------------------------------------------------------------------------------------
  Property                     Description
  DragAndDropEnabled           Gets / sets the boolean value, whether to allow nodes to be dragged and dropped. Default value is False.
  DraggingAcrossTreesEnabled   Gets / sets the boolean value, whether to allow dragging nodes between controls. Default value is False.
  DropChildEnabled             Gets / sets boolean value that allows to create child nodes on  drag and drop. Default value is True.
  DroppingAcrossTreesEnabled   Gets / sets the boolean value, whether to allow dropping nodes between controls. Default value is True.
  DropRootEnabled              Gets / sets boolean value that allows to create root nodes on  drag and drop. Default value is True.
  DropSiblingEnabled           Gets / sets boolean value that allows to create child nodes on  drag and drop. Default value is False.
  ---------------------------- ----------------------------------------------------------------------------------------------------------


[] 

Also, the drag and drop feature can be specified for individual nodes by setting the DraggingEnabled and DroppingEnabled in the TreeView Designer window for every node.

[] 


  ----------------- -------------------------------------------------------------------------------
  Property          Description
  DraggingEnabled   Specifies whether to allow the nodes to be dragged. Default value is True.
  DroppingEnabled   Specifies whether to drop another node on or below it. Default value is True.
  ----------------- -------------------------------------------------------------------------------


[] 

Drag and Drop between controls

[] 

To only drag nodes from a TreeView control just set **DraggingAcrossTreesEnabled** property. And to only if the nodes should be allowed to accept new nodes via dragging then **DroppingAcrossTreesEnabled** property can be used.

 

The following methods can also be used to handle the drag and drop features across controls and retrieve the status.

[] 


  ------------------------------- --------------------------- ---------------------------------------------------------------------------------------- ---------------------------
  Method                          Parameter                   Description                                                                              Return Type
  SetDroppingAcrossTreesEnabled   bool                        Set a value that indicates whether to allow nodes to be dropped from another TreeView.   [-]
  GetDroppingAcrossTreesEnabled   [-]   Get a value that indicates whether to allow nodes to be dropped from another TreeView.   bool
  SetDraggingAcrossTreesEnabled   bool                        Set a value that indicates whether to allow nodes to be dragged to another TreeView.     [-]
  GetDraggingAcrossTreesEnabled   [-]   Get a value that indicates whether to allow nodes to be dragged to another TreeView.     bool
  ------------------------------- --------------------------- ---------------------------------------------------------------------------------------- ---------------------------


[] 

Here depending on the status of the checkbox, nodes can be allowed or denied from being dragged or dropped, and every time the value is changed the Get methods updates the boolean value on the label.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DragAcrossTree()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox3\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDraggingAcrossTreesEnabled(status);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DragAcrossTreeEnabled: \"] + treeview.GetDraggingAcrossTreesEnabled();]  |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    [function] DropAcrossTree()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox4\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDroppingAcrossTreesEnabled(status);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DropAcrossTreeEnabled: \"] + treeview.GetDroppingAcrossTreesEnabled();]  |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>\<][td][\>]                       ]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox3\"] [OnChange][=\"DragAcrossTree()\"] [/\>]Drag Across Tree Enable]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>\<][td][\>]                        ]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox4\"] [OnChange][=\"DropAcrossTree()\"] [/\>]Drop Across Tree Enable]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Adding as root node

[] 

The property **DropRootEnabled** allows a new root node to be added with the existing nodes. But on setting this property, the **DropSiblingEnabled** must also be set respectively.

 

This can also be set using the SetDropRootEnabled method and the value can be retrieved using the GetDropRootEnabled method.

[] 


  -------------------- ----------- --------------------------------------------------------------------------------- -------------
  Method               Parameter   Description                                                                       Return Type
  SetDropRootEnabled   bool        Set a value that indicates whether to allow dropping, to create new root nodes.   \-
  GetDropRootEnabled   \-          Get a value that indicates whether to allow dropping, to create new root nodes.   bool
  -------------------- ----------- --------------------------------------------------------------------------------- -------------


[] 

Here, the value of the checkbox is passed as the parameter for the SetDropRootEnabled method and every time the checkbox is toggled the GetDropRootEnabled method retrieves and displays it\'s value on the label.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DropRootEnable()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox1\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDropRootEnabled(status);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DropRootEnabled: \"] + treeview.GetDropRootEnabled();]                   |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>\<][td][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox1\"] [OnChange][=\"DropRootEnable()\"] [/\>]Drop Root Enable]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Adding nodes as siblings and Style settings

[] 

**DropSiblingEnabled** when set allows the user to drag a node and place it only as a sibling node.

 

This can also be set using the SetDropSiblingEnabled method and it\'s value can be obtained using GetDropSiblingEnabled method.

[] 


  ----------------------- ----------- ------------------------------------------------------------------------------------------------ -------------
  Method                  Parameter   Description                                                                                      Return Type
  SetDropSiblingEnabled   bool        Set a value that indicates whether to allow dropping, to create siblings (drop between nodes).   \-
  GetDropSiblingEnabled   \-          Get a value that indicates whether to allow dropping, to create siblings (drop between nodes).   bool
  ----------------------- ----------- ------------------------------------------------------------------------------------------------ -------------


[] 

Here, the checkbox can be toggled to enable or disable the DropSiblingEnabled feature and it\'s status will be displayed on the label.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DropSiblingEnable()]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox2\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDropSiblingEnabled(status);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DropSiblingEnabled: \"] + treeview.GetDropSiblingEnabled();]             |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [   \<][tr][\>\<][td][\>][                       ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [       [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox2\"] [OnChange][=\"DropSiblingEnable()\"] [/\>]Drop Child Enable]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [   [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**DropSiblingCssClass** can be used to set styles for the target node that gets applied when the node is held over it. Just set the class name of the css definition to this property.

[] 


  --------------------- ----------------------------------------------------------------------
  Property              Description
  DropSiblingCssClass   Specifies the look for the target node, before dropping the sibling.
  --------------------- ----------------------------------------------------------------------


[] 


{border="0"}Note: Set the name of the stylesheet to the CustomCss property.


[] 

     {border="0"}

**[]** 

Figure 176: DropsiblingCssClass applied for TreeView / Image2: Calendar node is added as Junk E-mail node\'s sibling

[] 

Adding child nodes and Style settings

[] 

**DropChildEnabled** when set, allows the user to drag a node and add it as a child to the target node.

 

SetDropChildEnabled allows you to handle this feature for the tree control and the status of which can be obtained using the GetDropChildEnabled method.

[] 


  --------------------- ----------- ------------------------------------------------------------------------------------------------ -------------
  Method                Parameter   Description                                                                                      Return Type
  SetDropChildEnabled   bool        Set a value that indicates whether to allow dropping, to create child nodes (drop into nodes).   \-
  GetDropChildEnabled   \-          Get a value that indicates whether to allow dropping, to create child nodes (drop into nodes).   bool
  --------------------- ----------- ------------------------------------------------------------------------------------------------ -------------


[] 

Here, as the checkbox is toggled, it\'s value will be passed as a parameter to the SetDropChildEnabled method and the feature will be handled accordingly and it\'s value is displayed on the label using the GetDropChildEnabled method.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DropChildEnable()]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] status=document.getElementById([\"Checkbox2\"]).checked;]                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDropSiblingEnabled(status);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DropChildEnabled: \"] + treeview.GetDropSiblingEnabled();]               |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>\<][td][\>]                       ]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][input] [type][=\"checkbox\"] [id][=\"Checkbox2\"] [OnChange][=\"DropChildEnable()\"] [/\>]Drop Child Enable]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][td][\>\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The **DropChildCssClass** can be used to set styles for the target node (i.e., the styles that can be applied to highlight any of the target node, when the dragged node is hovered over it) before dropping the child. Just set the class name of the css definition to this property.

[] 


  ------------------- ----------------------------------------------------------------------
  Property            Description
  DropChildCssClass   Specifies the look for the target node, before dropping the sibling.
  ------------------- ----------------------------------------------------------------------


[] 


{border="0"}Note: Set the name of the stylesheet to the CustomCss property.


[] 

     {border="0"}

[] 

 Figure 177: DropChildCssClass applied for TreeView/ Fig2: Calendar node is added as Junk E-Mail node\'s child

[] 

Programmatically these properties can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                            |
| []                                                        |
|                                                                                                                            |
| [TreeView1.DragAndDropEnabled = [true];]          |
|                                                                                                                            |
| [TreeView1.DraggingAcrossTreesEnabled = [true];]  |
|                                                                                                                            |
| [TreeView1.DroppingAcrossTreesEnabled = [false];] |
|                                                                                                                            |
| [TreeView1.DropRootEnabled = [false];]            |
|                                                                                                                            |
| [TreeView1.DropSiblingEnabled = [true];]          |
|                                                                                                                            |
| [TreeView1.DropChildEnabled = [false];]           |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DragAndDropEnabled = [True]]          |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DraggingAcrossTreesEnabled = [True]]  |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DroppingAcrossTreesEnabled = [False]] |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DropRootEnabled = [False]]            |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DropSiblingEnabled = [True]]          |
|                                                                                                                                                                                                      |
| [Private][ TreeView1.DropChildEnabled = [False]]           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

DragHoverExpand

[] 

**DragHoverExpand** specifies the time duration, in milliseconds, after which the collapsed root node expands (if the node is collapsed) when the dragged node is held over the collapsed root node. A node can be simply dragged and dropped under the child node even though the node is collapsed just by holding the node over the collapsed root node.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                 |
|                                   |                                                                                                                                 |
| Property                          | Description                                                                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| DragHoverExpand                   | Specifies the time (in milliseconds) after which the collapsed node should expand when a node is held over that collapsed node. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the property can be set as follows.

[] 

+--------------------------------------------------------------------------------------------+
| **[\[C#\]]**                           |
|                                                                                            |
| []                        |
|                                                                                            |
| [TreeView1.DragHoverExpandDelay = 10;] |
+--------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [Private][ TreeView1.DragHoverExpandDelay = 10] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The expand delay can be set easily using the SetDragHoverExpandDelay method and the value can be retrieved using the GetDragHoverExpandDelay method.

[] 


  ------------------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  Method                    Parameter   Description                                                                                                                                 Return Type
  SetDragHoverExpandDelay   int         Set a value indicating the delay (in milliseconds) after which to expand the collapsed parent node, when the dragged node hovers over it.   [-]
  GetDragHoverExpandDelay   \-          Get a value indicating the delay (in milliseconds) after which to expand the collapsed parent node, when the dragged node hovers over it.   [int]
  ------------------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------


[] 

Here, the drag expand value should be chosen from the select options which will be passed to the set method. The get method will update the chosen value on the label.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] DragHoverExpandDelay()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        [var] delay=document.getElementById([\"Checkbox6\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [        treeview.SetDragHoverExpandDelay(1000);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [        document.getElementById([\"textarea\"]).innerText += [\"\\n\"] + [\"DragHoverExpandDelay: \"] + treeview.GetDragHoverExpandDelay();]         |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [AutoFormat][=\"Contacts\"] [BorderColor][=\"Gray\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [BorderStyle][=\"Solid\"] [BorderWidth][=\"1px\"] [Height][=\"211px\"] [Width][=\"160px\"] [ClientObjectId][=\"treeview\"\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<%][\--Add treeview nodes\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][td][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [            Drag Hover Expand Delay]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [            [\<][select] [id][=\"Select1\"] [OnChange][=\"DragHoverExpandDelay()\"\>]]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][option] [value][=\"100\"\>]100[\</][option][\>]]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][option] [value][=\"1000\"\>]1000[\</][option][\>]]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][option] [value][=\"1500\"\>]5000[\</][option][\>]]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [            [\</][select][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [        [\</][td][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][label][ [id][=\"textarea\"] [style][=\"width: 301px; height: 113px\"\>\</][label][\>]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[How to get the node level in the server side]{.UGHyperlink}[, ]{.UGHyperlink}[How to get node level information in the client side]{.UGHyperlink}[]{.UGHyperlink}

###### 5.3.1.2.4.3 Node\'s Visibility {#nodes-visibility style="tab-stops: 0pt"}

[] 

**EnsureVisibleItem** method is used to ensure that the selected item is visible. After the document is loaded, TreeView root html control will be scrolled automatically and selected item would be visible.

[] 


  ------------------------------- ------------------------------------------------------------------------------------------------
  Method                          Description
  EnsureVisibleItem(bool Value)   Ensures the visible selected item. If set to true, selected item will be visible on page load.
  ------------------------------- ------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                                         |
| [this][.TreeView1.EnsureVisibleItem([true]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                     |
|                                                                                                                      |
| []                                                  |
|                                                                                                                      |
| [this.TreeView1.EnsureVisibleItem([true]);] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 178: TreeView set with EnsureVisibleItem

 

###### 5.3.1.2.4.4 Multi-Node Selection {#multi-node-selection style="tab-stops: 0pt"}

[] 

TreeView control supports multiple selection mode, which allows the user to select more than one TreeViewNode at once by holding:

[] 

[·      ]CTRL key -- one by one selection or

[·      ]SHIFT key -- block selection.

[] 

The multiple nodes can be selected by enabling the **MultipleSelection** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"Server\"] [MultipleSelection][=\"true\"\>] [\</][syncfusion][:][TreeView][\>] ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Server-Side Properties

**[]** 


  ------------------- ----------------------------------------------------------------------------------------------------------
  Property            Description
  MultipleSelection   Specifies whether to allow the user to select multiple TreeViewNodes. Default value is False.
  SelectedNodes       Returns the selected nodes of type TreeViewNode.
  UnSelectAll         Specifies unselecting all the selected TreeViewNodes.  (TreeView1.UnSelectAll(TreeView1.SelectedNodes);)
  ------------------- ----------------------------------------------------------------------------------------------------------


[] 

The multi-selected nodes can be retrieved using the property **SelectedNodes** upon postback, which returns a collection of the nodes that have been selected. Refer the below code snippet to get the selected nodes in **ButtonClick** event.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [protected][ [void] Button1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [    [foreach] (TreeViewNode tv [in] TreeView1.SelectedNodes)]                                                                                           |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        Text1.Text  +=  tv.Text;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] Button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [For] [Each] tv [As] TreeViewNode [In] TreeView1.SelectedNodes]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [        Text1.Text += tv.Text]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [    [Next] tv]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Client-Side APIs

[] 


  ----------------------------- ----------------------------------------------------------------------------------
           Property             Description
  SetMultipleSelection(value)   Sets the value for MultiSelection. (\_sfTreeView1.SetMultipleSelection(true);)
  GetMultipleSelection          Gets the value for the MultipleSelection. (\_sfTreeView1.GetMultipleSelection();
  GetIsMultipleSelection        Check if the MultipleSelection is enabled or not.
  GetSelectedNodes              Returns an array of selected nodes.
  ----------------------------- ----------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"Text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] GetMultipleNodes(node)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [    {   ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [        [var] txt=document.getElementById([\'TextBox1\']);]                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [        [var] nodes=\_sfTreeView1.GetSelectedNodes(); [var] node=[null];]                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [        [for](node=0;node\<nodes.length;node++)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [            txt.innerHTML=txt.innerHTML + nodes\[node\].Text +[\"\\n\"];]                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [   }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [   ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.3.1.2.4.5 Node Sorting {#node-sorting style="tab-stops: 0pt"}

[] 

Nodes and SubNodes of the TreeView control are sorted by using either the **Sort** method or the **TreeViewNodeSorter** property.

[] 

Sort

[] 

Sort is a server-side method that enables you to sort all the nodes and subnodes of the TreeView control, based on the **Text** property of the nodes. You can override this by using the **TreeViewNodeSorter** property. Once this method is applied, the nodes that have been added, get sorted automatically.

[] 

+-------------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                         |
| []     |
|                                                                         |
| [TreeView1.Sort();] |
+-------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------+
| **[\[VB\]]**       |
|                                                                        |
| []    |
|                                                                        |
| [TreeView1.Sort()] |
+------------------------------------------------------------------------+

[] 

TreeViewNodeSorter

[] 

TreeViewNodeSorter property accepts the instance of the class that interfaces the Icomparer. This property is used to override the default node comparison by using the **Text** property of the nodes. It enables to compare node properties like node text length, value, and so on.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [// Create a node sorter that implements the IComparer interface.]                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [public][ [class] [NodeSorter] : IComparer]                                        |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [// Compare the length of the strings, or the strings themselves, if they are of the same length.]                                                                                 |
|                                                                                                                                                                                                                                                      |
| [public][ [int] Compare([object] x, [object] y)]                 |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [TreeViewNode tx = x [as] TreeViewNode;]                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [TreeViewNode ty = y [as] TreeViewNode;]                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [if][( tx.HasSubNodes == ty.HasSubNodes )]                                                                                      |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [return][ [string].Compare(tx.Text, ty.Text);]                                                             |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [else]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [return][ ( tx.HasSubNodes )? -1 : 1;]                                                                                          |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [// Compare the length of the strings, returning the difference.]                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [if][ (tx.Text.Length != ty.Text.Length)]                                                                                       |
|                                                                                                                                                                                                                                                      |
| [return][ tx.Text.Length - ty.Text.Length;]                                                                                     |
|                                                                                                                                                                                                                                                      |
| [// If they are the same length, call Compare.]                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [return][ [string].Compare(ty.Text, tx.Text);]                                                             |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [protected][ [override] [void] OnInitComplete([EventArgs] e)] |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [base][.OnInitComplete(e);]                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [// We should set TreeViewNodeSorter during each postbacks, because new added nodes should be sorted.]                                                                             |
|                                                                                                                                                                                                                                                      |
| [TreeView1.TreeViewNodeSorter = [new] [NodeSorter]();]                                                                                              |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Create a node sorter that implements the IComparer interface.]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Public][ [Class] NodeSorter]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Implements][ IComparer]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Compare the length of the strings, or the strings themselves, if they are of the same length.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Public][ [Function] Compare([ByVal] x [As] [Object], [ByVal] y [As] [Object]) [As] [Integer]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ tx [As] TreeViewNode = [TryCast](x, TreeViewNode)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ ty [As] TreeViewNode = [TryCast](y, TreeViewNode)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [If][ tx.HasSubNodes = ty.HasSubNodes [Then]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Return][ [String].Compare(tx.Text, ty.Text)]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Else]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Return][ [If]((tx.HasSubNodes), -1, 1)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Compare the length of the strings, returning the difference.]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [If][ tx.Text.Length \<\> ty.Text.Length [Then]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Return][ tx.Text.Length - ty.Text.Length]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' If they are the same length, call Compare.]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Return][ [String].Compare(ty.Text, tx.Text)]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Function]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Class]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Protected][ [Overloads] [Overrides] [Sub] OnInitComplete([ByVal] e [As] EventArgs)]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MyBase][.OnInitComplete(e)]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'We should set TreeViewNodeSorter during each postbacks, because new added nodes should be sorted.]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [TreeView1.TreeViewNodeSorter = [New] NodeSorter()]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

