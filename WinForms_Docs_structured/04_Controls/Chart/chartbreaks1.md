---
title: chartbreaks1.md
original_path: WinForms_Docs/04_Controls/Chart/chartbreaks1.md
created_at: 2025-08-05
---








  









### Chart Breaks {#chart-breaks style="tab-stops: 0pt"}

 

Breaks are very useful if you add points with too large difference in values. To enable breaks, you need to set the **ChartAxis.MakeBreaks** property to **true** and set the break mode (ChartAxis.BreakRanges.BreaksMode property).

 

There are three possible modes. They are,

 

[·      ]**ChartBreaksMode.None -** If this value is set, breaks are not used.

 

[·      ]**ChartBreaksMode.Manual** (default) - If this value is set, you can manually set the breaks ranges. To do this, use following methods.

[o  ]**ChartAxis.BreakRanges.Union** -- add a new break range.

[o  ]**ChartAxis.BreakRanges.Exclude** -- remove the break range.

[o  ]**ChartAxis.BreakRanges.Clear** -- remove all break ranges.

 

[·      ]**ChartBreaksMode.Auto -** If this mode is enabled, chart will compute the breaks ranges automatically. You can use the ChartAxis.BreakRanges.BreakAmount to set the minimal relative difference between values (default value is 0.1, value range is 0.1 ). The ratio of empty space should be less than the property value to break the range.

 

[·      ]This mode has several exclusions.

 

 

[·      ]Breaks are computed only for actual y-axis of series.

 

[·      ]Breaks don\'t work with zooming.

 

 

[·      ]Breaks don\'t work with stacking.

 

All breaks work only with decart axes.

 

{border="0"}

 

Figure 275: **[Illustrates Chart ]**BreakAmount**[ Value]**

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.MakeBreaks = [true];]                                                    |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = [ChartBreaksMode].Manual;]                      |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakRanges.Union([new] [DoubleRange](500, 600));]  |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakRanges.Union([new] [DoubleRange](950, 3000));] |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.LineType = [ChartBreakLineType].Wave;]                         |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5;]                                                                   |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.LineColor = [Color].Black;]                                    |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1;]                                                                     |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = [DashStyle].Dot;]                                  |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = [Color].White;]                                 |
|                                                                                                                                                                                                                       |
| [this][.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5;]                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.MakeBreaks = [True] ]                             |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual ]                      |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakRanges.Union([New] DoubleRange(500, 600)) ]  |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakRanges.Union([New] DoubleRange(950, 3000)) ] |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.LineType = ChartBreakLineType.Wave ]                         |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5 ]                                            |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.LineColor = Color.Black ]                                    |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1 ]                                              |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = DashStyle.Dot ]                                  |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = Color.White ]                                 |
|                                                                                                                                                                                              |
| [Me][.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5]                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 276: **[Chart ]**BreakAmount**[ = \"0.5\"]**

**[]** 

[]{#related-topics}

