---
title: supportforlabelsandstrokewiththeoriginaxis.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportforlabelsandstrokewiththeoriginaxis.md
created_at: 2025-07-03
---






#### Support for Labels and Stroke with the Origin Axis {#support-for-labels-and-stroke-with-the-origin-axis style="tab-stops: 0pt"}

Essential Chart for Silverlight now comes with the support to position the labels, tick lines, and header inside, outside, or over the axis. It also supports moving the axis along with the origin axis. The size of the tick lines and also the range of the tick size needed to be placed inside the axis can also be determined by the user using simple properties.

 

Use Case Scenarios

1.  It helps the user to have a better view of the graph and improves its readability.

2.  The values plotted with the negative y-axis and negative x-axis can be viewed clearly by having the labels and tick lines across the area along the origin.

Properties

+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| **Property**           | **Description**                                                                                       | **Type**        | **Data Type**   |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ChartLabelPosition     | Positions the labels.                                                                                 | AxisPosition    | Enum            |
|                        |                                                                                                       |                 |                 |
|                        |                                                                                                       |                 |                 |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ChartTickLinesPosition | Positions the tick lines and smaller tick lines.                                                      | AxisPosition    | Enum            |
|                        |                                                                                                       |                 |                 |
|                        |                                                                                                       |                 |                 |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| HeaderPosition         | Positions the header.                                                                                 | AxisPosition    | Enum            |
|                        |                                                                                                       |                 |                 |
|                        |                                                                                                       |                 |                 |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ChartTickLinesRange    | Determines the range of tick lines inside the axis.                                                   | Double          | Double          |
|                        |                                                                                                       |                 |                 |
|                        |                                                                                                       |                 |                 |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| AxisLabels             | Determines the position of the axis elements that includes labels, tick lines and smaller tick lines. | AxisLabels      | Enum            |
|                        |                                                                                                       |                 |                 |
|                        |                                                                                                       |                 |                 |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| TickSize               | Sets the size for the small tick lines.                                                               | Double          | Double          |
+------------------------+-------------------------------------------------------------------------------------------------------+-----------------+-----------------+

[] 

Sample Link

1.  Open the Silverlight sample browser.

2.  Click on the **Chart** product.

3.  Select **Sample Browser** \> **Chart** \> **Chart Axis** \> **Labels and Tick Lines Support**

More:





