---
title: chartlegend6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartlegend6.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### ChartLegend {#chartlegend style="tab-stops: 0pt"}

The legend is represented by the ChartLegend type.

**Default Legend**

By default, a custom ChartLegend instance gets added to the legends list in the control. You can access this default legend.

**Legend Look and Feel**

The following table lists some common properties you could use to customize the overall legend appearance:


+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| ChartLegend Property | Description                                                                                                              | Type of Property | Value it accepts   | Dependencies                            |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| Visible              | Gets or sets if the Legend is visible or not.                                                                            | bool             | True               | NA                                      |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | False              |                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| ItemPadding          | Gets or sets the padding for every item in the legend.                                                                   | double           | Any double value   | Visible---                              |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  |                    | Only applies if Chart legend is visible |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| TextColor            | Gets or sets the forecolor of te item                                                                                    | Color            | Color.AliceBlue    | Visible---                              |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  | Only applies if Chart legend is visible |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | Color.Black        |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | Color.White        |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | Color.YellowGreen  |                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| Shape                | Gets or sets the shape of the legend.                                                                                    | LegendShape      | LegendShape.Circle | Visible---                              |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | LegendShape.Cross  | Only applies if Chart legend is visible |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | .                  |                                         |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  | LegendShape.Wedge  |                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| ShapeSize            | Gets or sets the size of every legend item.                                                                              | Size             | SizeObject         | Visible---                              |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  |                    | Only applies if Chart legend is visible |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+
| Style                | Gets or sets the style of the legend item, which include the border, interior, line cap, line join, opacity, and shadow. | Style            | StyleObject        | Visible---                              |
|                      |                                                                                                                          |                  |                    |                                         |
|                      |                                                                                                                          |                  |                    | Only applies if Chart legend is visible |
+----------------------+--------------------------------------------------------------------------------------------------------------------------+------------------+--------------------+-----------------------------------------+


[] 

Legend Positioning

The legend positioning can be affected in the following ways:


+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| ChartModel      | Description                                                                                                              | Type of Property | Value it accepts       | Dependencies                            |
|                 |                                                                                                                          |                  |                        |                                         |
| Property        |                                                                                                                          |                  |                        |                                         |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| LegendAlignment | Gets or the alignment of the legend in the chart.                                                                        | StringAlignment  | StringAlignment.Far    | NA                                      |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | StringAlignment.Center |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | StringAlignment.Near   |                                         |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| LegendPosition  | Gets or sets the padding for every item in the legend.                                                                   | double           | Any double value       | Visible---                              |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  |                        | Only applies if Chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| TextColor       | Gets or sets the forecolor of te item                                                                                    | Color            | Color.AliceBlue        | Visible---                              |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      | Only applies if Chart legend is visible |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | Color.Black            |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | Color.White            |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | Color.YellowGreen      |                                         |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| Shape           | Gets or sets the shape of the legend.                                                                                    | LegendShape      | LegendShape.Circle     | Visible---                              |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | LegendShape.Cross      | Only applies if Chart legend is visible |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | .                      |                                         |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  | LegendShape.Wedge      |                                         |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| ShapeSize       | Gets or sets the size of every legend item.                                                                              | Size             | SizeObject             | Visible---                              |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  |                        | Only applies if Chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+
| Style           | Gets or sets the style of the legend item, which include the border, interior, line cap, line join, opacity, and shadow. | Style            | StyleObject            | Visible---                              |
|                 |                                                                                                                          |                  |                        |                                         |
|                 |                                                                                                                          |                  |                        | Only applies if Chart legend is visible |
+-----------------+--------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-----------------------------------------+


[] 

Chart with legend can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

More:







