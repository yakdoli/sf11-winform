---
title: chartpointslabels.md
original_path: WinForms_Docs/04_Controls/Chart/chartpointslabels.md
created_at: 2025-08-05
---






##### Chart Points Labels {#chart-points-labels style="tab-stops: 0pt"}

[] 

The OLAP Chart provides support to customize the Labels and the Symbols of the chart points. This is illustrated in the following code example:

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                  |
|                                                                                                                                             |
| [foreach] ([ChartSeries] series [in] [this].Series)\ |
| {\                                                                                                                                          |
|     series.AdornmentsInfo.Visible = [false];\                                                                          |
|     [ChartAdornmentInfo] cai = series.AdornmentsInfo;\                                                              |
|  \                                                                                                                                          |
|     [// To display the x-axis label value.]\                                                                          |
|     series.AdornmentsInfo.LabelContentPath = [\"DataPoint.X\"];\                                                    |
|  \                                                                                                                                          |
|     [// To display the y-axis label value.]\                                                                          |
|     series.AdornmentsInfo.LabelContentPath = [\"DataPoint.Y\"];\                                                    |
|  \                                                                                                                                          |
|     [// To display the Series label value.]\                                                                          |
|     series.AdornmentsInfo.LabelContentPath = [\"Series.Label\"];\                                                   |
| }                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                                                |
|                                                                                                                                                                                           |
| [For] [Each] series [As] [ChartSeries] [In] [Me].Series\ |
|     series.AdornmentsInfo.Visible = [False]\                                                                                                                         |
|     [Dim] cai [As] [ChartAdornmentInfo] = series.AdornmentsInfo\                                                        |
|  \                                                                                                                                                                                        |
|     [\' To display the x-axis label value.]\                                                                                                                        |
|     series.AdornmentsInfo.LabelContentPath = [\"DataPoint.X\"]\                                                                                                   |
|  \                                                                                                                                                                                        |
|     [\' To display the y-axis label value.]\                                                                                                                        |
|     series.AdornmentsInfo.LabelContentPath = [\"DataPoint.Y\"]\                                                                                                   |
|  \                                                                                                                                                                                        |
|     [\' To display the Series label value.]\                                                                                                                        |
|     series.AdornmentsInfo.LabelContentPath = [\"Series.Label\"]\                                                                                                  |
| [Next] series                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the appearance properties, is available in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Appearance**

[] 

[]{#related-topics}

