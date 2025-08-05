---
title: doughnutchart2.md
original_path: WinForms_Docs/04_Controls/Chart/doughnutchart2.md
created_at: 2025-08-05
---






#### Doughnut Chart {#doughnut-chart style="tab-stops: 0pt"}

 

DoughnutCoeficient

 

PieCharts specified with a **DoughnutCoeficient** will be rendered as the Doughnut chart. By default, this value is set to 0.0 and hence the chart will be rendered as a full pie. The DoughnutCoeficient property specifies the fraction of radius occupied by the doughnut whole. Hence the value can range from 0.0 to 0.9.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [this][.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoeficient=0.5f;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| **[]**                                                                                                        |
|                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoeficient=0.5f] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 82: Pie Chart with DoughnutCoeficient Property Set

 

HeightCoeficient

 

When in **3D** mode, the relative height of the pie chart can be specified via the **HeightCoeficient** property. Note that the **HeightByAreaDepth** property should be set as **false** for this to take effect. The valid values are 0.1f to 0.5f. This property is set to **0.2f by default**.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [this][.chartControl1.Series\[0\].ConfigItems.PieItem.HeightByAreaDepth = [false];] |
|                                                                                                                                                                                               |
| [this][.chartControl1.Series\[0\].ConfigItems.PieItem.HeightCoeficient = 0.1f;]                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Me][.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = [False]] |
|                                                                                                                                                                                          |
| [Me][.chartControl1.Series(0).ConfigItems.PieItem.HeightCoeficient=0.1f]                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 83: Pie Chart with HeightCoeficient Property Set

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                 |
|                                                                                                                                                                                |
| Customization Options                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AngleOffset[, ]Border, DisplayShadow, DisplayText, DoughnutCoeficient, DrawSeriesNameInDepth, ElementBorders, ExplodedAll, ExplodedIndex, ExplosionOffset |
|                                                                                                                                                                                |
| FillMode, Gradient, HeightByAreaDepth, HeightCoeficient, HighlightInterior, InSideRadius, OptimizePiePointPositions, PieType, ShadowInterior, ShadowOffset                     |
|                                                                                                                                                                                |
| ShowTicks, VisibleAllPies, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                                                                   |
|                                                                                                                                                                                |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible, ShowDataBindLabels                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p68} 

[]{#related-topics}

