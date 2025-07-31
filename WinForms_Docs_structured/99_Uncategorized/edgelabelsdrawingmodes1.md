---
title: edgelabelsdrawingmodes1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\edgelabelsdrawingmodes1.md
created_at: 2025-07-03
---






##### Edge Labels Drawing Modes {#edge-labels-drawing-modes style="tab-stops: 0pt"}

[] 

The EdgeLabelsDrawingMode property is used to determine the drawing options of edge labels. This property has the following two options to render the edge labels.

[] 


  ------------------------ -------------------------------------------------------------------------------------------------------------------------
  EdgeLabelsDrawingModes   Usage
  Center                   Axis labels are placed at the center of the Grid lines. Part of the axis label may be displayed outside the chart area.
  Shift                    The label should be shifted to either right or left so that it comes within the chart area.
  ------------------------ -------------------------------------------------------------------------------------------------------------------------


[] 

The following code snippet can be used to customize the edge labels:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [  \<][syncfusion:ChartAxis][ ][EdgeLabelsDrawingMode][=][\"[Shift]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                    |
|                                                                                                 |
| []                                                          |
|                                                                                                 |
| [ChartArea area = [new] ChartArea();]  |
|                                                                                                 |
| [ChartAxis axis = [new] ChartAxis();]  |
|                                                                                                 |
| [axis.EdgeLabelsDrawingMode = EdgeLabelsDrawingMode.Shift;] |
|                                                                                                 |
| [area.PrimaryAxis = axis;]                                  |
+-------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 91 : EdgeLabelsDrawingMode = \"Center\"[]

**[]** 

**[]** 

{border="0"}

 

Figure 92 : EdgeLabelsDrawingMode = \"Shift\"**[]**

**[]** 

[]{#related-topics}

