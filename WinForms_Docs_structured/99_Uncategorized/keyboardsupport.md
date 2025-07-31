---
title: keyboardsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\keyboardsupport.md
created_at: 2025-07-03
---






##### Keyboard Support {#keyboard-support style="tab-stops: 0pt"}

[] 

The TreeView control can be set to respond to cursor keys.

You can navigate through the nodes and expand / collapse by using the Arrow keys.

[] 


  ------------- -----------------------------------------------------------------------------------------------------------------------------------
  Arrow Key     Functionality
  UP ARROW      To move up through the TreeView.
  DOWN ARROW    To move down through the TreeView.
  LEFT ARROW    To collapse the selected node. If the left arrow key is pressed when the node is in collapsed state, it moves to its parent node.
  RIGHT ARROW   To expand the selected node. If the right arrow key is pressed when the node is in expanded state, it moves to its first child.
  ------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

The following keys can be used to select node, edit node text and to check / uncheck a node.

[] 


  ----------------- ------------------------------------------------------------------------------------------------------------
  Key               Functionality
  F2                To edit the selected node.
  ENTER             To select a node.
  ESC               To undo the modifications done to the node and return to the original state when the node is in edit mode.
  SPACEBAR          Toggles the state of the checkbox when a node is selected.
  HOME / PAGE UP    To select first node of the tree.
  END / PAGE DOWN   To select last node of the tree.
  ----------------- ------------------------------------------------------------------------------------------------------------


 

[]{#related-topics}

