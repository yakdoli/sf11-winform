---
title: rangecalculationmode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rangecalculationmode.md
created_at: 2025-07-03
---






##### Range Calculation Mode {#range-calculation-mode style="tab-stops: 0pt"}

[] 

Range Calculation mode is used to calculate range values for the x-axis, based on the selected chart type. The RangeCalculationMode property of ChartAxis class is used to set the range calculation mode.

 

Some chart types require an additional value to be added to the range values, so that the series segments will not be hidden. For example, Column, Bar, Stacking Column and Stacking Bar Charts require additional values to display all their segments. On the other hand, Line, Area and Stacking Area Charts do not require additional values and can be rendered from the start value.

 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Chart Axis Property               | Description                                                                                                                                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RangeCalculationMode              | This property is used to calculate range values for the x-axis of the Chart. It includes the following options.                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                           |
|                                   | **[]**                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                           |
|                                   | [·      ]AdjustAcrossChartTypes: All charts will have one plus interval added to the start and end of the axis to be consistent with the column chart.                                                                       |
|                                   |                                                                                                                                                                                                                                                           |
|                                   | [·      ]ConsistentAcrossChartTypes: All charts will be drawn from the axis start point. In this case column charts will also be drawn with same range as other charts, making the first and last segments hidden partially. |
|                                   |                                                                                                                                                                                                                                                           |
|                                   | [·      ]Default: Charts will be displayed in the AdjustAcrossChartTypes mode.                                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

The following code example illustrates how to set the Range Calculation mode for the Chart Axis.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\<][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [        ][\<][syncfusion][:][ChartAxis][ IsAutoSetRange][=\"True\"][ RangeCalculationMode][=\"AdjustAcrossChartTypes\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    ][\</][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                   |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// Create an instance for the Chart and Chart Area.]                                                                        |
|                                                                                                                                                                                |
| [Chart][ chart = [new] [Chart]();]        |
|                                                                                                                                                                                |
| [ChartArea][ area = [new] [ChartArea]();] |
|                                                                                                                                                                                |
| [chart.Areas.Add(area);]                                                                                                                   |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// Initialize the Range Calculation Mode values.]                                                                           |
|                                                                                                                                                                                |
| [chart.Areas\[0\].PrimaryAxis.RangeCalculationMode = [RangeCalculationMode].ConsistentAcrossChartTypes;]           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 103: RangeCalculationMode = \"ConsistentAcrossChartType\"

[] 

{border="0"}

Figure 104: RangeCalculationMode = \"AdjustAcrossChartTypes\" (Default Mode)

 

[]{#p101} 

 

[]{#related-topics}

