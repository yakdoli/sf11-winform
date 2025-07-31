---
title: showhidecurrentcellborder.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\showhidecurrentcellborder.md
created_at: 2025-07-03
---






##### Show/Hide Current Cell Border {#showhide-current-cell-border style="tab-stops: 0pt"}

[] 

**ShowCurrentCellBorderBehavior** property of the grid determines the behavior of the current cell\'s border. The **GridShowCurrentCellBorder** enumeration specifies display of current cell\'s frame or border.

[] 

Here is the list of options in GridShowCurrentCellBorder enumeration.

[] 

[·      ]**AlwaysVisible**-Setting ShowCurrentCellBorderBehavior property with this option displays the current cell borders/frame.

[·      ]**GrayWhenLostFocus**-Setting ShowCurrentCellBorderBehavior property with this option shows the current cell\'s borders in gray when it is not focused upon.

[·      ]**HideAlways**-Setting ShowCurrentCellBorderBehavior property with this option hides the borders of the current cell.

[·      ]**WhenGridActive**-Setting ShowCurrentCellBorderBehavior property with this option highlights the current cell\'s border when the grid is under focus.

[] 

The following code examples illustrate how to set the ShowCurrentCellBorderBehavior property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [this][.gridControl1.ShowCurrentCellBorderBehavior = [GridShowCurrentCellBorder].AlwaysVisible;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [Me][.gridControl1.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p81} 

 

[]{#related-topics}

