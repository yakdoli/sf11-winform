---
title: spacing.md
original_path: WinForms_Docs/99_Uncategorized/spacing.md
created_at: 2025-08-05
---






#### Spacing {#spacing style="tab-stops: 0pt"}

**[]** 

Spacing between data points

[] 

This specifies the space/width between data points in the x axis. This value is specified in percentage (%) of interval width. So, for example, if the value of the property is 20%, then only 80% of the interval width is used for rendering the data point(s). If there are multiple series then the available width is divided between the data points in the different series. This of course is used only for appropriate chart types like the column chart which has a width component.

 

This property will not be used when **ChartColumnWidth** is set to **FixedWidthMode**.

[] 


+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Details                                                                                                                                                 |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Possible Values          | A double value (10 to 99)                                                                                                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Default Value            | 30                                                                                                                           |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| 2D / 3D Limitations      | No                                                                                                                           |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Element | Any Series and points                                                                                                        |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Types   | Column Charts, BarCharts, Box and Whisker Chart, Gantt Chart, Tornado Chart, Candle Chart, Hilo Chart, Hilo Open Close Chart |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [//Indicates the spacing width in percentage that is to be applied between the datapoints of the column chart.] |
|                                                                                                                                                                   |
| [this][.ChartWebControl1.Spacing = 50;]                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [\'Indicates the spacing width in percentage that is to be applied between the data points of the column chart.] |
|                                                                                                                                                                    |
| [Me][.ChartWebControl1.Spacing = 50]                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 200: Series rendered with 50% Spacing

**[]** 

See Also

**[]** 

[Candle Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Three Line Break Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Box and Whisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Histogram Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Tornado Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p152} 

[]{#related-topics}

