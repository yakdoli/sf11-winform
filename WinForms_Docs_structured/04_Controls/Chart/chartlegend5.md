---
title: chartlegend5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartlegend5.md
created_at: 2025-07-03
---








  









### Chart Legend {#chart-legend style="tab-stops: 0pt"}

The legend is represented by the **ChartLegend** type.

**Default Legend**

By default, a custom **ChartLegend** instance is added to the legends list in the control. You can access this default legend.

**Legend Look and Feel**

The following table lists some common properties you could use to customize the overall legend appearance:


+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| Chart Legend Property | Description                                                                                                              | Property Type | Value it Accepts   | Dependencies                                          |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| Visible               | Gets or sets if the legend is visible or not.                                                                            | bool          | True               | NA                                                    |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | False              |                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| ItemPadding           | Gets or sets the padding for every item in the legend.                                                                   | double        | Any double value   | Visible---Only applies if chart legend is visible     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| TextColor             | Gets or sets the forecolor of the item                                                                                   | Color         | Color.AliceBlue    | Visible---Only applies if chart legend is visible     |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | Color.Black        |                                                       |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | Color.White        |                                                       |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | Color.YellowGreen  |                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| Shape                 | Gets or sets the shape of the legend.                                                                                    | LegendShape   | LegendShape.Circle | Visible---Only applies if the chart legend is visible |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | LegendShape.Cross  |                                                       |
|                       |                                                                                                                          |               |                    |                                                       |
|                       |                                                                                                                          |               | LegendShape.Wedge  |                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| ShapeSize             | Gets or sets the size of every legend item.                                                                              | Size          | SizeObject         | Visible---Only applies if chart legend is visible     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+
| Style                 | Gets or sets the style of the legend item which includes the border, interior, line cap, line join, opacity, and shadow. | Style         | StyleObject        | Visible---Only applies if chart legend is visible     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+--------------------+-------------------------------------------------------+


[] 

Legend Positioning

The legend positioning can be affected in the following ways:


+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| Chart Model     | Description                                                                                                              | Property Type   | Value it Accepts       | Dependencies                                      |
|                 |                                                                                                                          |                 |                        |                                                   |
| Property        |                                                                                                                          |                 |                        |                                                   |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| LegendAlignment | Gets or sets the alignment of the legend in the chart.                                                                   | StringAlignment | StringAlignment.Far    | NA                                                |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | StringAlignment.Center |                                                   |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | StringAlignment.Near   |                                                   |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| LegendPosition  | Gets or sets the padding for every item in the legend.                                                                   | double          | Any double value       | Visible---Only applies if chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| TextColor       | Gets or sets the forecolor of the item.                                                                                  | Color           | Color.AliceBlue        | Visible---Only applies if chart legend is visible |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | Color.Black            |                                                   |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | Color.White            |                                                   |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | Color.YellowGreen      |                                                   |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| Shape           | Gets or sets the shape of the legend.                                                                                    | LegendShape     | LegendShape.Circle     | Visible---Only applies if chart legend is visible |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | LegendShape.Cross      |                                                   |
|                 |                                                                                                                          |                 |                        |                                                   |
|                 |                                                                                                                          |                 | LegendShape.Wedge      |                                                   |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| ShapeSize       | Gets or sets the size of every legend item.                                                                              | Size            | SizeObject             | Visible---Only applies if chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+
| Style           | Gets or sets the style of the legend items which include the border, interior, line cap, line join, opacity, and shadow. | Style           | StyleObject            | Visible---Only applies if chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+-----------------+------------------------+---------------------------------------------------+


 

Chart legends can be added to the chart using the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][      ][]**                                                   |
|                                                                                                                                                                                                   |
| [this][.ChartAdv1.Legend.Visible = [true];]                   |
|                                                                                                                                                                                                   |
| [this][.ChartAdv1.LegendPosition = [DockPosition].Bottom;] |
|                                                                                                                                                                                                   |
| [ [this].ChartAdv1.Legend.Shape = [LegendShape].Rectangle;]                                         |
|                                                                                                                                                                                                   |
| []                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][      ][]**                                                 |
|                                                                                                                                                                                                 |
| [Me][.ChartAdv1.Legend.Visible = [True]]                    |
|                                                                                                                                                                                                 |
| [Me][.ChartAdv1.Legend.Shape = [LegendShape].Rectangle]  |
|                                                                                                                                                                                                 |
| [Me][.ChartAdv1.LegendPosition = [DockPosition].Bottom ] |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

 

Figure 19: Chart Legend

[]{#related-topics}

