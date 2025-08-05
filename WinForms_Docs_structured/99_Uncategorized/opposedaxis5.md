---
title: opposedaxis5.md
original_path: WinForms_Docs/99_Uncategorized/opposedaxis5.md
created_at: 2025-08-05
---






##### Opposed Axis {#opposed-axis style="tab-stops: 0pt"}

For every Chart Type, there is an implied X-axis and Y-axis position, and by default all the X-axes and Y-axes will be rendered in that corresponding position. You can override this default behavior by setting the **OpposedPosition** property to True for an axis, which will cause it to be rendered in the opposite side of the implied position. This feature is also used with Multiple Axes, where you can position the Secondary axis opposite to the Primary axis.

[] 

Table 136: ChartAxis Property


  -------------------- ----------------------------------------------------------------------------
  ChartAxis Property   Description
  OpposedPosition      Gets / sets a value indicating whether axis should be in opposed position.
  -------------------- ----------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][ChartArea][ Name][=\"area\"\>][                    ]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\<][syncfusion][:][ChartSeries][ Name][=\"series\"][ Data][=\" 1 35 2 45 3 30 4 25 5 40\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\<][syncfusion][:][ChartSeries][ Name][=\"series1\"][ Data][=\" 1 30 2 50 3 40 4 35 5 30\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [     ][\<][syncfusion][:][ChartSeries.YAxis][\>]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [          ][\<][syncfusion][:][ChartAxis][ [ Orientation][=\"Vertical\"][ OpposedPosition][=\"True\"/\>]]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [     ][\</][syncfusion][:][ChartSeries.YAxis][\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\</][syncfusion][:][ChartSeries][\>]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image illustrates Chart with Opposed Axis.

[] 

{border="0"}

Figure 191: Chart with Y-axis Opposed

 

See Also

[, ][[Opposed Axis]{.UGHyperlink}]()

 

[]{#p133} 

[]{#related-topics}

