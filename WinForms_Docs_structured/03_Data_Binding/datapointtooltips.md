---
title: datapointtooltips.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\datapointtooltips.md
created_at: 2025-07-03
---






#### DataPoint Tooltips {#datapoint-tooltips style="tab-stops: 0pt"}

Tooltips can be shown on each data point when the mouse hovers on them. The format of the tooltip is specified by the following property in ChartSeries:

 

Properties:


+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Property            | Description                                                                                                                                             | Property Type                                                      | Value it Accepts                                                   | Any Other Dependencies/Sub-properties Associated                                                                 |
+=====================+=========================================================================================================================================================+====================================================================+====================================================================+==================================================================================================================+
| PointsToolTipFormat | Specifies the format for the datapoint tooltips. The following place-holders can be used in the value:                                                  | [string] | [string] | [NA][] |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {0} - Will be replaced by the corresponding ChartSeries.Name.                                                                                           |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {1} - Will be replaced by the corresponding [ChartSeries.Style.ToolTip].                                                          |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {2} - Will be replaced by the corresponding data point\'s tooltip. For example, to set the first point\'s tooltip, use \"series1.Styles\[0\].ToolTip\". |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {3} - Will be replaced by the corresponding X value of the point.                                                                                       |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {4} - Will be replaced by the corresponding Y value of the point. This is the default setting.                                                          |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {5} - Will be replaced by the second Y value, if any.                                                                                                   |                                                                    |                                                                    |                                                                                                                  |
|                     |                                                                                                                                                         |                                                                    |                                                                    |                                                                                                                  |
|                     | {6} - Will be replaced by the third Y value, and so on.                                                                                                 |                                                                    |                                                                    |                                                                                                                  |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+


[] 

You can also customize the tooltip for individual data points by setting the ToolTip style for each data point. This is best accomplished by listening to the ChartSeries.PrepareStyle event, as shown below.

 

[]{#related-topics}

