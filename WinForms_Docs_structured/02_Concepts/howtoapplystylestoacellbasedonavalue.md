---
title: howtoapplystylestoacellbasedonavalue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\howtoapplystylestoacellbasedonavalue.md
created_at: 2025-07-03
---








  









## How to Apply Styles to a Cell Based on a Value {#how-to-apply-styles-to-a-cell-based-on-a-value style="tab-stops: 0pt"}

[] 

The QueryCellInfo() event can be used to apply styles to individual cells in the Grid control. The following code shows how the color of  the text in cells containing negative values can be set to red.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [private void][ GridWebControl1_QueryCellInfo([object] sender, Syncfusion.Windows.Forms.Grid.GridQueryCellInfoEventArgs e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [   [if] (lastUpdatedValue \< newValue)]                                                                                                                                     |
|                                                                                                                                                                                                                                       |
| [   {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [      e.Style.BackColor = Color.Yellow;]                                                                                                                                                         |
|                                                                                                                                                                                                                                       |
| [   }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [Private Sub][ GridWebControl1_QueryCellInfo([ByVal] sender [As Object], [ByVal] e [As] Syncfusion.Windows.Forms.Grid.GridQueryCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                             |
| [If Me][.lastUpdateValue\< me.newValue [Then]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [e.Style.BackColor = Color.Yellow]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [End If]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                             |
| [End Sub]                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The color of the text in cells containing negative values is set to red.

 

[]{#related-topics}

