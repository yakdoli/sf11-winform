---
title: activatingcurrentcellbehavior.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\activatingcurrentcellbehavior.md
created_at: 2025-07-03
---






##### Activating Current Cell Behavior {#activating-current-cell-behavior style="tab-stops: 0pt"}

[] 

When moving the current cell or clicking inside a cell, you can control the current cell\'s activation behavior by using the **ActivateCurrentCellBehavior** property. The **GridCellActivateAction** enumeration defines when to set the focus on the cell or toggle to edit mode for the current cell.

[] 

Here is the list of options under the GridCellActivateAction enumeration:

[] 

[·      ]**ClickOnCell**-Setting ActivateCurrentCellBehavior to this option sets the cell to editing mode or sets focus on the cell after user clicks the cell.

[·      ]**DblClickOnCell**-Setting ActivateCurrentCellBehavior to this option sets the cell to editing mode or sets focus on the cell when user double clicks the cell.

[·      ]**None**-Setting ActivateCurrentCellBehavior to this option deactivates the cell, even if the user clicks it.

[·      ]**PositionCaret**-Setting ActivateCurrentCellBehavior to this option sets the caret to be positioned at the character where the user clicks.

[·      ]**SelectAll**-Setting ActivateCurrentCellBehavior to this option sets the cell to editing mode or sets focus on the cell and keeps the entire text in the cell selected whenever it becomes the current cell irrespective of the click on the cell or movement over it using arrow keys.

[·      ]**SetCurrent**-Setting ActivateCurrentCellBehavior to this option sets the cell to editing mode or sets focus on the cell whenever it becomes the current cell irrespective of the click on the cell or movement over it using arrow keys.

[] 

The following code examples illustrate how to set the ActivateCurrentCellBehavior property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [this][.gridControl1.ActivateCurrentCellBehavior = [GridCellActivateAction].SelectAll;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [Me][.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.SelectAll] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p78} 

 

[]{#related-topics}

