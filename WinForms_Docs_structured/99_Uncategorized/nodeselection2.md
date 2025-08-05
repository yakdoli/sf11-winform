---
title: nodeselection2.md
original_path: WinForms_Docs/99_Uncategorized/nodeselection2.md
created_at: 2025-08-05
---






##### Node Selection {#node-selection style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[]{#p973}[] 

During drag and drop operation of the tree nodes, a single node or same level nodes or multi level nodes can be selected and dragged based on the selection mode set for the treeview control. **SelectionMode** property is used for this purpose.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| TreeViewAdv Properties            | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| SelectionMode                     | Specifies the selection mode of the treeview.                                                                              |
|                                   |                                                                                                                            |
|                                   | Options are,                                                                                                               |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | *Single* - The user can only select one node at a time and implement the drag-drop operation in the TreeViewAdv (Default). |
|                                   |                                                                                                                            |
|                                   | *MultiSelectSameLevel* - The user can only select nodes of the same level, i.e. only child nodes or only parent nodes.     |
|                                   |                                                                                                                            |
|                                   | *MultiSelectAll* - The user can select multiple nodes for implementing the DragDrop operation in the TreeViewAdv.          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [this][.treeViewAdv1.SelectionMode = TreeSelectionMode.MultiSelectSameLevel;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                       |
| [Me][.treeViewAdv1.SelectionMode = TreeSelectionMode.MultiSelectSameLevel][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 1137: Various Selection mode of TreeView Control

**[]** 

Extending the Selection

 

We can extend the selection of the nodes using ExtendSelectionTo method. []{#p974}

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Methods                           | Parameter                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------+
| ExtendSelectionTo                 | Extends the selection of the node to a specified node.                                               |
|                                   |                                                                                                      |
|                                   |                                                                                                      |
|                                   |                                                                                                      |
|                                   | *SelNode* - Represents a treeNodeAdv.                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------+
| ExtendSelectionTo (Overloaded)    | *SelNode* - Represents a treeNodeAdv.                                                                |
|                                   |                                                                                                      |
|                                   | *removeCurrentMultipleSelection* - Indicates whether or not any current selection should be removed. |
+-----------------------------------+------------------------------------------------------------------------------------------------------+


[] 


{border="0"} Note : This method will be effective only when the SelectionMode is MultiSelectSameLevel or MultiSelectAll.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [//Extend Selection using below method]                                                                                                                                                |
|                                                                                                                                                                                                                                          |
| [this][.treeViewAdv1.ExtendSelectionTo([this].treenode1);]                                                                     |
|                                                                                                                                                                                                                                          |
| [//Overloaded Method]                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [this][.treeViewAdv1.ExtendSelectionTo([this].treenode1, [false]);][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                                    |
|                                                                                                                                                                                               |
| [\'Extend Selection using below method]                                                                                                     |
|                                                                                                                                                                                               |
| [Me][.treeViewAdv1.ExtendSelectionTo([Me].treenode1)]                               |
|                                                                                                                                                                                               |
| [\'Overloaded Method]                                                                                                                       |
|                                                                                                                                                                                               |
| [Me][.treeViewAdv1.ExtendSelectionTo([Me].treenode1, [False])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

On Focus / Off Focus

 


  ------------------------- -----------------------------------------------------------------------------------------------------------------------------------------
  TreeViewAdv Properties    Description
  ShouldSelectNodeOnEnter   Indicates whether a default node should be selected when the treeviewadv control gains focus. By default this property is true.
  HideSelection             Indicates if the treeviewadv hides its selected nodes when not focussed. This should be set to false to highlight the select the nodes.
  ------------------------- -----------------------------------------------------------------------------------------------------------------------------------------


[] 

See Also

[] 

[[How to select a particular node as a first visible node?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_select)[]

 

 

 

 

###### []{#p975}[]{#_Mouse_and_Keyboard}3.11.3.2.3.1    Mouse and Keyboard Based Selection {#mouse-and-keyboard-based-selection style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Setting **AllowKeyboardSearch** property of the treeview to true, will allow the user to search for a node by typing the name of the node using the keyboard. User have to ensure that the TreeViewAdv control is focussed while searching.

 

By setting the **AllowMouseBasedSelection** property to true, multiple nodes can be selected with mouse down and these selected nodes can be dragged.

[] 


  -------------------------- --------------------------------------------------------------------------------
  TreeViewAdv Properties     Description
  AllowKeyboardSearch        Gets or sets a value indicating if keyboard based searching should be allowed.
  AllowMouseBasedSelection   Indicates if multiple nodes can be selected with mouse down and drag.
  -------------------------- --------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [this][.treeViewAdv1.AllowKeyboardSearch = [false];]                                                                                  |
|                                                                                                                                                                                                                                                 |
| [this][.treeViewAdv1.AllowMouseBasedSelection = [true];[ ]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [Me][.treeViewAdv1.AllowKeyboardSearch = [False]]                                                        |
|                                                                                                                                                                                                                    |
| [Me][.treeViewAdv1.AllowMouseBasedSelection = [True]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

