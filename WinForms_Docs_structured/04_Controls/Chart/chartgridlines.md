---
title: chartgridlines.md
original_path: WinForms_Docs/04_Controls/Chart/chartgridlines.md
created_at: 2025-08-05
---








  









### Chart Grid Lines {#chart-grid-lines style="tab-stops: 0pt"}

[] 

The grid lines in the chart that delineates the intervals in the axes can be customized using the following properties.

[] 


  ------------------------------ --------------------------------------------------
  Chart Web Control Properties   Description
  DrawGrid                       Specifies whether or not to draw the grid lines.
  GridLineType.ForeColor         The forecolor of the line.
  GridLineType.BackColor         The back color of the line.
  GridLineType.DashStyle         The **DashStyle** to use for drawing the line.
  GridLineType.PenType           The **PenType** to use for drawing the line.
  GridLineType.Width             The thickness of the lines.
  ------------------------------ --------------------------------------------------


[\
\
]

{border="0"}

**[]** 

Figure 264: Axes Gridlines customized with Properties

[] 

Using the **GridLineType** property, **BackColor**, **DashStyle**, **ForeColor**, **PenType** and the **Width** can be specified.

[] 

The following code snippet illustrates how to show the gridlines on both axes and how to customize them.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [//Customizing X-Axis Gridlines]                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryXAxis.DrawGrid = [true];]                                                        |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryXAxis.GridLineType.BackColor = System.Drawing.[Color].Transparent;]              |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryXAxis.GridLineType.DashStyle = System.Drawing.Drawing2D.[DashStyle].DashDotDot;] |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryXAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkBlue;]                 |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryXAxis.GridLineType.Width = 2F;]                                                                       |
|                                                                                                                                                                                                                            |
| [            ]                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [//Customizing Y-Axis Gridlines]                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryYAxis.DrawGrid = [true];]                                                        |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryYAxis.GridLineType.BackColor = System.Drawing.[Color].OliveDrab;]                |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryYAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkOrange;]               |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryYAxis.GridLineType.PenType = System.Drawing.Drawing2D.[PenType].LinearGradient;] |
|                                                                                                                                                                                                                            |
| [this][.ChartWebControl1.PrimaryYAxis.GridLineType.Width = 2F;]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                                         |
| [\'Customizing X-Axis Gridlines]                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryXAxis.DrawGrid = [True]]                                                        |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryXAxis.GridLineType.BackColor = System.Drawing.[Color].Transparent]              |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryXAxis.GridLineType.DashStyle = System.Drawing.Drawing2D.[DashStyle].DashDotDot] |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryXAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkBlue]                 |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryXAxis.GridLineType.Width = 2F]                                                                       |
|                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [\'Customizing Y-Axis Gridlines]                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryYAxis.DrawGrid = [True]]                                                        |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryYAxis.GridLineType.BackColor = System.Drawing.[Color].OliveDrab]                |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryYAxis.GridLineType.ForeColor = System.Drawing.[Color].DarkOrange]               |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryYAxis.GridLineType.PenType = System.Drawing.Drawing2D.[PenType].LinearGradient] |
|                                                                                                                                                                                                                         |
| [Me][.ChartWebControl1.PrimaryYAxis.GridLineType.Width = 2F]                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p191} 

[]{#related-topics}

