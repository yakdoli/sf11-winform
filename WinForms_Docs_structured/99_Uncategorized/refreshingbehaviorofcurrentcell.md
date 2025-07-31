---
title: refreshingbehaviorofcurrentcell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\refreshingbehaviorofcurrentcell.md
created_at: 2025-07-03
---






##### Refreshing Behavior of Current Cell {#refreshing-behavior-of-current-cell style="tab-stops: 0pt"}

[] 

The Grid property, **RefreshCurrentCellBehavior**, determines the behavior of refreshing the cells while the focus is moved from current cell to another. The **GridRefreshCurrentCellBehavior** enumeration specifies which cells to refresh when the focus is moved from current cell to another.

[] 


{border="0"}Note: Refreshing behavior of the cells enables them to display the current data automatically after updates.


[] 


{border="0"}Note: Refreshing the cells denote reloading the cell\'s value.


[] 

Following are the list of options provided by the GridRefreshCurrentCellBehavior enumeration.

[] 

[·      ]**None**-Setting ShowCurrentCellBorderBehavior property with this option does not initiate refresh when moving the current cell.

[·      ]**RefreshCell**-Setting ShowCurrentCellBorderBehavior property with this option refreshes the current cell only.

[·      ]**RefreshRow**-Setting ShowCurrentCellBorderBehavior property with this option refreshes the entire row to which the current cell belongs. Use this setting if you are using GridShowButtons.ShowCurrentRow.

[] 

The following code examples illustrate how to set the RefreshCurrentCellBehavior property:

 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [this][.gridControl1.RefreshCurrentCellBehavior = [GridRefreshCurrentCellBehavior].RefreshCell;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [Me][.gridControl1.RefreshCurrentCellBehavior = GridRefreshCurrentCellBehavior.RefreshCell] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p82} 

 

[]{#related-topics}

