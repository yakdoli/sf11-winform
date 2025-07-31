---
title: chartgridlines1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartgridlines1.md
created_at: 2025-07-03
---








  









### Chart Grid Lines {#chart-grid-lines style="tab-stops: 0pt"}

 

The grid lines in the chart that delineates the intervals in the axes can be customized using the following properties.

 


  ------------------------ --------------------------------------------------
  Chart control Property   Description
  DrawGrid                 Specifies whether or not to draw the grid lines.
  GridLineType.ForeColor   The forecolor of the line.
  GridLineType.BackColor   The back color of the line.
  GridLineType.DashStyle   The **DashStyle** to use for drawing the line.
  GridLineType.PenType     The **PenType** to use for drawing the line.
  GridLineType.Width       The thickness of the lines.
  ------------------------ --------------------------------------------------


\
\

{border="0"}

 

Figure 272: Axes Gridlines customized with Properties

 

Using the **GridLineType** property, **BackColor**, **DashStyle**, **ForeColor**, **PenType** and the **Width** can be specified.

 

The following code snippet illustrates how to show the gridlines on both axes and how to customize them.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                                         |
| [//Customizing X-Axis Gridlines]                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.DrawGrid = [true];]                                                        |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.GridLineType.BackColor = System.Drawing.[Color].Transparent;]              |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.GridLineType.DashStyle = System.Drawing.Drawing2D.[DashStyle].DashDotDot;] |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkBlue;]                 |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryXAxis.GridLineType.Width = 2F;]                                                                       |
|                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [//Customizing Y-Axis Gridlines]                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryYAxis.DrawGrid = [true];]                                                        |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryYAxis.GridLineType.BackColor = System.Drawing.[Color].OliveDrab;]                |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryYAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkOrange;]               |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryYAxis.GridLineType.PenType = System.Drawing.Drawing2D.[PenType].LinearGradient;] |
|                                                                                                                                                                                                                         |
| [this][.chartControl1.PrimaryYAxis.GridLineType.Width = 2F;]                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [\'Customizing X-Axis Gridlines]                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryXAxis.DrawGrid = [True]]                                                        |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryXAxis.GridLineType.BackColor = System.Drawing.[Color].Transparent]              |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryXAxis.GridLineType.DashStyle = System.Drawing.Drawing2D.[DashStyle].DashDotDot] |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryXAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkBlue]                 |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryXAxis.GridLineType.Width = 2F]                                                                       |
|                                                                                                                                                                                                                      |
| [            ]                                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [\'Customizing Y-Axis Gridlines]                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryYAxis.DrawGrid = [True]]                                                        |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryYAxis.GridLineType.BackColor = System.Drawing.[Color].OliveDrab]                |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryYAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkOrange]               |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryYAxis.GridLineType.PenType = System.Drawing.Drawing2D.[PenType].LinearGradient] |
|                                                                                                                                                                                                                      |
| [Me][.chartControl1.PrimaryYAxis.GridLineType.Width = 2F]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p189} 

[]{#related-topics}

