---
title: axislabelplacement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\axislabelplacement.md
created_at: 2025-07-03
---








  









### Axis Label Placement {#axis-label-placement style="tab-stops: 0pt"}

This feature enables you to specify the position of the label for an axis. You can place the label either inside or outside the plotted chart area.

 

Use Case Scenarios

When you have lengthy label for **the** chart axis, it will occupy more space. So the plotted chart area will **get** reduced. You can avoid this using this feature.

[] 

Properties

Table 3: Property Table


+--------------------+--------------------------------------------------------------------------------------+-------------+-------------+---------------------+
| Property           | Description                                                                          | Type        | Data Type   | **Reference links** |
+--------------------+--------------------------------------------------------------------------------------+-------------+-------------+---------------------+
| AxisLabelPlacement | Specifies the position of the label in a chart axes.                                 |     NA      |  NA         | NA                  |
|                    |                                                                                      |             |             |                     |
|                    | It can be placed inside or outside the plotted chart area using ChartPlacement enum. |             |             |                     |
+--------------------+--------------------------------------------------------------------------------------+-------------+-------------+---------------------+


 

Sample Link

To view a sample:

1.   Open the **Syncfusion Dashboard**.

2.   Click the **User Interface \> Windows Forms**.

3.   Click **Run Samples**.

4.   Navigate to **Chart samples \> Chart Axes  \> ChartAxisCustomization**.

 

Positioning Axis Label

You can position the chart axis label using the *Axes.AxisLabelPlacement* property. You can specify whether it has to be placed inside or outside the plotted chart area using the *ChartPlacement* enum.

The following code illustrates how to place the chart axis label inside the plotted chart area:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[C#\]]**                                                                                                 |
|                                                                                                                                                                                                                                      |
| [this][.chartControl1.PrimaryXAxis.AxisLabelPlacement = [ChartPlacement].Inside;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[VB\]]**                                                        |
|                                                                                                                                                                                             |
| [Me][.chartControl1.PrimaryXAxis.AxisLabelPlacement = [ChartPlacement].Inside] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 278: Chart Y- axis label placement Inside of axis

 

 

 

[] 

 

[]{#related-topics}

