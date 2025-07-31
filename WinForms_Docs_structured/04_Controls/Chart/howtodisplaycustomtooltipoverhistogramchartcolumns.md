---
title: howtodisplaycustomtooltipoverhistogramchartcolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtodisplaycustomtooltipoverhistogramchartcolumns.md
created_at: 2025-07-03
---








  









## How to display custom tooltip over Histogram Chart columns {#how-to-display-custom-tooltip-over-histogram-chart-columns style="tab-stops: 0pt"}

 

On Setting **ShowTooltip** property to **true**, the series name will be displayed as tooltip on the [histogram chart] columns by default. You can also set custom tooltip by handling **ChartRegionMouseMove** event as follows.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [private][ [void] chartControl1_ChartRegionMouseMove([object] sender, [ChartRegionMouseEventArgs] e)] |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    [string] text = [null];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [    [if] (e.Region.IsChartPoint)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        e.Region.ToolTip = [\"Tooltip \"] + e.Region.PointIndex.ToString();]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [    [else]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        text = [\"Not a chart Point\"];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [    }    ]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] chartControl1_ChartRegionMouseMove([ByVal] sender [As] [Object], [ByVal] e [As] ChartRegionMouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [Dim] text [As] [String] = [Nothing]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [If] e.Region.IsChartPoint [Then]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        e.Region.ToolTip = [\"Tooltip \"] & e.Region.PointIndex.ToString()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [Else]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        text = [\"Not a chart Point\"]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [End] [If]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 370: CustomTooltip Displayed for Histogram Chart

 

See Also

 

[Chart Region Events]{.UGHyperlink},[ ]{.UGHyperlink}[Tooltips]{.UGHyperlink}, [Histogram Chart]{.UGHyperlink}[]

[]{#p281} 

 

[]{#related-topics}

